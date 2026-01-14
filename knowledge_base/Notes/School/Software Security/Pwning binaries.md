# Tocttou - Time of check to time of use
Open two terminals. Run main program on one terminal. On the other terminal swap out whatever resource the main program is trying to access.

# Double vs Single Quotes
SIngle quotes in bash will prevent interpolation of variables, backticks, and certain escapes. Cannot escape single quote characters within single quotes. Double quotes will do all the normal command expansion.

# Backtick
Used for command substitution. An older version of command substitution. The preferred, newer method is with `$()`. 

# Find
Allows you to run custom commands easilydi

# Using GDB
## Setting breakpoints (stopping the program)
- `b <function name>` - set breakpoint at function name
- 

## Getting information
- `p <var>` - print variable
- `p *(argv + 1)` - print second command line argument
- `info variables` - list all globals and static variable names
- `info locals` - print local variables and addresses
- `info frame` - print information about current stack frame, including instruction pointer
- `info args` - list arguments of the current stack frame
- `layout asm` - show current assembly instruction and surrounding instructions
- `display/i $pc` - print current instruction after every advance

## Setting information
- `set {int}<address> = <value>` - put `<value>` at `<address>`
- `set <var name> = <value>`