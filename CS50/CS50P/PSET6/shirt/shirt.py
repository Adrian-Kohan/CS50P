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
        im1 = Image.open("shirt.png")
        size = im1.size

        im2 = Image.open(sys.argv[1])
        fited_img = ImageOps.fit(im2, size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        fited_img.paste(im1, (0, 0), im1)
        final = fited_img.convert("RGB")
        final.save(sys.argv[2])


    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")