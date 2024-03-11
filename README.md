# AirBnB Clone - The Console

## Introduction

Welcome to the first step of the AirBnB Clone project, "The Console," a comprehensive effort to replicate essential functionalities of the renowned accommodation rental platform, Airbnb. This phase focuses on a command-line interface (CLI) enabling the management of various AirBnB-like objects, including users, accommodations, and more, serving as the groundwork for a full web application.

### Overview

The AirBnB Clone Console, developed in Python, offers a versatile CLI for object management within the AirBnB clone ecosystem. It allows users to create, retrieve, update, and delete data, mirroring the operational dynamics of a web-based platform in a simplified environment.

## Tools

- **Programming Language**: Python
- **Version Control**: Git, GitHub
- **Coding Standards**: PEP8 for Python style guide compliance

## Installation

Get started with the AirBnB Clone Console by following these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/nuuxcode/AirBnB-Clone.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AirBnB-Clone
    ```
3. Execute the console script to enter the interactive mode:
    ```bash
    ./console.py
    ```

### Execution

- **Interactive Mode**:
    ```bash
    $ ./console.py
    (hbnb) help
    ```
    Use `help` for a list of available commands.

- **Non-Interactive Mode**:
    ```bash
    $ echo "help" | ./console.py
    ```

## Usage

The console supports various commands for managing AirBnB objects:

- **Create**: `create <ClassName>` - Generates a new instance with a unique ID.
- **Show**: `show <ClassName> <id>` - Displays the details of a specified instance.
- **Destroy**: `destroy <ClassName> <id>` - Removes an instance from storage.
- **All**: `all <ClassName>` - Lists all instances of a given class or all classes if none specified.
- **Count**: `count <ClassName>` - Counts instances of a given class.

## Testing

Testing is conducted using Python's `unittest` module:
- Run tests in interactive mode: `echo "python3 -m unittest discover tests" | bash`
- Run tests in non-interactive mode: `python3 -m unittest discover tests`

## Authors

- **Omar Merkous** - [omar.merkous@gmail.com](mailto:omar.merkous@gmail.com)


## About

The AirBnB clone project aims to recreate aspects of Airbnb's functionality through a step-by-step development process, starting with "The Console."

