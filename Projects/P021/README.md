# "mailrules" an imap based email rule engine with your own spam filter

There are the following additional common rules that apply:
https://github.com/stho32/Collection-Of-Challenges/blob/master/Common-Requirements.md

## Requirements

- [ ] (R001) The app connects to your e-mail account using imap. (Use an interface for the connection method, so you can change or extend the ways the connection works later.)

- [ ] (R002) The following base rules exist and can return "match" or "does not match" as results
  - [ ] (R007) check if the sender has a valid e-mail address (checking it lexically is enough)
  - [ ] (R008) check if the senders email contains a specific text
  - [ ] (R009) check if the subject contains a specific text
  - [ ] (R010) check if the email body contains a specific text
  - [ ] (R011) check if the email subject or body contain a specific text
  - [ ] (R012) check the length of the content in text representation in bytes
  - [ ] (R013) check the length of the content in html representation in bytes
  - [ ] (R014) check the age of an email (days since receiving it)
  - [ ] (R015) check the number of receipients (to + cc)

- [ ] (R016) the following operators are allowed/supported for text based checks
  - [ ] (R017) matches a given regular expression
  - [ ] (R018) starts with
  - [ ] (R019) ends with
  - [ ] (R020) contains
  - [ ] (R021) equals

- [ ] (R022) the following operators are allowed/supported for number based checks
  - [ ] (R023) is less than
  - [ ] (R024) is bigger than

- [ ] (R025) Checks can be combined using and and or. 
- [ ] (R026) We call 1..n checks in combination a "rule".

- [ ] (R027) We call a set of 0..n rules a formula.
- [ ] (R028) The rules within a formula are executed in a given order. As soon as one rule matches the formula is "matched"

- [ ] (R029) When a formula is matched 0..n of the following actions can be executed in a given order:
  - [ ] (R030) delete the email from the inbox/mail folder
  - [ ] (R031) save the mail contents as a json file to the disk
  - [ ] (R032) save the mail contents as an eml file to the disk
  - [ ] (R033) trigger an external application
  - [ ] (R034) move the mail from one imap folder to another

 - [ ] (R035) Use the possible checks and actions to implement a simple spam filter
   - [ ] (R036) create a sub-folder in your email account with the name "mySpam"
   - [ ] (R037) move all emails matching one of the following rules into your "mySpam" folder:
     - [ ] (R038) all emails that are not lexically correct
     - [ ] (R039) emails ending with a domain from countries that you do should not get emails from.
     - [ ] (R040) emails from a sender that says in the name something with "amazon", still the senders email address does not come from a domain called amazon.*

  - [ ] (R041) Use the possible checks and actions to implement a simple ham filter
    - [ ] (R042) create a sub-folder in your email account with the name "knownValidMail"
    - [ ] (R043) there is a learning mode within the app that allows you to whitelist senders of a mail
      - [ ] (R044) every sender you mark as ok is saved into the configuration
      - [ ] (R045) the mails of known senders are moved into your "knownValidMail"-folder

- [ ] (R046) there is a test mode which only lists which formulas would be fulfilled and why but does not execute the actions
- [ ] (R047) there is a mode in which all actions are executed accordingly



