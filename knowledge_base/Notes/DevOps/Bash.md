# Bash
## Lang notes
### Unset vs null
**Unset:** variable essentially doesn't exist
**Null:** variable exists but contains no value
### Single quote versus double quote
Double quoted strings allow for variable expansion, command substitution, and arithmetic substitution. Single quoted strings do not.
### Command substitution
Syntax: `$(command)`
Command is executed in a subshell environment and then returned. $(< file) == $(cat file) and is faster
### Variable/parameter expansion
Syntax: `${parameter}`
Substitutes the value of *parameter*. Curly braces are optional, but are useful to separate the variable name from the surrounding characters.
#### Fun tricks
`${parameter:-word}` - *word* is substituted if *parameter* is unset or null
`${parameter-word}` - *word* is substituted if *parameter* is null
`${parameter:offset:length}` - basically a substring function. Length is optional
`${}`
## Small scripts
### IP address with most HTTP requests in log
`cat log | sed 's/ .*//' | occurrence_counter.py`
occurrence.py:
```bash
declare -A freq    # Declare associative array

while read line
do
	if [ -v freq[$line] ]; then
		freq[$line] = $((freq[$line] + 1))
	else
		freq[$line]=1
	fi
done < "${1:-/dev/stdin}"

for ip in "${!freq[@]}"; do
	echo "${freq[$ip]} $ip"
done
```
