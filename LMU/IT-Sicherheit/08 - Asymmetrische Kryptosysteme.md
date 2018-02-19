# Asymmetrische Kryptosysteme

### Protokoll
1. Erzeugung von Schlüsselpaaren
2. Austausch Öffentlicher Schlüssel
3. Verschlüsselung mit öffentlichem Schlüssel (oder privat bei Signatur)
4. Entschlüsselung mit privatem Schlüssel (oder öffentlich bei Signatur)

## RSA
- Sicherheit basiert auf Faktorisierungsproblem: 
  - p und q sind große Primzahlen
  - n = pq ist einfach
  - n -> p, q ist eindeutig, aber schwer
  
### Erzeugung eines Schlüsselpaars
1. Wähle zwei Primzahlen p, q
2. n = pq = RSA-Modul
3. Da n nur die 1, p, q und n als Teiler hat, sind alle Zahlen zwischen 1 und $\Phi(n)=(p-1)(q-1)$ teilerfremd zu n
4. Wähle 1 < e < $\Phi(n)$ (sollte groß sein, z.B. 65537, dauert dann aber länger
5. Public Key = $(n, e)$
6. $d = e^{-1} \text{ mod } \Phi(n)$ (über Euklid bestimmen)
7. Private Key = $(n, d)$

### Multiplikative Inverse 
- $d = e^{-1} \text{ mod } \Phi(n)$
- $d = Euklid(e, \Phi(n))$
- Search $d$ with $1 = _ \cdot \Phi(n) + d \cdot e$

### Ver- und Entschlüsselung
- $m$ ist die Nachricht mit $0 < m < n$
- $c = m^e \text{ mod }n$
- $m = c^d \text{ mod }n$

### Angriffe auf RSA
1. Brute Force - Zerlege n in p und q
2. Chosen-Ciphertext 
  1. Angreifer wählt Ciphertext $c' = s^e c mod n$ mit Zufallszahl s
  2. Angreifer bekommt $m'$ geliefert (wie auch immer)
  3. $m = m's^{-1}$
3. Timing Angriff
  - Laufzeit der Entschlüsselung verrät $d$
  - Lösung: Entschlüsselung mit zusätzlicher einmaliger Zufallszahl 
4. Angriff auf Signaturen
  - $m^e r^e = (mr)^e$
  - -> man kann ein Dokument aus korrekt signierten Teildokumenten zusammensetzen

## Schlüssellängen
- $n$ mit 1039-bit konnte bereits faktorisiert werden (über 300 Dezimalstellen)
- Bits of Security = äquiv. Schlüssellänge asymmetrischer Verfahren
  - 1024 bit RSA ist so sicher wie 80 bit AES
  - 2048 RSA - 112 AES
  - 3072 RSA - 128 AES
- Bis 2022 reicht 100 Bits of Security, danach 120

## Hybride Verfahren
- SSL/TLS, PGP, SSH

## Digitale Signatur
- Asymmetrische Verfahren sehr langsam
- -> nur Hash-Wert (Prüfsumme) signieren
- Prüfsumme muss signiert werden, dass sie nicht auch geändert werden kann
- MD5 Checksums sind auf Webseiten anzugeben, um zu:
  - Überprüfen, ob Datei richtig gedownloaded wurde
  - Datei über HTTP downloaden zu können und nur die Prüfsumme über HTTPS downloaden zu müssen
  - Datei von einer anderen Quelle downloaded zu können und bei der offiziellen Quelle überprüfen zu können, dass sie valide ist
  
### Anforderungen an Elektronische Signatur
1. Perpetuierungsfunktion - Fälschungssicher und dauerhaft
2. Echtheitsfunktion - Authentizität (CA ordnet Public Key einem Namen zu)
3. Wiederverwendbarkeit - Verhindert (nur möglich mit Private Key)
4. Abschlussfunktion - Nicht veränderbar (nur möglich mit Private Key)
5. Beweisfunktion - Nicht zu leugnen (durch Public Key eindeutig)
