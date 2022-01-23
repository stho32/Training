# "code2json" a scanner/parser that will convert your code to easily processable json for analytics

There are the following additional common rules that apply:
https://github.com/stho32/Collection-Of-Challenges/blob/master/Common-Requirements.md

## Requirements

- [ ] (R005) there are preconfigured scanners/parsers for the following languages
  - [ ] (R006) C#
  - [ ] (R007) T-SQL
- [ ] (R008) the official output format of the scanner is json
- [ ] (R011) the app can be called with a file filter expression which causes it to scan a directory recursivly and scan all contents at once, e.g. all \*.cs files
- [ ] (R012) in the resulting json you can see which results belong to which source file

- [ ] (R013) answer the following questions on a test set of files of your choice:
  - [ ] (R014) Which files contain references to the t-sql table named xyz? (t-sql)
  - [ ] (R015) What stored procedures do exist? (t-sql)
  - [ ] (R016) Which of those stored procedures contain a reference to the table xyz? (t-sql)
  - [ ] (R017) Which classes are implemented? (c#)
  - [ ] (R018) From which other classes or interfaces are those classes derived from (only direct parents)?
  - [ ] (R019) When you resolve all the direct parents parents, what are the root classes and/or interfaces of each class? E.g. if "Scanner" is derived from "ScannerBase" which is derived from "IScanner" then the root of Scanner is "IScanner".
   

# Variants

You can achieve the goals using different approaches. Here are some ideas (based on c# experience).
- (V001) write your own scanner / parser (should work in any language)
- (V002) use existing libraries for the creation of scanners/parsers
- (V003) find the answers using scanner output
- (V004) find the answers using parser output (walking through the abstract syntax tree)
- (V005) find the answers using reflection on the compiled results

