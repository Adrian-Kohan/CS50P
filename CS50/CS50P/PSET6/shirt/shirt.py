import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith((".jpg",".jpeg", "png")) or not sys.argv[2].endswith((".jpg",".jpeg", "png")):
    sys.exit("Invalid input")

elif sys.argv[1][-2] != sys.argv[2][-2]:
    sys.exit("Input and output have different extensions")

else:
    try:
        with Image.open(sys.argv[1]) as im1:
            size = im1.size()
            print(size)

        with Image.open(sys.argv[2]) as im2:
            ImageOps.fit(im2, size, method=Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
            Image.paste(im1, box=None, mask=None)
            im2.save("after.jpg")





    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")