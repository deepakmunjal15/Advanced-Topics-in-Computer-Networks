def transmitter(msg,gen,gencode):
    msgg = msg+gencode
    msg = list(msg)
    msgg = list(msgg)
    gen = list(gen)
    for p in range(len(msgg)-len(gen)):
         if msgg[p] == '1':
             for q in range (len(gen)):
                 msgg[p+q] = str((int(msgg[p+q])+int(gen[q]))%2)
                
    remainder = (msgg[-(len(gen)-1):])
    print("remainder is","".join(remainder))
    transmitted_msg = msg+remainder
    print("message to be transmited, without error:","".join(transmitted_msg))
    
def error_checker(transmitted_msgg,gen):
    transmitted_msgg = list(transmitted_msgg)
    gen = list(gen)
    for i in range(len(transmitted_msgg)-len(gen)):
        if transmitted_msgg[i] == '1':
             for j in range (len(gen)):
                 transmitted_msgg[i+j] = str((int(transmitted_msgg[i+j])+int(gen[j]))%2)
                
    error = (transmitted_msgg[-(len(gen)-1):])
    error = list(error)
    for m in range(len(error)):
         if error[m] == '1':
            print("since there is remainder, error has been detected","".join(error))
            break
         elif m == (len(error)-1):
            print("there is No error")

transmitter("100000011000","10011","0000")
error_checker("1000000110000000","10011")
