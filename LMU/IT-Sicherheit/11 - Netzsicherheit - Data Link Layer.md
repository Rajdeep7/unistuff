# Netzsicherheit - Data Link Layer

## VPN
- Nachbildung eines LAN in beliebigen Topologien / Technologien
- Vertraulichkeit und Datenintegrität wie in physischem LAN
- Auf allen Schichten des ISO/OSI

### VPN auf Schicht 1
Virtual Private Wire Service - Provider bietet Punkt zu Punkt Verbindung, die Kunde selber nutzen darf

### VPN auf Schicht 2
- VLAN
- Virtual Private LAN Services - verbindet physisch getrennte LANs
- Point to Point Verbindungen

### VPN auf Schicht 3
- IPSec
- SSL/TLS
. OpenVPN

## VLAN
- LAN-Infrastruktur über mehrere Switches hinweg
- Definiert über IEEE 802.1Q
- Ethernet-Frame wird um VLAN-ID erweitert, 4094 verschiedene VLANs möglich

### Reminder: Schicht 2 Aufgaben
- Fehlerfreie Übertragung von Frames (Prüfsummen)
- Flusskontrolle
- CSMA/CD bei Ethernet / CSMA/CA bei WLAN

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

### CHAP
- Shared Secret zwischen A und B
- Zu Authentsierung werden öffentliche Infos (id, Zufallszahl, Name) mit Shared Secret gehasht und übertragen
- Sicher gegen Replay-Angriffe
- Implementierungen unterstützen leider immer noch PAP als Fallback -> Einfacher M.i.t.M. Angriff

### EAP 
- Bietet Aushandlungsmechanismen für konkretes Verfahren, also quasi ein Meta-Protokoll

### Point to Point Tunneling Protocol
- PPP wurde für direkt verbundene Systeme entwickelt
- PPTP schickt seine Pakete durch das Internet und realisiert einen Tunnel

## IEEE 802.1X
- 802.1Q für Virtual Bridged LANs
- 802.1X = Port Based Network Access Control
  - Authentisierung und Autorisierung in IEEE 802 Netzen
  - z.B. in WLANs

### Rollen
- Supplicant: 802.1X Gerät, das sich authentisieren möchte
- Authenticator: Gerät, an dem der Supplicant angebunden ist (Switch, oder WLAN AP)
- Authentication Server: z.B. RADIUS-Server
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
