#FDB is stored in FDB.txt and a randomly generated frame, saved in frame.txt, is considered for the FDB.
#For each time i.e. each random frame, our file frame.txt will be overwritten and that new random frame is only considered for the FDB in FDB.txt.  

import random
import string

fdb = []
h = open('FDB.txt','r')
for line in h:
    for char in line.split(" "):
        fdb.append(char)
        
length = len(fdb)
h.close()

for j in range(0, length, 2):
    fdb[j] = int(fdb[j])
    
port_num_limit=fdb[0]

for i in range(length-1):
    fdb[i] = fdb[i+1]
    
fdb.pop()
length=length-1

#Original FDB as taken from FDB.txt file
print("\nOriginal FDB is:")
print(fdb)

#Random values are taken for source host, destination host and arrival port.
string.letter = 'ABCDEFGH'
source_host = random.choice(string.letter)
arrival_port = random.randint(1, port_num_limit)
destination_host = random.choice(string.letter)

print("\nFrame coming is:")
print(source_host+" "+destination_host+" "+str(arrival_port))

#the randomly generted frame is saved in a file named frame.txt
data = []
fr = open('frame.txt','w')
fr.write(source_host+' ')
fr.write(destination_host+' ')
fr.write(str(arrival_port))
fr.close()

file = open('FDB.txt','a')

if source_host in fdb:
    b = fdb.index(source_host)
    if fdb[b + 1] is not arrival_port:
        fdb[b + 1] = arrival_port
        print("port number for source host", source_host, "has been updated to:", arrival_port)
else:
    fdb.append(source_host)
    fdb.append(arrival_port)
    print("FDB has been updated with source host",source_host,"having port number",arrival_port)
    
#Updated FDB
new_sourcelist= fdb
print("\nUpdated FDB is:")
print(new_sourcelist)

if destination_host in fdb:
    k = fdb.index(destination_host)
    outgoing_port = fdb[k+1]
    if source_host == destination_host:
      print("Source and destination hosts of frame can not be same.")
    if source_host != destination_host:
      if arrival_port == outgoing_port:
        print("Frame is discarded since arrival port i.e.",arrival_port,"for source host",source_host,"is same as outgoing port i.e.",outgoing_port,"for destination host",destination_host,"for this frame.")
      else:
        print("Frame sent on port",outgoing_port)
else:
    print("Frame broadcast on all out ports")
    
file.close()