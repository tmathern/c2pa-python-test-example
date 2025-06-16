"""
C2PA (Content Authenticity Initiative) Python Example

This module demonstrates how to read and extract C2PA data from images using the c2pa-python package.
The example reads the C2PA data from the `C.jpg` file included in the repo.

The Reader API used in the example:

c2pa.Reader(image_path: str) -> Reader
    A class for reading C2PA from images (can be sued with Context Manager).
    Note that reading from streams is also supported.

    Parameters:
        image_path (str): Path to the image file to read from

    Methods used:
        json() -> dict
            Returns the manifest store data as a JSON-compatible dictionary containing
            all C2PA associated with the image.

    Raises:
        c2pa.C2paError: If there is an error reading the C2PA data

Usage:
    Run this script directly with Python 3:
    $ python3 example.py

    Make sure the c2pa-python package is installed and the target image file exists.
"""

import c2pa

def read_c2pa_data(image_path):
    try:
        # Create a reader instance for the image with the file path
        with c2pa.Reader(image_path) as reader:
            # Read the manifest store data as JSON
            manifest_data = reader.json()

            # Pretty print the JSON data
            print("C2PA Manifest Data:")
            print(manifest_data)

    except c2pa.C2paError as e:
        print(f"Error reading C2PA data: {e}")

def read_c2pa_data_from_stream(image_path):
    try:
        # Open the file in binary read mode
        with open(image_path, 'rb') as file_stream:
            # Create a reader instance using the file stream
            # First parameter is the file type (jpg, png, etc.) as extension, or mimetype
            with c2pa.Reader("jpg", stream=file_stream) as reader:
                # Read the manifest store data as JSON
                manifest_data = reader.json()

                # Pretty print the JSON data
                print("C2PA Manifest Data (from stream):")
                print(manifest_data)

    except c2pa.C2paError as e:
        print(f"Error reading C2PA data from stream: {e}")
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run by running python3 example.py from the command line
# (Make sure dependencies are installed)
if __name__ == "__main__":
    # Read C2PA data from included demo file C.jpg
    # read_c2pa_data("C.jpg")

    # Also demonstrate reading from a stream
    read_c2pa_data_from_stream("C.jpg")
