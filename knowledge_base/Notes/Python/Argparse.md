# argparse
```python
import argparse
parser = argparse.ArgumentParser()

# Positional argument
parser.add_argument("echo", help="Explanation of argument")
# Boolean named argument
parger.add_argument("--debug", action="store_true")
# Named argument with automatic type validation
parser.add_argument("--verbosity", type=int, choices=[0, 1, 2])
# Nmap style verbosity levels
parser.add_argument("-v", "--verbosity", action="count", default=0)
# Named argument with short option
parser.add_argument("-q", "--query")

args = parser.parse_args()
print(args.echo)
```
