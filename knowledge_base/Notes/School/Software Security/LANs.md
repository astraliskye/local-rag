Compromising confidentiality or integrity by sniffing a LAN

# Goals

- Impersonate a host
	- Exploit trust relationships between hosts
- Deny service
- Access information
- Tamper with delivery mechanisms
	- Break integrity

# Types of attacks

Sniffing: passively listen to conversations between nodes
Spoofing: pretending to be another machine
Hijacking: actively get in between a conversation in a MitM attack, able to later communication

Hub vs Switch
- Easy to sniff on a hub network
- Switches keep a table of ports and the MAC addresses of the interfaces connected to those ports in order to forward frames only to the port corresponding to the destination MAC address
	- Broadcast traffic is sent to all hosts
	- Directed traffic is only sent to the intended host

# Sniffing

Attacker's interface must be set to promiscuous mode
If on a switched network, the attacker must convince the switch to send a copy of the network traffic to the sniffing host

MAC flooding: send switch too many MAC addresses to overload its table so that when the switch gives up it may revert to hub behavior
MAC spoofing: attacker changes their MAC address to be the victim's in the hopes that the switch will forward traffic destined for the victim to the attacker
ARP spoofing with forwarding

Sniffing is effective because many protocols send authentication information in plaintext (FTP, POP, HTTP, IMAP)

Usually traffic is copied to a file for later analysis

- Collect
- Analyze
- Replay

## Tools
- `tcpdump`: collects traffic
	- Based on libpcap, which can be used to create custom sniffers
	- Requires root privileges to set interface to promiscuous mode
	- Can write expressions to define which packets to print
	- Options
		- -n: don't translate IP addresses to FQDN
		- -w: write packets to a file
		- -i: specify which interface to user
		- -e: print link-level address
		- -f: use a file for the filter expression
	- Filter expression: one or more "primitives" (qualifier + ID)
		- Qualifiers
			- host
			- net
			- port
			- src
			- dst
			- src and dst
			- ether
			- ip
			- arp
			- rarp
			- examples:
				- host hedwig and not ssh
				- less & greater to specify size
				- broadcast to get only broadcast packets
				- gateway to check if  packet used a host as a gateway
- `tcpflow`: reassembles TCP flows
- `tcpreplay`: re-sends recorded traffic
- `wireshark`: gui tool that supports TCP reassembling and can parse many protocols

# ARP Spoofing

Machines need to know what MAC addresses are associated with which IP addresses so that they know where to send packets on the local network

Attacker host sends ARP replies because ARP does not track state and doesn't know that it wasn't expecting a reply, so it accepts the reply and associates the attacker's MAC address with the intended IP address

ARP entries timeout and can be replaced by legitimate ARP replies. The attacker could spam ARP replies so that the ARP entry doesn't expire

MitM attack
- Victim machine 1 has MAC address MAC1 and IP address IP1
- Victim machine 2 has MAC address MAC2 and IP address IP2
- Attacker machine has MAC address MAC3 and IP address IP3
- Attacker spams ARP replies to victim 1, telling it that IP2 is located at MAC3
- Attacker spams ARP replies to victim 2, telling it that IP1 is located at MAC3
- Attacker sets IP forwarding to forward packets. The attacker machine's ARP table isn't poisoned, so it knows where to forward the packets to so that the communication between victim 1 and victim 2 continues

Tools for passively monitoring network traffic:
- `dsniff`
- `filesnarf`
- `mailsnarf`
- `msgsnarf`
- `urlsnarf`
- `webspy`

Tools for automatic spoofing:
- `arpspoof`
- `dnsspoof`
- `macof`

Tools for MitM attacks:
- `sshmitm`
- `webmitm`

Ettercap: tool for MitM attacks on LANs
- Supports ARP spoofing attacks
- Supports intercepting SSH1 and SSL connections
- Supports the collection of passwords for a number of protocols

Steps:
1. Setup IP forwarding: (linux) `echo 1 > /proc/sys/net/ipv4/ip_forwarding`
2. Start poisoning: `ettercap -C -o -M arp:remote /192.168.1.1/ /192.168.1.10-20/`
	- 
3. Collect traffic: `tcpdump -i eth0 -s 0 -w dump.pcap`

Defenses
- Static ARP entries
	- If org is too large, set static ARP entries on essential hosts like DNS servers and gateways
- Ignore unsolicited ARP replies (ARP requests can still be hijacked)
- Set timeouts on ARP entries
- Monitor with `arpwatch`

# Detecting Sniffers and Controlling Access

On each host, look for interfaces in `PROMISC` mode using `ifconfig`
- Not effective if the attacker has a kernel rootkit and can lie to `ifconfig`
Look for suspicious ARP activity with `arpwatch` and `XArp` for evidence of ARP spoofing
Sniffers may do reverse DNS lookups for IP addresses (turn IP addresses into domain names)
- Detect this by generating fake IP addresses and listen for reverse DNS lookups
If an interface is in promiscuous mode, the sniffer's OS is processing every single packet
- This lets us ping the sniffing host with low traffic on the network and compare with ping times with high traffic on the network. If there is a lot of traffic, the sniffing host, will take a lot of time to respond to a ping because it's processing so many packets
Look for weird kernel behavior
- Send an ICMP request with a wrong MAC address and a correct IP address. Since the sniffing host's interface is in promiscuous mode, it will accept the frame despite having the wrong MAC address and open the frame up and look inside. Upon seeing the correct IP address, it might respond. An interface that isn't in promiscuous mode would drop the packet as soon as it saw the incorrect MAC address
AntiSniff tool
- Overload sniffers to induce latency
Control network access
- Sniffing and hijacking attacks require physical access to the network, either physically being inside the network or by infecting a host that is on the network
802.1x - port-based access control protocol
- Devices authenticate when they're connected to the network before they can communicate