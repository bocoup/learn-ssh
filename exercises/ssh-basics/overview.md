# SSH BASICS

SSH is a protocol which facilitates the creation of a secure text-based shell
connection between machines. While many developers use SSH every day, the
particulars of what's happening under the hood are often overlooked.

### HOW SSH USES YOUR KEYS

In SSHv1, the basic form of asymmetric cryptography is used. During connection,
the server encrypts a message for the user and it's expected that the user's
machine is capable of decrypting it and responding with the correct plain text.
This is known as a cryptographic challenge.

In SSHv2, the user sends a cryptographic signature that the server validates
prior to granting access.

In both cases, the result is the same: *the server assumes that possession of
the private key is proof of identity*.

If you're curious how the server is able to do this, check out the next section
which covers the `authorized_keys` file.

### PERMISSIONS

Due to the importance of keeping a private key secret, SSH expects your key to
have a very restrictive set of permissions. It is outside the scope of this
workshop to explain how this works, but the correct "mode" for a private key
is `0400`.

This prevents any action on a file except reading by the owner. Should you ever
need to edit this file, you can change to mode `0600` to enable write access by
the owner.

You can set the mode of a file with the following command:

```
chmod <mode> <filename>
```

### SPECIFYING A USER

When connecting to a remote machine, SSH will attempt to connect with the
username of the host machine's currently logged in user. You can see the
username of the currently logged in user by running `echo $USER` or `whoami`
in your terminal. Assuming the current user is `alice`, the following three
commands are equivalent:

*Default Behavior (will use alice as the username)*:
```
ssh workshop.learndeployment.com
```

*Username Explicitly Provided with @*:
```
ssh alice@workshop.learndeployment.com
```

*Username Explicitly Provided with CLI flag*:
```
ssh -l alice workshop.learndeployment.com
```

### SPECIFYING A PRIVATE KEY

When connecting to a remote machine, SSH will attempt to use one of several
default private keys:

- `~/.ssh/identity` for SSHv1
- `~/.ssh/id_rsa` or `~/.ssh/id_dsa` for SSHv2

If you have a specific private key you wish to use, you can override this
default behavior with the `-i` flag like so:

```
ssh -i /path/to/key workshop.learndeployment.com
```

## EXERCISE

This exercise comes with a private key called `privatekey.pem`. Use it in
conjunction with the `ssh` command to connect with the username `workshop` to
the server running at `workshop.learndeployment.com`.

## LEARNING OBJECTIVES

- How do you specify a private key when using SSH?
- How do you specify which user to connect as when using SSH?
- What are the correct permissions for a private key?
