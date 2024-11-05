The error message you received indicates that the pytest command could not find the `operations.py` file. This typically occurs because of a path issue – pytest is looking for the file in a different directory than where it is located. The test code itself is correct given the initial requirements, but to ensure it works, you might need to adjust how you're running pytest or where you've placed the test file relative to `operations.py`.

Here are some steps to troubleshoot and ensure your tests run correctly:

1. **Correct Directory Structure**: Make sure that your test file is in the correct location relative to `operations.py`. Given your file structure, your `test_operations.py` should ideally be in a `tests/` directory at the same level as your `utils/` directory, like so:
   
   ```
   project_root/
   ├── tests/
   │   └── test_operations.py
   └── utils/
       └── operations.py
   ```

2. **Running pytest**: When running pytest, make sure you're in the `project_root/` directory, and then run pytest like this:

   ```
   pytest tests/
   ```

   This command tells pytest to look for tests in the `tests/` directory. pytest will automatically discover any files that match its naming conventions (files prefixed with `test_`).

3. **Python Path Issue**: If the issue persists, it might be related to Python not being able to find your module. You can address this by setting the `PYTHONPATH` environment variable to your `project_root/`. On Unix-like systems, you can do this by running:

   ```
   export PYTHONPATH="${PYTHONPATH}:/path/to/your/project_root"
   ```

   Replace `/path/to/your/project_root` with the actual path to where your `project_root/` directory is located. On Windows, you would set the environment variable like this:

   ```
   set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project_root
   ```

4. **pytest Configuration**: Alternatively, you can add a `pytest.ini`, `tox.ini`, or `pyproject.toml` file in your `project_root/` directory with the following content (for `pytest.ini`):

   ```ini
   [pytest]
   testpaths = tests
   ```

   This configuration tells pytest to look for tests in the `tests/` directory by default.

If after trying these steps, you find that the issue is not related to the file location or Python path but rather with the test cases themselves (which doesn't seem to be the case based on your provided test code), you might then look into more specific logic or code-related errors in your tests or the `operations.py` module. However, based on the error message you've shared, the problem seems to be with pytest not being able to locate the `operations.py` file, not with the test cases themselves.