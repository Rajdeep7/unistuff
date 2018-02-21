## 2 - Grundlagen

### Was sind die Ziele der Informationssicherheit? Beschreibe jeweils, worum es geht, und nenne eine gebräuchliche Maßnahme. Nenne zudem ein zusätzliches Ziel.
1. Confidentiality / Vertraulichkeit - Daten können nur von Berechtigten genutzt werden - Verschlüsselung
2. Integrity / Integrität - Geschützte Daten können nicht unbemerkt und unautorisiert modifiziert werden - Prüfsummen
3. Availability / Verfügbarkeit - Berechtigte können störungsfrei Berechtigungen wahrnehmen - Redundanz
4. Authentizität / Nicht-Abstreitbarkeit

### Nenne zwei Dimensionen zur Einordnung von Sicherheitsmaßnahmen und ihre Werte.
1. technisch / organisatorisch
2. präventiv / detektiv / reagierend

### Was ist die ISO/IEC 27000 und was sind ihre Ziele?
Richtlinie, wendet Grundprinzipien des QM auf das IT-Sicherheitsmanagement an

Ziele:
1. Organisationen sollen keine wichtigen Aspekte übersehen
2. Organisationen sollen Engagement nachweisen können
3. Organisationen sollen organisationsübergreifend vergleichen können

### Was beschreibt die ISO/IEC 27001?
1. Mindestanforderungen an IT-Sicherheit Management Systeme
2. Risikogetriebener Plan - Do - Check - Act Zyklus

### Grenze die Begriffe Security und Safety voneinander ab.
- Safety = Funktionssicherheit / Ausfallsicherheit
- Security = Informationssicherheit = Hardware, Software und Netzbasierte Angriffe und Gegenmaßnahmen
- IT-Sicherheit ist ein Teil von Security ist ein Teil von Safety

## 3 - Technische Schwachstellen und Angriffe

### Wofür stehen die Namen Alice, Bob, Carol, Dave, Eve, Mallory, Trent, Walter gewöhnlich?
- Alice initiiert Protokoll
- Bob = Empfänger
- Carol, Dave zusätzliche Partner
- Eve = Eavesdropper (passiv)
- Mallory = Angreifer
- Trent = TTP
- Walter = Wächter

### Nenne vier Eigenschaften zur Differenzierung von Angriffen, deren verschiedenen Ausprägungen. Nenne zu jeder Ausprägung ein Beispiel.
1. Ziel
  - Confidentiality (Kryptographischen Schlüssel knacken)
  - Integrity (Rootkit)
  - Availability (DDoS)
2. Aktiv / Passiv
  - Aktiv (Stack Smashing)
  - Passiv (Kryptoanalyse)
3. Direkt / Indirekt
  - Direkt (Stack Smashing)
  - Indirekt (Indirekt)
4. Einstufig / Mehrstufig
  - Mehrstufig (Stuxnet)

### Nenne sieben Kategorien von Angriffsvarianten und jeweils ein Beispiel.
1. DoS (SMURF)
2. Malicious Code (Virus)
3. Email (Spam)
4. Mobile Code (JavaScript mit malicious Webserver)
5. Systemnahe Angriffe (Buffer Overflow)
6. Web-basierte Angriffe (XSS)
7. Netzbasierte Angriffe (Port-Scanner)

### Was ist ein DoS Angriff und auf welche 3 Arten kann er ausgeführt werden?
Denial of Service durch
1. Überlastung
2. Fehlersituation
3. Absturz durch Ausnutzung von Programmfehlern

### Nenne drei beschränkte Ressourcen eines OS.
- CPU-Zeit
- Speicher
- Bandbreite

### Nenne drei DoS Attacken, die die Bandbreite aufbrauchen
1. DDoS
2. SMURF
3. SYN-Flooding
4. DNS Amplification Attack

### Was ist IP-Spoofing?
Fälschen der IP-Adresse

### Erläutere den Ablauf von SMURF
1. Mallory schickt Ping an Broadcast IP Adresse mit gefälschter IP-Absender Adresse von Alice
2. Alle Rechner, die auf Broadcast Pings antworten, schicken ihre Antwort an Alice -> Nutzen Bandbreite

### Nenne zwei Gegenmaßnahmen gegen SMURF
1. Nicht auf Broadcast Pings antworten
2. Keine externen IP Pakete mit Broadcast IP Adresse weiterleiten

### Nenne die Schritte einer DNS Amplification Attack
1. Mallory sucht oder erstellt einen langen DNS Eintrag in einem DNS Server
2. Mallory fragt mehrere DNS Server nach dem Eintrag, um sicherzustellen, dass sie ihn im Cache haben. DNS Server müssen auf rekursive Anfragen antworten, sonst schicken sie als Antwort nur eine Weiterleitung an einen anderen DNS Server.
3. Mallory schickt möglichst viele rekursive DNS Anfragen an Server in UDP Paketen mit Alice als Absenderadresse

### Würde DNS Amplification auch mit TCP funktionieren? Warum?
Nein, da beim Verbindungsaufbau von TCP sichergestellt wird, dass die Anfrage auch wirklich von Alice kam. Das heißt, die würde nicht auf die ganzen SYN-ACK Antworten der Server reagieren.

### Nenne zwei Gegenmaßnahmen gegen DNS Amplification
1. Rekursive DNS Auflösung deaktivieren für externe Anfragen
2. Limit für identische Anfragen desselben (vermeintlichen) Clients

### Wie funktioniert SYN Flooding?
1. SYN Paket mit SeqNr x eröffnet den Handshake
2. Opfer reserviert Speicher und Port für einkommende Pakete und antwortet mit SYN, ACK x+1
3. Halboffene TCP-Verbindungen so lange aufbauen, bis Ressourcen von Bob erschöpft sind

### Warum ist der Linux Kernel von SYN Flooding besonders betroffen?
1. Harmloser Exponential Backoff (3, 6, 12 Sekunden)
2. 7 Erlaubte Wiederholungsversuche -> 381 Sekunden Zeit

### Erläutere vier Gegenmaßnahmen gegen SYN Flooding
1. Zufällige halboffene Verbindungen schließen bei Knappheit
2. SYN-RECEIVED Timer
3. Maximale Anzahl an halboffenen Verbindungen pro Quell-Adresse
4. SYN Cookies

### Wie funktionieren SYN Cookies? Welche Informationen enthalten sie?
- Es werden keine Ressourcen reserviert, bis das ACK y+1 von Mallet eingeht
- In der SeqNr werden codiert:
  - 3 Bit MSS "Code"
  - 5 Bit Zeit für Timeout
  - 24 Bit gehashte IP, Port, eigene IP, eigener Port und Zeit aus 5 Bit
- Wenn ACK eintrifft, Zeit checken, Hash checken und tatsächliche MSS nachschauen

### Wann funktionieren SYN Cookies nicht?
Wenn ACK von Alice verloren geht und Alice auf Nachrichten vom Server wartet (z.B. bei SSH)

### Nenne drei Nachteile von SYN Cookies
- Nur 8 verschiedene MSS Werte pro Server möglich
- Keine TCP Options
- Wenn ACK verloren geht

### Nenne die Schritte eines DDoS Angriffs
1. Angreifer kompromittiert eine oder mehrere Masters
2. Master kompromittiert automatisch weitere Maschinen (Daemons) und installiert DDoS Software
3. Angreifer startet Programm auf Master, das den Daemonen die Angriffsdaten mitteilt

### Nenne zwei Gegenmaßnahmen gegen DDoS Angriffe
1. Software-Updates
2. Firewall-Regeln

### Nenne die drei Schritte eines Virus
1. Infektionsteil, suche Programme ohne Signatur und füge Virus ein
2. Schadensteil
3. Sprung an Anfang des Wirtsprogramms

### Was ist eine Virus-Signatur?
Byte-Sequenz, die in einer Virus-Datei enthalten ist. Hilft Virenprogrammen bei der Erkennung

### Nenne 1 Unterschied und 2 Gemeinsamkeiten von Viren und Würmern
1. = Selbstreplikation
2. = Schädlicher Code
3. != Wurm ist ein eigenständiges Programm

### Was ist ein Trojaner? Wie unterscheidet er sich von Viren und Würmern?
Programm mit Nutzfunktionalität und gleichzeitigem Malicious Code, der unbemerkt ausgeführt wird
- Unterschied: Keine Selbstreplikation, eigenständiges Programm

### Nenne drei Gegenmaßnahmen gegen Malicious Code
1. Virenscanner
2. Daten-Backups
3. Software in VM ausprobieren

### Nenne drei Varianten von Malicious Code
1. Virus
2. Trojaner
3. Wurm

### Was ist ein Hoax?
Falsche Geschichte, die rum geht. Im Endeffekt eine Lüge, die per E-Mail verbreitet wird.

### Was ist Phishing?
Versuch, Daten unberechtigt zu erlangen, indem Nutzer zu einer Aktivität gelockt werden, z.B. Weiterleiten von Benutzern auf gefakte Webseiten. 

### Erläutere drei Arten von Spam-Filtern und nenne jeweils einen Vor- und einen Nachteil
1. Blacklist / Whitelist mit Mail-Servern / Mail-Domains
  - Vorteil: Schnell, es muss lediglich der Header gescannt werden
  - Nachteil: Kann zu vielen FP/FNs führen je nach Einstellung
2. Regelbasiert auf Header und Body (Wörter, die vorkommen)
  - Vorteil: Granular
  - Nachteil: Langsamer
3. Machine Learning (NN, Naive Bayes)
  - Vorteil: Lernt dazu
  - Nachteil: Computationally expensive

### Wozu dient Greylisting und wie funktioniert es?
Mail von unbekanntem Tupel (Absender, Quell-Mailserver, Empfänger) ablehnen und Fehlermeldung zurückschicken. Erst nach Wartezeit neue Versuche zulassen.

### Was ist Mobile Code? Wie unterscheidet er sich von Web-basierten Angriffen? Warum heißt er Mobile?
- Schadcode, wird über JavaScript / Flash etc. ausgeführt
- Ist allerdings fest in Webseiten eingebettet
- Mobile, weil er auf entferntem Rechner generiert wird und auf lokalem ausgeführt

### Was ist sicherheits-technisch das Problem von JavaScript? Was ist es bei HTML5?
- JavaScript: kein explizites Sicherheitsmodell. "Identify and Patch" Ansatz
- HTML5: Web Storage API, Cross-Origin Resource Sharing -> Immer mehr Berechtigungen

### Was ist Stack Smashing und wie funktioniert es? 
- Programm erwartet Eingabe
- Programmpuffer wird druch zu große Eingabe / Datenpakete überschrieben
- Dadurch werden Rücksprungadresse und der Stackinhalt darüber überschrieben
- Rücksprungadresse wird so manipuliert, dass sie auf eingefügtes Programm im überschriebenen Stackinhalt verweist

### Was sind die verwendeten Kommandos im Schadcode bei Stack Smashing?
- `system("/bin/sh")` -> Shell mit root-Rechten nutzen
- return-to-libc

### Was ist return-to-libc?
- Schleust keinen eigenen Code ein, sondern nutzt Funktionen der Standard-Funktionsbibliothek, z.B. system() / `system("/bin/sh")`

### Was für Hürden gibt es beim Stack Smashing für einen Angreifer und was ist die jeweilige Lösung? 
- Rücksprungadresse ist absolut -> NOPs Einfügen
- Überschreibbarer Speicher ist begrenzt -> Schadcode dynamisch nachladen
- Quellcode von proprietärer Software nicht verfügbar -> Fuzzing

### Was ist Fuzzing?
Kucken was passiert bei Fehleingaben / Edge Cases, wenn proprietärer Quellcode nicht verfügbar ist.

### Nenne drei Gegenmaßnahmen gegen Stack Smashing
- Sicheres Programmieren - `strncpy` anstatt `strcpy` 
- Stack Guarding - Mehrere Kopien der Rücksprungadresse speichern, bevor Funktion aufgerufen wird
- Nicht ausführbare Stacks (NX bit)

### Was ist das NX bit? Wann hilft es? Wann hilft es nicht?
- Nicht ausführbare Stacks / Kein Code im Stack
- Schützt vor Stack Smashing
- Bringt nichts bei return-to-libc

### Nenne vier Arten von Systemnahen Angriffen
- Buffer Overflow
- Rootkits
- Back Doors
- Password Cracking

### Nenne zwei Buffer Overflow Attacken
1. Stack Smashing
2. Heap Corruption

### Nenne vier Varianten von Password Cracking
1. Brute Force
2. Dictionary Attack
3. Brechen des Hashalgorithmus
4. Social Engineering

### Nenne vier Gegenmaßnahmen gegen Brute-Force Password Cracking
1. Langes Salt, um Nutzung von Hash -> Password Tabellen zu verhindern
2. Aufwendige Hashverfahren
3. Slow Hash Functions
4. Shadow Password System - Nur Root kann Passwörter lesen

### Nenne drei Varianten, eine Back Door zu installieren
1. Versteckter Netzdienst, der hin und wieder auf Kommandos wartet
2. Eintrag in .rhosts bzw authorized_keys
3. SUID-root Programm austauschen mit Schadfunktionalität

### Was ist SUID?
Set Owner User ID upon execution

### Nenne zwei Gegenmaßnahmen gegen Back Doors
1. Überprüfung der offenen Ports und aktiven Netzwerkdienste
2. Suche nach ungewöhnlichen SUID-Programmen

### Nenne die zwei Schritte bei einem Rootkit Angriff
1. Angreifer kompromittiert die Maschine und erlangt root
2. Angreifer installiert Rootkit

### Was ist der Unterschied zwischen Rootkits der 1. und der 2. Generation? Nenne jeweils eine Gegenmaßnahme
1. Generation: Systembefehle wurden ersetzt. Verstecken Prozesse, Dateien, etc. des Angreifers. Gegenmaßnahme: Rootkitscanner chkrootkit
2. Generation: Modifiziert den Kernel, um Dateien vor allen Systemprogrammen zu verstecken. Gegenmaßnahme: Loadable Kernel Modules deaktivieren

### Was ist CSS? Erläutere drei verschiedene Arten.
1. DOM-basiertes (lokales) XSS - über JavaScript und URL Parameter
2. Reflexives (nicht-persistentes) XSS - über PHP und URL Parameter
3. Persistentes (stored) XSS - wird bei jeder Anfrage ausgeliefert

### Nenne zwei Gegenmaßnahmen gegen CSS
1. Escapen von Inputs 
2. JavaScript deaktivieren

### Nenne zwei Arten Web-basierter Angriffe
1. XSS
2. SQL Injection

### Schreibe ein Beispielbefehl einer SQL Injection hin
Bob'; DROP TABLE students;--

### Nenne zwei Arten Netzbasierter Angriffe und je eine Gegenmaßnahme
1. Sniffing - Verschlüsselung
2. Port Scanning - Proaktive Netzüberwachung mit Portscans

### Wofür steht CVSS und was ist sein Ziel?
- Common Vulnerability Scoring System
- Priorisierung von Vulnerabilities

### Was sind Input und Output des CVSS?

### Welche Kennzahlen gibt es im CVSS und was beschreiben sie?

### Woraus bestehen die CVSS Base Metrics?

### Woraus bestehen die CVSS Temporal Metrics?

### Woraus bestehen die CVSS Environmental Metrics?

### Was ist ein Zero-Day Exploit?

### Ordne alle bekannten Varianten von den sieben Kategorien für Angriffe je C, I, A und A zu.

## 4 - Social Engineering

### Nenne zwei Ziele eines Social Engineering Angriffs

### Nenne zwei Arten, Social Engineering zu kategorisieren

### Nenne je drei Beispiele für passive und aktive Social Engineering Angriffe

### Nenne je drei Beispiele für Human- und Computer-based Social Engineering Angriffe

### Nenne vier Gegenmaßnahmen gegen Social Engineering

### Erläutere das Vier-Phasen-Modell nach Fox/Kaun

### Was ist ein Penetration Test?

### Was sind die 5 Phasen eine Social Engineering Penetration Tests?

## 5 - Rechtliche Regelungen

### Was ist der Unterschied zwischen einem Antrags und einem Offizialdelikt?

### Welche drei Elemente beschreibt der §202 StGB? Beschreiben sie jeweils den Tatbestand.

### Welche der drei Elemente des §202 sind Offizialdelikte?

### Was regelt der §303a StGB?

### Was regelt der §303b StGB?

### Nenne 4 Grundprinzipien der Datenschutz-Gesetzgebung

### Nenne 3 Datenschutzgesetze

### Welche Macht hat ein Datenschutzbeauftragter?

### Was ist Auftragsdatenverarbeitung?

### Nenne zwei Regelungen des IT-Sicherheitsgesetzes

## 6 - Kryptographische Grundlagen

### Grenze die Begriffe Krpytographie, Kryptoanalyse und Kryptologie voneinander ab

### Was ist Stenographie? Welche Formen gibt es? Was ist ein Semagramm?

### Was ist ein verdeckter Kanal?

### Woraus besteht ein Krpytographisches System?

### Nenne drei Symmetrische Verfahren

### Nenne drei Asymmetrische Verfahren

### Nenne drei Unterschiede zwischen Symmetrischen und Asymmetrischen Verfahren

### Was sind One-Time Pads? Was sind die Nachteile?

### Nenne die 5 Klassen Kryptoanalytischer Angriffe

## 7 - Symmetrische Kryptosysteme
