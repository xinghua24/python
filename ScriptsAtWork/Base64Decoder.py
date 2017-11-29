import base64

inputString = input("Please enter string to decode: ")
decoded = base64.b64decode(bytes(inputString, "utf-8"))
print(decoded.decode("utf-8"))
input("press close to exit")
