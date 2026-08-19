import os
import urllib.request

def main():
    dest_dir = "weights"
    os.makedirs(dest_dir, exist_ok=True)
    
    filename = "sam_vit_h_4b8939.pth"
    filepath = os.path.join(dest_dir, filename)
    url = "https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth"
    
    if os.path.exists(filepath):
        print(f"Weights are already in {filepath}!")
    else:
        print("Downloading weights of SAM (ViT-H)...")
        try:
            urllib.request.urlretrieve(url, filepath)
            print("Download completed!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()