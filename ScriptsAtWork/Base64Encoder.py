import base64  
inputString = input("Please enter string to encode: ")
encoded = base64.b64encode(bytes(inputString, "utf-8"))
print(encoded.decode("utf-8"))
input("press close to exit")
