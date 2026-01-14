# Defaults
Remote management enabled. Allows managing remote servers using Server Manager
# Bare Minimum Setup
## Install Updates
Do this via `sconfig`
## Set Static IP Address
Get the interface index to configure it
```powershell
# Get index of interface to configure
Get-NetIPInterface -AddressFamily IPv4
# Disable DHCP
Set-NetIPInterface -InterfaceIndex <index> -Dhcp Disabled
# Set IP, network mask, and default gateway
New-NetIPAddress -InterfaceIndex <index> -AddressFamily IPv4 -IPAddress "192.168.1.70" -PrefixLength 24 -DefaultGateway "192.168.1.1"
# Configure DNS (optional)
Set-DnsClientServerAddress -InterfaceIndex <index> -ServerAddress "10.0.0.1"
# Verify config
ipconfig /all
```
## Setup PSRemoting (Remote PowerShell Sessions)
On domain controller:
- `Enable-PSRemoting`
- Potentially have to run `winrm quickconfig`
Connecting from a management client:
- Enable winrm: `Start-Service winrm` -- does this need to be run as admin?
- Add entry to trustedhosts: `set-item wsman:\localhost\client\trustedhosts -value <ip address of server>` -- does this need to be run as admin?
- Create PS session: `new-pssession -computername <server ip> -credential (get-credential)`
- Enter session: `enter-pssession <id>`
- List available ps sessions: `get-pssession`
## Rename computer
Open `sconfig`, select option 2, and rename
## Install AD DS
```powershell
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
Install-ADDSForest
```
## Set Desired DNS (it gets set to localhost)
Get the interface index of the desired interface
```powershell
# If you know the IP of the interface
Get-NetIPAddress <ip address if known>
# To get all interfaces
Get-NetIPInterface -AddressFamily IPv4
```
Optimum west coast DNS server: 167.206.112.138 or 68.111.106.68
```powershell
Set-DNSClientServerAddress -InterfaceIndex <idx> -ServerAddress <dns_ip>
```
Verify new config with
```powershell
Get-DNSClientServerAddress
```
## Set DNS for Pop!\_OS
`resolvectl dns <interface> <dns server address>`
This is a temporary change unless changed via the GUI tools
## Create Users
Command to create users:
```powershell
New-ADUser
   [-AccountExpirationDate <DateTime>]
   [-AccountNotDelegated <Boolean>]
   [-AccountPassword <SecureString>]
   [-AllowReversiblePasswordEncryption <Boolean>]
   [-AuthenticationPolicy <ADAuthenticationPolicy>]
   [-AuthenticationPolicySilo <ADAuthenticationPolicySilo>]
   [-AuthType <ADAuthType>]
   [-CannotChangePassword <Boolean>]
   [-Certificates <X509Certificate[]>]
   [-ChangePasswordAtLogon <Boolean>]
   [-City <String>]
   [-Company <String>]
   [-CompoundIdentitySupported <Boolean>]
   [-Country <String>]
   [-Credential <PSCredential>]
   [-Department <String>]
   [-Description <String>]
   [-DisplayName <String>]
   [-Division <String>]
   [-EmailAddress <String>]
   [-EmployeeID <String>]
   [-EmployeeNumber <String>]
   [-Enabled <Boolean>]
   [-Fax <String>]
   [-GivenName <String>]
   [-HomeDirectory <String>]
   [-HomeDrive <String>]
   [-HomePage <String>]
   [-HomePhone <String>]
   [-Initials <String>]
   [-Instance <ADUser>]
   [-KerberosEncryptionType <ADKerberosEncryptionType>]
   [-LogonWorkstations <String>]
   [-Manager <ADUser>]
   [-MobilePhone <String>]
   [-Name] <String>
   [-Office <String>]
   [-OfficePhone <String>]
   [-Organization <String>]
   [-OtherAttributes <Hashtable>]
   [-OtherName <String>]
   [-PassThru]
   [-PasswordNeverExpires <Boolean>]
   [-PasswordNotRequired <Boolean>]
   [-Path <String>]
   [-POBox <String>]
   [-PostalCode <String>]
   [-PrincipalsAllowedToDelegateToAccount <ADPrincipal[]>]
   [-ProfilePath <String>]
   [-SamAccountName <String>]
   [-ScriptPath <String>]
   [-Server <String>]
   [-ServicePrincipalNames <String[]>]
   [-SmartcardLogonRequired <Boolean>]
   [-State <String>]
   [-StreetAddress <String>]
   [-Surname <String>]
   [-Title <String>]
   [-TrustedForDelegation <Boolean>]
   [-Type <String>]
   [-UserPrincipalName <String>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```
ex: `New-LocalUser -Name "Skye Gibney" -GivenName "Skye" -Surname "Gibney" -SamAccountName "S. Gibney" -UserPrincipalName "sgibney@archie.local" -Path "OU=OGs,DC=archie,DC=local" -AccountNeverExpires -Description "Just a really chill enby" -Password (Read-Host -AsSecureString "Input Password")`
### Users
- skye
	- Groups
		- Domain Admins
	- Password: Adaptive23!
# Setup Share Folder
Create the directory
Alter credentials on the directory
- e.g. grant domain admins full control`icacls C:\PublicFolder /grant "Domain Admins:F"`
Create share
- `net share Public=C:\PublicFolder`
Navigate to share via file explorer
- `\\dc01\Public`