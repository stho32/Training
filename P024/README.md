# "bld" A generic build script, that autodetects the contents of the repository / directory

(Although named "build script" the script can be a compiled tool as well.)

There are the following additional common rules that apply:
https://github.com/stho32/Collection-Of-Challenges/blob/master/Common-Requirements.md

## Requirements

- [ ] (R001) When run, the script will search the directory tree from its current working directory recursivly
- [ ] (R002) It will autodetect types of programming languages, at least two. Possible ideas:
  - C#
  - python
  - javascript
  - rust
- [ ] (R003) It will detect if the computer, that it runs on, has the needed environment installed. If not, it will set up the computer so that it has. This means for example: 
  - download and install the dotnet sdk
  - download and install python3
  - download and install nodejs
  - download and install rust
- [ ] (R004) It will run build processes using the following process
  - [ ] (R005) build as release
  - [ ] (R006) automatically execute all contained unit tests
  - [ ] (R007) create a release directory and copy all essential stuff into it


