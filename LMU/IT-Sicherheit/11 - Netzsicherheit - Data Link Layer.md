# Netzsicherheit - Data Link Layer

## VPN
- Nachbildung eines LAN in beliebigen Topologien / Technologien
- Vertraulichkeit und Datenintegrität wie in physischem LAN
- Auf allen Schichten des ISO/OSI

### VPN auf Schicht 1
- Virtual Private Wire Service 
- Provider bietet Punkt zu Punkt Verbindung, die der Kunde selber nutzen darf

### VPN auf Schicht 2
- VLAN -> Mehrere Netze werden über denselben physischen Link betrieben, aber sind getrennt voneinander
- Virtual Private LAN Services - verbindet physisch getrennte LANs
- Point to Point Verbindungen

### VPN auf Schicht 3 und höher
- IPSec
- SSL/TLS
- OpenVPN
- Peer to Peer Anwendung (Schicht 7)

## VLAN / 802.1Q
### Reminder: Schicht 2 Aufgaben
- Fehlerfreie Übertragung von Frames (Prüfsummen)
- Flusskontrolle
- CSMA/CD bei Ethernet / CSMA/CA bei WLAN

VLAN:
- LAN-Infrastruktur über mehrere Switches hinweg -> Broadcasts usw. möglich über gesamtes VLAN Netz
- Soll aber andere VLAN-Netze, die auf gleicher LAN-Struktur arbeiten, nicht betreffen
- Definiert über IEEE 802.1Q
- Ethernet-Frame wird erweitert um 32 Bit Tag:
  - 16 Bit: 0x8100 für VLAN
  - 3 Bit: Priority 
  - 1 Bit: Canonical Format Indicator (Ethernet oder Token Ring)
  - 12 Bit: VLAN-ID -> 4094 verschiedene VLANs möglich

## PPP
- Punkt-zu-Punkt Protokoll
- Für Verbindungsaufbau über Wählleitungen: DSL, ISDN, Modem etc.
- Beinhaltet Link Control Protocol für Verbindungsaufbau, abbau und Aushandeln der Konfiguration
- Authentifizierung (optional) Protokolle:
  - Password Authentication Protocol (PAP)
  - Challenge-Handshake Authentication Protocol (CHAP)
  - Extensible Authentication Protocol (EAP)
  
### PAP
- Überträgt Passwörter im Klartext. WOW.
- Server kennt ID und Passwort aller Clients und schickt ACK
- Keine Authentisierung des Authenticators durch den Client :(

### CHAP
- Shared Secret zwischen A und B
- Zu Authentisierung werden öffentliche Infos (id, Zufallszahl, Name) mit Shared Secret gehasht und übertragen
- Sicher gegen Replay-Angriffe
- Implementierungen unterstützen leider immer noch PAP als Fallback -> Einfacher M.i.t.M. Angriff
- Keine Authentisierung des Authenticators durch den Client :(

### EAP 
- Bietet Aushandlungsmechanismen für konkretes Verfahren, also eher ein Framework

### Point to Point Tunneling Protocol
- PPP wurde für direkt verbundene Systeme entwickelt
- PPTP schickt seine Pakete durch das Internet und realisiert einen Tunnel
- Simuliert ein Kabel zwischen zwei Systemen
- Voluntary Tunneling -> Client setzt PPTP aktiv ein
- Compulsory Tunneling -> Client denk, es ist eine PPP Verbindung

### MS-CHAPv1 - Microsoft PPTP Implementierung
- Sau viele Sicherheitslücken
- Zentral: ermöglicht Known-Plaintext, da Challenge C im Klartext übertragen wurde und dann zurück entschlüsselt übertragen wurde.

### MS-CHAPv2 Änderungen
- Sau kompliziert
- Hängt von Benutzerpasswortsicherheit ab

## IEEE 802.1X
- 802.1X = Port Based Network Access Control
- Authentisierung und Autorisierung in IEEE 802 Netzen (WLANs, Bluetooth, Ethernet, VLAN etc.)
- Definiert kein eigenes Protokoll, sondern nutzt EAP, EAP-TLS und RADIUS
- Authentisierung ist immer Ende zu Ende -> Authenticator kann nicht mitlesen -> Eduroam

### Rollen
- Supplicant: 802.1X Gerät, das sich authentisieren möchte
- Authenticator: Gerät, an dem der Supplicant angebunden ist (Switch oder WLAN AP)
- Authentication Server: z.B. RADIUS-Server -> Macht eigentliche Authentisierung
- Port Access Entity (PAE): Port, an dem Supplicant angeschlossen ist
  - Uncontrolled Port für Authentisierung
  - Controlled Port für Kommunikation

### Ablauf
1. Supplicant fordert Controlled Port
2. Authenticator fordert Authentisierung
3. Nach erfolgreicher Authentisierung Port wird freigeschaltet

- RADIUS als AAA Protokoll (Authentisierung, Autorisierung, Accounting)
- Eduroam nutzt 802.1X mit RADIUS-Authentifizierung an der jeweiligen Hochschule
- Eduroam baut End-zu-End verschlüsselten Kanal zwischen Supplicant und seiner Hochschule auf, um Passwort zu bestätigen
- Eduroam kann mit eduroam-spoofing angegriffen werden, ist aber einfach zu erkennen, da falsches Zertifikat
