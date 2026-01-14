# DHCP
Ports 67 and 68
Clients will set the destination IP address for a DHCP Discover packet to 255.255.255.255 (it's a broadcast)
Clients will use 0.0.0.0 as the source address of packets when trying to get network configs over DHCP
# ARP
The destination Ethernet address for ARP packets is ff:ff:ff:ff:ff:ff (i.e. a broadcast)
# ICMP
Types of ICMP packets
- 0: reply
- 8: ping
# Routing Protocols
- OSPF
- EIGRP
	- Cisco proprietary
- BGP
- RIP
Router can hold about 65k TCP connections simultaneously if processing power is not a factor
# DNS
Port 53
Review record types
`whois` - command to find information about a DNS record
# HTTP
Port 80
Can use telnet or netcat to hand craft HTTP requests
- `telnet <ip> <port>`
- `netcat <ip> <port>`
## HTTPS
Port 443
1. Establish TCP connection
2. Establish TLS session
3. Communicate using HTTP
# FTP
Ports 20 and 21
Text-based protocol, can connect with telnet or netcat and use text to send commands
Can use client app with more intuitive repl commands
Client commands:
- `USER` - input username
- `PASS` - enter password
- `RETR` - retrieve a file from server
- `STOR` - upload file to server
- `LIST` - get list of files on the server
- `TYPE A` - switch to ascii mode (text)
- `SYST` - get system info
- `QUIT` - quit session
# SMTP
Port 25
Only for sending email
Text-based like FTP and HTTP 1
Client commands:
- `HELO` or `EHLO` - initiate session
- `MAIL FROM <sender address>`
- `RCPT TO <recipient address>`
- `DATA` - begin sending content of the message
- `.` on a line by itself - signal the end of the message
# POP3
Port 110
Retrieving email
Client commands
- `USER <username>`
- `PASS <password>`
- `STAT` - get number of messages and the total size
- `LIST` - list all messages and their sizes
- `RETR <message_number>`
- `DELE <message_number>` - mark for deletion
- `QUIT` - end session and apply marked changes
# IMAP
Port 143 or 993 with TLS
More complicated commands than POP3
Client commands:
- `LOGIN <username> <password>`
- `SELECT <mailbox>`
- `FETCH <mail_number> <data_item_name>`
	- e.g. `FETCH 3 body[]` - get body of message number 3
- `MOVE <sequence_set> <mailbox>` - move messages to another mailbox
- `COPY <sequence_set> <mailbox>` - copy messages to another mailbox
- `LOGOUT`
# Ports

| Telenet | 23                                        |
| ------- | ----------------------------------------- |
| DNS     | 53                                        |
| HTTP    | 80                                        |
| HTTPS   | 443                                       |
| FTP     | 20, 21                                    |
| FTPS    | 990                                       |
| SMTP    | 25                                        |
| smtps   | 465 (legacy), 587 (with starttls command) |
| POP3    | 110                                       |
| POP3S   | 995                                       |
| IMAP    | 143                                       |
| IMAPs   | 993                                       |
# TLS
Don't trust self-signed certificates
# Using wireshark to intercept chromium traffic
Start chromium using `chromium --ssl-key-log-file=~/ssl-key.log`
Use wireshark to capture packets
Tell wireshark where the ssl key log file is
# Wireshark
See file properties: Statistics > Capture File Properties
Merge PCAP Files: File > Merge
Go to packet number: Go > Go to Packet...
Search packets: Edit > Find Packet
Mark packets: right click or go to Edit
Comment on packets: right click or go to Edit
Export packets: File > Export Specified Packets...
Export Objects (i.e. files): File > Export Objects
Time format: View > Time Display Format > ...
Export view: Analyze > Expert Information or bottom left thingy
Easily create filter: Right click > apply as filter
Easily prepare filter: Right click > Prepare as Filter
Follow a conversation
- Right click > Conversation Filter > ...
- Right click > Colourise Conversation > ...
Create column from packet section: Right click > Apply as Column
Follow stream: Right Click > Follow > ...
# Tcpdump
Based on libpcap (ported to Windows as winpcap)
Pipe to wc to get number of packets (i.e. number of lines)
Pipe to head or tail to get the first or last n packets
`man pcap-filter` to get filtering options
Options
- -i _interface_ 
- -w _output_file_
- -r _input_file_
- -c _count_
- -n - don't resolve IP addresses
- -nn - don't resolve IP addresses and don't resolve protocol numbers
- -v - verbose
- -vv - more verbose
- -vvv - even more verbose
Filters
- \[_src_|_dst_] port _port_num_
- \[_src_|_dst_] host _ip_or_hostname_
- icmp - get all icmp packets
- "tcp[tcpflags] & tcp-syn != 0" - get all packets with at least syn flags
- "tcp[tcpflags] == (tcp-syn|tcp-rst)" - get all packets with only syn and reset flags
	- tcp-syn
	- tcp-ack
	- tcp-fin
	- tcp-rst
	- tcp-push
- _greater_|_less_ _LENGTH_ - filter packets greater or less than a certain length
Display
- -q - quick output
- -e - print link-level header
- -A - print packet data in ASCII
- -xx show entire packet in hex
- -X show packet headers and data in hex and ASCII
# nmap
Default scan when run with local user privileges is -sT (connect scan)
Specify targets
- Range: 192.168.0.2-10
- Subnet: 192.168.0.0/24
- Hostname: example.home
Options
- -sn - perform a ping scan to see what hosts are on the network
- -sL - list targets without scanning
- -sT - scan using TCP connects (connect scan)
- -sS - scan using TCP syn (syn scan)
- -sU - UDP scan
- -F - scan only the 100 most common ports
- -p- - scan all ports
- -p-25 - scan ports 1-25
- -p10-1025 - scan ports 10 - 1024
- -O - detect OS
- -sV - detect services and version
- -A - detect everything
- -Pn - scan all possible hosts, even if no ICMP reply was received
- -T - timing
	- 0 - 9.8 hours
	- 1 - 27.53 minutes
	- 2 - 40.56 seconds
	- 3 - 0.15 seconds
	- 4 - 0.13 seconds
- --host-timeout - max time to wait for a host
- --min-rate and --max-rate - specify packets per second
- --min-parallelism and --max-parallelism
- Same verbosity controls as tcp-dump (-v, -vv, -vvv, -vvvv)
- -d - debugging (also -dd, -ddd, -dddd, -d2, -d3, -d9, etc)
- -oN _filename_ - normal output
- -oX _filename_ - xml output
- -oG _filename_ - grepable output for grep and awk
- -oA _basename_ - output in all major formats
