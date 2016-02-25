# EXERCISE

The instructor of this workshop should have provided you with an un-configured
server to connect to. Copy your public key to the `workshop` user's home directory
with this command:

`scp -i privatekey.pem ~/.ssh/id_rsa.pub workshop@<username>.learndeployment.com:~/`

Next, connect to the machine as the `workshop` user and create your own account:

`sudo adduser --disabled-password <username>`

Finally, using knowledge from previous exercises, configure an `authorized_keys`
file for the new user using the public key you just copied. Don't forget to set
the right permission and ownership using `chmod` and `chown`!

You'll know you've succeeded when you can ssh to your server without specifying
a user or private key.

## LEARNING OBJECTIVES

- How do you create a user on an Ubuntu machine?
- How do you configure passwordless SSH access?
