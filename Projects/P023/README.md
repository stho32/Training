# Command Line Argument Parser

A routing-style argument parser teaching command-line interface design, parsing techniques, and validation patterns.

## Level 0 - Basic Parsing
- [ ] Create argument tokenizer
  - Split command line
  - Identify flags
  - Extract values
- [ ] Add route matching
  - Pattern recognition
  - Parameter extraction
  - Basic validation
- [ ] Implement help system
- [ ] Create error handling

## Level 1 - Route Management
- [ ] Add route registration
  - Command patterns
  - Handler binding
  - Parameter mapping
- [ ] Implement optional parameters
- [ ] Add parameter validation
- [ ] Create route conflicts detection
- [ ] Support subcommands

## Level 2 - Parameter Features
- [ ] Add parameter types
  - String values
  - Numeric types
  - Boolean flags
  - File paths
  - Lists/arrays
- [ ] Implement parameter aliases
- [ ] Add default values
- [ ] Create custom validators
- [ ] Support environment variables

## Level 3 - Advanced Features
- [ ] Add command groups
- [ ] Implement middleware
- [ ] Create interactive mode
- [ ] Add command suggestions
- [ ] Support auto-completion
- [ ] Create parameter dependencies

## Level 4 - Documentation
- [ ] Add usage generation
  - Command summary
  - Parameter details
  - Examples
- [ ] Create man pages
- [ ] Add markdown output
- [ ] Implement version info
- [ ] Support localization

## Level 5 - Integration
- [ ] Add plugin system
- [ ] Create API interface
- [ ] Add shell completion
- [ ] Implement logging
- [ ] Support scripting
- [ ] Create testing tools

## Core Features
```csharp
var parser = new CommandLineParser(
    args, 
    "Command description");

parser.On("command --param $value [--optional $opt]")
    .Execute((args, parser) => {
        // Command handler
    });

parser.Run();
```

## Parameter Types
- Required parameters
- Optional parameters
- Flag parameters
- Value parameters
- Array parameters
- Custom validators

## Validation Features
- Type checking
- Value constraints
- File existence
- Custom rules
- Error messages
- Help generation

## Requirements

- (R001) The following library works with code similarly to this example (example given in c#, may be modified for other target languages)

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
  - (R006) There is the possibility of adding additional validators to parameters which validate the content before the event handler is called. E.g. you might want to let the library know something is a path to a file and only let it through if the file exists.
  - (R007) There is a way to add aliases to arguments, e.g. --ftp can be abbreviated as -f
  - (R008) "--ignores" is correctly handled as optional argument
