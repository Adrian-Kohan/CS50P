import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


else:
    try:
        size = (100, 150)
        with Image.open(sys.argv[1]) as im:
            ImageOps.fit(im, size).save("imageops_fit.png")
            Image.paste(im, box=None, mask=None)
            im.save(file + ".thumbnail", "JPEG")





    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")