import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


else:
    try:
        with Image.open(sys.argv[1]) as im1:
            size = im1.size()
            print(size)

        with Image.open(sys.argv[2]) as im2:
            ImageOps.fit(im2, size).save("image_fit.jpg")
            Image.paste(im1, box=None, mask=None)
            im2.save("Output", "JPG")





    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")