Windows hashes password with NTLM
`man 5 shadow` - learn more about shadow password file
`man 5 crypt` - learn more about hashes
Use passwd to reset your own password
`sudo passwd <otheruser>`
`faillock --user <username> --reset` - reset failed login attempts
`hashcat -m <hash type> -a <attack type> hashfile wordfile`
# HMAC
Keyed-Hash Message Authentication Code
Provides authentication and integrity
1. Secret is padded and XOR'd with a constant
2. This value is concatenated with the data and then hashed
3. The key is padded and XOR'd with another constant, concatenated with the result of the last step, then hashed again


`base64 -d b64file`
# Cracking Hashes w/ John the Ripper
Note: John will say "no passwords loaded" when you fuck up the format
## Hash ID Utility
https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py
## Follow John the Ripper Installation Instructions
`john --format=<hash format> --wordlist=<wordlist> <path to hash file>`
Get available formats: `john --list=formats`
## NTLM & Windows
LM - old way Windows would hash passwords
NTLM - "new technology" (i.e. not MS-DOS) way Windows hashes passwords
Can obtain hashes using Mimikatz to dump the Windows SAM database or with the AD database NDTS.dit
You don't always have to crack the hashes to escalate in Windows/AD
## Shadow files
`unshadow` utility takes the /etc/shadow file and the /etc/passwd file and outputs a format that John the Ripper can crack
- `unshadow <passwd file> <shadow file> > <output file>`
Shouldn't have to specify the format when it is formatted like this
## Single Crack Mode
Mangle username to try to guess the password
Hash needs to be in the form: `<username>:<pw hash>`
Use the --single flag to specify
Don't need to specify a wordlist obviously, as this technique is based on username mangling
## Password Complexity Predictability
Define patterns for which passwords to generate, useful for example if you know that a user will end their password with a number followed by a symbol