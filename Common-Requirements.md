# Common Requirements

When professionally writing software it is necessary to uphold a set of common standards.
To simulate this we have this file with common requirements:

## Repository Quality

- [ ] (Q001) The repository should contain a documentation that describes all common use cases and how to obtain the executables/library.
- [ ] (Q002) If the content is written in a compiled language the repository should contain a build script.
- [ ] (Q003) The repository should contain a github workflow which will compile the code, build distribution packages and creates a new release.
- [ ] (Q004) Has the code in the repository at least a test coverage of 80%?
- [ ] (Q005) The github workflow should execute the unit tests and fail when they are failing.

## Environment Integration

- [ ] (E001) The application contains an understanding of "environment". An environment is a central class that provides configuration and access to the logging mechanisms.
- [ ] (E002) The application is using a logging mechanism.
- [ ] (E003) When logging to the console every message has a timestamp that is printed with it.
- [ ] (E004) The implemented logging mechanism allows for change of log targets, so everything can be logged to console or a file, or a database or something.
- [ ] (E005) The most basic implementation for aquiring configuration values is reading those values from command line input when requested. 
- [ ] (E006) It is possible to implement other configuration stores (the configuration stores are implemented using an interface that could be overridden)

If no configuration is needed then it is ok not to implement the configuration stuff.
But logging is necessary in any circumstance.


use this snippet to add these rules to all projects
```
There are the following additional common rules that apply:
https://github.com/stho32/Collection-Of-Challenges/blob/master/Common-Requirements.md
```