#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
from operator import itemgetter
from urllib import urlencode

DOCUMENTATION = '''
---
module: cloudflare_domain
short_description: Create or delete Cloudflare DNS records.
description:
  - Create or delete Cloudflare DNS records.
author: Marcus Fredriksson <drmegahertz@gmail.com>
options:
  state:
    description:
      - Whether or not this record should be present in the given zone.
    default: present
    choices: ['present', 'absent']
  name:
    description:
      - Name of the DNS record. For example: www
    required: true
  zone:
    description:
      - The target domain to add this record to.
    required: true
    aliases: ['z']
  type:
    description:
      - Type of DNS record.
    required: true
    choices: ['A', 'CNAME', 'MX', 'TXT', 'SPF', 'AAAA', 'NS', 'SRV', 'LOC']
  content:
    description:
      - The content of the DNS record, will depend on the the type of record being added.
    required: true
  token:
    description:
      - This is the API key made available on your CloudFlare account page.
      - This can also be provided by setting the CLOUDFLARE_API_TOKEN environment variable.
    required: true
    aliases: ['tkn']
  email:
    description:
      - The e-mail address associated with the API key.
      - This can also be provided by setting the CLOUDFLARE_API_EMAIL environment variable.
    required: true
'''

EXAMPLES = '''
- cloudflare_domain: >
    state=present
    name=www
    zone=example.com
    type=A
    content=127.0.0.1
    email=joe@example.com
    token=77a54a4c36858cfc10321fcfce22378e19e20
'''

class CloudflareException(Exception):
    pass

class Cloudflare(object):
    def __init__(self, email, token, zone):
        self.url   = 'https://www.cloudflare.com/api_json.html'
        self.email = email
        self.token = token
        self.zone = zone

    def request(self, **kwargs):
        # remove unset
        kwargs = dict((k, v) for k, v in kwargs.iteritems() if v)

        kwargs.update(email=self.email, tkn=self.token, z=self.zone)

        req = urllib2.urlopen(self.url, urlencode(kwargs))
        response_json = json.loads(req.read())

        if response_json['result'] != 'success':
            raise CloudflareException(response_json['msg'])

        return response_json

    def rec_load_all(self):
        return self.request(a='rec_load_all')

    def rec_new(self, type, name, content, ttl=1, mode=None):
        mode_types = ['A', 'AAAA', 'CNAME']

        # mode is only allowed in DNS record types
        if mode and not type in mode_types:
            raise Exception(mode, 'is only allowed with one of this types:', mode_types)

        return self.request(
            a='rec_new',
            type=type,
            name=name,
            content=content,
            ttl=ttl,
            service_mode=service_mode.index(mode) if mode else None
        )

    def rec_delete(self, id):
        return self.request(a='rec_delete', id=id)

def cloudflare_domain(module):
    cloudflare = Cloudflare(module.params['email'], module.params['token'], module.params['zone'])
    responseRecordCollection = cloudflare.rec_load_all()['response']['recs']
    existing_records = responseRecordCollection.get('objs', [])

    # Shortcuts
    get_record_attributes = itemgetter('name', 'type', 'content')
    name, type, content = get_record_attributes(module.params)
    zone, state = module.params['zone'], module.params['state']

    if name != zone:
        name += '.' + zone

    # Fetch the existing record, if any.
    existing_record = None
    for each in existing_records:
        if get_record_attributes(each) == (name, type, content):
            existing_record = each
            break

    if state == 'present':
        if existing_record:
            module.exit_json(changed=False, name=module.params['name'], type=type, content=content)

        if not module.check_mode:
            response = cloudflare.rec_new(type, module.params['name'], content, mode=module.params['mode'])

        module.exit_json(changed=True, name=module.params['name'], type=type, content=content, service_mode=module.params['mode'])

    elif state == 'absent':
        if existing_record:
            record_id = existing_record['rec_id']

            if not module.check_mode:
                response = cloudflare.rec_delete(record_id)

            module.exit_json(
                changed=True,
                delete=record_id,
                record={
                    'name': module.params['name'],
                    'content': content,
                    'type': type
                }
            )

        module.exit_json(changed=False, name=module.params['name'], type=type, content=content)

    module.fail_json(msg='Unknown value "{0}" for argument state. Expected one of: present, absent.')

service_mode = ['DNS', 'CDN']
def main():
    domain_types = ['A', 'CNAME', 'MX', 'TXT', 'SPF', 'AAAA', 'NS', 'SRV', 'LOC']

    module = AnsibleModule(
        argument_spec = dict(
            state   = dict(default='present', choices=['present', 'absent']),
            name    = dict(required=True),
            zone    = dict(required=True, aliases=['z']),
            type    = dict(required=True, choices=domain_types),
            mode    = dict(default='DNS', choices=service_mode),
            content = dict(required=True),
            email   = dict(no_log=True, default=os.environ.get('CLOUDFLARE_API_EMAIL')),
            token   = dict(no_log=True, default=os.environ.get('CLOUDFLARE_API_TOKEN'), aliases=['tkn']),
        ),
        supports_check_mode=True,
    )

    try:
        cloudflare_domain(module)
    except Exception as e:
        module.fail_json(msg=str(e))


from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()