Passwords must be sent in plaintext to authenticate. Sending fingerprint data over a network is basically the same as sending a plaintext password, except you can't change your fingerprints!

Always [[Hash Functions|hash]] passwords before storing them

## Salting

Salt passwords by adding random data to the end of the password before hashing it. Store salt with the password. Salting passwords makes it more difficult for attackers to recover passwords from user data in the event of a data leak. Attackers can't use [[Dictionary Attack|precomputed dictionaries]]
or [[Rainbow Tables|rainbow tables]] to recover the passwords from the password hashes.

Windows does not salt passwords by default (with its NTLM hashing algorithm)

Unix has salted passwords since the 70s

## Unix Password Storage (how it used to be)

Passwords have been salted and hashed since the 70s

Passwords are 8 characters max. With 7 bits per char, that's 56 bits

### Hashing

Input plaintext "0" into a DES encryption function with the password and salt as the key. Take the output and feed it into another DES encryption function with the password and the salt as the key. Do this 25x to slow down the hashing so that password attempts are more computationally expensive, slowing down attackers by reducing the speed at which they can guess passwords

Salt was used to perturb S-boxes. Could not be appended to password, as DES supports 56 bit keys

Improvements to password authentication in nix systems today:
- Larger passwords
- 256 bit salts
- SHA hashes
- 1000s of rounds of hashing to slow down attackers