## 1 - Einführung

### Wie schnell hat sich der SQL Slammer in der ersten Minute ausgebreitet? Wie schnell waren wie viele Hosts infiziert? 
- Verdopplung alle 8 Sekunden
- 90% nach 10 Minuten
- 75.000 nach 30 Minuten

### Wie hat sich der SQL Slammer ausgebreitet? Welche Form von Scanning hat er verwendet? Wie hoch war die Probing Rate?
- 376 UDP Paket
- Buffer Overflow Bug -> Konnte Registry öffnen
- Random Scanning
- 26,000 Scans pro Sekunde

### Wie viele Infektionsversuche hat der SQL Slammer insgesamt nach 1 Minute pro Sekunde durchgeführt?
- 26,000 Scans pro Sekunde
- 8 Verdopplungen in der ersten Minute -> 256 Hosts * 26,000 Scans = 6,6 Mio

## 2 - Grundlagen

### Was sind die Ziele der Informationssicherheit? Beschreibe jeweils, worum es geht, und nenne eine gebräuchliche Maßnahme. Nenne zudem zwei zusätzliche Ziele.
1. Confidentiality / Vertraulichkeit - Geschützte Daten können nur von Berechtigten genutzt werden - Verschlüsselung
2. Integrity / Integrität - Geschützte Daten können nicht unbemerkt und unautorisiert modifiziert werden - Prüfsummen
3. Availability / Verfügbarkeit - Berechtigte können störungsfrei Berechtigungen wahrnehmen - Redundanz
4. Authentizität - Subjekte sind die, für die sie sich ausgeben / Betrug kann leicht erkannt werden - CA
5. Nicht-Abstreitbarkeit - Digitale Signaturen

### Beschreibe das Bell LaPadula Modell. Welche Form von Zugriffskontrolle implementiert es? Was ist eine Dominance Relation?
- Setzt Mandatory Access Control um
- Schützt die Vertraulichkeit von Daten
- Dominance Relation = Inverse von [Information]-Can-Flow Relation
- Drei Regeln
  1. No-Read-Up - Tiefe Personen dürfen nicht Dateien von hohen Personen lesen
  2. No-Write-Down - Hohe Personen dürfen nicht in Dateien von tiefen Personen schreiben -> Können nicht Informationen leaken
  3. Access-Control Matrix definiert Zugriff von Subjekt auf Objekt

### Nenne zwei Dimensionen zur Einordnung von Sicherheitsmaßnahmen und ihre Werte.
1. Technisch /organisatorisch
2. Präventiv / detektiv / reagierend

### Was ist die ISO/IEC 27000 und was sind ihre Ziele?
Richtlinie, wendet Grundprinzipien des QM auf das IT-Sicherheitsmanagement an

Ziele:
1. Organisationen sollen keine wichtigen Aspekte übersehen
2. Organisationen sollen Engagement nachweisen können
3. Organisationen sollen organisationsübergreifend vergleichen können

### Was beschreibt die ISO/IEC 27001? Aus welchen Elementen besteht sie?
- Mindestanforderungen an IT-Sicherheit Management Systeme
- Risikogetriebener Plan - Do - Check - Act Zyklus
- Elemente:
  - Organisation der Informationssicherheit
  - Verwaltung der Werte
  - Kryptographie
  - Physische Sicherheit
  - Personal Sicherheit
  - etc.

### Was ist ein Information Security Management System?
- Aufstellung von Verfahren und Regeln
- Innerhalb eines Unternehmens
- Zur Definition, Steuerung, Kontrolle und Verbesserung von Informationssicherheit

### Nenne die 4 Schritte des Risikomanagements
1. Identifikation
2. Klassifikation
3. Risikobewertung / Gewichtung
4. Risikobehandlung oder Risikoakzeptant

### Grenze die Begriffe Security und Safety voneinander ab und nennen sie zwei Beispiele pro Themengebiet
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
- Trent = Trusted Third Party
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
  - Indirekt (-)
4. Einstufig / Mehrstufig
  - Einstufig (-)
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

### Nenne drei beschränkte Ressourcen eines OS
- CPU-Zeit
- Speicher
- Bandbreite

### Nenne vier DoS Attacken, die die Bandbreite aufbrauchen
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
- Wenn ACK eintrifft, Zeit checken, Hash checken und tatsächliche MSS nachschauen -> SYN Queue Eintrag rekonstruieren

### Nenne drei Nachteile von SYN Cookies
- Nur 8 verschiedene MSS Werte pro Server möglich
- Keine TCP Options möglich
- Wenn ACK von Alice verloren geht, denkt Alice, die Verbindung ist zustande gekommen. Bei SSH z.B. wartet Alice dann auf Daten von Bob, aber der sendet weder Daten noch wiederholt er sein SYN+ACK, da er keinen SYN Queue Eintrag angelegt hat -> Application Layer Timeout, was relativ lang dauern kann

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
1. == Selbstreplikation
2. == Schädlicher Code
3. != Wurm ist ein eigenständiges Programm

### Was ist ein Warhol Wurm?
Infiziert in 15 Minuten viele Hosts (wie auch immer), z.B. SQL Slammer

### Erkläre 4 Arten der Wurm-Verbreitung und nenne jeweils einen Vorteil und einen Nachteil
1. Random Scanning -> Zufällige IP-Adressen
   - Vorteil: Wenig Code, Tod von Wurm-Instanzen ist nicht schlimm
   - Nachteil: Redundanz, Ineffizient, falls es wenige angreifbare Hosts gibt
2. Topological Scanning -> Information auf dem Host nutzen, z.B. Logs Parsen
   - Vorteil: Effizient, Unauffällig
   - Nachteil: Erreicht keine Saturation, Viel Code
3. Hit-List Scanning -> Vordefinierte Liste an angreifbaren Hosts
   - Vorteil: Schnelle Ausbreitung
   - Nachteil: Große Liste, Teilweise Redundanz für Fehlertoleranz nötig
4. Permutation Scanning -> Vordefinierte Permutation von IP-Adressen (z.B. durch 32 bit Cipher)
   - Vorteil: Wenig Code, Keine Redundanz (wenn System schon infiziert, springt er mehrere IPs weiter), Perfekte Fehlertoleranz
   - Nachteil: Ineffizient, falls es wenige angreifbare Hosts gibt

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

### Erkläre drei Arten zur Erkennung von Malicious Code. Nenne jeweils Vorteile und Nachteile
- Signatur-basiert
  - Erkennt Malware, falls exakte Folge an Codebefehlen im Programm erkannt wird
  - Vorteil: Gut gegen alte noch aktive Malware
  - Nachteil: Veröffentlichung dauert teilweise lange, Kann leicht umgangen werden
- Heuristisch/Anomalie-basiert
  - Sucht nach auffälligem Verhalten, z.B. Registering for Autostart, Installing rootkits etc.
  - Statische Analyse
  - Vorteil: Schützt gegen neue Malware Attacken
- Emulations-basiert
  - Dynamische Analyse
  - Nachteil: Malware kann erkennen, dass sie in einer Sandbox läuft, Langsamer, oft Cloud-basiert
  
### Was ist ein polymorpher Virus?
Virus, der seinen Code bei der Selbstreplikation ändert, um nicht über Signaturen erkannt zu werden.
  
### Nenne drei Methoden, die Malware nutzt, um nicht von Virenscannern erkannt zu werden
- Garbage Instruction
- Instruction Reordering
- Interchangeable Instructions

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
  
### Welche rechtlichen Probleme ergeben sich aus der Nutzung von Spam Filtern?
Wenn eine Mailadresse für den geschäftlichen Verkehr eröffnet ist, muss täglich der Spam-Ordner kontrolliert werden.

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
- Programmpuffer wird durch zu große Eingabe / Datenpakete überschrieben
- Dadurch werden Rücksprungadresse und der Stackinhalt darüber überschrieben
- Rücksprungadresse wird so manipuliert, dass sie auf eingefügtes Programm im überschriebenen Stackinhalt verweist

### Was sind zwei mögliche verwendete Kommandos im Schadcode bei Stack Smashing?
- Shellcode: Nachbildung von `system("/bin/sh")` in Assembler, um die Shell mit root-Rechten nutzen zu können
- *return-to-libc* 
  - Keinen eigenen Code einfügen, sondern Funktionen der Standard-Funktionsbibliothek nutzen, z.B. `system()`
  - Parameter für die `system` Funktion werden über den Eintrag mit der Rücksprungadresse geschrieben

### Was ist return-to-libc?
- Schleust keinen eigenen Code ein, sondern nutzt Funktionen der Standard-Funktionsbibliothek, z.B. system() / `system("/bin/sh")`

### Was für Hürden gibt es beim Stack Smashing für einen Angreifer und was ist die jeweilige Lösung? 
- strcpy bricht bei Nullbytes (0x00) ab - Lösung: String Encoder verwenden
- Rücksprungadresse ist absolut - Lösung: NOPs vor Schadcode
- Wenig Speicher in Stack-Segment - Lösung: Dynamisches Nachladen von Schadcode
- Quellcode von proprietärer Software nicht verfügbar - Lösung: Fuzzing (Kucken, was bei Fehleingaben / Edge Cases passiert)

### Was ist Fuzzing?
Kucken was passiert bei Fehleingaben / Edge Cases, wenn proprietärer Quellcode nicht verfügbar ist.

### Nenne vier Gegenmaßnahmen gegen Stack Smashing
- Sicheres Programmieren - `strncpy` statt `strcpy`
- Stack-Guarding 
  - Vor Rücksprungsadresse ein Canary ablegen und danach prüfen, ob es noch intakt ist
  - Kann vom Compiler automatisch generiert werden, Prüfwert wird in globaler Variable gespeichert
  - Variante: Mehrere Kopien von Rücksprungadresse machen, bevor die Unterfunktion aufgerufen wird
- Nicht-ausführbare Stacks - Keinen Code im Stack ausführen (NX bit), schützt nicht gegen return-to-libc
- Address Space Layout Randomization
  - Auch Speicheradressen der Systemfunktionen werden zufällig erteilt
  - Schützt gegen return-to-libc

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

### Was ist eine Back Door? Nenne drei Varianten, eine Back Door zu installieren
Dauerhafter Zugang zu kompromittierten Maschine durch
1. Versteckter Netzdienst, der hin und wieder auf Kommandos wartet
2. Eintrag in .rhosts bzw authorized_keys
3. SUID-root Programm austauschen mit Schadfunktionalität

### Was ist SUID?
Set Owner User ID upon execution - Wenn ein Nutzer eine Datei ausführt hat er die Rechte des Eigentümers der Datei

### Nenne zwei Gegenmaßnahmen gegen Back Doors
1. Überprüfung der offenen Ports und aktiven Netzwerkdienste
2. Suche nach ungewöhnlichen SUID-Programmen

### Nenne die zwei Schritte bei einem Rootkit Angriff
1. Angreifer kompromittiert die Maschine und erlangt root
2. Angreifer installiert Rootkit
  - bereinigt Spuren
  - öffnet Backdoors
  
### Erkläre die drei Bestandteile eines Rootkits
- Droper -> Wird von User gestartet, startet Loader und entfernt sich
- Loader -> Sorgt für BufferOverflow und lädt das Rootkit in den Speicher
- Rootkit

### Was ist der Unterschied zwischen Rootkits der 1. und der 2. Generation? Nenne jeweils eine Gegenmaßnahme
1. Generation: Systembefehle wurden ersetzt. Verstecken Prozesse, Dateien, etc. des Angreifers. Gegenmaßnahme: Rootkitscanner chkrootkit
2. Generation: Modifiziert den Kernel, um Dateien vor allen Systemprogrammen zu verstecken. Gegenmaßnahme: Loadable Kernel Modules deaktivieren

### Erkläre drei unterschiedliche Rootkit-Modi
1. Application Rootkits -> 1. Generation
2. Kernelmode Rootkits -> 2. Generation
3. Usermode Rootkits
  - Benötigen keinen Zugriff auf den Kernel
  - Klinken sich in alle Prozesse ein
  - Leiten Auführung von API-Funktionen auf sich um
  - Unter Windows Populär
  
### Nenne drei Anti-Forensik-Maßnahmen eines Rootkits
- Data Destruction - Möglichst wenig Spuren / Beweise hinterlassen
- Data Concealment - Hinterlassene Spuren sollten schwer zu entdecken sein
- Data Fabrication - Hinterlasse falsche Spuren

### Was ist CSS? Erläutere drei verschiedene Arten.
1. DOM-basiertes (lokales) XSS - über JavaScript und URL Parameter
2. Reflexives (nicht-persistentes) XSS - über PHP und URL Parameter
3. Persistentes (stored) XSS - wird bei jeder Anfrage ausgeliefert

### Nenne drei Gegenmaßnahmen gegen CSS
1. Escapen von Inputs 
2. JavaScript deaktivieren
3. HTTPOnly -> Attribut bei HTTP Cookies, sodass JavaScript nicht auf den Cookie zugreifen kann

### Wie funktioniert Cross-Site-Request-Forgery?
- Problem: Ein mal authentisiert, schickt der Browser implizit jedes Mal seine Sitzungsdaten an den Server
- Angreifer bewirkt HTTP-Anfrage ohne Wissen des Opfers (z.B. RESTApi Call, der die Rechte eines Nutzers ändert)
- Z.B. über falsche URL bei einem img Tag oder über tinyurl per Mail

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
- Input: Bewertung von Schwachstellen durch vorgegebene Fragen und Antwortmöglichkeiten
- Output: CVSS-Score und Vektor

### Welche Kennzahlen gibt es im CVSS und was beschreiben sie?
- Base Metrics: Grundlegende Verwundbarkeitseigenschaften
- Temporal Metrics: Zeitabhängige Verwundbarkeitseigenschaften
- Environmental Metrics: Anwenderspezifische Verwundbarkeitseigenschaften

### Woraus bestehen die CVSS Base Metrics?
- Exploitability metrics 
  - Attack Vector (Physisch, auf Rechner, LAN, Internet)
  - Attack Complexity 
  - Required Privileges
  - User Interaction (was muss das Opfer tun)
- Impact metrics: C, I, A
- Scope - Auswirkung auf andere Systeme

### Woraus bestehen die CVSS Temporal Metrics?
- Exploit Code Maturity
- Remediation Level
- Report Confidence

### Woraus bestehen die CVSS Environmental Metrics?
- C, I, A Requirements
- Modified Base Metrics

### Was ist ein Zero-Day Exploit?
Angriff, der eine unbekannte / soeben erst bekannt gewordene / unbeseitigte Sicherheitslücke ausnutzt

### Nenne alle bekannten Varianten von den sieben Kategorien für Angriffe
1. DoS -> Availability zentral
   1. SMURF
   2. DNS Amplification
   3. SYN Flooding
   4. DDoS
2. Malicious Code
   1. Virus
   2. Wurm
   3. Trojaner
3. E-Mail -> Confidentiality, Authenticity
   1. Hoax
   2. Spam
   3. Phishing
4. Mobile Code - JavaScript, HTML, Flash
5. Systemnahe Angriffe
   1. Buffer Overflow / Stack Smashing
   2. Rootkits
   3. Password Cracking
   4. Back Doors
6. Web-basierte Angriffe
   1. XSS
   2. SQL Injection
7. Netzbasierte Angriffe
   1. Sniffing
   2. Port Scanning

## 4 - Social Engineering

### Nenne zwei Ziele eines Social Engineering Angriffs
1. Informationsgewinnung (vs. Vertraulichkeit)
2. Nutzer führt vom Angreifer gewünschte Aktionen aus (vs. Integrität)

### Nenne zwei Arten, Social Engineering zu kategorisieren
- Passiv vs. Aktiv
- Human- vs. Computer-based

### Nenne je drei Beispiele für passive und aktive Social Engineering Angriffe
Passiv:
1. Belauschen
2. Shoulder Surfing
3. Dumpster Diving
4. Liegenlassen präparierter USB-Sticks (Baiting)

Aktiv:
1. Phishing
2. Pretexting
3. Internet-Bekanntschaften

### Nenne je drei Beispiele für Human- und Computer-based Social Engineering Angriffe
Human-based:
1. Dumpster Diving
2. Shoulder Surfing
3. Tailgating
4. Pretexting

Computer-based:
1. Forensic analysis
2. Phishing
3. Baiting

### Nenne vier Gegenmaßnahmen gegen Social Engineering
1. Vereinzelungsmaschinen
2. Aktenvernichtung
3. Sichtschutzfolien
4. Schulungen

### Erläutere das Vier-Phasen-Modell nach Fox/Kaun
1. Aufmerksamkeit
2. Wissen & Einstellung
3. Verstärkung
4. Öffentlichkeit

### Erkläre drei Varianten des Phishing
- Spear Phishing - Zielen auf bestimmte Personen ab, Angreifer sammelt erst Informationen
- Clone Phishing 
  - Kopiert Email und schickt veränderten Anhang / Inhalt (Hier ist die aktualisierte Version)
  - Funktioniert gut über bereits kompromittierte Maschinen
- Whaling - Angriff auf Senior Executives

### Was sind 4 Elemente einer Phishing Attacke?
- Link-Spoofing (angezeigter Link != tatsächlicher Link)
- Ähnliche Absender Adresse (1 und l vertauschen z.B.)
- Vertrauen etablieren (ähnliches Design etc.)
- Call to Action

### Was ist ein Penetration Test?
White-Hat Hacker identifizieren und melden unbekannte Sicherheitslücken

### Was sind die 5 Phasen eine Social Engineering Penetration Tests?
1. Planung und Zielfestlegung
2. Informationsakquise
3. Spezifikation der Angriffe
4. Angriff
5. Ergebnisbericht und Beratung

## 5 - Rechtliche Regelungen

### Was ist der Unterschied zwischen einem Antrags und einem Offizialdelikt?
Antragsdelikt wird nur verfolgt, falls es eine Anzeige gibt. Offizialdelikt wird von Amts wegen verfolgt.

### Welche drei Elemente beschreibt der §202 StGB? Beschreiben sie jeweils den Tatbestand.
1. Ausspähen von Daten
  - Zugang
  - unbefugt / nicht für Täter bestimmt
  - Überwindung einer Zugangssicherung
  - elektronisch gespeicherte oder übermittelte Daten
2. Abfangen von Daten
  - Datenbeschaffung
  - unbefugt
  - aus nichtöffentlicher Datenübermittlung
3. Vorbereitung von a und b durch Passwörter oder Computerprogramme

### Welche der drei Elemente des §202 sind Offizialdelikte?
Nur §202c

### Was regelt der §303a StGB?
Datenveränderung

### Was regelt der §303b StGB?
Computersabotage

### Nenne und erkläre 3 verschiedene Arten von Daten
- Nutzungsdaten -> Identifikation des Nutzers + Metadaten über Nutzung
- Bestandsdaten -> Vertragliche Daten eines Nutzers -> Bei Anfang, Änderung und Ende des Vertrags erhoben
- Inhaltsdaten -> Inhalt einer Kommunikation

### Nenne 4 Grundprinzipien der Datenschutz-Gesetzgebung
1. Generelles Verbot mit Erlaubnisvorbehalt
2. Datenvermeidung / -sparsamkeit
3. Zweckbindung
4. Transparenz

### Nenne 3 Datenschutzgesetze
1. BayDSG
2. BDSG
3. EU-Datenschutzgrundverordnung

### Welche Macht hat ein Datenschutzbeauftragter?
Gar keine, nur beratend, kein Veto-Recht

### Was ist Auftragsdatenverarbeitung?
Datenverarbeitung wird ausgelagert an andere Stelle im Auftrag.

### Nenne zwei Regelungen des IT-Sicherheitsgesetzes
1. Webserver-Betreiber müssen Kundendaten nach Stand der Technik schützen
2. AKW-Betreiber müssen erhebliche IT-Sicherheitsvorfälle melden

## 6 - Kryptographische Grundlagen

### Grenze die Begriffe Kryptographie, Kryptoanalyse und Kryptologie voneinander ab.
- Kryptographie - Verschlüsseln und Entschlüsseln von Nachrichten
- Kryptoanalyse - Entschlüsseln von Nachrichten, ohne im Besitz des Schlüssels zu sein
- Kryptologie = Kryptographie + Kryptoanalyse

### Was ist Stenographie? Welche Formen gibt es? Was ist ein Semagramm?
- Stenographie = Methoden, die bereits die Existenz einer geheimen Nachricht verbergen
- Linguistische und Technische Stenographie
- Semagramm = geheime Nachricht im Bild

### Was ist ein verdeckter Kanal?
Nachrichtentransport über nicht erkennbares Medium

### Woraus besteht ein Krpytographisches System?
(K, M, C, e, d)

### Nenne drei Symmetrische Verfahren
DES, AES, Serpent, Blowfish

### Nenne drei Asymmetrische Verfahren
RSA, ElGamal, DSA

### Nenne drei Unterschiede zwischen Symmetrischen und Asymmetrischen Verfahren
1. Schnelligkeit (Faktor 100-1000)
2. Gemeinsamer Schlüssel
3. Schlüsselgröße - 128/256 vs. 2048 / 4096

### Was sind One-Time Pads? Was sind die Nachteile?
- Schlüssel wird niemals wiederverwendet
- Schlüssel ist mindestens genauso lang wie der Klartext
- Schlüssel wird auf Nachricht modulo 26 addiert

Nachteile:
- Schlüsselmanagement aufwendig
  - Viele echte Zufallszahlen nötig
  - Schlüssel müssen sicher ausgetauscht werden
- Keine Integritätssicherung

### Nenne die 5 Klassen Kryptoanalytischer Angriffe
1. Brute Force
2. Ciphertext-only
3. Known-plaintext
4. Chosen-ciphertext
5. Chosen-plaintext

## 7 - Symmetrische Kryptosysteme

### Nenne zwei Forderungen an Kryptosysteme und erkläre, was sie bedeuten
- Konfusion - es kann möglichst wenig von Chiffretext auf Klartext geschlossen werden
- Diffusion - kleine Inputänderungen -> große Outputänderungen

### Was für ein Chiffre ist DES? Mit wie viel Bit? Wie lang ist der Schlüssel?
- Blockchiffre mit 64 Bit
- Schlüssellänge 64 Bit, davon 8 Paritätsbits (jedes 8.)

### Welche Operationen nutzt DES?
Permutation, Substitution und XOR

### Aus welchen 3 groben Schritten besteht DES?
1. Initialpermutation
2. 16 Schlüsselabhängige Iterationen mit je einem 48 Bit Teilschlüssel
3. Inverse Initialpermutation

### Wozu dient die Initialpermutation bei DES?
- Verteilt Bits gleichmäßig auf linke und rechte Hälfte
- Verbessert die Sicherheit nicht, nur die Hardware-Implementierung

### Skizziere eine DES Iteration
https://github.com/batzner/unistuff/raw/master/LMU/IT-Sicherheit/img/des-iteration.png

### Aus welchen 4 Schritten besteht die DES Funktion?
1. Expanson (fix)
2. XOR mit Teilschlüssel
3. S-Box Substitution von 6 zu 4 Bit
4. Permutation (fix)

### Skizziere die DES Funktion
https://github.com/batzner/unistuff/raw/master/LMU/IT-Sicherheit/img/des-funktion.png

### Wie werden die Teilschlüssel bei DES generiert?
1. Kürzung auf relevante Bits -> 56 Bit
2. Permutation
3. Aufteilen in C und D
4. Zyklisches shiften nach links der Blöcke
5. C(i) und D(i) nach jedem Shift zusammenfügen
6. Aus C(i)+D(i) bestimmte Bits entfernen und nochmal permutieren -> 48 Bit

### Was ist bei der DES Entschlüsselung anders?
- Schlüsselreihenfolge ist umgekehrt

### Nenne drei Stärken von DES
1. Avalanche-Effekt durch S-Boxen und Permutation. Ein Bit verursacht Änderung von durchschnittlich 50% der Ausgabe
2. 16 Iterationen - Brute Force ist genauso effizient wie known-plaintext bei 16+ Iterationen
3. Hardware-effizient, da Iterationen und ähnliche Ver- / Entschlüsselung

### Nenne drei Schwächen von DES
1. Teilweise geheimes Design
2. Zu geringe Schlüssellänge
3. Optimiert auf Implementierung in Hardware, IP und IIP verbessern die Sicherheit nicht

### Wie funktioniert 3DES?
Verschlüsseln, entschlüsseln mit zweitem Key und verschlüsseln mit drittem Key

### Was für Keying Options gibt es bei 3DES?
1. Alle drei Schlüssel unterschiedlich
2. K1 = K3 -> besser als 2DES
3. Alle gleich -> Backwards Kompatibilität mit DES

### Nenne 5 Eigenschaften von Feistel-Chiffren
1. Symmetrisch
2. Zerlegung des Eingabeblocks in zwei Teile
3. n Runden mit Rundenschlüsseln
4. Funktion f ist nicht umkehrbar
5. Alternierende Substitutionen und Permutationen für Konfusion und Diffusion

### Wie funktionieren Blockchiffren? Wie wird mit Input variabler Länge umgegangen?
- Feste Blocklänge
- Ciphertext = Konkatenation der Output-Blöcke
- Padding, Länge des Paddings muss hinterlegt werden

### Wie funktionieren Stromchiffren?
- Kleine Einheiten werden mit Keystream XOR verknüpft
- Keystream wird aus PRNG erzeugt
- PRNG wird mit Shared Secret initialisiert

### Was ist Electronic Codebook Mode? Nenne zwei Nachteile
- Jeder Block wird mit demselben Schlüssel verschlüsselt -> identische Ciphertext-Blöcke
- Nachteile:
  1. Angreifer können Blöcke Löschen, Vertauschen und Einfügen
  2. Erlaubt Rückschlüsse auf Klartext
  
### Was ist Cipher Block Chaining?
- Klartext-Block wird **vor** der Verschlüsselung mit letztem Ciphertext-Block XOR verknüpft
- Keine Fortpflanzung von Übertragungsfehlern über den nächsten Block hinaus :)

### Wie berechnet sich die Rundenanzahl in AES?
max(Blockbit, Schlüsselbit) / 32 + 6

### Nenne die Schritte der Verschlüsselung bei AES
1. Addition des Rundenschlüssels
2. Byte-Substitution
3. Zeilenshift
4. Außer in letzter Runde: Spaltenmix
5. Addition des Rundenschlüssels
6. Zurück zu 2

### Nenne die Schritte der Entschlusselung bei AES
1. Addition des Rundenschlüssels 
2. Inv. Zeilenshift
3. Inv. Byte-Substitution
4. Addition des Rundenschlüssels
5. Außer in letzter Runde: Inv. Spaltenmix
6. Zurück zu 2

### Wie funktioniert die Bytesubstitution bei AES?
- Aktueller Byteinhalt gibt Zeile und Spalte der Lookup-Tabelle vor
- Größe ändert sich nicht, nur Inhalt

### Wie funktioniert der Zeilenshift bei AES?
- Zeile i (beginnend bei 1) wird um i-1 nach links geshiftet

### Wie funktioniert der Spaltenmix bei AES?
- $s' = A s$
- $A = ((02, 03, 01, 01), ...)$ geshiftet nach links pro Reihe

### Wie wird der Rundenschlüssel bei AES addiert?
- Rundenschlüssel wird in Worte unterteilt
- Jedes Wort wird auf eine Spalte addiert
- Schlüssel wird rotiert und mit S-Box Bytesubstituiert, abhängig von Rundenkonstante

### Nenne vier Vorteile von AES
1. Design-Kriterien offen gelegt, kein geheimes Design
2. Rundenschlüsselgenerierungsvorteile (siehe unten)
3. Diffusion: Nach 2 Runden hängen 50% der Output-Bits von jedem Input-Bit ab
4. Keine Angriffe bekannt, die besser als Brute Force sind ab 8+ Runden

### Nenne drei Vorteile der Rundenschlüsselgenerierung bei AES
- S-Box verhindert, dass mit Teilen des Schlüssels der Rest berechnet werden kann
- S-Box verhindert, dass zwei ähnliche Schlüssel viele gemeinsame Rundenschlüssel haben
- Rundenkonstante verhindert Symmetrien im Prozess

### Nenne drei Protokolle, die AES einsetzen
WPA2, SSH, IPsec

### Nenne drei Programme, die AES einsetzen
FileVault, Skype, ZIP

### Nenne zwei Nachteile von symmetrischen Verschlüsselungsverfahren
1. Schlüssel müssen sicher ausgetauscht werden / vor der Kommunikation bekannt sein
2. Quadratische Anzahl an Schlüsseln bei linearen Kommunikationspartnern

## 8 - Asymmetrische Kryptosysteme

### Nenne die Schritte einer Asymmetrischen Verschlüsselung
1. Erzeugung von Schlüsselpaaren
2. Austausch / Öffentlichmachung öffentlicher Schlüssel
3. Verschlüsselung mit öffentlichem Schlüssel
4. Entschlüsselung mit privatem Schlüssel

### Nenne die Schritte bei der Erzeugung eines RSA Schlüsselpaares
1. Wähle Primzahlen p, q
2. n = pq = RSA-Modul
3. $\Phi(n) = (p-1)(q-1)$
4. Wähle $1 < e < \Phi(n)$, z.B. 65537
5. Public Key = (n, e)
6. $d = e^{-1} \text{ mod } \Phi(n) = Euklid(e, \Phi(n))
7. Private Key = (n, d)

### Erkläre die Ver- und Entschlüsselung bei gegebenem RSA Schlüsselpaar und Nachricht m
- $c = m^e mod n$
- $m = c^d mod n$

### Erkläre vier Angriffe auf RSA
1. Brute Force - Zerlege n in p und q
2. Chosen-Ciphertext - (-)
3. Timing Angriff - Laufzeit der Entschlüsselung verrät d. Lösung Entschlüsselung mit zusätzlicher Zufallszahl
4. Angriff auf Signaturen. Man kann Dokument aus korrekt signierten Teildokumenten zusammensetzen aufgrund von Multiplikativität von RSA

### Wie viel Bit Schlüssel konnten bereits faktorisiert werden bei RSA?
1039

### Wie viel Bits of Security haben gängige RSA Schlüssellängen?
- 1024 -> 80 AES
- 2048 -> 112 AES
- 3072 -> 128 AES

### Wie viel Bits of Security werden aktuell empfohlen?
Bis 2022 100, danach 120

### Nenne drei Hybride Verfahren, die RSA nutzen
SSL/TLS, PGP, SSH

### Wie funktioniert eine Digitale Signatur?
Prüfsumme wird auf Daten generiert und mit privatem Key signiert

### Nenne 5 Anforderungen an eine Signatur und erkläre, ob sie die elektronische Signatur erfüllt
1. Perpetuierungsfunktion - Fälschungssicher und dauerhaft (gegeben, falls private Key private bleibt)
2. Echtheitsfunktion - Authentizität (gegeben, durch CA [Public Key -> Name]
3. Wiederverwendbarkeit - Verhindert (nur möglich mit Private Key)
4. Abschlussfunktion - Dokument nicht veränderbar (nur möglich mit Private Key)
5. Beweisfunktion - Nicht zu leugnen (durch Public Key eindeutig)

### Skizziere den Ablauf einer Signatur und deren Verifikation

https://github.com/batzner/unistuff/raw/master/LMU/IT-Sicherheit/img/certification-steps.png

## 9 - Kryptographische Hashfunktionen

### Wozu dienen kryptographische Hashfunktionen?
Integritätssicherung - Manipulationen an einer Nachricht sollen erkannt werden können

### Was ist der Unterschied zwischen einer Hashfunktion und einer kryptographischen Hashfunktion?
Kollisionsresistenz = Ähnliche Eingaben sollen nicht denselben Hashwert haben

### Was ist der Unterschied zwischen einer schwachen und einer starken Hashfunktion?
- Schwach: für einen gegebenen Hashwert ist es praktisch unmöglich, eine Nachricht mit selbem Hash zu finden
- Stark: Schwach + es ist allgemein praktisch unmöglich, eine Kollision zu finden

### Beschreibe, wie kryptographische Hashfunktionen konstruiert sind
- Kompressionsfunktion G wird wiederholt auf Block M_i und bisherigen Hashwert angewandt
- Benötigt IV und Padding

### Beschreibe grob die Funktionsweise von MD5
- Eingabe: 512-bit Blöcke
- Ausgabe: 128 bit
- Padding: 0en + Länge der Eingabe
- Fixer IV
- Vier Runden für einen 512-bit Block

### Evaluiere die Sicherheit von MD5 und nenne eine Alternative
- Für jeden IV lassen sich in einer Stunde zwei Paare von Blöcken finden, die denselben Hash produzieren
- Ist unabhängig davon, was davor kommt und was danach kommt
- Zwei Daten sind gleich außer in je zwei aufeinanderfolgenden Blöcken
- Lösung: SHA-256, hat längeren Hash

### Wie funktionierte der MD5 CA Angriff? Skizziere die Vorgehensweise
- Verwendete Rouge CA Zertifikat zum Signieren falscher Zertifikate
- Route CA Zertifikat wurde aus validem Webseiten Zertifikat erstellt

### Nenne die Schritte bei der Zertifizierung bei HTTPS
1. Server schickt CA seinen Public Key und Identität
2. CA überprüft Identität
3. CA erstellt Zertifikat und signiert mit seinem Private Key und schickt resultierendes X.509 Certificate an Server
4. Client initiiert HTTPS mit Server
5. Server schickt X.509 Zertifikat an Client (enthält eigenen Public Key)
6. Client überprüft X.509 Zertifikat mit Public Key von CA (schon im Voraus als CA Root Certificate installiert)

### Nenne 6 Eigenschaften von SHA-3 / Keccak
- Sponge-Funktion mit absorbing und squeezing
- Addition von Rundenkonstanten
- Nichtlinear
- Diffusion
- Variable Output-Länge -> kann als PRNG für Stream Ciphers genutzt werden
- Noch weniger von Kryptanalytikern untersucht
- Effiziente Implementierung möglich

## 10 - Sicherheitsmechanismen

### Reicht Verschlüsselung zur Wahrung der Integrität? Beschreibe eine bessere Alternative!
- Nein, da Daten blind modifiziert werden
- Hashwert gegen Modifikation, muss auch verschlüsselt übertragen werden (z.B. signiert)
- Hashwert + gesicherte Sequenznummern / Zeitstempel gegen Replay-Angriff

### Nenne drei Arten der Authentisierung
1. Datenursprung
2. Benutzer
3. Peer Entity (Client - Server)

### Nenne fünf Möglichkeiten der Authentisierung
1. Wissen
2. Besitz
3. Persönliche Eigenschaft
4. Kombination aus 1-3
5. Delegation (z.B. CA)

### Nenne drei Kategorien der Benutzerauthentisierung und jeweils ein Beispiel
1. Wissen -> Passwort, PIN
2. Besitz -> Smartcard, Private Key
3. Eigenschaft -> Biometrie

### Was ist die Motivation hinter Einmalpasswörtern?
Abgehörtes Passwort soll für Angreifer möglichst nutzlos sein -> nicht wiederverwendbar, begrenzte Dauer, und nachfolgendes Passwort nicht ableitbar

### Erläutere die Schritte bei S/Key
1. Client schickt N (Anzahl gewünschter Passwörter) an Server
2. Server schickt Seed an Client
3. Client berechnet nachfolgende Passwörter über Kette von MD4 Hashes
4. Client nutzt Passwörter in umgekehrter Reihenfolge
5. Client übersetzt ein Passwort in 6 Wörter über ein fixes Wörterbuch
6. Server verifiziert Passphrase

### Was ist die Schwachstelle von S/Key?
Anfällig für Man in the Middle 
- Angreifer kennt N und seed -> Dictionary Attack
- Server wird nicht authentisiert

### Erläutere OTP
Änderungen zu S/Key:
- Passwort kann nur ein einziges Mal verwendet werden -> keine parallelen Sessions mit gleichem Passwort
- MD5 und SHA unterstützt
- Empfiehlt IPSec

### Nenne zwei Angriffe auf OTP bzw. S/Key
- Man in the Middle, kann über IPSec Authentifizierung des Servers vermieden werden
- Wenn Hashes im Klartext abgefangen werden, kann man Passwort erraten

### Wie funktioniert RSA SecurID?
- Jede Minute neue Zahl, die nur zentraler Authentifizierungsserver vorhersagen kann
- 2 Faktor-Authentisierung zusammen mit Benutzerpasswort
- Berechnung über AES mit echtem Zufalls-Seed + Vergangene Sekunden seit 1986
- Hardwaremanipulation führt zu Hardwarebeschädigung

### Was würden Sie einem Unternehmen zur Benutzerauthentifizierung empfehlen, dessen Mitarbeiter auf auf Dienstreisen -> in Internet-Cafes sind?
- Biometrie kommt nicht in Frage 
- Falls Mitarbeiter auch ohne ihren Laptop Zugriff zum Firmennetz haben müssen: 
  - Wissen -> Einmalpasswörter über OTP -> Problem des Man in the Middle Angriff -> Muss Server Zertifikat signiert mit Root CA laden
  - Besitz -> RSA SecurID
- Falls Mitarbeiter nur eigene Laptops verwenden -> Haben Zertifikate der Firmenserver bereits vorinstalliert

### Nenne zwei Nachteile von Smartcard / OTP-Token-basierten Lösungen
1. Abhängig von Besitz -> Kann verloren gehen
2. Hohe Anschaffungskosten im Vergleich zu Software-basierten Lösungen

### Welche beiden Fehlerarten gibt es bei biometrischer Benutzerauthentisierung?
- False Acceptance
- False Rejection

### Was ist der Unterschied zwischen 1:1 und 1:N Authentifizierung? Nenne jeweils einen Nachteil
- 1:N -> Man muss keinen Benutzer spezifizieren, sucht einfach nach Match
- 1:1 -> Verfizierung, Problem: erkennt keine Duplikate in der Datenbank

### Nenne vier Möglichkeiten, um den Datenursprung zu Authentisieren
1. Verschlüsselung (Shared Secret)
2. Digitale Signatur 
3. Message Authentication Code
4. Hashed MAC

### Was sind die Vor- und Nachteile von symmetrischer Verschlüsselung zur Authentisierung des Datenursprungs?
Vorteile
- Authentisierung des Datenursprungs
- Vertraulichkeit der Daten
- Empfänger nicht authentisiert, aber effektiv der einzige mit Zugang

Nachteile
- Sender kann Sendung leugnen
- Empfang kann nicht bewiesen werden
- Keine Integritätssicherung

### Was sind die Vor- und Nachteile von asymmetrischer Verschlüsselung (nicht Signatur) zur Authentisierung des Datenursprungs?
Vorteile
- Vertraulichkeit der Daten
- Empfänger nicht authentisiert, aber effektiv der Einzige mit Zugang

Nachteile
- Keine Authentisierung des Datenursprungs
- Sender kann Sendung leugnen
- Empfang kann nicht bewiesen werden
- Keine Integritätssicherung

### Was sind die Vor- und Nachteile von Signaturen zur Authentisierung des Datenursprungs?
Vorteile
- Authentisierung des Datenursprungs
- Sendung kann nicht geleugnet werden

Nachteile
- Keine Vertraulichkeit der Daten
- Keine Integritätssicherung
- Empfang kann nicht bewiesen werden
- Empfänger wird nicht authentisiert

### Was sind die Vor- und Nachteile von asymmetrischer Verschlüsselung + Signatur zur Authentisierung des Datenursprungs?
Vorteile
- Authentisierung des Datenursprungs
- Keine Authentisierung des Empfängers, aber effektiv der Einzige mit Zugang
- Vertraulichkeit der Daten
- Vertraulichkeit der Signatur, da Empfänger zuerst mit Private Key entschlüsseln muss
- Sendung kann nicht geleugnet werden

Nachteile
- Keine Integritätssicherung
- Empfang kann nicht bewiesen werden
- Dauert lange

### Welche Methoden gibt es, um Integrität und Authentisierung des Datenursprungs sicherzustellen? Was ist das Häufigste Verfahren?
1. Hash[Nachricht + Shared Secret] mitschicken
2. SymmE[Nachricht + Hash] 
3. Nachricht + Signierter Hash
4. SymmE[Nachricht + Signierter Hash] (häufigstes)

### Was sind die Vor- und Nachteile von Hash[Nachricht + Shared Secret] zur Authentisierung des Datenursprungs?
Vorteile
- Integrität

Nachteile
- Keine Vertraulichkeit
- Sendung kann geleugnet werden
- Empfang kann nicht bewiesen werden

### Was sind die Vor- und Nachteile von SymmE[Nachricht + Hash] zur Authentisierung des Datenursprungs?
Vorteile
- Integrität
- Vertraulichkeit
- Authentisierung des Datenursprungs

Nachteile
- Sendung kann geleugnet werden
- Empfang kann nicht bewiesen werden

### Was sind die Vor- und Nachteile von SymmE[Nachricht + Signierter Hash] zur Authentisierung des Datenursprungs?
Vorteile
- Integrität
- Vertraulichkeit
- Authentisierung des Datenursprungs
- Sendung kann nicht geleugnet werden

Nachteile
- Empfang kann nicht bewiesen werden

### Was ist eine Merkle-Damgard-Konstruktion?
- Initialisierungsvektor
- Input ist Block und vorheriger Output-Block
- Eventuell Finalisierung des Output N zum resultierenden Hash

### Wie funktionieren Message Authentication Codes?
- Wird aus Nachricht und Shared Secret berechnet
- Entweder mit Hash-Funktion, die Nachricht und Schlüssel zusammen hasht
- Oder z.B. AES im CBC Mode mit Schlüssel pro Block = Shared Secret

### Was ist ein Angriff auf MACs, die über Hash-Funktionen erzeugt wurden?
Length Extension - Bei Merkle-Damgard-Konstruktion können 0en ohne Kenntnis des Shared Secret eingefügt werden

### Wie funktionieren Hashed MACs? Warum kann man nicht einfach den Schlüssel mithashen?
- Keine symmetrische Verschlüsselung, sondern Hash-Funktion
- Problem: Hash-Funktionen nutzen keinen Schlüssel
- Problem: Einfache Konkatenierung erlaubt Length Extension Attack (z.B. bei SHA-1(k||m))
- Schlüssel wird verarbeitet und dann mit Nachricht konkateniert -> Dann gehasht
- Hash wird nochmal gehasht mit konkateniertem Schlüssel, um das Ende der Nachricht zu sichern

### Nenne zwei Authentisierungsprotokolle
1. Needham Schröder
2. Kerberos

### Erkläre den Ablauf von Needham Schröder
1. Alice schickt Trent A, B und Nonce
2. Trent schickt Alice verschlüsselt [B, Nonce, Sitzungsschlüssel und E_B[A, K]]
3. Alice schickt Bob E_B[A, K]
4. Bob schickt Alice K[Nonce]
5. Alice schickt Bob K[Nonce-1]

### Nenne eine Schwachstelle von Needham Schröder und zeige Lösungen auf
- Replay-Angriff: Alte Sitzungsschlüssel bleiben gültig, Mallory kann einfach E_B[A, K] nochmal schicken, wenn es K geknackt hat
- Lösung: Sequenznummern in E_B[K, A]] Nachricht, Timestamps, begrenzte Gültigkeitsdauer

### Was ist der Unterschied zwischen einem Ticket und einem Authenticator in Kerberos?
- Ticket ist für einen Client für einen Server gültig
- Ticket wird vom TGS erstellt, Authenticator vom Client

### Was speichert ein Ticket in Kerberos?
1. Client
2. Server
3. Client-Adresse
4. Lifetime
5. Timestamp
6. Symmetrischer Schlüssel

### Was speichert ein Authenticator in Kerberos?
1. Client
2. Client-Adresse
3. Timestamp

### Erläutere den Ablauf von Kerberos
1. Request for Ticket Granting Ticket $c, tgs$
   - Client an Kerberos Server
   - Kerberos überprüft, ob Client in Datenbank
2. Ticket Granting Ticket $K_c[K_{c, tgs}], K_{tgs}[T_{c,tgs}]$
   - $T_{c,tgs}$ ist Ticket und enthält Schlüssel $K_{c,tgs}$
3. Request für Server Ticket $s, K_{c, tgs}[A_{c, tgs}], K_{tgs}[T_{c,tgs}]$
   - $A_{c, tgs} = c,a,t$
4. Server Ticket $K_{c, tgs}[K_{c,s}], K_s[T_{c,s}]$
   - $T_{c,s}$ ist ein Ticket und enthält Schlüssel $K_{c,s}$
5. Request für Service $K_{c,s}[A_{c,s}], K_s[T_{c,s}]$
   - $A_{c,s} = c,a,t,key,seqNo$
6. Server Authentication $K_{c,s}[t, key, seqNo]$

### Wie wird das Nutzerpasswort in Kerberos überprüft?
Implizit, da die Antwort des Kerberos Servers mit dem Nutzerpasswort verschlüsselt ist. Passwörter werden nie verschickt! 

### Warum werden Kerberos Server und TGS oft getrennt?
Erlaubt Skalierung von Ticket Granting Servern, die öfter gebraucht werden als Kerberos Server

### Skizziere, wie Multi-Domain-Kerberos abläuft
https://github.com/batzner/unistuff/raw/master/LMU/IT-Sicherheit/img/kerberos-multi-domain.png

### Was sind zwei Probleme bei Multi-Domain-Kerberos?
1. Beide Domänen müssen sich vertrauen
2. n Realms fordern n(n-1)/2 Schlüssel

### Nenne vier Schwächen von Kerberos
1. IP-Spoofing ist u.U. möglich, Authentisierung basiert auf IP-Adresse
2. Kerberos-Schlüssel wird aus Passwort abgeleitet -> Sicherheit hängt davon ab
3. Kerberos-Server und TGS sind Single Point of Failure -> Wenn die nicht verfügbar sind geht gar nichts
4. Verlässt sich auf vertrauenswürdige Software -> Problem Kerberos-Trojaner

### Was ist Autorisierung und was ist Zugriffskontrolle?
- Autorisierung: Vergabe von Berechtigungen
- Zugriffskontrolle: Durchsetzung dieser Berechtigungen

### Erkläre drei Zugriffskontrollstrategien
1. Discretionary Access Control (z.B. chmod auf Datei für Yuxiang)
   - Eigentümerprinzip - Eigentümer spezifiziert die Berechtigungen an seinen Objekten
   - Auf Basis der Objekte
2. Mandatory Access Control
   - Regelbasierte Festlegung der Rechte, z.B. über Sicherheitsklassen 
   - Systemglobal
3. Role-based Access Controll (z.B. chmod auf Datei für Administratoren)
   - Subjekt -> Aufgabe / Rolle -> Berechtigungen
  
### Nenne drei Aufgaben eines Referenzmonitors / Access Control Monitor
- Regelt Zugriff auf Objekte
- Kann Subjekte authentisieren 
- Kann Objektzugriff unterbrechen / verhindern

### Was ist Identifikation? Was sind die zwei impliziten Stufen?
- Verbindung von digitaler ID und Real-World Entity

Zwei Stufen:
1. Personalisierung 
   - Ermittlung der Real-World Identität
   - Vergabe einer digitalen ID (Benutzername)
2. Identifikation
   - Verbindung beider mit Informationen, die nur die Entität kennt (Passwort)
  
### Was ist der Realm einer Certification Authority?
Realm = Alle Nutzer, die der CA vertrauen

### Nenne 4 CA Aufgaben
- Generierung von C
- Speicherung von C
- Widerruf und Sperrung von C 
- Aktualisierung von C
- Beglaubigung von Verträgen (wie Notar)

### Welche zwei Methoden gibts es für den Widerruf von Zertifikaten?
1. Certificate Revocation Lists
2. Online Certificate Status Protocol

### Was sind die 4 Schritte einer Benutzerzertifizierung?
1. Schlüsselgenerierung
2. Personalisierung, Certification Request
   - Feststellung der Identität
   - Benutzer beweist Besitz des privaten Schlüssels
3. Zertifikat generieren
4. Zertifikat signieren

### Nenne die wichtigen X.509 Attribute
- Version
- SerialNumber
- SignatureAlgorithm `SHA-256 mit RSA`
- Issuer
- Validity
- Subject
- SubjectPublicKeyInfo (Algorithmus, Schlüssel, Verwendung, Länge, Exponent)
- Alternativer Name (mittlerweile wichtig für mehrere Domains)
- Signature (signiert alles obere)

### Was ist das Problem mit CRLs?
Problem mit Certificate Revocation Lists: Werden immer nur länger, da alle Revocations gespeichert werden.

### Wie läuft OCSP ab?
1. Client schickt Hash des Zertifikats
2. Responder prüft und antwortet mit Good / Revoked / Unknown 

### Welche zwei Schutzmechanismen hat OCSP?
- Replay Protection über Zufallszahl
- Client kann Positiv-Antwort fordern -> Responder antworte mit Hash des gültigen Zertifikats

## 11 - Netzsicherheit - Data Link Layer

### Was ist der Sinn eines VPN?
- Nachbildung eines LAN in beliebigen Topologien / Technologien
- Vertraulichkeit und Datenintegrität wie in physischem LAN

### Was gibt es für VPN Lösungen auf Schicht 1?
- Virtual Private Wire Service
- Virtual Private Line Service

### Was gibt es für VPN Lösungen auf Schicht 2? Was tun diese speziell?
- VLAN -> Mehrere Netze werden über denselben physischen Link betrieben, aber sind getrennt voneinander
- Virtual Private LAN Services - verbindet physisch getrennte LANs
- Point to Point Verbindungen

### Was gibt es für VPN Lösungen auf Schicht 3 und höher?
- IPSec
- SSL/TLS
- OpenVPN
- Peer to Peer Anwendung (Schicht 7)

### Was regelt der 802.1Q?
VLAN

### Was ist das Ziel von VLAN?
- LAN-Infrastruktur über mehrere Switches hinweg -> Broadcasts usw. möglich über gesamtes VLAN Netz
- Soll aber andere VLAN-Netze, die auf gleicher LAN-Struktur arbeiten, nicht betreffen

### Wie funktioniert VLAN?
- Ethernet-Frame wird erweitert um 32 Bit Tag:
  - 16 Bit: 0x8100 für VLAN
  - 3 Bit: Priority 
  - 1 Bit: Canonical Format Indicator (Ethernet oder Token Ring)
  - 12 Bit: VLAN-ID -> 4094 verschiedene VLANs möglich

### Was ist PPP?
- Punkt-zu-Punkt Protokoll
- Für Verbindungsaufbau über Wählleitungen: DSL, ISDN, Modem etc.
- Beinhaltet Link Control Protocol für Verbindungsaufbau, abbau und Aushandeln der Konfiguration

### Welche Möglichkeiten der Authentifizierung bestehen bei PPP?
- Authentifizierung (optional) Protokolle:
  - Password Authentication Protocol (PAP)
  - Challenge-Handshake Authentication Protocol (CHAP)
  - Extensible Authentication Protocol (EAP)

### Wie funktioniert PAP? Was ist seine Schwäche?
- Authentifizierungsprotokoll für PPP
- Überträgt Passwörter im Klartext. WOW.
- Server kennt ID und Passwort aller Clients und schickt ACK
- Keine Authentisierung des Authenticators durch den Client :(

### Wie funktioniert CHAP?
- Shared Secret zwischen A und B
- Zu Authentisierung werden öffentliche Infos (id, Zufallszahl, Name) mit Shared Secret gehasht und übertragen
- Sicher gegen Replay-Angriffe

### Ist PAP sicher gegen Replay Angriffe? Was ist mit CHAP?
PAP nicht. CHAP schon, durch Zufallszahl, die mit Shared Secret gehasht wird

### Nenne zwei Schwächen von CHAP
- Implementierungen unterstützen leider immer noch PAP als Fallback -> Einfacher M.i.t.M. Angriff
- Keine Authentisierung des Authenticators durch den Client :(

### Was ist EAP?
- Authentisierungsmechanismus für PPP
- Bietet Aushandlungsmechanismen für konkretes Verfahren, also eher ein Framework

### Wozu dient das PPTP? Zwischen welchen Tunneling Modi wird unterschieden?
- PPP wurde für direkt verbundene Systeme entwickelt
- PPTP schickt seine Pakete durch das Internet und realisiert einen Tunnel
- Simuliert ein Kabel zwischen zwei Systemen
- Voluntary Tunneling -> Client setzt PPTP aktiv ein
- Compulsory Tunneling -> Client denkt, es ist eine PPP Verbindung

### Was ist MS-CHAP? 
Microsofts PPTP Implementierung

### Nenne eine Sicherheitslücke von MS-CHAPv1
Ermöglicht Known-Plaintext, da Challenge C im Klartext übertragen wurde und dann zurück entschlüsselt übertragen wurde.

### Nenne eine Schwäche von MS-CHAPv2
Hängt von Benutzerpasswortsicherheit ab

### Was regelt der 802.1X? Definiert er ein eigenes Protokoll? Wie wird verschlüsselt?
Port Based Network Access Control
- Authentisierung und Autorisierung in IEEE 802 Netzen (WLANs, Bluetooth, Ethernet, VLAN etc.)
- Definiert kein eigenes Protokoll, sondern nutzt EAP, EAP-TLS und RADIUS
- Authentisierung ist immer Ende zu Ende -> Authenticator kann nicht mitlesen -> Eduroam

### Erkläre die vier Rollen bei 802.1X
- Supplicant: 802.1X Gerät, das sich authentisieren möchte
- Authenticator: Gerät, an dem der Supplicant angebunden ist (Switch oder WLAN AP)
- Authentication Server: z.B. RADIUS-Server -> Macht eigentliche Authentisierung
- Port Access Entity (PAE): Port, an dem Supplicant angeschlossen ist
  - Uncontrolled Port für Authentisierung
  - Controlled Port für Kommunikation
  
### Erkläre den Ablauf von 802.1X
1. Supplicant fordert Controlled Port
2. Authenticator fordert Authentisierung
3. Nach erfolgreicher Authentisierung: Port wird freigeschaltet

### Erkläre einen Angriff auf Eduroam
Eduroam kann mit eduroam-spoofing angegriffen werden, ist aber einfach zu erkennen, da falsches Zertifikat

## 12 - Netzsicherheit - WLAN-Sicherheit

### Nenne vier Anforderungen an WLAN Protokolle
1. Vertraulichkeit
2. Integrität
3. Authentisierung
4. Zugriffskontrolle

### Was ist der Unterschied zwischen einem BSS und einem ESS?
- Basic Service Set -> STAs, die denselben AP nutzen
- Extendes Service Set -> gleiche SSID, Netz aus mehreren BSS (z.B. Eduroam in München = 1 ESS)

### Wie funktioniert WEP?
- PRNG = RC4
- 24-bit IV + 40-bit K = 64-bit Seed -> Keystream
- C = (M + CRC) XOR Keystream
- C und IV werden übertragen

