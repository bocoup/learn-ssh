# EXERCISE

This exercise contains a [Vagrantfile](http://vagrantup) which we will use to
create a virtual machine running Ubuntu. You can get started using Vagrant with
just a few commands:

- To start the server, run `vagrant up`
- To shut down the server (saving your changes), run `vagrant halt`
- To destroy the server (discarding your changes), run `vagrant destroy`
- To connect to your server, run `vagrant ssh`

## VAGRANT SSH

Now that you understand how SSH works. What do you think is going on under the
hood when you run `vagrant ssh`? As a hint, check out the `.vagrant` folder,
it was created sibling to your Vagrantfile when you ran `vagrant up`.

See if you can connect to the vagrant machine using the `ssh` command directly.
The IP address of your machine is specified in the Vagrantfile. Be sure to
specify the right user!

## ADD YOUR OWN USER

While connected to the VM, create a user for yourself:

`sudo adduser --disabled-password <username>`

Finally, using knowledge from previous exercises, configure an `authorized_keys`
file for the new user using your own public key. Don't forget to set the right
permission and ownership using `chmod` and `chown`!

You'll know you've succeeded when you can ssh to your VM without specifying
a user or private key.

## LEARNING OBJECTIVES

- How do you spin up a VM using Vagrant?
- How do you spin down a VM using Vagrant?
- How do you erase a VM created by vagrant?
- How does `vagrant ssh` work?
- How do you create a user on an Ubuntu machine?
- How do you configure password-less SSH access?
