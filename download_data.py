import os
import requests
import zipfile
import io

def main():
    dest_dir = "data"
    os.makedirs(dest_dir, exist_ok=True)

    url_zip = "https://github.com/matildeelippii/3D-Artwork-Viewer-from-2D-Images/releases/download/v1.0-data/raw_images.zip"

    try:
        print("Downloading the dataset...")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url_zip, headers=headers)
        response.raise_for_status()
        
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(dest_dir)
            
        print("Success! The images are in data/raw_images!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()