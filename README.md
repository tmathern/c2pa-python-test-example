# C2PA Python Installation Guide

This guide provides step-by-step instructions for installing the c2pa-python package from TestPyPI.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (recommended)

## Test installation from test.pypi

1. Create and activate a virtual environment (if not already done):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   ```

2. Install the package with `--no-deps` flag to bypass dependency checking:

   ```bash
   pip install --no-deps -i https://test.pypi.org/simple/ c2pa-python==0.10.15
   ```

## Troubleshooting

### Conflicting dependencies during install (for install from PyPiTest)

In case the installation from PyPI test shows an error similar to:

```txt
ERROR: Cannot install c2pa-python==0.10.1, c2pa-python==0.10.10, c2pa-python==0.10.11, c2pa-python==0.10.12, c2pa-python==0.10.13, c2pa-python==0.10.14, c2pa-python==0.10.15, c2pa-python==0.10.2, c2pa-python==0.10.5, c2pa-python==0.10.6, c2pa-python==0.10.7, c2pa-python==0.10.8 and c2pa-python==0.10.9 because these package versions have conflicting dependencies.

The conflict is caused by:
    c2pa-python 0.10.15 depends on wheel>=0.41.2
    c2pa-python 0.10.14 depends on wheel>=0.41.2
    c2pa-python 0.10.13 depends on wheel>=0.41.2
    c2pa-python 0.10.12 depends on wheel>=0.41.2
    c2pa-python 0.10.11 depends on wheel>=0.41.2
    c2pa-python 0.10.10 depends on wheel>=0.41.2
    c2pa-python 0.10.9 depends on wheel>=0.41.2
    c2pa-python 0.10.8 depends on wheel>=0.41.2
    c2pa-python 0.10.7 depends on wheel>=0.41.2
    c2pa-python 0.10.6 depends on wheel>=0.41.2
    c2pa-python 0.10.5 depends on wheel>=0.41.2
    c2pa-python 0.10.2 depends on wheel>=0.41.2
    c2pa-python 0.10.1 depends on wheel>=0.41.2

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict
```

Follow the following steps to fix:

1. Create and activate a virtual environment (if not already done):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   ```

2. Install the package with `--no-deps` flag to bypass dependency checking:

   ```bash
   pip install --no-deps -i https://test.pypi.org/simple/ c2pa-python==0.10.15
   ```

3. Install required dependencies:

   ```bash
   pip install "wheel>=0.41.2" cryptography requests setuptools toml pytest
   ```

4. Verify the installation:

   ```bash
   python3 -c "import c2pa; print('C2PA package successfully imported')"
   ```

(Stop here if those steps installed the dependency properly)

5. If dependency conflicts persist, try installing dependencies one by one:

   ```bash
   pip install wheel>=0.41.2
   pip install cryptography
   pip install requests
   pip install setuptools
   pip install toml
   pip install pytest
   ```

6. Verify the installation:

   ```bash
   python3 -c "import c2pa; print('C2PA package successfully imported')"
   ```
