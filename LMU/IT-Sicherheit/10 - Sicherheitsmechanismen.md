# Sicherheitsmechanismen
Für
1. Vertraulichkeit
2. Integrität
3. Authentisierung
4. Autorisierung und Zugriffskontrolle
5. Identifikation

## Vertraulichkeit
- Verschlüsselung!

## Integrität
- Hashwerte gegen Modifikation
- Hashwert + gesicherte Sequenznummern + Zeitstempel gegen Duplikate (**Replay-Angriff**)
- Verschlüsselung allein schützt nicht die Integrität! Daten können blind modifiziert werden
- Lösung: Hashwert und Sequenznummern verschlüsseln, Nachricht nicht

## Authentisierung
### 3 Arten
1. Datenursprung
2. Benutzer
3. Peer Entity (Client - Server)

### 5 Möglichkeiten
1. Wissen
2. Besitz
3. Persönliche Eigenschaft
4. Kombination aus 1-3
5. Delegation (z.B. CA)

## Benutzerauthentisierung
- Wissen -> Passwort, PIN
- Besitz -> Smartcard, Private Key
- Eigenschaft -> Biometrie

### Einmalpasswörter
- Abgehörtes Passwort soll für Angreifer möglichst nutzlos sein
- Gut für Internet-Cafes

### S/Key
Server und Client kennen beide Clients Passwort
1. Client schickt N (Anzahl gewünschter Passwörter) an Server
2. Server schickt Seed und N an Client
3. Client berechnet nachfolgende Passwörter über Kette von MD4 Hashes (Client gibt sein Passwort bei Stelle 0 ein)
4. Client nutzt Passwörter in umgekehrter Reihenfolge (N, N-1, N-2 ...)
5. Client übersetzt ein Passwort in 6 Wörter über ein fixes Wörterbuch
6. Server verifiziert Passphrase

Kritik:
- Anfällig für Man in the Middle 
  - Angreifer kennt N und seed -> Dictionary Attack
  - Server wird nicht authentisiert

### One Time Password System
Änderungen zu S/Key:
- Ein Passwort kann nur ein einziges Mal verwendet werden -> nicht für parallele Sessions
- MD5 und SHA unterstützt
- Empfiehlt IPSec

Angriffe:
- Wie oben, M.i.t.M., kann aber über IPSec Authentifizierung des Servers vermieden werden
- Wenn Hashes im Klartext abgefangen werden, kann man Passwort erraten
- Hängt also vom Passwort ab (sollte nicht in Dictionary sein)

### Smartcards
Zugangsdaten werden auf Karte gespeichert oder erzeugt

### RSA SecurID
- Jede Minute neue Zahl, die nur zentraler Authentifizierungsserver vorhersagen kann
- 2 Faktor-Authentisierung zusammen mit Benutzerpasswort
- Berechnung über AES mit "echtem" Zufalls-Seed + Vergangene Sekunden seit 1986
- Hardwaremanipulation führt zu Hardwarebeschädigung

### Biometrie
- Extrahiert Master-Charakteristika
- Matching Score regelt FN und FP Rate (Acceptance und Rejection)
- 1:N -> Man muss keinen Benutzer spezifizieren, sucht einfach nach Match
- 1:1 -> Verfizierung, Problem: erkennt keine Duplikate in der Datenbank

## Datenursprung Authentisierung
Möglichkeiten
1. Verschlüsselung (Schlüssel muss bekannt sein = Authentisierung=
2. Digitale Signatur
3. Message Authentication Code (MAC) = Hash + gemeinsamer Schlüssel
4. Hashed MAC

### 1. Symmetrische Verschlüsselung
Erfüllt:
- Authentisierung des Datenursprungs
- Vertraulichkeit der Daten
- Empfänger nicht authentisiert, aber effektiv der einzige mit Zugang

Nachteile:
- Sender kann Sendung leugnen
- Empfang kann nicht bewiesen werden
- Keine Integritätssicherung (blinde Modifikation des Chiffretextes wird nicht erkannt)

### 2. Asymmetrische Verschlüsselung
Erfüllt:
- Vertraulichkeit der Daten
- Empfänger nicht authentisiert, aber effektiv der einzige mit Zugang

Nachteile:
- Keine Authentisierung des Datenursprungs
- Sender kann Sendung leugnen
- Empfang kann nicht bewiesen werden
- Keine Integritätssicherung

### 3. Digitale Signatur
Erfüllt:
- Authentisierung des Datenurpsrungs
- Sendung kann nicht geleugnet werden

Nachteile:
- Keine Vertraulichkeit
- Empfänger wird nicht authentisiert
- Empfang kann nicht bewiesen werden
- Keine Integritätssicherung

### 4. Authentisierung: asym. Verschlüsselung + Signatur
1. Mit eigenem Private Key verschlüsseln
2. Dann mit Empfängers Public Key verschlüsseln

Erfüllt:
- Authentisierung des Datenursprungs
- Nur Bob kann Nachricht nutzen
- Vertraulichkeit der Daten
- Vertraulichkeit der Signatur, da zuerst Empfänger mit Private Key entschlüsseln muss
- Sendung kann nicht geleugnet werden

Nachteile:
- Dauert lange
- Empfang kann nicht bewiesen werden
- Keine Integritätssicherung

### 5.1 Hash mit Nachricht mitschicken
1. Nachricht + Shared Secret werden gehasht
2. Nachricht + Hash werden übertragen

Erfüllt:
- Integrität

Nachteile:
- Keine Vertraulichkeit
- Sendung kann geleugnet werden
- Empfang kann nicht bewiesen werden

### 5.2 Symmetrisch Verschlüsselter [Hash + Nachricht]
- Shared Secret muss nicht mitgehasht werden

Erfüllt:
- Vertraulichkeit
- Authentisierung des Datenursprungs
- Integrität

Nachteile:
- Sendung kann geleugnet werden
- Empfang kann nicht bewiesen werden

### 5.3 Nachricht + Signierter Hash
- Standardverfahren der Digitalen Signatur
- Ziemlich kacke, aber erfüllt Authentisierung von Alice

### 5.4 Symmetrisch Verschlüsselte [Signierter Hash + Nachricht]
- Vertraulichkeit
- Authentisierung des Datenursprungs
- Sendung kann nicht geleugnet werden
- Integrität
- Wird von allen fast Protokollen, die Authentisierung und Vertraulichkeit benötigen, verwendet (SSL etc.)

Nachteil:
- Empfang kann nicht bewiesen werden

### Merkle-Damgard-Konstruktion
- Initialisierungsvektor
- Input ist (Block i, Output i-1)
- Eventuell Finalisierung des Output N zum resultierenden Hash (Nochmal mischen etc.)

### Message Authentication Codes (MAC)
- Wird aus Nachricht und Shared Secret berechnet (5.1)
- AES im CBC Mode mit Rundenschlüssel = immer gleiches Shared Secret
- Angreifer kennt Klartext und MAC und muss Shared Secret raten

Angriff:
- Length Extension - Bei Merkle-Damgard-Konstruktion können 0en ohne Kenntnis des Shared Secret eingefügt werden

### Hashed MAC (HMAC)
- Keine symmetrische Verschlüsselung wie bei MAC, sondern Hash-Funktion
- Hashs sind normalerweise schneller als symm. Verfahren
- Problem: Hash-Funktionen nutzen keinen Schlüssel
- Schlüssel wird verarbeitet und dann mit Nachricht konkateniert -> Dann gehasht

## Authentisierungsprotokoll Needham Schröder
- Third Party teilt mit jedem Kommunikationspartner eigenen Schlüssel
- $R$ = Einmalige Zufallszahl (Nonce) verhindert Replayattacken
- $E$ = Symmetrische Verschlüsselung
- $K$ = Sitzungsschlüssel

Ablauf:
1. Alice schickt eigene $A, B, R_A$ an TTP
2. TTP schickt verschlüsselt $[R_A, B, K, E_B[K, A]]$ an Alice zurück
3. Alice schickt Bob $E_B[K, A]]$
4. Bob schickt Alice $K[R_B]$
4. Alice schickt Bob $K[R_B-1]$

Problem: 
- Replay-Angriff
- K bleibt gültig
- Wenn ein altes K geknackt wird, kann Mallory einfach nochmal $E_B[K, A]]$ schicken

Lösung: Sequenznummern / Timestamps / begrenzte Gültigkeitsdauer

## Kerberos
- Kerberos-Server (TTP) kennt Schlüssel aller Clients
- Authentisierung basiert auf symmetrischer Verschlüsselung
- Single-Sign-On über Kooperation mehrerer Server

### Authentisierungsdaten
1. Ticket 
  - Nur für einen Server gültig
  - Wird vom Ticket Granting Server erstellt
  - Speichert Client, Server, Lifetime und Timestamp und symmetrischen Schlüssel
2. Authenticator
  - Vom Client erstellt
  - Wir zusammen mit Ticket verschickt
  - Speichert Client und Timestamp

### Ablauf
Kerberos Server und TGS Server sind zusammen in "sicherem Bereich", Server s ist außerhalb dieses Bereichs
- $T_{c,tgs}$ = Ticket für c, um tgs zu nutzen
- $A_{c,tgs}$ = Authenticator von c für tgs
- $c$ = Client
- $a$ = Adresse
- $t$ = Zeitstempel

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

### Multi-Domain-Kerberos
- TGS der fremden Realm wird "normaler" Server
- Probleme: 
  1. Beide Domänen müssen sich vertrauen
  2. $n$ Realms erfordern $\mathcal{O}(n^2)$ Schlüssel

<img src="https://github.com/batzner/unistuff/raw/master/LMU/IT-Sicherheit/img/kerberos-multi-domain.png" width=500/>

### Bewertung
- IP-Spoofing u.U. möglich
- Kerberos-Schlüssel wird aus Passwort abgeleitet -> Sicherheit hängt davon ab
- Synchronisation über lose gekoppelte globale Zeit
- Kerberos-Server und TGS sind "Single Point of Failure"
- Verlässt sich auf vertrauenswürdige Software -> Problem Trojaner

## Autorisierung und Zugriffskontrolle
- Autorisierung: Vergabe von Berechtigungen
- Zugriffskontrolle: Durchsetzung dieser Berechtigungen

### Zugriffskontrollstrategien
1. Discretionary Access Control (z.B. chmod auf Datei für Yuxiang)
   - Eigentümerprinzip - Eigentümer spezifiziert die Berechtigungen an seinen Objekten
   - Auf Basis der Objekte
2. Mandatory Access Control
   - Regelbasierte Festlegung der Rechte, z.B. über Sicherheitsklassen 
   - Systemglobal
3. Role-based Access Controll (z.B. chmod auf Datei für Administratoren)
   - Subjekt -> Aufgabe / Rolle -> Berechtigungen
  
### Referenzmonitor / Access Control Monitor
- Regelt Zugriff auf Objekte
- Kann Subjekte authentisieren 
- Kann Objektzugriff unterbrechen / verhindern

## Identifikation
- Verbindung von digitaler ID und Real-World Entity

Zwei Stufen:
1. Personalisierung 
   - Ermittlung der Real-World Identität
   - Vergabe einer digitalen ID (Benutzername)
2. Identifikation
   - Verbindung beider mit Informationen, die nur die Entität kennt (Passwort)
  
### Certification Authority
- Realm = Alle Nutzer, die der CA vertrauen

### CA Aufgaben
- Generierung von C
- Speicherung von C
- Widerruf und Sperrung von C 
  - **Certificate Revocation Lists**
  - **Online Certificate Status Protocol**
- Aktualisierung von C
- Beglaubigung von Verträgen (wie Notar)

### Benutzerzertifizierung Ablauf
1. Schlüsselgenerierung
2. Personalisierung, Certification Request
   - Feststellung der Identität
   - Benutzer beweist Besitz des privaten Schlüssels
3. Zertifikat generieren
4. Zertifikat signieren

### X.509 Attribute
- Version
- SerialNumber
- SignatureAlgorithm `SHA-256 mit RSA`
- Issuer
- Validity
- Subject
- SubjectPublicKeyInfo (Algorithmus, Schlüssel, Verwendung, Länge, Exponent)
- Alternativer Name (mittlerweile wichtig für mehrere Domains)
- Signature (signiert alles obere)
