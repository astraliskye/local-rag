Similar to the [[Dictionary Attack|dictionary attack]] but saves on storage space by using more on-the-spot computation.

## Setting up the rainbow table

1. Generate a number of candidate passwords (e.g. a million)
2. Come up with a "reversal function"/"reduction function" that will take a hash and come up with another candidate password
3. For each candidate password, [[Hash Functions|hash]] it, run the reversal function to get a new candidate password, then hash that candidate password. Do this a certain number of times (e.g. a million), depending on how long you want to spend computing during the password cracking process
4. Record the first candidate password as well as the last hash

Stores 2 million records (if hashing a million passwords a million times), but represents a trillion passwords

Rainbow tables can take a month or more to create

The ideal reversal function will not generate a previously generated candidate password

Coverage: the amount of passwords the table represents (i.e. the number of initial candidate passwords x the number of hashing rounds - the number of collisions in the reversal function)

Can leverage parallel computing to speed up this process

## Using the rainbow table

For each user password hash:
1. Use the reversal function on the hash and hash the generated candidate password
2. Search the rainbow table hashes for a match
3. If there is a match, start at the beginning of the row where the match occurred and run the reversal/hash chain until the password is found
4. If there is not a match, go back to step 1, stop after you have hashed it ~1 million times or however long your hash chains are

## Combatting rainbow tables

Salt yer dang passwords