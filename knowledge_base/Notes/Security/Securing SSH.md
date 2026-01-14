# Securing SSH
Exposing SSH to the public technically exposes the attack surface of the org. It's not necessarily less secure than anything else, but to keep with defense in depth and to give hackers a hard time, here are some other security controls that can be implemented:
- Require users to VPN into the network and then SSH to the machine
- Use a non-standard port for SSH
- Use pub/priv keypairs rather than credentials
- Implement fail2ban on the machine
- Deny root user logins on the machine