# ASYMMETRIC CRYPTOGRAPHY

In order for communication between two parties to be secure, it is necessary
that they trust each other. One foundation for building this trust is asymmetric
cryptography, also known as public key cryptography.

Asymmetric cryptography requires two related but different keys: one public,
one private. In its most basic form, secure communication using asymmetric
cryptography looks like this:

```
1. Bob generates a public/private keypair.
2. Bob sends his public key to Alice.
3. Alice encrypts a message with Bob's public key and sends him the resulting
   ciphertext.
4. Bob uses his private key to decrypt the ciphertext, revealing the message.
```

While this method of exchanging messages effectively prevents third parties
from eavesdropping, Bob has no way of knowing who authored the messages he
has received (any number of people may have access to his public key). One
solution for this problem is to use a cryptographic signature.

Before showing how this works, it's important to note that a cryptographic
signature is not meant to be decrypted. It can only be validated (pass/fail).

```
1. Both Bob and Alice generate a public/private keypair.
2. Bob and Alice share public keys with one another.
3. Alice encrypts a message with Bob's public key.
4. Alice wants Bob to be 100% sure that she is the person who sent the message.
   So, she uses her private key to generate a signature based on the ciphertext
   of her message.
5. Alice sends Bob her ciphertext and the corresponding signature.
6. Bob, wanting to verify the author of the message, passes the ciphertext, the
   signature, and his copy of Alice's public key into a cryptographic function.
   This verification function will only return true if all three inputs are
   mathematically linked. If the ciphertext or signature have been tampered with
   in any way, verification will fail.
7. Bob, having verified the ciphertext came from Alice, proceeds as normal by
   decrypting the message using his private key.
```

The assumption in asymmetric cryptography is that possession of the private key
is proof of identity. Keep your private key secure, or anyone can pretend to be
you!

## EXERCISE

Before moving to the next exercise, be sure you have a keypair. If you list the
contents of `~/.ssh` you should see at least two files: `id_rsa` (the private
key) and `id_rsa.pub` (the corresponding public key).

If you don't have these files, create them by following this guide:

https://help.github.com/articles/generating-ssh-keys/

## LEARNING OBJECTIVES

- What are the basics of asymmetric cryptography?
- What is a digital signature used for in SSH?
- Why is asymmetric cryptography used for SSH?
- How do you generate a SSH key?
