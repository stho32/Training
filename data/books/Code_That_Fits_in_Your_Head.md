# Code That Fits in Your Head - Heuristics for Software Engineering

- authors: Mark Seemann
- published: 2022

## Summary

### Chapter 1: Art or Science?

The author lists different analogies that are usually used when trying to explain what software development is like. Building a house, growing a garden, crafting and more. He shows that, while all of them contain some truth, none fits right. But for the moment software engineering seems right for him and he wants to contribute something in this direction.

### Chapter 2: Checklists

Checklists improve the outcome with no increase in skill.

Consider the following checklist for creating new repositories:

- use git
- automate the build
- turn on all error messages

### Chapter 3: Tackling complexity

Software engineering is about tackling complexity. The brain works in certain ways, e.g. we can only keep track of 7 things in our short term memory. Our code needs to respect that.

### Chapter 4: Vertical Slice

A vertical slice is a good way to start: It contains all layers of architecture for just one functionality.

Your vertical slice has advantages:

- it is working software
- you get early feedback about the life cycle of the development process

Use unit testing ("Walking skeleton"): 

- start with a characterization test, this is a high level test that describes a functionality
- from there on write more tests and code to complete the functionality
- Test code should be in balance. When you turn the code 90 degrees and then point to the middle you should point to the act section (this essentially means that the arrange and assert blocks should have about equal length).

"Documentation should prioritise explaining *why* a descision was made, rather than *what* was decided."

Begin at the outside boundary (user interface) and work your way into the software.
(The author calls this method : outside-in test driven development)

The author lists different other methodologies:

- Test-driven development
- Behaviour-driven development
- Domain-driven design
- Type-driven development
- Property-driven development

"The goal is not to write code fast. The goal is sustainable software."

The author suggests using value objects making the Domain Model easier and easier to test (Example given on Page 71)Also he does not create tests for those value objects, because they are implemented by a tool which makes error probability very low.

- Commit database schema to the Git repository.
- Classes that interact with subsystems are not easily tested. Therefor remove internal logic of those classes to the utmost extend so you do not have much that could fail.




