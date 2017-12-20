import os.path

# name of module
print(__file__) 

# directory where program resides
print(os.path.join(os.path.dirname(__file__), '..'))

# cannonicalised directory where theprogram resides
print(os.path.dirname(os.path.realpath(__file__)))

# absolute path of the directory where the program resides
print(os.path.abspath(os.path.dirname(__file__)))

