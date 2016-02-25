# WHAT IS KNOWN_HOSTS AND HOW DOES IT WORK?

So far, we've focused on how a remote machine can trust an incoming connection
from the open internet. Now, let's talk about why the person who initiates the
connection should trust the response. At first, this trust might seem tacit.
You've requested the connection, after all. Why wouldn't it be secure?

If you use a domain name, you are relying on DNS to resolve the correct IP
address. Are you sure the DNS server you are using has not been tampered with?
Assume you cut out DNS and use an IP address directly. Do you trust the network
you are using to route the connection accurately?

Poisoned DNS or "man-in-the-middle" attacks can be difficult to detect and could
cause an unsuspecting user to communicate with a bad actor. This can lead to
confidential information being compromised.

To control for this, SSH stores the public key of every remote host it has ever
made a connection to inside `~/.ssh/known_hosts` so it can verify that the
corresponding private key is held by that machine for all future connections
using one of the asymmetric scenarios we discussed in the ssh-basics section.

Like `authorized_keys` this file contains public keys delimited with the newline
character and is maintained distinctly for each user on the machine originating
the SSH connection. Unlike `authorized_keys`, each line starts with a machine
identifier, either the IP address or fully qualified domain name followed by a
space and the public key.

If the remote machine cannot prove it has the correct private key SSH will warn
the user that there might be someone eavesdropping and refuse to connect. This
process is called host key checking and is the first thing which occurs when an
SSH request is made.

SSH provides the `StrictHostKeychecking` option which can be disabled for those
brave and foolish souls who wish to communicate with anything that picks up the
line.

Unfortunately for us, today's tools make it easier than ever to redeploy servers
and DNS propagation can happen almost instantly; meaning there are lots of times
when a server's keypair has changed legitimately.

If SSH warns you that a server's identity cannot be verified, ask yourself the
following questions:

- Is this a server I know has been recreated?
- Is this a vagrant box? Running `vagrant destroy` and `vagrant up`
  completely recreates the underlying virtual machine.
- If connecting via fully qualified domain name does the `dig` command report
  the IP address I expect this server to have? If you don't have the `dig`
  command, you can try https://toolbox.googleapps.com/apps/dig/.
- Do I trust the network I'm currently connected to?

It's important to note that the server uses the same keypair for all incoming
connections, and restarting a server will not cause the keypair to change; only
completely swapping out the underlying machine or reinstalling the operating
system will.

To remove an outdated known host, the command `ssh-keygen -R DOMAIN_OR_IP`
can be used. Alternatively, `~/.ssh/known_hosts` can be manually edited and the
outdated line removed. If the `known_hosts` file is removed completely it will
be recreated and any established trust relationships will be lost.

## EXERCISE

In this exercise, the instructor of the workshop will swap the server that is
running at `workshop.learndeployment.com` to illustrate what a `known_hosts`
conflict looks like. Resolve this conflict so you can connect to the server
again.

## LEARNING OBJECTIVES

- How is the identity of a machine you are SSHing to validated?
- What are some common false positives for invalid known host warnings?
- How do you clear invalid entries in `known_hosts`?
