suffixes = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

file_name = input("Flie name: ")
if ".gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name or ".jpeg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
