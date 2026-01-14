`tcpdump -A -i eth0`
- -A will attempt to print packet contents in ascii, useful for unencrypted payloads
- -i specifies which interface to listen on
When tcpflow is unavailable:
- `tcpdump -w output.pcap --print`
	- Then open the file in wireshark and do Analyze > Follow > TCP Stream
ip spoofing: `ifconfig <interface> <ip> netmask <network mask>`

## Scapy
- `sendp()` will send frames at the layer 2 level(???) and `send()` will send packets at the layer 3 level
