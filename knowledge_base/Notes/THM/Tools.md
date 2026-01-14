Hydra - url login brute forcer
Gobuster - dns, vhost, and url directory enumberator
John the Ripper - hash cracker
Metasploit - all around exploitation framework
SQLMap- automated tool for detecting and exploiting SQL injection vulnerabilities
 - `--wizard` - have the tool ask you questions about what you want
 - `-u` - specify url
 - `--dbs` - extract all database names
 - `-D DATABASE_NAME --tables` - extract all tables
 - `-D DATABASE_NAME -T TABLE_NAME --dump` - dump table contents
 - `sqlmap -u http://example.com/param=value`
	 - Tests whether the parameter is exploitable
- Note: wrap url in single quotes to avoid interpreting escape or interpolation sequences
	- Use `--level=#` to specify the level of the scan
- `--time-sec=1` - number of seconds to delay DBMS response during time-based SQL injection testing
- `--threads=8` - use 8 threads to speed up queries
# Other Defensive tools
- Autopsy - end to end open source digital forensics platform
- CAPA (Common Analysis Platform for Artifacts) - describes what a program or piece of code is capable of. Good for malware analysis
	- Note: use -j to output json, -v for verbose output, and -vv for super verbose output. Upload json file to CAPA Web Browser to get gui navigation of the information
- REMnux VM - Linux VM with included malware analysis utilities (Volatility, YARA, Wireshark, oledump, INetSim) and a sandbox-like environment
	- oledump - tool for reading alternate data streams
	- INetSim - kind of like a 
	- Volatility - analyzing memory images to extract artifacts and save the results, especially during investigations
- FlareVM - forensics, log analysis, and reverse engineering
	- Reverse engineering and debugging
		- Ghidra
		- x64dbg
		- OllyDbg
		- Radare2
		- Binary Ninja
		- PEiD
		- Flare Obfuscated String Solver
	- Disassemblers and decompilers
		- CFF Explorer
		- Hopper Disassembler
		- RetDec
	- Static and dynamic analysis
		- Process hacker
		- PEview
		- Dependency walker
		- DIE
	- Forensics and incident response
		- Volatility
		- Rekall
		- FTK Imager
	- Network analysis
		- Wireshark
		- Nmap
		- Netcat
	- File analysis
		- FileInsight
		- Hex Fiend
		- HxD
	- Scripting and automation
		- Python
		- PowerShell Empire
	- Sysinternals suite
		- Autoruns
		- Process explorer
		- Process monitor
# SIEM
False alarms indicate that some alerts need tuning
Generate alerts based on rules
## Windows Logs
Event Viewer + Sysmon
## Linux Logs
Popular locations:
- /var/log/httpd
- /var/log/apache
- /var/log/cron
- /var/log/auth.log - auth-related logs
- /var/log/secure - auth-related logs
- /var/log/kern - kernel logs
- /var/log/audit/audit.log - auditd log
### Ingestion methods
Agent/forwarder
Syslog
Manual upload
Port-forwarding
# Host-based FW
## Windows
Windows Defender.
## Linux
iptables
nftables
firewalld

ufw - simplified interface for iptables and nftables
# IDS
snort
- Modes
	- Packet sniffer
	- Packet logger
	- NIDS (default)
- PCAP analysis: `sudo snort -q -l /var/log/snort -r Task.pcap -A console -c /etc/snort/snort.conf`
# Vulnerability Scanner
OpenVAS (Greenbone)
Nessus