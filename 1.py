try:
 with open("secret_codes.txt", "r") as file:
 print(file.read())
except FileNotFoundError:
 print("Oops! That file does not exist yet. Please check the filename.")