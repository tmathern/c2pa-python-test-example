"""
This script performs introspection on the c2pa Python module to analyze
and display its structure and capabilities. This can help verifying
proper installation of the package.

The code does the following:

1. First Section - Basic Module Analysis:
  - Uses Python's inspect module to examine the c2pa module
  - Lists all public (non-private) members of the c2pa module
  - Prints each member's name and its type (class, function, etc.)

2. Second Section - Detailed Component Analysis:
  - Performs a deeper analysis of each public member
  - For classes:
     * Lists all public methods available in each class
     * Shows the class hierarchy and available functionality
  - For functions:
     * Displays the function signature
     * Shows parameter information and return types

This script is particularly useful for:
- Understanding the available functionality in the c2pa module
- Discovering the API surface and available methods
- Debugging and development purposes
- Documentation generation

Note: The script specifically filters out private members (those starting with '_')
to focus on the public API that users should interact with.
"""

# c2pa module import
import c2pa

# for introspection of c2pa module
import inspect

# Print all available functions and classes in the c2pa module
print("Available functions and classes in c2pa module:")
for name, obj in inspect.getmembers(c2pa):
    if not name.startswith('_'):  # Skip private members
        print(f"{name}: {type(obj).__name__}")

# API analysis
# Try to get more detailed information about the main classes/functions
print("\nDetailed information about main components:")
for name, obj in inspect.getmembers(c2pa):
    if not name.startswith('_'):
        if inspect.isclass(obj):
            print(f"\nClass: {name}")
            print("Methods:")
            for method_name, method in inspect.getmembers(obj):
                if not method_name.startswith('_'):
                    print(f"  - {method_name}")
        elif inspect.isfunction(obj):
            print(f"\nFunction: {name}")
            print(f"Signature: {inspect.signature(obj)}")
