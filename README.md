# doit-speedy

A minimalist CLI tool for GitHub repository management.

## Overview

`doit-speedy` is a simple Python script that provides commands for creating and finding GitHub repositories using the GitHub CLI (`gh`).

## Features

- Create public or private GitHub repositories with customizable options (README, license, .gitignore)
- Find GitHub repositories by name and optionally by author, opening the search results in your browser

## Installation

To get the program working, you need to do three things:

1. Make the script executable:
   ```
   chmod +x main.py
   ```
2. In the terminal with main.py, run:
   ```
   readlink -f main.py
   ```
   This will output the path (e.g., `/home/user/doit-speedy/main.py`).
3. Create an alias for easy access:
   ```
   alias github='YOUR_PATH'
   ```
   Replace `YOUR_PATH` with the path obtained in step 2.

   To make the alias permanent, add the above line to your shell's configuration file (e.g., `~/.bashrc` or `~/.zshrc`).

   Then, run:
   ```
   source ~/.bashrc
   ```
   to apply the changes immediately.

Additional requirements:
- Ensure you have Python 3 installed on your system.
- Install the GitHub CLI (`gh`) if not already installed. Follow the instructions at [https://cli.github.com/](https://cli.github.com/).
- Authenticate with GitHub using `gh auth login`.

## Usage

Once the alias is set, use the tool as follows:

### Creating a repository:
```
github doit <repo_name> [public on/off] [readme on/off] [license/off] [gitignore/off]
```

### Finding repositories:
```
github find <repo_name>
github find <repo_name> from <author>
```

### Arguments for doit command

- `<repo_name>`: The name of the new repository (required).
- `[public on/off]`: Set to `on` for public repo, `off` for private (default: private).
- `[readme on/off]`: Set to `on` to add a README file (default: off).
- `[license/off]`: License template (e.g., `mit`, `apache-2.0`). Set to `off` to skip (default: off).
- `[gitignore/off]`: .gitignore template (e.g., `Python`, `Node`). Set to `off` to skip (default: off).

### Arguments for find command

- `<repo_name>`: The name of the repository to search for (required).
- `from <author>`: Optional author (GitHub username) to filter the search.

### Examples

- Create a private repo named "my-project":
  ```
  github doit my-project
  ```

- Create a public repo with README and MIT license:
  ```
  github doit my-project on on mit
  ```

- Create a private repo with Python .gitignore:
  ```
  github doit my-project off off off Python
  ```

- Find a repository named "my-repo":
  ```
  github find my-repo
  ```

- Find a repository named "my-repo" by author "john":
  ```
  github find my-repo from john
  ```

## Future Enhancements

- Soon a new clone command by project nickname will be added.

## Requirements

- Python 3
- GitHub CLI (`gh`)
- Authenticated GitHub account