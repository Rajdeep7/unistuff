# Kryptographische Grundlagen
- **Kryptographie** - Lehre von Methoden zur Ver- und Entschlüsselung von Nachrichten
- **Kryptoanalyse** - Lehre von Methoden zur Entschlüsselung, ohne im Besitz des Schlüssels zu sein
- **Kryptologie** = Kryptographie + Kryptoanalyse
- **Stenographie** - Methoden, die bereits die Existenz einer geheimen Nachricht verbergen  
  -> geheime Nachricht im Bild = **Semagramm**
  - Linguistische Steganographie
  - Technische Steganographie (Geheimtinten, unwichtige Bits in Bildern)
- Verdeckte Kanäle - Nachrichtentransport über nicht erkennbare Medien / Kanäle  
  Oftmals geringe Bandbreite, da sonst erkennbar
- **Geheimtext (Ciphertext)** - Verschlüsselte Nachricht

## Kryptographisches System
$KS = (M,K,C,e,d)$
- $M$ = Alle möglichen Klartexte (Messages)
- $K$ = Alle möglichen Schlüssel (Keys)
- $C$ = Alle möglichen Chiffretexte
- $e = M \times K \rightarrow C$ - Verschlüsselungsfunktion
- $d = C \times K \rightarrow M$ - Entschlüsselungsfunktion

## Symmetrische Verfahren
- Gemeinsamer, geheimer Schlüssel oder Shared Secret, aus dem die Schlüssel abgeleitet werden können
- DES, AES, Blowfish
- Meist 128 oder 256 Bit

## Asymmetrische Verfahren
- Schlüsselpaar: private key (wird nie übertragen) und public key
- RSA, DSA, ElGamal
- Meist 2048 bis 8192 Bit
- Meist Faktor 100 bis 1000 langsamer

## One-Time Pads
- Schlüssel wird niemals wiederverwendet
- Schlüssel ist mindestens genauso lang wie der Klartext

Nachteile:
- Schlüsselmanagement extrem aufwendig
  - Viele echte Zufallszahlen nötig
  - Schlüssel müssen sicher ausgetauscht werden
- Keine Integritätssicherung (Angreifer kann Ciphertext modifizieren)

## 5 Klassen Kryptoanalytischer Angriffe
- Brufe Force Schlüsselsuche
- ciphertext-only - Angreifer kennt Chiffren
- known-plaintext - Angreifer kennt Klartext-Chiffren-Kombinationen
- chosen-plaintext - Angreifer kann selber Klartexte wählen und verschlüsseln lassen
- chosen-ciphertext - Angreifer kann sich zu ausgewählten Chiffren den Klartext berechnen lassen
