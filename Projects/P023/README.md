# "ArgLang" A library to parse command line arguments as if they would be routes

There are the following additional common rules that apply:
https://github.com/stho32/Collection-Of-Challenges/blob/master/Common-Requirements.md

## Requirements

- (R001) The following library works with code similay to this example (example given in c#, may be modified for other target languages)

```csharp
  var parser = new CommandLineParser(
      args, 
      "FTPdeploy is a program that helps you with your ftp based deployment");

  parser.On("describe-dir --local $local-dir [--ignores $ignores] --output $output")
      .Execute((parsedArgs, parser) => {
          Console.WriteLine("Yey! You have a match.");
          Console.WriteLine(parsedArgs.ToString());
      });

  parser.On("describe-dir --ftp $ftp [--ignores $ignores] --output $output").
         Execute((parsedArgs, parser) => {
              Console.WriteLine("Yey! You have a match.");
              Console.WriteLine(parsedArgs.ToString());
          });

  parser.Run();
```

- (R002) The essential thing is that the possible command lines are formulated as strings. 
- (R003) If no command line argument or -h or --help is given then we show a usage-help
- (R004) The parameter parsedArgs is passed to the event handler and provides it with a simple possibility to access the scanned values by parameter name.
- (R005) There are unit tests that explain and validate how/what the following things do
  - (R006) There is the possiblity of adding additional validators to parameters which validate the content before the event handler is called. E.g. you might want to let the library know something is a path to a file and only let it through if the file exists.
  - (R007) There is a way to add aliases to arguments, e.g. --ftp can be abbreviated as -f
  - (R008) "--ignores" is correctly handled as optional argument


