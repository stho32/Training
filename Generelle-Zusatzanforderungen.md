# Generelle Zusatzanforderungen

Zur professionellen Softwareentwicklung ist es notwendig sich an eine Reihe von Rahmenbedingungen zu halten.
Im Rahmen dieser Challenges simulieren wir diese Umgebung mit folgenden Zusatzanforderungen:

## Zusatzanforderungen

### Qualität des Repositories

- [ ] (Z001) Das Repository sollte eine Dokumentation enthalten
- [ ] (Z002) Wenn es sich um eine kompilierte Sprache handelt, ist ein build-Skript beinhalten, das angibt, wo/wie der Code zu übersetzen ist
- [ ] (Z003) Das Repository enthält einen github-Workflow, der den Code übersetzt und ein neues Release bereitstellt.
- [ ] (Z004) Der Code im Repository hat eine Test-Coverage von 80%, wobei Unit-Test-Bibliotheken aus der Betrachtung ausgeschlossen sind
- [ ] (Z005) Die vorhandenen Unit-Tests werden im Github-Workflow bei jedem Push ausgeführt. Die Bereitstellung des binären Releases wird abgebrochen, wenn die Unit Tests nicht erfolgreich ausgeführt werden konnten

### Laufzeitumgebung

- [ ] (L001) Die Anwendung enthält ein Verständnis von "Umgebung". Dies beinhaltet ein zentrales Umgebungsobjekt, welches Zugriff auf Logging und Konfiguration ermöglicht, oder etwas vergleichbares.
- [ ] (L002) Die Anwendung benutzt einen Logging-Mechanismus. 
- [ ] (L003) Der Logging-Mechanismus gibt die Daten mit Zeitstempel auf der Kommandozeile aus.
- [ ] (L004) Der Logging-Mechanismus könnte um weitere Logging-Ziele erweitert werden.
- [ ] (L005) Der Konfigurations-Mechanismus liest notwendige Konfigurationswerte aus der Kommandozeile.
- [ ] (L006) Der Konfigurations-Mechanismus könnte um weitere Konfigurationsquellen erweitert werden.
