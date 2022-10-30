# devops

This project is really more of an idea.
You know you have at least one project where the packaging and deployment is not yet automated.
Try it.

e.g.:

-   Use github actions or create a build process using powershell or make ...
-   Zip the results of the build process
-   Upload the zip using ftp or ssh or load it into a database
-   Set a signal (version number) somewhere
-   Let the server check for that signal
-   When the signal is set, let the server trigger a scripted process that downloads and installs the update
