file = input("File name: ").lower()
if ".gif" in file:
    print("image/gif")
elif ".jpg" or ".jpeg" in file:
    print("image/jpeg")
elif ".png" in file:
    print("image/png")
elif ".pdf" in file:
    print("application/pdf")


else:
    print("application/octet-stream")
