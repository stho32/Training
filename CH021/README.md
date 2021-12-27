# Ein externer IMAP-Spam-Filter / Rule-Engine für deinen IMAP Account

Eine Challenge aus https://github.com/stho32/Collection-Of-Challenges

## Anforderungen

- [ ] (A001) Die Anwendung verbindet sich per IMAP mit deinem E-Mail Account, es ist aber generell möglich auch andere Methoden der Verbindung zu verwenden
- [ ] (A002) Umgebung
  - [ ] (A003) Die Anwendung nutzt einen Logging-Mechanismus
  - [ ] (A004) Die Anwendung zieht die nötige Konfiguration aus der Kommandozeile
  - [ ] (A005) Mit einem Parameter kann die Konfiguration auch aus einer Konfigurationsdatei gelesen werden

- [ ] (A006) Es gibt folgende Basisregeln, die jeweils einen "Match" oder "keinen Match" zurückliefern können
  - [ ] (A007) Prüfung einer Absende-Email-Adresse auf lexikalische Validität
  - [ ] (A008) Prüfung einer Absende-Email-Adresse auf einen bestimmten Anteil eines Textes
  - [ ] (A009) Prüfung eines E-Mail-Betreffs auf einen bestimmten Text
  - [ ] (A010) Prüfung eines E-Mail-Inhalts auf einen bestimmten Text
  - [ ] (A011) Prüfung eines E-Mail-Betreffs und -Inhalts auf einen bestimmten Text
  - [ ] (A012) Prüfung auf die Länge des Inhaltes des Text-Inhaltes in Bytes
  - [ ] (A013) Prüfung auf die Länge des Inhaltes des HTML-Inhaltes in Bytes
  - [ ] (A014) Prüfung des Alters einer E-Mail (Tage ab dem Empfangszeitpunkt)
  - [ ] (A015) Prüfung auf die Anzahl der Empfänger außer einem selbst (An + Cc)

- [ ] (A016) Folgende Operanden sind für Text-basierte Vergleiche zulässig
  - [ ] (A017) Regulärer Ausdruck
  - [ ] (A018) Beginnt mit
  - [ ] (A019) Endet mit
  - [ ] (A020) Enthält
  - [ ] (A021) Entspricht

- [ ] (A022) Folgende Operanden sind für numerische Vergleiche zulässig
  - [ ] (A023) Kleiner als
  - [ ] (A024) Größer als

- [ ] (A025) Die Basisregeln können mit UND und ODER kombiniert werden. Das gemeinsame Konstrukt nennt sich Regel.

- [ ] (A026) Die Kombination einer Regel mit 1..n Aktionen nennt sich Formel.

- [ ] (A027) Folgende Aktionen sind möglich, wenn die Regel einer Formel als erfüllt identifiziert wird:
  - [ ] (A028) Löschen der E-Mail aus dem E-Mail-Account
  - [ ] (A029) Speichern einer E-Mail als JSON auf der Festplatte
  - [ ] (A030) Speichern einer E-Mail als eml auf der Festplatte
  - [ ] (A031) Triggern einer externen Anwendung
  - [ ] (A032) Bewegung einer E-Mail von einem Ordner in einen anderen E-Mail-Ordner

 - [ ] (A033) Benutze die Regeln für einen einfachen Spam-Filter
   - [ ] (A034) Erstelle einen Unter-Ordner in deinem E-Mail-Account "MySpam"
   - [ ] (A035) Verschiebe automatisiert alle E-Mails aus deinem Posteingang in diesen Ordner, die folgende Merkmale aufweisen
     - [ ] (A036) Alle E-Mails, deren Absende-Email-Adresse keine lexikalische Validität aufweisen
     - [ ] (A037) E-Mails mit Domänenendungen, die aus Ländern kommen, aus denen Du nie Post erhalten würdest
     - [ ] (A038) E-Mails von einem Absendenamen der "Amazon" enthält, die aber nicht von amazon.* gesendet wurden

  - [ ] (A039) Benutze die Regeln für einen einfachen Ham-Filter
    - [ ] (A040) Erstelle einen Unter-Ordner "Bekannte Absender"
    - [ ] (A041) Es gibt einen Lern-Modus, in dem zu jeder E-Mail im Eingang angegeben werden kann, ob dieser ok ist
      - [ ] (A042) Jede "bekannte" E-Mail-Adresse wird gespeichert
      - [ ] (A043) Bekannte E-Mail-Adressen werden in der Folge automatisch in den Ham-Ordner sortiert

- [ ] (A044) Es gibt einen Test-Modus in dem lediglich aufgelistet wird, welche Formeln angewandt würden
- [ ] (A045) Es gibt einen Modus, in dem die Formeln angewandt werden


