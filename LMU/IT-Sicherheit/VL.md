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
