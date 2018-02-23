# Einführung
## SQL Slammer
- Verdopplung alle 8 Sekunden
- Nach 10 Minuten 90% aller anfälligen Hosts infiziert, ca. 75.000 nach 30 Minuten
- Buffer Overflow Bug -> konnte Registry öffnen
- War in SW von Drittanbietern enthalten
- 376 Byte UDP Paket
- Rät IP-Adressen
- Probing Rate: 26,000 Scans pro Sekunde

# Grundlagen

### Ziele der Informationssicherheit
CIA
- **Confidentiality / Vertraulichkeit**
  - Daten können nur von Berechtigten genutzt werden
  - Maßnahme: Verschlüsselung
- **Integrity / Integrität**
  - Geschützte Daten können nicht unautorisiert und unbemerkt modifiziert werden
  - Maßnahme: Prüfsummen
- **Availability / Verfügbarkeit**
  - Autorisierte Subjekte können störungsfrei Berechtigungen wahrnehmen
  - Maßnahme: Redundanz
  
Zusätzliche Ziele: 
- **Verbindlichkeit / Nicht-Abstreitbarkeit** -> Signaturen
- **Authentizität** - Echtheit, Überprüfbarkeit und Vertrauenswürdigkeit eines Objektes

### Bell LaPadula Modell
- Setzt Mandatory Access Control um
- Schützt die Vertraulichkeit von Daten
- Dominance Relation = Inverse von [Information]-Can-Flow Relation
- Drei Regeln
  1. No-Read-Up - Tiefe Personen dürfen nicht Dateien von hohen Personen lesen
  2. No-Write-Down - Hohe Personen dürfen nicht in Dateien von tiefen Personen schreiben -> Können nicht Informationen leaken
  3. Access-Control Matrix definiert Zugriff von Subjekt auf Objekt

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
- Beschreibt risikogetriebenen [Plan - Do - Check - Act] Zyklus
- Beschreibt:
  - Organisation der Informationssicherheit
  - Personalsicherheit
  - Verwaltung der Werte
  - Kryptographie
  - Physische Sicherheit
  - etc.
  
**Information Security Management System**
- Aufstellung von Verfahren und Regeln
- Innerhalb eines Unternehmens
- Dienen zur Definition, Steuerung, Kontrolle und Verbesserung von Informationssicherheit

**Risikomanagement**
- = Risikoeinschätzung -> Risikobehandlung OR Risikoakzeptanz
- Risikoeinschätzung = Risikoanalyse -> Risikobewertung
- Risikoanalyse = Identifikation -> Klassifikation

### Security vs. Safety
- **Safety**: Funktionssicherheit / Ausfallsicherheit bei sicherheitskritischen Programmen
- **Security**: Informationssicherheit -> Hardware- / Software- / Netz-basierte Angriffe und Gegenmaßnahmen
- IT-Sicherheit $\subset$ Informationssicherheit / Security $\subset$ Funktionssicherheit / Safety
