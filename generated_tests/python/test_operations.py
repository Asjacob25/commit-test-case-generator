The error message you've received, "ERROR: file or directory not found: operations.py," suggests a problem with the way the test environment is set up or how pytest is invoked, rather than an issue with the test cases themselves. This error typically occurs when pytest cannot locate the file it's supposed to test, which might be due to one of the following reasons:

1. **Incorrect Working Directory**: Ensure you're running pytest from the root directory of your project, or use the `-k` option to specify the path to your tests.

2. **Incorrect File Path in Tests**: If your tests reference `operations.py` directly (as seen in the error), make sure the import statement in `test_operations.py` correctly reflects the directory structure. Since `operations.py` is in the `utils` directory, your import statement should be correct as `from utils.operations import add, subtract, multiply, power, divide`. Double-check the directory name and spelling.

3. **Pytest Configuration**: Check if there's a `pytest.ini` or any configuration file that might be incorrectly specifying test paths or patterns.

To address the issue based on the provided context, please ensure that:
- You're running pytest from the correct directory. If your project's root directory is the parent directory of `utils`, navigate there before running pytest.
- Your IDE or command line is pointed to the correct directory.
- If you're using a CI/CD pipeline or a virtual environment, ensure the paths are correctly set up to include your project structure.

Based on the provided error and ensuring there's no misunderstanding about the test file itself (since the provided test cases are correctly designed for the `operations.py` functions), here are additional steps or checks you might perform:

- **Running Pytest with Full Path**: Try specifying the full path to the test file when running pytest, e.g., `pytest path/to/test_operations.py`.
- **Check for Typographical Errors**: Confirm that the file name and directory are spelled correctly in both the filesystem and your test file.

Since the error is not about the test cases failing but rather about pytest not being able to locate the `operations.py` file, the provided test cases should be correct given the correct setup. Once the path or configuration issue is resolved, pytest should be able to discover and run the tests as intended.