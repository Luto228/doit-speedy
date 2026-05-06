# doit-speedy

A minimalist CLI tool for rapid GitHub repository creation and project scaffolding.

## Overview

`doit-speedy` is a simple Python script that automates the creation of GitHub repositories using the GitHub CLI (`gh`). It allows you to quickly set up new repos with customizable options for visibility, README, license, and .gitignore templates.

## Features

- Create public or private GitHub repositories
- Automatically add a README file
- Choose from various license templates
- Include .gitignore templates for different languages/frameworks
- Minimalist and fast execution

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the GitHub CLI (`gh`) if not already installed. Follow the instructions at [https://cli.github.com/](https://cli.github.com/).
3. Authenticate with GitHub using `gh auth login`.
4. Make the script executable:
   ```
   chmod +x main.py
   ```
5. Find the absolute path to the script:
   ```
   realpath main.py
   ```
   Copy the output path (e.g., `/home/user/doit-speedy/main.py`).
6. Create an alias for easy access. In your terminal (e.g., VS Code's integrated terminal), run:
   ```
   alias doit='/path/to/main.py'
   ```
   Replace `/path/to/main.py` with the path you obtained in step 5.

   To make the alias permanent, add the above line to your shell's configuration file (e.g., `~/.bashrc` or `~/.zshrc`).

## Usage

Once the alias is set, use the tool as follows:

```
doit <repo_name> [public on/off] [readme on/off] [license] [gitignore]
```

### Arguments

- `<repo_name>`: The name of the new repository (required).
- `[public on/off]`: Set to `on` for public repo, `off` for private (default: private).
- `[readme on/off]`: Set to `on` to add a README file (default: off).
- `[license]`: License template (e.g., `mit`, `apache-2.0`). Set to `off` to skip (default: off).
- `[gitignore]`: .gitignore template (e.g., `Python`, `Node`). Set to `off` to skip (default: off).

### Examples

- Create a private repo named "my-project":
  ```
  doit my-project
  ```

- Create a public repo with README and MIT license:
  ```
  doit my-project on on mit
  ```

- Create a private repo with Python .gitignore:
  ```
  doit my-project off off off Python
  ```

## Future Enhancements

- Support for adding custom README descriptions during repo creation.

## Requirements

- Python 3
- GitHub CLI (`gh`)
- Authenticated GitHub account

## License

This project is open-source. Feel free to contribute or modify as needed.
