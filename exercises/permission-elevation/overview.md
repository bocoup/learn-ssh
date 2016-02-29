# WHAT IS PERMISSION ELEVATION AND HOW/WHEN/WHY IS IT USED?

It can be tempting to log in to your server as the administrator or root user.
This is risky for several reasons, the main being that it can be quite easy to
accidentally run a destructive command when you don't mean to. Likewise, if
your session is ever compromised or rogue software is running on your machine,
it will have a much broader reach into your infrastructure.

For these reasons and more it's a best practice to always create a standard user
account for each administrator to use and force them to "elevate" themselves
when needed.

### SUDO

In a Linux environment permissions elevation is most commonly handled with the
`sudo` command. Prefixing any command with `sudo` causes it to be executed with
administrative privileges.

### SUDOERS

Determining who is able to run `sudo` is generally accomplished by editing the
`/etc/sudoers` file. This configuration determines who is able to act as an
administrator, and also specifies what is required to do so (a password in most
cases).

### SU

Sometimes, it's necessary for one user to assume the identity of another for
an extended period. In these cases, the command `su` is used. Invoking it with
no arguments is the same as invoking it with `root`: `su - root`.

An administrator is able to `su - USERNAME` and assume the identity of that user
on the machine provided they are able to authenticate or elevate permissions to
that user. The `exit` command can be used to end the session and return to the
previous user's prompt.

There are *many* usages for the `su` command but for the majority of everyday
tasks `sudo` will likely be sufficient and preferred.

## LEARNING OBJECTIVES

- Why is logging in as the root user a bad idea?
- How can an administrator assume the role of any user on the box?
- How can a regular user execute a single command as an administrator?
- How do you give your account sudo access?
