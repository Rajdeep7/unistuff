# Sicherheitsmechanismen

## Vertraulichkeit
- Verschlüsselung!

## Integrität
- Hashwerte gegen Modifikation
- Hashwert + gesicherte Sequenznummern + Zeitstempel gegen Duplikate (**Replay-Angriff**)
- Verschlüsselung allein schützt nicht die Integrität! Daten können blind modifiziert werden
- Lösung: Hashwert und Sequenznummern ebenfalls verschlüsseln

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

### S/Key
1. Client schickt N (Anzahl gewünschter Passwörter) an Server
2. Server schickt Seed an Client
3. Client berechnet nachfolgende Passwörter über Kette von MD4 Hashes
4. Client nutzt Passwörter in umgekehrter Reihenfolge (N, N-1, N-2 ...)
5. Client übersetzt ein Passwort in 6 Wörter über ein fixes Wörterbuch
6. Server verifiziert Passphrase

Anfällig für Man in the Middle (Angreifer simuliert Server)

### One Time Password System
Änderungen zu S/Key:
- Ein Passwort kann nur ein einziges Mal verwendet werden -> nicht für parallele Sessions
- MD5 und SHA unterstützt

Angriffe:
- Wie oben, M.i.t.M., kann aber über IPSec Authentifizierung des Servers vermieden werden
- Wenn Hashes im Klartext abgefangen werden, kann man Passwor erraten

### Smartcards
Zugangsdaten werden auf Karte gespeichert oder erzeugt

### RSA SecurID
- Jede Minute neue Zahl, die nur zentraler Authentifizierungsserver vorhersagen kann
- 2 Faktor-Authentisierung zusammen mit Benutzerpasswort
- Berechnung über AES mit "echtem" Zufalls-Seed + Vergangene Sekunden seit 1986
- Hardwaremanipulation führt zu Hardwarebeschädigung

### Biometrie
- Matching Score regelt FN und FP Rate

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
- Ziemlich kacke, aber erfüllt Authentisierung von Alice

### 5.4 Symmetrisch Verschlüsselte [Signierter Hash + Nachricht]
- Vertraulichkeit
- Authentisierung des Datenursprungs
- Sendung kann nicht geleugnet werden
- Integrität

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
- Problem: Hash-Funktionen nutzen keinen Schlüssel
- Schlüssel wird verarbeitet und dann mit Nachricht konkateniert -> Dann gehasht

## Authentisierungsprotokoll Needham Schröder
- Third Party teilt mit jedem Kommunikationspartner eigenen Schlüssel

Ablauf:
1. Alice schickt eigene Adresse, Zieladresse und Zufallszahl an TTP
2. TTP schickt verschlüsselt Sitzungsschlüssel K an Alice zurück
3. TTP schickt außerdem den für Bob verschlüsselten Sitzungsschlüssel K, den Alice nicht lesen aber weiterleiten kann
4. Alice kommuniziert mit Bob über K

Problem: Replay-Angriff, K bleibt gültig

Lösung: Sequenznummern / Timestamps / begrenzte Gültigkeitsdauer

## 
