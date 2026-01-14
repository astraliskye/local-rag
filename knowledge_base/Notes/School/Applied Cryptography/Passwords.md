# Password Insecurity

Cryptographic techniques come in handy both when defending and attacking passwords
Passwords are highly usable and due to that they are insecure
Passwords are "shared secrets"

Password attacks:
- Brute force
- Sniffing
- Phishing
- Leakage
	- Users telling others their passwords
	- Others see your fingers when typing in password
- Cross site leakage
	- Password re-use across websites
- 

Securing passwords:
- Make it take more time per login attempt
- Increase password strength
	- Length
	- Larger set of possible characters
- Use a password manager to create long, random passwords without the stress of remembering
	- Has it's own issues, sending passwords between devices, single point of failure, etc.
- MFA
# Password Attacks

Password attacks:
- Password recovery
	- Issue with email recovery: email is itself insecure
- Stealing stored passwords
	- Cryptographic techniques are typically implemented in attacks here
	- Passwords are shared secrets. Applications host password files (password hashes)
	- SQLi

Cryptographically, can't really fix many of the weaknesses of passwords

Password protection for when passwords inevitably get leaked
- Can hash passwords
	- Counter: dictionary attack/rainbow table attack/brute force attack
		- Counter: salting
			- 
