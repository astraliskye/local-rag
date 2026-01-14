# uv
Python tool intended to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, etc.
## Phrases

| Phrase                                      | Description                                 |
| ------------------------------------------- | ------------------------------------------- |
| `uv init <project name>`                    | Initialize a new project                    |
| `uv run <script>.py`                        | Run script in virtual environment           |
| `uv add <library>`                          | Add library to pyproject.toml               |
| `uv remove <library>`                       | Remove library from pyproject.toml          |
| `uv add -r requirements.txt`                | Install dependencies from requirements.txt  |
| `uv lock --upgrade-package <library>`       | Upgrade a library version                   |
| `uv run -- flask run -p 3000`               | ex: run flask on port 3000                  |
| `uv build`                                  | Build project, put artifacts in dist dir    |
| `uv export --format requirements.txt`       | Create requirements.txt file from lockfile  |
| `uv sync`                                   | Ensure deps are up to date with lockfile    |
| `uv python install <version>`               | Install a particular python version         |
| `uv python upgrade`                         | Upgrade all uv-managed Python versions      |
| `uv python upgrade 3.12`                    | Upgrade Python 3.12 to the latest patch     |
| `uv init <project name> --python <version>` | Init project with particular Python version |
| `uv python list`                            | List installed Python versions              |
## Files

| File name       | Description                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| pyproject.toml  | Metadata about the project                                                                                                   |
| .python-version | Project's default Python version                                                                                             |
| .venv           | Virtual environment                                                                                                          |
| uv.lock         | Do not edit: contains information about dependencies. Automatically managed by uv. Ensure it is checked into version control |
