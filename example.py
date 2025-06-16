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
