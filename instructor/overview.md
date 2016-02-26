# Preparation

Before the workshop the instructor should make sure they have a profile called `bocoup`
in their `~/.aws/credentials` file. They should also copy the `learn-deployment.pem` key
from Lastpass to `~/.ssh` and ensure it has the correct permissions 
`chmod 400 ~/.ssh/learn-deployment.pem`. 

The remote server can be setup using the commands:

```
AWS_PROFILE=bocoup ansible-playbook -i localhost, instructor_setup.yml
AWS_PROFILE=bocoup ansible-playbook --private-key=~/.ssh/learn-deployment.pem -u ubuntu -i inventory/ec2.py create_workshop_user.yml
```

Optionally, the instructors can create additional users by modifying the `group_vars/all.yml`
file in the `ansible` directory and give them access to the server by running:

```
AWS_PROFILE=bocoup ansible-playbook --private-key=~/.ssh/learn-deployment.pem -u ubuntu -i inventory/ec2.py grant_personalized_access.yml
```

# Introduction

The workshop opens by having everyone `npm install -g bocoup/learn-ssh`.
The instructor's terminal should be visible to the workshop as he or she demos
how to use the tool. Each time an exercise is selected, some files will be
copied to the current directory under a folder matching the exercise name.

Each exercise contains a detailed exploration of the concept being introduced,
as well as sample configuration files and solutions where applicable.

The instructor will begin each section by using the overview file as a guide to
explain the new concept. After fielding any questions, attendees will then run
`learn-ssh` on their own machine to begin development.

## ssh-basics

The exercise folder contains a private key which can be used to connect to
an EC2 instance accessible at `workshop.learndeployment.com` with the
username `workshop`. Notably, the key has the wrong permissions. Attendees must
first correct this before they can connect (chmod 400, owner read only).

Once all attendees have successfully connected, everyone should log off and
try to connect as themselves. This will fail.

We'll explore why that is in the next few exercises.

## asymmetric-cryptography

The instructor will explain asymmetric cryptography.

## authorized-keys

Attendees should be connected to `workshop.learndeployment.com` as the
workshop user. The instructor will show the `authorized_keys` file on the screen
and talk about how it got there (pre-class prep).

Then the instructor will modify the `authorized_keys` and show how everyone is still
logged in and explain how once the server has authorized your session it does not
continue to authorize you; when you're in you're in. The students should then `exit`
their existing ssh session and try to reconnect, this will fail.

After this the instructor should ensure a stable server state by re-running:

```
AWS_PROFILE=bocoup ansible-playbook --private-key=~/.ssh/learn-deployment.pem -u ubuntu -i inventory/ec2.py create_workshop_user.yml
```
Everyone should then try to SSH again, and it will pass. Students should `exit` this 
session before starting the next exercise.

## known-hosts

To illustrate what a MiTM attack might look like, the instructor will regenerate the 
host keys on the remote server using the command:

```
AWS_PROFILE=bocoup ansible-playbook --private-key=~/.ssh/learn-deployment.pem -u ubuntu -i inventory/ec2.py regenerate-host-keys.yml
```

Attendees will then attempt to SSH to the server. This will trigger a warning.

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


## permissions-elevation

Attendees will learn how to use sudo and su, the difference between them, and
how to manage sudoers.

Finally, the existence of http://github.com/username.keys will be pointed out as
a matter of convenience.
