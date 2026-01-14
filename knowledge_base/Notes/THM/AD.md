Windows domain: group of users and computers under the administration of a given business
Active directory: repository to centralize management of Windows machines
- Identity management
- Security policies
- Catalogues objects:
	- Users: people or services
	- Machines
		- Machines are considered **security principals** like users and services
		- Machine accounts are the computer name followed by a dollar sign (e.g. the machine account for a computer named AUDIT01 is AUDIT01$)
			- Machine accounts are local administrators for the computer itself and are not intended to be used by others to log in
				- Passwords are 120 random characters and are automatically changed every so often
			- Machine accounts have limited privileges within the domain
	- Security groups
		- Default groups:
			- Domain admins - administrative privileges over the entire domain
			- Server operators - can administer DC, but can't change administrative group memberships
			- Backup operators - allowed to access any file, ignoring permissions
			- Account operators - can create or modify other accounts in the domain
			- Domain users - all users
			- Domain computers - all computers
			- Domain Controllers - all DCs
	- Printers
Domain controller: server that runs active directory services
GPOs are stored in AD as well as the SYSVOL folder on each domain controller
Have to enable View > Advanced Features to be able to delete OUs
**Delegation** of control
- Right click OU, select Delegate Control
- This allows others to administer the OU without domain admin (e.g. IT Support)
All computers are put into Computers OU by default
- Good practice to organize computers by use and at least separate servers, workstations, and domain controllers
Main idea behind OUs is to deploy policies per OU
### Group Policy
GPO - how Windows manages policies
gpupdate /force
Group Policy Management Console
Lives on SYSVOL share
- Defaults to C:\Windows\SYSVOL\sysvol
### Authentication
Services check user credentials against the domain controller
Two types of auth:
- Kerberos: default and newer
- NetNTLM: legacy
#### Kerberos
1. User sends username as well as a timestamp encrypted with the user's password hash to the KDC
	1. Key distribution center is often a service on the domain controller
2. KDC responds with a Ticket Granting Ticket and a Session Key. The user can use the Ticket Granting Ticket to request tickets for other services, meaning the user doesn't  have to send credentials any time they want to access a service
Then, say the user wants to talk to a service:
3. The user sends the TGT to the KDS
4. The user receives a Ticket Granting Service which contains a Service Session Key. The ticket Granting Service is encrypted with the hash of the owner of the service the user is trying to talk to
5. The user sends the TGS
6. The service decrypts the TGS using its own password hash and verifies the Service Session Key
#### NetNTLM
Challenge-response
1. Client sends auth request to the server they want to access
2. Server generates random number as a challenge to the client
3. Client generates a response using their password hash and the challenge. It sends this back to the server
4. The server forwards the challenge and the response to the Domain Controller
5. The server authenticates the credentials and sends the authentication result back to the client
This is the way domain accounts are authenticated. Local accounts can be authenticated on the server using credentials store locally
### Trees, Forests, Trusts
Tree: multiple domains that share the same namespace
- e.g. thm.local, uk.thm.local, us
Forest: union of multiple trees with different namespaces into the same network
Trust: a relationship between two domains
- One-way: one domain establishes trust with another. That other domain can then access resources in the original domain. E.g a user on the other domain can access a file server on the original domain
- Two-way

