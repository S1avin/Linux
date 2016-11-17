#Create multiple numbered folders in the same directory.
import os
for i in range(int(input("First - ")),int(input("Last - "))+1):
    if not os.path.exists(str(i)):
        os.mkdir(str(i))
