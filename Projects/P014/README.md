# "righteous" A full blown rights management

The aim is to write a full blown generic rights management system including a demo that one could use for a single application or a cluster of apps.

There are the following additional common rules that apply: 
https://github.com/stho32/Collection-Of-Challenges/blob/master/Common-Requirements.md

## Requirements

- [ ] (R001) There are users in the system.
- [ ] (R002) There are groups in the system.

- [ ] (R003) There are two kinds of rights:
    - [ ] (R004) There are individual rights in the system, that are just representing a single thing that can be done.
    - [ ] (R005) There are groups of rights, that always come together. Like access rights normally consist of a right to create, read, write and/or delete that kinda needs to be bunched together all the time.

- [ ] (R006) There are "things" in the system. The defined rights refer to these things.
    - [ ] (R007) A thing can be a database table.
    - [ ] (R008) A thing can be a row or a set of rows in a database table.
    - [ ] (R009) A thing can be one column or a set of columns in a database table.
    - [ ] (R010) A thing can be a selection of rows and columns in a database table.
    - [ ] (R011) A thing can also be a file or a bunch of files on the disk.
    - [ ] (R012) A thing can be an external url describing an resource

- [ ] (R013) The system has a website where you can compfortably configure all those rights.
- [ ] (R014) The system has an integrated api with keys that allow for scripted management and retrieval.



