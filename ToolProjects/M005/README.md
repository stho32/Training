# "prov" Provisioning infrastructure and development environments

When working as a software developer you will constantly need to install stuff and document what you have done. 

This is necessary to e.g.:
- create test environments
- create staging environments
- create production environments (at least you have to be able to communicate the needs to system administrators)
- create consistent developer environments for your developer group
- create consistent build machines for your continuous integration workflow

Optimally you document in a way that is repeatable and can be executed automatically.

When you get stuck and do not know what you need, take 1..n of the projects you have already implemented and think: what if you would need to quickly create all the environments mentioned above for these.

## Requirements

### degree of detail

- [ ] Make sure that you install and/or document the specific version of each tool. Do not simply use "an installer from the internet for node" but instead install node 16.0.10 e.g. to make sure that the environments you create are really consistent.

### locations

- [ ] You can easily set up an environment on a hoster, like vultr.
- [ ] You can easily set up a environment on your local computer.
- [ ] You can easily install a local machine to make it the way you need it. E.g. a physical laptop. Not a virtual machine.

### variants

- you might try to use provisioning tools that are already available, like terraform, ansible, chef ... still, keep in mind that they contain lots of code and might become a weak spot in your environment creation process by themselfs, as they might break when you do not expect it

