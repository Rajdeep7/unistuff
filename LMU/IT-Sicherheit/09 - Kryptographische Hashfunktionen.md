# Kryptographische Hashfunktionen
- Integritätssicherung
- Manipulationen an einer Nachricht sollen erkannt werden können
- Normale Hashfunktion: nicht injektiv, Kollisionen möglich

### Kryptographische Hashfunktion: 
- Möglichst kollisionsresistent 
- = Ähnliche Eingaben sollten nicht denselben Hashwert haben
 
### Schwache Hashfunktion:
- Es ist praktisch unmöglich, für einen gegebenen Hashwert ein $m'$ mit selbem Hash zu finden
- Für ein k Bit langen Hash, braucht man $2^{k/2}$ Variationen der gefälschten Nachricht, um mit 50% Wahrscheinlichkeit eine Kollision zu erzeugen. Sehr einfach, da Leerzeichen, Synonyme etc. variiert werden können.
 
### Starke Hashfunktion:
- Es ist allgemein praktisch unmöglich, eine Kollision zu finden

### Konstruktion
- Kompressionsfunktion G wird wiederholt auf Block Mi und bisherigem Hashwert angewandt
- Benötigt Initialisierungsvektor
- Benötigt Padding für letzten Block
- Beispiel: DES CBC 

## MD5
- Eingabe: 512-bit Blöcke
- Ausgabe: 128 Bit
- Padding: 0's + Länge der Eingabe, um Kollisionen zwischen Dateien mit tatsächlichen 0en am Ende zu vermeiden
- Fixer Initialisierungsvektor (0x01234567 ...)
- Funktion besteht aus 4 Runden (für einen 512-bit Block)

### Sicherheit
Wang & Yu: Für jeden Initialisierungsvektor lassen sich in einer Stunde zwei Paare von Blöcken finden, die denselben Hash produzieren
- Ist also Unabhängig davon, was davor kommt und was danach kommt
- Zwei Dateien sind gleich außer in den Blöcken $M_i, M_{i+1}$ und $N_i, N_{i+1}$
- $MD5(M_i, M_{i+1}) = MD5(N_i, N_{i+1})$
- Trick für zwei Programme good und evil: So programmieren, dass die beiden Blöcke eine bestimmte Variable belegen und dann überprüfen, ob diese Variable `== M_i, M_{i+1}` ist. In der einen Version wird sie es sein, in der anderen nicht.
- Lösung: SHA-256, hat längeren Hash

## Zertifikierung
- "Yes, this person is who they say they are, and we, the CA, certify that."
- CA = Trusted Third Party
- Spezifiziert im X.509 Standard -> X.509 certificate, enthält Domain für HTTPS
- 

1. Server schickt CA seinen Public Key und eigene Identität
2. CA bestätigt Public Key und Identität (z.B. Domain Inhaberschaft)
3. CA signiert den Public Key mit eigenem Private Key und schickt resultierendes X.509 Certificate an Server
4. Client initiiert HTTPS mit Server
5. Server schickt Public Key und X.509 Certificate an Client
6. Client überprüft X.509 Certificate mit Public Key von CA (Schon im Voraus installiert)
