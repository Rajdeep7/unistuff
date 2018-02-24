# Netzsicherheit - WLAN-Sicherheit

### Anforderungen
- Vertraulichkeit
- Integrität
- Authentisierung
- Zugriffskontrolle

## Betriebsmodi
- Infrastrukturmodus
  - Access Point 
  - Station -> Client
  - Basic Service Set -> STAs, die denselben AP nutzen
  - Extended Service Set -> Hat SSID, Netz aus mehreren BSS (Eduroam in München = 1 ESS)
- Ad-Hoc-Modus
  - Kein Access Point erforderlich
  - Nur lokale Kommuniation zwischen STAs
  
## WEP
- PRNG = RC4
- 24-bit IV + 40-bit K = 64-bit Seed -> Keystream
- C = (M + CRC) XOR Keystream
- C und IV werden übertragen

### Authentisierung
- Open System Authentication -> Keine oder implizite durch Schlüssel
- Shared Key -> 4-Way-Challenge-Response, nur einseitig, mit WEP Schlüssel :(

### Zugangskontrolle
- Nicht standardisiert
- Teilweise MAC-Adressenbasierte ACLs -> kann einfach mitgelesen und gefälscht werden

### Probleme
- Keine Vertraulichkeit: Gleicher K für alle Kommunikationen mit dem AP -> Jeder kann mitlesen
- Keine Integrität: CRC ist gut zur Zufallsfehlererkennung, ist keine kryptographische Hashfunktion, sinnvolle Kollisionen können leicht erzeugt werden
- WEP Authentisierung ist keine wirkliche Authentisierung
- Kein Zugriffskontrolle
- Schlüsselmanagement: sehr selten gewechselt, 40 Bit oder 104 Bit -> fehleranfällig, da mühsam -> oft einfache Schlüssel gewählt

### WEP Known-Plaintext-Angriff 1
- Mallet kennt M und C
- C = (M|CRC) + RC4(IV,K)
- -> C1 + C2 = (M|CRC)1 + (M|CRC)2, falls IV gleich
- -> Man muss nur warten, bis IV nochmal kommt, kann gesteuert werden, durch Daten von außen schicken

### WEP Known-Plaintext-Angriff 2
- Mallet kennt M und C
- Keystream = C + (M|CRC)
- IV wiederverwenden, M ändern, Keystream verwenden -> Gültige Nachricht

### WEP Integritätsangriff
- C' = C + (M', CRC(M'))
- Kann Bits flippen, z.B. in IP Adresse

### 104-bit Angriff in 60 Sekunden
- ARP Pakete haben feste Länge -> erkennbar
- ARP Pakete sind vorhersagbar in den ersten 16 Byte
- Liefert erste 16 Byte des Keystream
- Abgehörte ARP Requests ins Netz einspielen -> beschleunigt Angriff, liefert viele IVs

## WPA
- Vertraulichkeit durch
  - TKIP
  - Rekeying Mechanismus
  - Schlüssel-Hierarchie
- Integritätssicherung durch 
  - MIC / Michael = kryptographische Hashfunktion
  - Mit Schlüssel parametrisiert
- Authentisierung
  - Erlaubt PSK (Pre-Shared Key) (sucks)
  - Bietet auch 802.1X
  
### Temporal Key Integrity Protocol

**1. Temporal Key**
- Für jede Richtung und für jede Station eigene Schlüssel
- 128 Bit für Verschlüsselung
- 64 Bit für Integritätssicherung
- rekey key Nachricht zur Erneuerung

**2. Pairwise Transient Key**
- Sicherung der Übertragung von TKs
- Ein Key für rekey nachricht, ein Key für Sicherung des TKs
- Key für rekey braucht man gegen DoS Angriffe

**3. Pairwise Master Key**
- Erzeugt von 802.1X Authentication Server, wird vom AP an STA weitergereicht
- Oder aus Preshared Key abgeleitet

### Schlüsselkey
- PMK -> PTK -> TK
- PTK wird über Zufallszahlen erzeugt

### WPA Schwächen
- Hardware-Abwärtskompatibel -> Verwendung von RC4 weiterhin problematisch
- Sicherheit hängt stark von PSK ab bei PSK
- Passwort kann innerhalb von wenigen Tagen geknackt werden

### Chop-Chop Angriff 
??? Fehlt, skipped

## Rainbow Tables
- Versuchen, optimalen Tradeoff zwischen Zeit und Speicher zu nutzen
- Hashfunktion n mal hintereinander auf Wörter anwenden -> Anfangswort und letzten Hash speichern
- Reduktionsfunktion zwischen den Hashes, um Kollisionen zu vermeiden
- Bei gegebenem Hash nach Zeile mit gegebenem Hash suchen -> Kette erneut durchlaufen
- Falls nicht in Tabelle: Reduzieren und dann nochmal hashen, bis gefunden

## WPA2
AES anstatt RC4
