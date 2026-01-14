Shell - facilitator b/w user and os
grep - search for things in files
chsh -s /usr/bin/zsh
- Change default shell
history - see past commands
## Bash
read name
- Read input into a variable called name. Reference it later with $name
### Conditionals
if [ "$name" = "Stewart" ] && ["$preference" = "IDEK"]; then
	echo ...
else
	echo ...
fi
### Loops
for i in {1..10};
do
	....
done
## Just Unix things
#! - shebang. Tells Unix that the file is an executable