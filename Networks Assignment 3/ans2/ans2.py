#all packets are stored in file packets_file.txt
packets = []
fr = open("packets_file.txt",'r')
for line in fr:
    for char in line.split(" "):
        packets.append(char)
        
#routing table is stored in file routing_file.txt        
routing = []
h = open("routing_file.txt",'r')
for line in h:
    for char in line.split(" "):
        routing.append(char)
        
#various chunks of addresses are compared within routing table        
for n in range(0,len(packets)):
   ip_chunk = packets[n].rstrip("\n")
   if ip_chunk in routing:
       match = routing.index(ip_chunk)
       if routing[match+1] == "NA":
        print("It is on a Directly Connected Network: So a frame with destination address of",ip_chunk,"will be sent on the network",ip_chunk,"out on interface",routing[match+3])
       else:
        print("Packet with destination address",ip_chunk," will be forwarded to ",routing[match+1],"out on interface",routing[match+3])
   else:
       ip_part = packets[n].split(".")
       ip_part[3] = '0'
       ip_chunk_1 = ".".join(ip_part)
       if ip_chunk_1 in routing:
           match = routing.index(ip_chunk_1)
           if routing[match+1] == "NA":
            print("It is on a Directly Connected Network: So a frame with destination address of",ip_chunk,"will be sent on the network",ip_chunk_1,"out on interface",routing[match+3])
           else:
            print("Packet with destination address",ip_chunk," will be forwarded to ",routing[match+1],"out on interface",routing[match+3])

       else:
           ip_part[2] = "0"
           ip_chunk_2 = ".".join(ip_part)
           if ip_chunk_2 in routing:
               match = routing.index(ip_chunk_2)
               if routing[match+1] == "NA":
                print("It is on a Directly Connected Network: So a frame with destination address of",ip_chunk,"will be sent on the network",ip_chunk_2,"out on interface",routing[match+3])
               else:
                print("Packet with destination address",ip_chunk," will be forwarded to ",routing[match+1],"out on interface",routing[match+3])
           else:
               ip_part[1] = "0"
               ip_chunk_3 = ".".join(ip_part)
               if ip_chunk_3 in routing:
                   match = routing.index(ip_chunk_3)
                   if routing[match+1] == "NA":
                    print("It is on a Directly Connected Network: So a frame with destination address of",ip_chunk,"will be sent on the network",ip_chunk_3,"out on interface",routing[match+3])
                   else:
                    print("Packet with destination address",ip_chunk," will be forwarded to ",routing[match+1],"out on interface",routing[match+3])
               else:
                   ip_part[0] = "0"
                   ip_chunk_4 = ".".join(ip_part)
                   if ip_chunk_4 in routing:
                       match = routing.index(ip_chunk_4)
                       if routing[match+1] == "NA":
                        print("It is on a Directly Connected Network: So a frame with destination address of",ip_chunk," will be sent on the network",ip_chunk_4,"out on interface",routing[match+4])
                       else:
                        print("Packet with destination address",ip_chunk," will be forwarded to ",routing[match+1],"out on interface",routing[match+4])
#closing both files
h.close()
fr.close()