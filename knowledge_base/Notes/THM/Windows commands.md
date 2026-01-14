%windir% - Windows directory environment variable
lusrmgr.msc - manage users
msconfig - system configuration
taskmgr - task manager
useraccountcontrolsettings - UAC settings
compmgmt- computer management
perfmon- performance monitor
? - disk management
msinfo32 - system information
resmon- resource monitor
cmd
- hostname
- whoami
- ipconfig
- netstat
- net
regedit32 - registry editor
control /name
- Microsoft.WindowsUpdate
Volume Shadow Copy???

cmd commands
- set - print all environment variables
- ver - get version info
- systeminfo
- netstat
- ipconfig
- tracert
- net
- whoami
- hostname
- ping
- tree
- type - cat alternative
- copy - cp alternative
- move - mv alternative
- dir - ls alternative
	- /s - list all subdirectories as well
	- /a - show hidden files
- mkdir
- rmdir
- erase - remove files
- more - can be piped to or can list contents of a file
- tasklist
	- /? - help with filters
	- /FI "imagename eq *imagename*" - all tasks where the image name is equal to *imagename* (executable name - e.g. notepad.exe)
- taskkill /PID *pid*
- chkdsk
- drierquery
- sfc /scannow - system file checker checks for corrupted OS files and replaces them
- shutdown /s
	- /r - restart
	- /a - abort scheduled shutdown

# Powershell
Can interface with the .NET framework
Object-oriented
Start powershell from cmd: `powershell`
Powershell commands are known as cmdlets
Uses pipes like unix, except ps can pass objects instead of just text

## cmdlets
- Get-Content - show file contents
- Set-Location - set current working directory
- Get-Command - list all available cmdlets, functions, aliases, and scripts
	- -commandtype 'function' - get only functions
	- -name 'remove*' - get all commands starting with 'remove'
- Get-Help - man alternative
	- -examples - get examples of command
- Get-Alias - get all aliases
	- Stuff like `ls` is an alias for a powershell cmdlet
- Find-Module -name 'modulename*' - find all modules starting with 'modulename'
- Install-Module -name 'modulename' - install the 'modulename' module
- Get-ChildItem - ls and dir are aliases for this command
- Set-Location - cd is an alias
- New-Item
- Remove-Item
- Sort-Object *property* - e.g. Get-ChildItem | SortObject Length
- Where-Object - specify conditions
	- e.g. Get-ChildItem | Where-Object -Property "Extension" -eq ".txt"
		- Get all files in the current directory with the .txt extension
		- Can use eq, neq, lt, gt, lt, ge, like
- Select-String - findstr is an alias
	- e.g. Select-String -Path "./file.txt" -Pattern "term"
- Get-ChildItem | Where-Object -Property Length -gt 100
	- Get all files in the current directoy that are greater than 100 bytes
- Get-ComputerInfo
	- systeminfo gets similar information but less
- Get-LocalUser - show all local user profiles
- Get-NetIPConfiguration
- Get-NetIPAddress
- Get-FileHash
- Get-NetTCPConnection
- Get-Service
- Get-Process
- Invoke-Command - can execute commands on remote machines
	- e.g. Invoke-Command -ComputerName DC01 -ScriptBlock { some-commands }
# Windows Security Event IDs

| Event ID | Description            |
| -------- | ---------------------- |
| 4624     | Successful login       |
| 4625     | Failed login           |
| 4634     | Successful logoff      |
| 4720     | Account created        |
| 4724     | Password reset attempt |
| 4722     | Account enabled        |
| 4725     | Account disabled       |
| 4726     | Account deleted        |
| 104      | Event logs removed     |
