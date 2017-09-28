fname=input("please enter file name: ")

with open(fname) as f:
  content = f.readlines()
  content = [print(x.strip()) for x in content]

print("")


input("please close to exit")
