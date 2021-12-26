# Ein externer IMAP-Spam-Filter / Rule-Engine für deinen IMAP Account

Eine Challenge aus https://github.com/stho32/Collection-Of-Challenges

## Anforderungen

- [ ] (A001) Die Anwendung verbindet sich per IMAP mit deinem E-Mail Account
- [ ] (A002) Die Anwendung implementiert mindestens 3 Regeln für die Blacklist-Identifikation von Spam, z.B.
  - [ ] (A003) E-Mails, die keinen Absender oder keine oder keine valide E-Mail-Adresse (mindestens *@*.*) im Absender haben, sind Spam
  - [ ] (A004) E-Mails, die "Amazon" in dem Namen des Absenders angeben, aber nicht von der Domain amazon.de oder amazon.com gesendet wurden, sind Spam
  - [ ] (A005) E-Mails, die in Betreff oder Inhalt bestimmte Schlüsselwörter beinhalten sind Spam
- [ ] (A007) Es gibt mindestens 1 Regel für White-Listing, d.h. expliziten Spam-Ausschluss
  - [ ] (A008) Es gibt die Möglichkeit ein Adressbuch von Kontakten zu konfigurieren, die auf jeden Fall nicht als Spam angesehen werden
- [ ] (A009) Es gibt einen Test-Modus in dem lediglich aufgelistet wird, welche der E-Mails in Deinem Account für Spam gehalten werden
- [ ] (A010) Es gibt einen Modus, in dem identifizierter Spam in den IMAP-Spam-Ordner verschoben wird.

## Zusatzanforderungen

- [ ] (Z001) Das Repository sollte eine Dokumentation und/ oder ein build-Skript beinhalten, das angibt, woe der Code zu übersetzen ist
- [ ] (Z002) Das Repository kann/möchte wenn möglich einen github-Workflow beinhalten, der den Code übersetzt und ein neues Release bereitstellt.
