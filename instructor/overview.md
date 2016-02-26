# Instructor Notes

At least one day prior to the workshop, attendees must provide the public half
of their public/private keypair, and the username of their machine. This public
key should also be registered with github.

If attendees do not have a public/private keypair, they can follow this guide
to create one:
https://help.github.com/articles/generating-ssh-keys/

The instructor should prepare the ansible configuration in this folder to grant
all attendees access to `workshop.learndeployment.com`. This should **NOT** be
run before the first exercise begins.

The workshop opens by having everyone `npm install -g tkellen/learn-deployment`.
The instructor's terminal should be visible to the workshop as he or she demos
how to use the tool. Each time an exercise is selected, some files will be
copied to the current directory under a folder matching the exercise name.

Each exercise contains a detailed exploration of the concept being introduced,
as well as sample configuration files and solutions where applicable.

The instructor will begin each section by using the overview file as a guide to
explain the new concept. After fielding any questions, attendees will then run
`learn-deployment` on their own machine to begin development.

The instructor should now setup the student and instructor servers:

```
ansible-playbook -i localhost, instructor_setup.yml
ansible-playbook -i localhost, student_setup.yml
```

Grant student access to all the servers by creating the `workshop` user on all
machines. You might have to wait a few seconds after the first two commands so the
AWS API and dynamic inventory are up to date.

```
ansible-playbook -i inventory/ec2.py -u ubuntu --private-key <PATH_TO_ADMIN_KEY> create_workshop_user.yml
```

## ssh-basics

The exercise folder contains a private key which can be used to connect to
an EC2 instance accessible at `workshop.learndeployment.com` with the
username `workshop`. Notably, the key has the wrong permissions. Attendees must
first correct this before they can connect (chmod 400, owner read only).

Once all attendees have successfully connected, everyone should log off and
try to connect as themselves. This will fail.

Then, the instructor will tell the attendees to wait a moment as they run a
playbook to give everyone personalized access.

```
ansible-playbook -i inventory/ec2.py -l tag_learn_deployment_student_False -u ubuntu --private-key <PATH_TO_ADMIN_KEY> grant_personalized_access.yml
```

A few seconds later, everyone in the room has
access to the machine. Cool! Once everyone is logged in, move to the next
exercise.

## asymmetric-cryptography

The instructor will explain asymmetric cryptography.

## authorized-keys

Attendees should be connected to `workshop.learndeployment.com` as their own
user.

Because each attendee provided their public key before the workshop, the
instructor can now point out that it is listed in `~/.ssh/authorized_keys`.

Attendees are encouraged to edit this file, log off, and try to log in again.
Once everyone is satisfied they understand how this works, the instructor can
run their setup playbook again, renewing access for everyone.

## known-hosts

Everyone should be able to SSH to `workshop.learndeployment.com` as their own
user before this exercise begins.

To illustrate what a MiTM attack might look like, the instructor will switch EC2
instances for `workshop.learndeployment.com`:

```
ansible-playbook -i inventory/ec2.py -l tag_learn_deployment_student_False teardown.yml
ansible-playbook -i localhost, instructor_setup.yml
```

Some time should pass before running these as the API calls for dynamic inventory do
not update immediately and these tasks will fail if called before everything is up to date.

```
ansible-playbook -i inventory/ec2.py -l tag_learn_deployment_student_False -u ubuntu --private-key <PATH_TO_ADMIN_KEY> create_workshop_user.yml
ansible-playbook -i inventory/ec2.py -l tag_learn_deployment_student_False -u ubuntu --private-key <PATH_TO_ADMIN_KEY> grant_personalized_access.yml
```

Attendees will then SSH to the server. This will trigger a warning.

The instructor will then explain how to fix this problem using `ssh-keygen`,
with an emphasis that the veracity of the server should be verified before this
is done.

## ssh-key-passphrases

Attendees will now learn about passphrases, how to add them to their keys if
they don't have them, and how they are a type of two factor authentication.
This will lead into dealing with ssh-agent.

## ssh-agent

Attendees now understand the basic usage of private keys. We'll now make
managing them easier to deal with by adding to/listing the keys in our agent.

We can check if ssh-agent is running by echoing the environment variable
$SSH_AUTH_SOCK.

Attendees can then check to see if forwarding works by ssh-ing to
`workshop.learndeployment.com` and running `ssh git@github.com`. If agent
forwarding is functioning they should see "Hi <username>! ....".

The `-A` flag must be specified with SSH to enable this. We should also cover
how to configure `~/.ssh/config` to enable this for specific domains/machines
etc.

## your-server

Attendees will each be given a `username.learndeployment.com` domain that
points to a server of their own. They will then be instructed to connect using
the provided private key, and to create a user for themselves that supports
public key auth.

If this goes quickly, attendees will be encouraged to make accounts for other
users in the workshop.

In the event a user needs assistance their username can be automatically created on the
box by filtering the ec2 dynamic inventory and running the personalized access playbook.

```
ansible-playbook -i inventory/ec2.py -l tag_username_<USERNAME> -u ubuntu --private-key <PATH_TO_ADMIN_KEY> grant_personalized_access.yml
```

## permissions-elevation

Attendees will learn how to use sudo and su, the difference between them, and
how to manage sudoers.

Finally, the existence of http://github.com/username.keys will be pointed out as
a matter of convenience.
