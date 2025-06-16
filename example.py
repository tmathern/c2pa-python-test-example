"""
C2PA (Content Authenticity Initiative) Python Example

This module demonstrates how to read and extract C2PA metadata from images using the c2pa-python package.
C2PA is a standard for content provenance and authenticity that allows embedding and reading metadata
about the origin and history of digital content.

The Reader API used in the example:

c2pa.Reader(image_path: str) -> Reader
    A class for reading C2PA metadata from images (can be sued with Context Manager).
    Note that reading from streams is also supported.

    Parameters:
        image_path (str): Path to the image file to read metadata from

    Methods used:
        json() -> dict
            Returns the manifest store data as a JSON-compatible dictionary containing
            all C2PA metadata associated with the image.

    Raises:
        c2pa.C2paError: If there is an error reading the C2PA metadata

Usage:
    Run this script directly with Python 3:
    $ python3 example.py

    Make sure the c2pa-python package is installed and the target image file exists.
"""

import c2pa

def read_c2pa_metadata(image_path):
    try:
        # Create a reader instance for the image with the file path
        with c2pa.Reader(image_path) as reader:
            # Read the manifest store data as JSON
            manifest_data = reader.json()

            # Pretty print the JSON data
            print("C2PA Manifest Data:")
            print(manifest_data)

    except c2pa.C2paError as e:
        print(f"Error reading C2PA metadata: {e}")

# Run by running python3 example.py from the command line
# (Make sure dependencies are installed)
if __name__ == "__main__":
    # Read metadata from included demo file C.jpg
    read_c2pa_metadata("C.jpg")
