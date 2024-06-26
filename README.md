# Control Flow Python Project

This project demonstrates various control flow structures in Python, including if-else statements, for loops, while loops, and try-except blocks.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setting Up the Project](#setting-up-the-project)
- [Running the Script](#running-the-script)
- [Running the Tests](#running-the-tests)
- [Explanation of the Code](#explanation-of-the-code)
- [Using `.gitignore`](#using-gitignore)
- [Additional Resources](#additional-resources)

## Prerequisites

- [Python 3](https://www.python.org/downloads/) installed on your system
- [Git](https://git-scm.com/) installed on your system

## Project Structure

The project has the following structure:

```
control_flow/
│
├── .gitignore
├── control_flow.py
├── test_control_flow.py
└── README.md
```

- `control_flow.py`: The main Python script that demonstrates various control flow structures.
- `test_control_flow.py`: Unit test for the `demonstrate_control_flow` function.
- `.gitignore`: A file specifying which files and directories to ignore in the Git repository.
- `README.md`: A comprehensive tutorial on how to set up and run the control flow project.

## Setting Up the Project

1. **Clone the Repository**

   First, clone the repository to your local machine. Open your terminal and run the following command:

   ```sh
   git clone https://github.com/coder50yo/python-control-flow.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```sh
   cd control_flow
   ```

## Running the Script

To run the script and see the demonstration of various control flow structures, execute the following command in your terminal:

```sh
python3 control_flow.py
```

## Running the Tests

To run the unit test for the `demonstrate_control_flow` function, execute the following command in your terminal:

```sh
python3 -m unittest test_control_flow.py
```

You should see output indicating that the test passed.

## Explanation of the Code

### `control_flow.py`

The `control_flow.py` script defines the `demonstrate_control_flow` function, which demonstrates various control flow structures available in Python, including if-else statements, for loops, while loops, and try-except blocks. The function prints the result of each control flow structure.

### `test_control_flow.py`

The `test_control_flow.py` script contains a simple unit test for the `demonstrate_control_flow` function. The test ensures that the function runs without errors.

## Using `.gitignore`

The `.gitignore` file specifies files and directories that Git should ignore, such as temporary files, build artifacts, and environment-specific directories.

Here are some common entries in the `.gitignore` file:

- `__pycache__/`: Python's bytecode cache directory
- `*.pyc`: Compiled Python files
- `venv/`, `env/`: Virtual environment directories

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Control Flow Tools in Python Documentation](https://docs.python.org/3/tutorial/controlflow.html)
- [Git Documentation](https://git-scm.com/doc)