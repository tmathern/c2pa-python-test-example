import c2pa
import inspect

# Print all available functions and classes in the c2pa module
print("Available functions and classes in c2pa module:")
for name, obj in inspect.getmembers(c2pa):
    if not name.startswith('_'):  # Skip private members
        print(f"{name}: {type(obj).__name__}")

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
