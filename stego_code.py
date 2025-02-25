import cv2
import os
import string


image_name = input("Enter the image filename (e.g., 'mypic.png'): ")


# Load the image
image_path = os.path.join(os.getcwd(), image_name)
img = cv2.imread(image_path)


if img is None:
    print("Error: Image not loaded! Check the file path or format.")
    exit()  # Exit the script if the image is not found


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)


m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]  # Loop through height
    m = (m + 1) % img.shape[1]  # Loop through width
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[int(img[n, m, z])]

        n = (n + 1) % img.shape[0]  # Loop through height
        m = (m + 1) % img.shape[1]  # Loop through width
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")

