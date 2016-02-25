# AUTHORIZED KEYS

In the previous section, we learned about the underlying mechanics of asymmetric
cryptography, and how SSH uses your public and private keypair to ensure a
secure trusted connection can be established between two machines. Perhaps after
that primer you're wondering how the server is able to verify signatures or
encrypt messages for any given user.

The answer to this question lies in the file `~/.ssh/authorized_keys`.

A few things should jump out at you about this file path. The first is that it
lives inside a user's home directory (`~`). That means every user has their own
`authorized_keys` file, as opposed to the system keeping a global one. Further,
the file is stored in the `~/.ssh` directory which is also the default location
for ssh keys.

It's important to note that the `authorized_keys` file is only used by SSH when
a machine receives a request for an *incoming* ssh connection. Outgoing SSH
requests do not use the `authorized_keys` file in any way.

The format of the `authorized_keys` file is relatively straightforward. A valid
`authorized_keys` file contains string representations of one or more public
keys delimited with a newline character.

When a request to connect to a machine as a particular user is received, SSH
reads that user's `authorized_keys` file into memory and uses ALL of the public
keys it contains in an effort to validate the connection using one of the
cryptographic scenarios outlined in the previous ssh keys section.

Because possession of the private key is proof of identity, the assumption is
that if the machine requesting the connection can either produce a signature
that can be verified using one of the public keys in the `authorized_keys` file
(SSHv2), or correctly complete a cryptographic challenge generated using one of
those public keys (SSHv1), then the connection should be allowed.

On most Linux distributions the `authorized_keys` file and `~/.ssh` directory
might not exist by default and will need to be created by the user. The `.ssh`
directory should have `0700` permissions and the `authorized_keys` file `0600`.

## EXERCISE

In the previous exercise, the instructor of this workshop created an account
for your username at `workshop.learndeployment.com`. Try editing or removing
the `authorized_keys` file for that user. Then, log off and try to log on again.

## LEARNING OBJECTIVES

- How does a server cryptographically verify who you are?
- Where do you put your public key to allow password-less SSH?
- What are the correct permissions for the `~/.ssh` folder?
- What are the correct permissions for the `~/.ssh/authorized_keys` file?
