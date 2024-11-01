import os

def list_files(startpath, max_depth, file_extensions):
    with open('repo_structure.txt', 'w') as f:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            if level > max_depth:  # Limit the depth
                continue
            indent = ' ' * 4 * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                if any(file.endswith(ext) for ext in file_extensions):  # Filter by extensions
                    f.write(f'{subindent}{file}\n')

if __name__ == '__main__':
    repo_path = r'C:\Users\ashle\Documents\GitHub\commit-test-case-generator'
    max_depth = 2  # Change this value to limit depth
    file_extensions = [
        '.py',   # Python files
        '.js',   # JavaScript files
        '.java', # Java files
        '.c',    # C files
        '.cpp',  # C++ files
        '.h',    # C/C++ header files
        '.rb',   # Ruby files
        '.go',   # Go files
        '.md',   # Markdown files for documentation
        '.txt',  # Text files (optional)
        'Dockerfile', # Dockerfile for environment context
        'requirements.txt', # Python dependencies
        'Pipfile', # Python dependency management
        'package.json', # JavaScript dependencies
        # Add any other specific file names or extensions you want to include
    ]
    
    list_files(repo_path, max_depth, file_extensions)
    print('Filtered repository structure saved to repo_structure.txt')
