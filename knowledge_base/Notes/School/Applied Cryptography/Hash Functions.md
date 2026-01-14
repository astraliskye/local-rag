Speeds up indexing by compressing larger data to a small number of bits. Does not preserve data. Deterministic (same output for same input)

Collision: when two inputs map to the same output

Techniques for simple hashing: truncation, modulus

Document: any data given as input to a hash function

## Cryptographic hashes
Useful for signatures, integrity checks, storing passwords, security checks, etc.

Properties
* No collisions
	* In any hash function, there are theoretically infinite amount of collisions
	* Hash size can be large enough that the likelihood of finding a collision is extremely unlikely (a probability so small that we treat it as zero)
* Cannot reverse the hash function to find the original data
* It should be quick to compute
* Small changes in input should result in drastic (~50%) changes in output

Two types of weaknesses:
- Attacker can find two different data that hash to the same value
- Attacker can take one datum and construct or reverse-engineer another datum that hashes to the same value

## Constructing Cryptographic Hashing Functions

Merkle Damgard Construction/Compression
* Take data and split into blocks n-bits wide, where n is the size of the resulting hash. Pad the last block with a fixed pattern
* For each block run a function on each block which takes the outputs of previous rounds as another input (an initialization vector for the first round)
* The final n-bit value is run through a finalization (permutation-ish) step, which then outputs the hash

## Common Hash Functions

SHA3 - complex, industry-capable hash function
- Since 2012
- Created in a hash function competition organized by NIST
- Joan Daemen part of the team that developed it
- Hash 224, 256, 384, and 512 bit versions
- Considered secure

MD5 (1992) Message Digest 5 was created by Ronald Rivest
- Weaknesses found in 2010
- Should no longer be used
- Attackers could construct collisions by reverse-engineering the MD5 hash function
- 128-bit hash length
- Operates on 512-bit blocks

SHA1
- Digest size: 160 bit hash

SHA2
- Digest size: 224, 256, 384, or 512 bits