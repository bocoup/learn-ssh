# SSH KEY PASSPHRASES

Recall that possession of a private key is proof of identity when communicating
securely via asymmetric cryptography. In other words, if a bad actor manages to
obtain your private key, they can digitally impersonate you.

In practice, that means access to all of your servers, github, etc. This single
point of failure is a clear representation of bad information security.

Happily, the solution to this problem is trivial: encrypt your private key with
a passphrase. This protection is a form of two factor authentication. The first
factor is something you have (the private key) and the second is something you
know (the passphrase).

Passphrases are most effective when they are long and complex. Consider using a
phrase or full sentence. If you already have a private key and it does not have
a passphrase, add one with the following command:

```
ssh-keygen -p -f /path/to/key
```

Once your private key is encrypted, you'll need to decrypt it before you can use
it. SSH will handle this automatically, prompting for your passphrase any time
you perform an operation that requires your private key. Without some additional
tooling, this could have you entering your passphrase every time you ssh into a
server, perform git command that communicates with a private remote, etc.

In the next exercise, we'll discuss SSH Agent, a tool that resolves this problem
and provides other highly-desirable features for managing private keys.

## LEARNING OBJECTIVES

- Why is a SSH key passphrase desirable?
- How do you add a passphrase to a private key lacking one?
- What tool can be used to manage private keys?
