# Hash Values (Bottom of the Pyramid)
Use hash values to identify malicious files
Windows: `Get-FileHash <file> -Algorithm MD5`
Linux: `md5sum <file>`
# IP Addresses
Can block IP addresses
Adversaries can use Fast Flux to evade blocklists - essentially they use a large number of compromised hosts as reverse proxies so that the malicious traffic comes from many different domains/IPs
# Domain Names