import c2pa

def read_c2pa_metadata(image_path):
    try:
        # Create a reader instance for the image with the file path
        reader = c2pa.Reader(image_path)

        # Read the manifest data as JSON
        manifest_data = reader.json()

        # Pretty print the JSON data
        print("C2PA Manifest Data:")
        print(manifest_data)

    except c2pa.C2paError as e:
        print(f"Error reading C2PA metadata: {e}")
    finally:
        # Make sure to close the reader
        if 'reader' in locals():
            reader.close()

if __name__ == "__main__":
    # Read metadata from C.jpg
    read_c2pa_metadata("C.jpg")
