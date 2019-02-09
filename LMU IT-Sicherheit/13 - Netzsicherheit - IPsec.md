# Netzsicherheit - IPSec

## Überblick
- IP Authentication Header
  - Integrität
  - Authentisierung des Datenursprungs
  - Optional: Anti-Replay durch Sequenznummer
- IP Encapsulating Security Payload
  - Vertraulichkeit
  - Integrität
  - Authentisierung der Security Association
  - Anti-Replay Dienst
  
Betriebsmodi:
- Transport Mode -> Ende zu Ende
- Tunnel Mode -> Nur Gateways müssen wissen, was IPSec ist

## Authentication Header
- Integrität durch ICV = HMAC-MD5( gesamtes Paket, Key )
  - Nicht auf Time To Live etc.
- Authentisierung durch gemeinsamen Schlüssel
- Anti-Replay durch Sequenznummer

### Transport Mode
IP-Header | AH-Header | Daten

### Tunnel Mode
IP-Header neu | AH-Header | IP Header alt | Daten

IP-Header neu ist ebenfall gesichert durch Hashing
- Wird vom Security Gateway generiert mit seiner IP-Adresse als Quelladresse

### Aufbau
- 8 Next Header -> =TCP / =IP etc.
- 8 AH Length -> für unterschiedliche ICVs 
- 16 Reserved
- 32 Security Parameter Index -> Legt verwendete Verfahren fest
- 32 Sequence Number
- 64 Integrity Check Value 

## Encapsulating Security Payload

