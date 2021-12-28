# CH023 - Eine Bibliothek zum Parsen von Kommandozeilen

- (A001) Die Bibliothek kann etwas mit einem so formulierten Quelltext anfangen (Beispiel in C#, darf entsprechend der Zielsprache umformuliert werden). 

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

- (A002) Das wesentliche hieran ist, dass die Kommandozeilen als Zeichenkette formuliert werden. 
- (A003) Wenn keine Kommandozeilenparameter angegeben werden, oder -h oder --help, dann wird eine usage-Hilfe angezeigt.
- (A004) Im Parameter parsedArgs wird an den Ereignishandler eine Möglichkeit übergeben auf die Daten der Parameter zuzugreifen
- (A005) Es gibt Unit-Tests, die die Fähigkeiten demonstrieren
  - (A006) Es gibt Validatoren, die an jeden Parameter zusätzlich angehängt werden können, die dann den Inhalt prüfen und ggf. vor der Verarbeitung (Ereignisbehandlung) abbrechen
  - (A007) Es gibt die Möglichkeit zu Argumenten, z.B. "--ftp", ein Alias anzugeben, z.B. -f .
  - (A008) "--ignores" ist ein optionaler Parameter, er kann vorhanden sein, muss aber nicht

## Zusatzanforderungen

Es gelten die generellen Zusatzanforderungen aus [Generelle-Zusatzanforderungen.md](../Generelle-Zusatzanforderungen.md).
