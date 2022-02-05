# "numbermd" a tool for working with number groups in markdown files

There are [common requirements](https://github.com/stho32/Training/blob/master/Common-Requirements.md) that should be satisfied, too.

## Requirements

In the training repository I use markdown files a lot that describe requirements. The requirements are written as list items with checkboxes. Those list items should always have explicit numbers. 

Now, when such a file grows or changes it becomes difficult to see which numbers are already taken or might be used twice with different descriptions. The tool is there to help with that.

### General Data

- [ ] A number group consists of:
  - [ ] a prefix of some characters, all in upper case
  - [ ] a number in 3 digits
- [ ] We call a combination prefix + specific number a reference. E.g. R001 is a reference, derived from a specific number group.
- [ ] A reference is associated by putting (Xddd) next to the checkbox like so: "- [ ] (R001) ..."
- [ ] A file might contain items using multiple different number groups

### Extracting Information

- [ ] The tool can read a markdown file and list all contained list items that have checkboxes including the information which number is associated.
- [ ] The tool knows what indentation level a specific item is, so you can: 
  - [ ] list items of a specific level, e.g. get the root nodes only from a file
  - [ ] The tool can list the direct children by a given reference to a root node
- [ ] The tool can retrieve all list items from a file as json that also contains the tree structure with root and child nodes

### Linting

- [ ] It will show there is a problem when: 
  - [ ] It finds the same reference associated with list items with different text.
- [ ] It has an option to list all missing numbers from a number group e.g. if you have a reference R001 and one R003 it will tell you that you have not used R002.

### Helping and auto-fixing

- [ ] It will give you the number groups in the file and the next free references for each one
- [ ] It can automatically generate and add references to list items with checkboxes that do not have an associated reference following the rules:
  - [ ] A child of a list item always inherits the number group. E.g. if the parent has a number from the number group "R..." the child gets a number of the group "R...", too.
  - [ ] Each number in each number group is only to be used once in the file.
  - [ ] The automatic completion only adds references above the currently highest reference, it does not fill "the gaps". E.g. if you have R001 and R003 already taken, the next reference it will generate and use is R004. R002 is ignored.
  - [ ] When no number group is given, then R... is used
- [ ] There is an option to remove all references from a file
- [ ] There is an option to remove all references from a parent node and all its children. E.g. `remove-from-subtree R001` will remove all references from a file.

### Import/Export

- [ ] There is an option to export the content to a dot file to visualize the relationships of all list items in the file
- [ ] There is an option to export hte content to flying logic to visualize the relationships of all list items in the file
