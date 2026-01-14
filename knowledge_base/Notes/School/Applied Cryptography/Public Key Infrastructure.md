# Digital Signatures and Certificates

Document: message or data (i.e. a bunch of bits)

Digital signature: encrypt hash of document with signer's private key
- Not forgeable - only the signer should have that private key
- Not alterable - if the document changes, it will not match the hash any longer and invalidate the signature
- Not reusable - based on the hash of the document, so cannot be applied to other documents
- Not repudiable - signer cannot deny signing the document
- Used in BitCoin

Don't sign anything you did not create
- Create the document yourself
- Alter or perturb the document before signing

Digital Certificates
- Serial Number - added by CA to perturb document
- Subject's information
	- Name
	- Web address
	- etc.
- Subject's public key
	- Varies on how this is given from CA to CA
- Hash of that information
- Signature of Certificate Authority
- Name of Certificate Authority
- When someone asks for your public key, you send them the digital certificate
	- Verifier has to know CA's public key
		- Public keys are installed in the OS or browser
		- Hundreds of CA public keys
		- Stored in keystore

Certificate Authorities
- Private companies who 
- ex: Verisign, Let's Encrypt
- Their private key is extremely valuable
	- Stored on a secure airgapped computer
	- Technicians bring information into secure room on USB and sign on that computer
- A centralized form of trust management

Components of PKI: public-key cryptography, digital certificates, and certificate authorities

Web of trust: decentralized trust management
- People meet in person to verify identity and establish trust
- If enough people do this, a web of trust grows where
- Heavy use of hierarchical certificates

Issue: can't have secure communication between two endpoints if neither one knows the other's public key. Need trust to be able to obtain public key, due to MITM attacks. Keystores are the root of trust in centralized trust management, which are collections of hundreds of CA public keys
- One endpoint then will send a certificate to the other endpoint over an insecure connection containing their public key. This certificate is signed by a CA, which the other endpoint will be able to verify using their keystore and henceforth trust the other endpoint's public key

China and Germany have state-run certificate authorities

Companies can run internal CAs and provide sub-certificates to internal servers. Must install root certificates for each machine. Although this means that the company can MITM inbound and outbound connections

Should not have ISPs be certificate authorities. Google has CA status and is also an ISP in some sense. They are therefore able to MITM any connection

Hierarchical certificates:
- Contents
	- Public key
	- Signature by ASU CA
	- ASU certificate from Verisign
	- Verisign signature
- End CA > Intermediate CA > Root CA

Root CA: a CA whose certificates come pre installed in keystores
Internal CAs: CAs trusted within corporate networks

Revoking certificates
- Windows update
- Browser updates
- OCSP - Online Certificate Status Protocol
	- Verify whether a CA's private key is still confidential

CAs are never contacted to verify certificates

Attacking PKI: modify keystore of client

