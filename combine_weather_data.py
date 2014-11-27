# combine 1376 csv files into one file

fout=open("merged.csv","a")
# first file:
for line in open("day1.csv"):
  fout.write(line)
# now the rest:    
for num in range(2,3):
  f = open("day"+str(num)+".csv")
  f.next() # skip the header
  for line in f:
    fout.write(line)
  f.close() # not really needed
fout.close()