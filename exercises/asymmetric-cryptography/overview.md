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

A more visual metaphor for this transaction is thinking of the public key like an 
unbreakable padlock that you give out to anyone you want to be able to securely 
communicate with you. Folks are able to lock a box containing a message with this 
padlock and only the person who holds the key to the lock is able to open the box 
and read the message inside. While this is a great way to prevent third parties 
from learning what is in the locked metaphorical box, there's no way to really know 
who authored the message and locked the box, since the assumption is that you'd give 
out the same padlock to anyone who wanted to securely communicate with you.

In order for Bob to securely identify the message's author Alice would have to provide 
what is known as a cryptographic signature along with her encrypted message. It's 
important to note that a cryptographic signature is not something that is decrypted, 
instead it is validated (pass/fail).

Here's how that same scenario would unfold using cryptographic signatures.

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

#### The assumption in asymmetric cryptography is that possession of the private key is proof of identity. Keep your private key secure, or anyone can pretend to be you!

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
