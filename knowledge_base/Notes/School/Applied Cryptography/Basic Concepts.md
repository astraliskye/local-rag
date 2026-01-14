Cryptography meaning
- Crypto - secret
- -graphy - writing

# History

- 1500 B.C. - Interest in number theory was beginning
- 300 B.C. - Euclid talked about units and prime numbers and other math stuff
- 150 B.C. - Caesar Cypher and other substitution ciphers
- 1550 A.D. - more ciphers (e.g. vignere)
- WW2 - most advancement toward modern cryptography
	- German enigma machine
	- Navajo code talkers
		- Part because no one knew the language
		- Part because the U.S. transposed word meanings (e.g. bird means ocean)
		- Technically steganography, not cryptography
- 1970 A.D. - modern cryptography begins being openly talked about outside of secret and proprietary projects
	- Number theory is introduced
	- DES (Digital Encryption Standard)
		- Superseded by AES
	- RSA - Public key encryption system
		- Still used today, along with ECC (Elliptic Curve Cryptography)
	- MD5
		- Superseded by SHA

Applied cryptography is taking the theoretical, number-theory based subject of cryptography and using it to determine how to secure data

Data can be either at rest (files) or in motion (stuff flying around on networks)

Cryptography ensures the **Confidentiality** of data at rest and in motion

# Intro

Random numbers, hashing functions, encryption

Use cases:
- Authentication
- Password management
- Secret communication
	- Authentication
	- Integrity (ensure messages cannot be modified)
	- Encryption
- Digital signatures/certificates
* RSA
* Number theory
* Timestamping
* Secret sharing
* Oblivious transfer
* Digital cash transfer
* Bitcoin
* Election algorithm

Protocols:
- AES
- RSA
- SHA

Cryptography protocols are brittle, subtle, and error prone
- Just because something is over-complicated doesn't mean it's secure
- Can ensure the algorithm is good through public disclosure
	- Researchers will test the algorithm and try to break it, and only by a large amount of unsuccessful attempts to break it can we ensure that the algorithm is secure

Example: use an RNG and a hash function to flip a coin over a network

- Alice
	- Picks a large random number `c`
	- Calculates the hash of `c` and calls it `p`
	- Sends `p` to Bob
- Bob
	- Bob guesses whether `c` is even or odd
- Alice
	- Sends `c` to Bob
- Bob
	- Calculates hash of `c` and ensures that it equals `p`

This assumes collision-free hashing and a secure RNG source

# Good Crypto and Bad Crypto

1974 - DES (Digital Encryption Standard) is published by NSA through NIST (invented by people at IBM)
- 56 bits
- People have not been able to break it, but it can easily be brute forced with today's consumer computation abilities
- Superseded by AES (Advanced Encryption Standard)
	- 128/256/512 bits

Don't invent, reuse

MD1-5 (Message Digest) - all insecure
SHA class of algorithms
* SHA-0 (1993)
	* Never established to be secure
- SHA-1
	- Developed by NSA
	- No longer approved for most cryptographic uses after 2010
- SHA-2
	- Both designed by the NSA
	- SHA-256
	- SHA-512
- SHA-3
	- Chosen in 2012 after a competition
	- Non-NSA

Cryptography is a small part of security, not the cornerstone
- Key management
- Side channel attacks
- Software corruption
- Bugs

Crypto is unbreakable theoretically, but is vulnerable to side channel attacks

A hashing algorithm is broken when one can reasonably find two inputs that correspond to the same output

An encryption algorithm is broken when the output can be reversed into the input without the key

The best way to attack established crypto algorithms is with side channel attacks

# Number Theory - The Study of Properties of Numbers

In cryptography, we specifically deal with non-negative, finite integers

A lot of things that are possible to solve for real numbers are very difficult to solve for non-negative, finite integers (e.g. finding logarithm)

Everything is a binary number

We do not care for the interpretation of the underlying data, we will view all data as a sequence of binary numbers, creating blocks of 128, 256, ... , or 2048 bits (common upper limit)

AES, SHA, and other algorithms are not super closely tied to number theory, there is a lot of improvisation in their implementations

RSA, ECC, DH (Diffie-Hellman) are closely tied to number theory

Prime numbers
- Have been studied since ~1000 B.C.
- There have been no practical implementations of prime numbers until cryptography
- It is difficult to find the prime factors of very large numbers whose factors are also very large numbers (100 - 200 digits)
	- Foundational property of public key encryption (RSA, ECC, DH)
	- There are infinitely many prime numbers
	- The density of prime numbers does not decrease significantly as it goes toward infinity
		- If you pick two random very large prime numbers, it is extremely unlikely that anyone else has picked those two prime numbers

You study number theory because it's good for the soul. The more useless it is, the more profound it is

# Large Numbers

How to know what numbers are large enough?
- Test: how long does it take to overflow an integer with that many bits at the speed of 1 GHz (or however fast the CPU is)
	- ex:
		- 30-bit: 1 second
		- 40-bit: 18 minutes
		- 50-bit: 13 days
		- 60-bit: 34 years
		- 70-bit: 37,436 years
		- 80-bit: 38 million years
		- 90-bit 38 billion years
		- 100-bit: 37 trillion years
		- 128-bit: 10 trillion trillion years

Implications of the mind-boggling size of a 128-bit number
- Random numbers: if we generate two random numbers in this range, we can confidently say that the two numbers are not equal without even knowing what numbers were generated
- Hash functions: 128-bit hash functions can pretty much guarantee no collision (at least for collision-resistant hash functions)
- Encryption: if data is encrypted with a random key, an attacker cannot brute-force the key to decode the ciphertext

# Kerckhoffs's Principle

- How machinery should be used to transform things for secrecy
- Very important when designing security protocols

The Principle
- System must be practically, if not mathematically indecipherable
- *It should not require secrecy* and it should not be a problem if it falls into enemy hands
- It should be possible to communicate and remember the key without notes or correspondence. Should be able to modify it at will
	- Today, we use very long keys (up to 2048-bit) and require key management
- It should be applicable to telegraph communications
- It should be portable and not require several persons to operate
- Given the circumstances in which it's used, it must be easy to use and should not be stressful or require its users to know and comply with a long list of rules. Keep it simple

Many eyes theory: when something becomes more popular and open, more people will try to break your encryption

Outside of asymmetric key algorithms, it is difficult to prove the effectiveness of cryptographic algorithms

No one human/team can design good crypto, it needs the feedback loop of the developers and the people trying to crack it

Designers do not see flaws

# Random Numbers, Hashes, and Encryption

There are a set of statistical tests that measure the randomness of 