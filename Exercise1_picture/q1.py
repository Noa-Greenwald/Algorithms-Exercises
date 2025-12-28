import sys
from PIL import Image

def main():
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
    else:
        file_name = "img94089.jpg"
        print("No image filename provided, using default:", file_name)

    try:
        img = Image.open(file_name)
    except Exception as e:
        print("Error opening image:", e)
        return

    img.show()

    img = img.convert("RGB")

    r, g, b = img.split()

    r.show()
    g.show()
    b.show()

if __name__ == "__main__":
    main()
