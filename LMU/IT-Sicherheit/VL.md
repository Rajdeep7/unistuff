# 1 - Einführung

# 2 - Grundlagen

### Ziele der Informationssicherheit
CIA
- **Confidentiality / Vertraulichkeit**
  - Daten können nur von Berechtigten genutzt werden
  - Maßnahme: Verschlüsselung
- **Integrity / Integrität**
  - Geschützte Daten können nicht unautorisiert und unbemerkt modifiert werden
  - Maßnahme: Prüfsummen
- **Availability / Verfügbarkeit**
  - Autorisierte Subjekte können störungsfrei Berechtigungen wahrnehmen
  - Maßnahme: Redundanz
  
Zusätzliches Ziel: **Verbindlichkeit / Authentizität / Nicht-Abstreitbarkeit**

### Einordnung von Sicherheitsmaßnahmen
- nach technisch / organisatorisch
- nach präventiv / detektiv / reagierend

### ISO/IEC 27000
- Anwendung der Grundprinzipien des **Qualitätsmanagement** auf das Management der Informationssicherheit
- Soll Organisationen helfen, 
  - keine wichtigen Aspekte zu übersehen
  - Engagement nachweisen zu können
  - organisationsübergreifend vergleichen zu können

**ISO/IEC 27001**
- Mindestanforderungen an Information Security Management Systems
- Risikogetriebener [Plan - Do - Check - Act] Zyklus

### Security vs. Safety
- **Safety**: Funktionssicherheit / Ausfallsicherheit bei sicherheitskritischen Programmen
- **Security**: Hardware- / Software- / Netz-basierte Angriffe und Gegenmaßnahmen
- IT-Sicherheit $\subset$ Informationssicherheit / Security $\subset$ Funktionssicherheit / Safety

# 3 - Technische Schwachstellen und Angriffe
Eigenschaften zur Differenzierung 
- Ziel (C,I,A)
- Aktiv / Passiv (Eingriff vs. sniffing)
- Direkt / Indirekt (Manipulation von System X betrifft System Y)
- Ein- / Mehrstufig (Stuxnet)

## DoS und DDoS
- Überlastung / Fehlersituation 
- oder Absturz durch Ausnutzung von Programmierfehlern
- Häufig werden **beschränkte** und **unteilbare** Ressourcen des OS angefordert (CPU-Zeit, Bandbreite)

Aufbrauchen von Bandbreite z.B. durch
- SMURF
- SYN-Flooding
- Low Orbit Ion Cannon

### SMURF
1. Ping an IP-Broadcast Adresse mit gefälschter Absender Adresse von Alice (IP-Spoofing)
2. Alle Rechner aus dem Netz antworten an Alice

Gegenmaßnahmen
1. IP-Broadcast am Router komplett deaktivieren oder nach außen hin deaktivieren
2. Server nicht auf Broadcast-Pings antworten lassen

### DNS Amplification / Reflection Attack
- UDP-Anfrage hat nur 60 Byte, Antwort kann bis zu 3000 Byte haben (Frage nach allen DNS Einträgen in einer bestimmten Zone)
- UDP hat keinen Handshake -> Es kann nicht sichergestellt werden, dass die Anfrage auch wirklich von Alice kommt
- Rekursive Anfrage: DNS-Server löst die komplette Adresse auf und leitet nicht einfach an nen anderen DNS-Server weiter
- Anfragen gehen an Open Resolvers - DNS-Server, die externe rekursive Anfragen beantworten

1. Vorbereitung: ein mal die Anfrage an alle DNS Server, sodass sie sie im Cache haben
2. Ausführung: viele Anfragen 

Gegenmaßnahme:
- Keine rekursiven Anfragen von extern beantworten

### SYN Flooding
- SYN Paket mit SeqNr = x eröffnet den Handshake. 
- Opfer reserviert Speicher (Connection object) und Port für einkommende Pakete und antwortet ACK x+1
- Halboffene TCP-Verbindungen so lange aufbauen, bis Ressourcen von Bob erschöpft sind. Dann kann Bob keine weiteren Verbindungen aufbauen

Linux kernel 2.2.9 besonders betroffen, da
- Harmloser Exponential Backoff (3s, 6s, 12s ...) für Wartezeit für Sende-Wiederholungen
- Viele Erlaubte Wiederholungs-Versuche (7 -> nach 381 Sekunden)

Gegenmaßnahmen:
- Timer für ACK von Mallet, danach Ressourcen freigeben (SYN-RECEIVED Timer)
- Zufällige halboffene Verbindung schließen bei Knappheit
- Maximale Anzahl an halboffenen Verbindungen pro Quell-Adresse
- SYN Cookies
- Micro blocks: administrators can allocate a micro-record (as few as 16 bytes) in the server memory for each incoming SYN request instead of a complete connection object.

### SYN Cookies
- Ressourcen erst reservieren, wenn ACK y+1 von Mallet eingeht
- Bis dahin essentielle Verbindungsinfos in der SeqNr an Mallet codieren:
  - 3 bit MSS "Code"
  - 5 bit Zeit (für Timeout)
  - 24 bit gehashte IP, Port, eigene IP, eigener Port und Zeit aus 5 bit
  - Problem: Wenn ACK y+1 von Alice verloren geht, kommt keine legitime Verbindung zustande
- Wenn ACK eintrifft:
  - Zeit checken (Timeout)
  - 24 bit rehashen und prüfen, ob es ein valider SYN Cookie ist
  - MSS aus 3 bit nachschauen und SYN Queue Eintrag rekonstruieren
  
Nachteile:
- Nur 8 (3 bit) verschiedene MSS Werte pro Server möglich
- Keine TCP Options möglich
- Wenn ACK von Alice verloren geht, denkt Alice, die Verbindung ist zustande gekommen. Bei SSH z.B. wartet Alice dann auf Daten von Bob, aber der sendet weder Daten noch wiederholt er sein SYN+ACK, da er keinen SYN Queue Eintrag angelegt hat -> Application Layer Timeout, was relativ lang dauern kann

### Distributed Denial of Service 
DoS-Angriffswerkzeuge werden auf mehrere Maschinen verteilt und führen auf Befehl eines Masters den Angriff durch.
1. Intruder findet Maschine(n), die kompromittiert werden können -> Werden zum Master
2. Master kompromittiert automatisch weitere Maschinen und installiert DDoS-Software (Daemon)
3. Intruder startet Programm auf Master, das den Daemonen die Angriffsdaten mitteilt

Gegenmaßnahmen:
- Software-Updates
- Firewall-Regeln
- Anomalieüberwachung

## Malicious Code
### Virus
- Kein eigenständiges Programm
- Befehlsfolge, in ein Wirtsprogramm eingefügt:
  1. Infektionsteil, suche Programme ohne Signatur und füge Virus ein
  2. Schadensteil (lösche Daten am 1.1.2018)
  3. Sprung an Anfang des Wirtsprogramms
  
Virus-Signatur: Byte-Sequenz, die in einer Virus-Datei enthalten ist. 
  
### Wurm
- Eigenständiges Programm, benötigt keinen Wirt
- Selbstreplikation

### Trojaner
- Eigenständiges Programm
- Sinnvolle "Nutzfunktionalität"
- Versteckte Schadfunktionalität
- Keine Selbstreplikation

**Staatstrojaner**
- Macht Screenshots, Hört Skype / VoIP ab, Lädt weitere Module nach
- Wird per Registry-Eintrag geladen
- Unsichere Kommunikation mit Command and Control Server -> Malware kann von Dritten gesteuert werden

Gegenmaßnahmen:
- Antiviren-Software
- Keine Software zweifelhafter Herkunft installieren
- Daten-Backups
- Software in VMs ausprobieren

### Ransomware
- Krypto-Erpressungstrojaner

## Email: Hoaxes, Spam, Phishing
- AIDS-Infektion im Kino etc.
- Über 99% aller Mails sind Spam

### Spamfilter
Unterschiedlich schnell / granular
1. Blacklist / Whitelist:  
  Blockieren von Mail-Servern und Mail-Domänen, die üblicherweise von Spammern benutzt werden
2. Regelbasiert im Header und Body
3. Filtersoftware lernt (NN, Bayes)

Greylisting: 
- Jede Email mit unbekanntem Tripel (Absender, Quell-Mailserver, Empfänger) ablehnen und Fehlermeldung zurückschicken
- Erst nach Wartezeit erneute Versuche zulassen

## Mobile Code
- Typischerweise in Webseiten eingebettet
- Nutzt Sicherheitslücken in JavaScript, Flash, HTML5 etc.
- Auf entferntem Rechner generiert und auf lokalem Rechner ausgeführt

Problem mit JavaScript: kein explizites Sicherheits modell / "Identify and Patch" approach
Problem mit HTML5: Web Storage API, WebSockets API, Cross-Origin Resource Sharing

## Systemnahe Angriffe

### Buffer Overflow
- Ziel: Ausführen von Code auf fremdem Rechner unter fremden Rechten

### Variante: Stack Smashing
- Überschreiben von Programmpuffer (z.B. durch Eingabe, Dateien, Datenpakete eines Protokolls) 
- Manipulation der Rücksprungadresse

Erinnerung:

> **The Stack** - When you call a function the arguments to that function plus some other overhead is put on the stack. Some info (such as where to go on return) is also stored there. When you declare a variable inside your function, that variable is also allocated on the stack.
> 
> Deallocating the stack is pretty simple because you always deallocate in the reverse order in which you allocate. Stack stuff is added as you enter functions, the corresponding data is removed as you exit them. This means that you tend to stay within a small region of the stack unless you call lots of functions that call lots of other functions (or create a recursive solution).

From https://stackoverflow.com/questions/79923/what-and-where-are-the-stack-and-heap

<img src="https://github.com/batzner/unistuff/blob/master/img/it-security-buffer-overflow-stack.png?raw=true" width=500/>

**Hürden**
- Rücksprungadresse ist absolut - Lösung: NOPs vor Schadcode
- Wenig Speicher in Stack-Segment - Lösung: Dynamisches Nachladen von Schadcode
- Quellcode von proprietärer Software nicht verfügbar - Lösung: Fuzzing (Kucken, was bei Fehleingaben / Edge Cases passiert)

**Beispiele**
- Nachbildung von `system("/bin/sh")`, um die Shell mit root-Rechten nutzen zu können
- *return-to-libc* -> keinen eigenen Code einfügen, sondern Funktionen der Standard-Funktionsbibliothek nutzen, z.B. `system()`

**Gegenmaßnahmen**
- Sicheres Programmieren `strncpy` statt `strcpy`
- Stack-Guarding - Mehrere Kopien von Rücksprungadresse machen, bevor die Unterfunktion aufgerufen wird
- Nicht-ausführbare Stacks - Keinen Code im Stack ausführen (NX bit), schützt nicht gegen return-to-lib

### Weiter Buffer-Overflow Attacken
- Heap Corruption (Datenstrukturen werden überschrieben)
- Format String Attacks

### Account / Password Cracking
- Brute-Force
- Dictionary Attack
- Brechen des Hashalgorithmus 
- Social Engineering

Salt:
- Zunächst wurde das Password mit sich selbst als Schlüssel verschlüsselt -> Immer derselbe Hash
- Mit Salt muss der Angreifer alle Einträge im Wörterbuch für jedes Passwort / jeden Salt-Wert erneut ausprobieren

Maßnahmen:
- Langes Salt
- Aufwendige Hashverfahren (mehrere Runden)
- Slow Hash Functions verwenden
- Shadow Password System (nur root kann Passwörter lesen)

### Back Doors, Trap Doors
- Dauerhafter Zugang zu kompromittierten Maschine durch
  - Installation eines versteckten Netzdienstes, der hin und wieder auf Kommandos wartet
  - Eintrag in `.rhosts` von root bzw. `authorized_keys` für SSH
  - SUID-root Programm austauschen mit Schadfunktionalität
  
**SUID** 
- "Set Owner User ID upon execution"
- Wenn ein Nutzer eine Datei ausführt hat er die Rechte des Eigentümers der Datei
  
Maßnahmen:
- Überprüfung der offenen Ports und aktiven Netzdienste
- Suche nach ungewöhnlichen SUID-Programmen

### Rootkits
1. Angreifer kompromittiert Maschine und erlangt root
2. Angreifer installiert Rootkit
  - bereinigt Spuren
  - öffnet Backdoors

1. Generation:
- Ersetzt Systembefehle (ls, top, find, netstat, passwd etc.) mit eigenen Varianten
- Verstecken Prozesse, Dateien etc. des Angreifers

2. Generation:
- Modifiziert den Kernel, um Dateien vor **allen** Systemprogrammen zu verstecken
- z.B. durch Loadable Kernel Module unter Linux

Moderne Ausprägungen
- Hypervisor-level Rootkits: Ursprüngliches OS läuft als virtuelle Maschine
- Bootkits: Bootloader wird durch Malware ersetzt
- Hardware / Firmware-Rootkits: BIOS / Firmware der Netzwerkkarte

## Web-basierte Angriffe
### Cross Site Scripting
Einbetten von Schadcode in vertrauenswürdigen anderen Code
1. DOM-basiertes (lokales) XSS
  - Ohne Beteiligung eines Webservers
  - JavaScript schreibt irgendwo URL Parameter ins Dokument -> Schadcode wird in URL Parameter übergeben
  - Mallet bringt Alice dazu, einen Link mit entsprechenden Parametern anzuklicken
2. Reflexives (nicht-persistentes) XSS
  - Webserver liefert Webseite mit Schadcode über URL Parameter aus (z.B. über PHP)
  - Mallet bringt Alice dazu, einen Link mit entsprechenden Parametern anzuklicken
3. Persistentes (stored) XSS
  - Schadcode wird vom Webserver gespeichert und bei jeder Anfrage ausgeliefert
  
Gegenmaßnahme:
- Webserver muss Script-Code entfernen oder escapen
- Client-seitig JavaScript deaktivieren

### SQL Injection
`ID=42;DROP+TABLE+students;--`

## Netzbasierte Angriffe
### Sniffing
- Netzwerkkarten können gesamten Verkehr mithören im WLAN / Ethernet
- Promiscuous Mode: Auch an andere Rechner adressierte Pakete werden gelesen und ans OS durchgereicht
- tcpdump, wireshark, ngrep

### Port-Scanner
- Suchen auf entferntem Rechner nach offenen Ports -> identifizieren Dienste
- Suchen nach Diensten mit bekannten Schwächen

Gegenmaßnahme:
- Proaktive Netzüberwachung mit Portscans

## Common Vulnerability Scoring System
- Hauptziel: Priorisierung
- Drei Gruppen von Kennzahlen:
  - Base Metrics: Grundlegende Verwundbarkeitseigenschaften
  - Temporal Metrics: Zeitabhängige Verwundbarkeitseigenschaften
  - Environmental Metrics: Anwenderspezifische Verwundbarkeitseigenschaften
  
Input:
- Bewetung von Schwachstellen durch vorgegebene Fragen und Antwortmöglichkeiten
Output:
- CVSS-Score [0, 10]
- CVSS-Vektor = Kurzfassung des gesamten Inputs

**Base Metrics**
Konstante intrinsische Eigenschaften von Schwachstellen
- Exploitability metrics
  - Attack vector (Physisch, auf Rechner, LAN, Internet)
  - Attack complexity 
  - Required Privileges
  - User Interaction (was muss das Opfer tun)
- Impact metrics
  - C
  - I
  - A
- Scope -> Auswirkung auf andere Systeme

**Temporal Metrics**
Aktueller Stand
- Exploit Code Maturity
- Remediation Level
- Report Confidence

**Environmental Metrics**
Einsatzgebiet des betroffenen Systems
-> Ändern den Score basierend auf der Bedeuting des betroffenen Systems für die Organisation
- C, I, A Requirements -> gering, mittel, hoch
- Modified Base Metrics -> Falls die Organisation besondere Sicherheitsmaßnahmen einsetzt, die die Base Metric Eigenschaften ändern

## Zero-Day Exploits
Angriff, der eine unbekannte (/soeben erst bekannt gewordene / unbeseitigte) Sicherheitslücke ausnutzt

# Social Engineering
Ziele:
- Informationsgewinnung (vs. Vertraulichkeit)
- Nutzer führt vom Angreifer gewünschte Aktionen aus (vs. Integrität)

## Kategorisierung
Passive Angriffe  (keine Interaktion mit Opfer)
- Belauschen
- Über Schulter schauen
- Durchsuchen von Papiertonnen
- Liegenlassen präparierter USB-Sticks (baiting)
Aktive Angriffe
- Pretexting - Als Mitarbeiter etc. ausgeben
- Phishing
- Internet-Bekanntschaften

Kategorien:
- Human-based Social Engineering
  - Dumpster Diving
  - Shoulder Surfing
  - Tailgating
  - Pretexting
- Computer-based Social Engineering (mit technischen Hilfsmitteln)
  - Phishing
  - Baiting
  - Forensic analysis (Elektronik-Dumpster diving)

## Gegenmaßnahmen
- Aktenvernichtung
- Sichtschutzfolien
- Vereinzelungsanlagen
- Schulungen etc.

Sensibilisierungs-Phasen-Modell:
- Aufmerksamkeit
- Wissen & Einsetllung
- Verstärkung
- Öffentlichkeit

## Penetration Tests
-> White-Hat Hacker identifizieren und melden unbekannte Sicherheitslücken

5 Phasen
1. Planung und Zielfestlegung
2. Informationsakquise und Auskundschaften
3. Spezifikation der Angriffe
4. Angriff
5. Ergebnisbericht und Beratung

# Rechtliche Regelungen
## Strafrecht
- Antragsdelikt: Tat wird auf Anzeige hin verfolgt
- Offizialdelikt: Takt wird "von Amts wegen" (Staatsanwaltschaft) verfolgt

### 

# Fragen in letzter VL
1. Wie genau muss man die Paragraphennummern den Tatbeständen zuordnen können?

# TODO
Alle Angriffsvarianten nach Auswirkung auf Vertraulichkeit, Integrität und Verfügbarkeit bewerten
