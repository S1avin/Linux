#For Linux ofc.
#file should be in "~/"
lines = []    # Will store all bash lines in this list
with open(".bashrc", 'r') as f:   # Openning and reading file, could be any other custom file with your alias
    for line in f: lines.append(line.rstrip())  # All string -> in list withou "\n"
for line in lines[lines.index("#:::")+2:]:    # printing custom alias which must go AFTER string "#:::"
    print (line)
