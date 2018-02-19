# Symmetrische Kryptosysteme

### Forderungen
- Konfusion - es kann möglichst wenig von Chiffretext auf Klartext geschlossen werden
- Diffusion - kleine Inputänderungen -> große Outputänderung

### Lesen von Look-Up Tabellen
- Rows first, Columns second
- Zahlen sind die Bit-Indizes aus dem Input

## DES
- Blockchiffre mit 64 Bit
- Schlüssellänge 64 Bit, davon 8 Paritätsbits (jedes 8.)
- Permutation, Substitution und XOR

### Ablauf
1. Initialpermutation des 64-bit Inputs
2. 16 Schlüsselabhängige Iterationen mit je einem 48-bit Teilschlüssel
3. Inverse Initialpermutation

### Initialpermutation
- Wird von der Inversen Initialpermutation aufgehoben
- Verteilt die 64 Bit gleichmäßig auf linke und rechte Hälfte
- Verbessern die Sicherheit nicht, nur die Implementierung auf Hardware

### DES Iteration
- $L, R$ = linker und rechter Block
- $K(i)$ = Schlüssel in Iteration $i$
- $f$ = Verschlüsselungsfunktion

<img src="https://github.com/batzner/unistuff/raw/master/LMU/IT-Sicherheit/img/des-iteration.png" width=500/>

### DES Funktion f
- $E$ = Expansion (fix)
- $A = K(i+1) \bigoplus E(R(i))$ (XOR)
- $SX$ = S-Box Substitution von 6 zu 4 Bit
- $P$ = Permutation (fix)

<img src="https://github.com/batzner/unistuff/raw/master/LMU/IT-Sicherheit/img/des-funktion.png" width=500/>

### DES S-Boxen
- Input Bits 1 und 6 bestimmen Zeilenindex
- Input Bits 2, 3, 4 und 5 bestimmen Spaltenindex
- Output ist Wert der Zelle

### DES Schlüsselauswahl
1. 64-Bit Key wird auf relevante Bits gekürzt
2. Key wird permutiert
3. Key wird in zwei Teile C und D mit je 28 Bit aufgeteilt
4. Blöcke werden zyklisch nach links geshiftet (um 2 Bit, außer in 4 Runden)
5. C(i) und D(i) werden nach jedem Shift zusammengefügt, 
6. Aus C(i)+D(i) 8 bestimmte Bits entfernen und die restlichen 48 Bit permutieren = K(i)

### DES Entschlüsselung
- Schlüsselreihenfolge ist umgekehrt (K16 für erste Runde)

### Stärken
1. Avalanche-Effekt durch S-Boxen und Permutation P  
  Eine Änderung eines Bits verursacht Änderung von durchschnittlich 50% der Ausgabe. Breitet sich schnell aus.
2. 16 Iterationen - alles drunter macht known-plaintext Angriffe effizienter als Bruteforce
3. Hardware-effizient, da Iterationen und ähnliche Ver- /Entschlüsselung

### Schwächen
1. Teilweise geheimes Design
2. Zu geringe Schlüssellänge
3. Optimiert auf Implementierung in Hardware - IP und IIP verbessern die Sicherheit nicht

### 2DES und 3DES
- Doppelte Ausführung bringt keine relevante Steigerung, verdoppelt nur die Komplexität
- 3DES verschlüsselt, entschlüsselt mit zweitem Key und verschlüsselt dann mit drittem Key

## Abstraktionen

### Feistel-Chiffren
- Symmetrisch
- Zerlegung von Eingabeblock in zwei Teile
- n Runden mit Rundenschlüsseln
- Funktion f ist nicht umkehrbar
- Alternierende Substitutionen und Permutationen für Konfusion und Diffusion

### Blockchiffren
- Feste Blocklänge
- Am Ende Padding - Länge des Paddings muss hinterlegt werden
- Ciphertext = Konkatenation der Output-Blöcke

### Stromchiffren
- Verschlüsseln jeweils kleine Einheiten (1 Bit / 1 Byte)
- XOR mit Keystream
- Keystream wird aus Pseudo-Zufallszahlen-Generator erzeugt
- PRNG wird mit Shared Secret initialisiert

### Electronic Codebook Mode
- Jeder Block wird mit demselben Schlüssel verschlüsselt -> identische Ciphertext-Blöcke
- Erlaubt Angreifern Löschen, Vertauschen und Einfügen von Blöcken 
- Erlaubt Angreifern Rückschlüsse auf den Klartext

### Cipher Block Chaining
- Klartext-Block wird **vor** der Verschlüsselung mit letztem Ciphertext-Block XOR verknüpft
- Fortpflanzung von Übertragungsfehlern

## AES
- $N_b$ = Blocklänge = $4 \cdot N_b$ Bytes = Anzahl der Reihen 
- $N_k$ = Schlüssellänge = $4 \cdot N_k$ Bytes
- $N_r$ = Runden = $max(N_b, N_k) + 6$
- Runden arbeiten auf State. Input wird als Column-First-Matrix interpretiert!

### Verschlüsselung
1. Addition des Schlüssels
2. Byte-Substitution
3. Zeilenshift
4. Außer in letzter Runde: Spaltenmix
5. Addition des Schlüssels
6. Zurück zu 2

### Entschlüsselung
1. Addition des Schlüssels
2. Inverser Zeilenshift
3. Inverse Bytesubstitution
4. Addition des Schlüssels
5. Außer in letzter Runde: Inverser Spaltenmix
6. Zurück zu 2

### Bytesubstitution
Mit S-Box -> aktueller Byte-Inhalt = (Zeile, Spalte)

### Zeilenshift
Jede Zeile um i-1 nach Links

### Spaltenmix 
- $s' = A s$
- $A = ((02, 03, 01, 01), ...)$ geshiftet nach links pro Reihe

### Addition des Rundenschlüssels
- Rundenschlüssel hat gleiche Form wie State
- Jede Spalte des Rundenschlüssels ist ein Wort
- Schlüssel wird rotiert und mit S-Box Bytesubstituiert, abhängig von Rundenkonstante

## AES Designkriterien

### Vorteile des Rundenschlüssels
- S-Box verhindert, dass mit Teilen des Schlüssels der Rest berechnet werden kann
- S-Box verhindert, dass zwei ähnliche Schlüssel viele gemeinsame Rundenschlüssel haben
- Rundenkonstante verhindert Symmetrien im Prozess

### Diffusion
- Nach 2 Runden hängen 50% Output-Bits von jedem Input-Bit ab
- Diffusion durch MixColumn - Änderung in einem Input-Byte verursacht Änderung in allen Output-Bytes

### Keine Angriffe bekannt, die besser als Brute Force sind ab 8+ Runden

