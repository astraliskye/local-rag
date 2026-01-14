Setup Burp with any browser. Install a proxy manager extension like FoxyProxy.
Navigate to http://burpsuite and download the CA Certificate
Add it to the browser trust store
- In Brave:
	- Settings
	- Privacy and Security
	- Security
	- Manage certificates
	- Authorities
	- Import
	- Navigate to the .der file that was downloaded from Burp
# Site Map
Target > Site Map
Populates as you navigate throughout the site
# Limiting Scope
Go to Target > Scope and add the domains/IPs you want to focus on
Go to Proxy Settings and select "AND target in scope"
