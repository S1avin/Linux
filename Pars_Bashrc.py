#For Linux ofc.
#file should be in "~/"
lines = []    # Will store all bash lines in this list
with open("/home/ser/.bashrc", 'r') as f:   # Openning and reading file, could $
    for line in f: lines.append(line.rstrip())  # All string -> in list withou $
for line in lines[lines.index("#:::")+2:]:    # printing custom alias which mus$
    print (line)
