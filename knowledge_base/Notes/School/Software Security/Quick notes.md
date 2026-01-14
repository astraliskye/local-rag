`hashlib.md5(payload).digest()` -> outputs a 
`b''.join(random.choice(string.ascii_lowercase)).encode('ascii') for i in range(48)])` -> creates a random byte array of 48 lowercase letters
`hashlib.md5(payload).digest()[0] == 0` -> test if first byte of hash is null byte