# Naming convention for repositories

This is not a must, but I recommend it when you find yourself implementing the projects more often and want to retain a certain overview in your github. I certainly use it.

I recommend the following structure for naming your repositories:
 - first the project Id: Pxxx
 - then the project type you are going for: Console, WebApp, WebApi, GUI, Library ...
 - then the operating system you are going for: Win32, Win64, Linux, MacOS, X (x=cross platform)
 - then the name of the programming language or stack you want to use: C, CSharp, JavaScript, Python...
 - optionally followed by a 3 digit number which is the iteration
and all seperated by hyphens
 - optionally, if there are variants listed in the requirements, you might add the variant number Vxxx you are going for

examples: 
- P001-Console-Linux-C
- P001-Console-Linux-C-002
- P001-Console-Linux-C-003-V004
- P001-Console-Linux-CSharp
- P001-GUI-Win64-CSharp-V001

This might make my repositories a little bit less readable, unless you know what you are looking for. Nontheless it is a more structured approch and it really makes sense in the grand scope of things.
