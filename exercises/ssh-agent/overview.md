# WHAT IS SSH-AGENT?

In the previous exercise, we showed how to encrypt a private key with a user
supplied passphrase. We also noted that each subsequent use of said key will
require decryption. In practice, this can be onerous for day-to-day development.

Enter ssh-agent, a tool which can store the unencrypted versions of your private
keys in memory, and communicate directly with ssh-based tools to provide them
automatically. Most modern operating systems ship with some form of ssh-agent,
which should run in the background after you log in, and terminate when you log
out.

You can add a key to ssh-agent any time with the following command:

```
ssh-add /path/to/key
```

Running `ssh-add` without arguments will automatically attempt to add all of
these default keys: `~/.ssh/id_rsa`, `~/.ssh/id_dsa` and `~/.ssh/identity`.

You can list all keys currently stored in your ssh-agent with the following:

```
ssh-add -l
```

Not only does ssh-agent effectively allow a user to unlock their keys one time
and continue using them without being prompted for their passphrase, this state
can be *forwarded* to remote machines the user connects to using SSH's `-A`
option.

This means users need not copy their private keys to machines they regularly SSH
into. A common example of this would be a production server which is expected to
have access to a private version controlled repository. Rather than configuring
the server with a "deploy key", the server can perform the checkout as though it
were the user actually running the deployment.

Further, ssh-agent obviates the need to specify a private key when connecting to
a remote machine (e.g. `ssh -i /path/to/key`), as it will automatically loop
through all of your private keys until it's able to establish a successful
connection (or it runs out of keys).

## EXERCISE

Confirm your agent is running by checking the value of $SSH_AUTH_SOCK. Then,
confirm your agent is forwarding by ssh-ing to `workshop.learndeployment.com`
and checking $SSH_AUTH_SOCK again. Finally, confirm your agent is configured
with your private key by trying to ssh to git@github.com both locally and
remotely.

As extra credit, edit `~/.ssh/config` to make agent forwarding the default
behavior for `workshop.learndeployment.com`.

## LEARNING OBJECTIVES

- What is ssh-agent used for?
- How do you add keys to your agent?
- How do you list keys in your agent?
- How do you forward your agent with a ssh command line flag?
- How do you check to see if your agent is running or forwarding?
- How do you configure ~/.ssh/config to enable forwarding for a specific server?
