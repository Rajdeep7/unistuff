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
