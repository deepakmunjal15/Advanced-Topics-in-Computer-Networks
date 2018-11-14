import random

x=0
def transmitter(msg,gen,gencode):    
    msgg = msg+gencode
    msg = list(msg)
    errorr = "10010001010101111111111000011111"
    errorr = list(errorr)
    gen = list(gen)
    msgg = list(msgg)
    for p in range(len(msgg)-len(gen)):
         if msgg[p] == '1':
             for q in range (len(gen)):
                 msgg[p+q] = str((int(msgg[p+q])+int(gen[q]))%2)

    remainder = (msgg[-(len(gen)-1):])
    print("remainder is:","".join(remainder))
    transmitted_msg = msg+remainder
    print("message to be transmitted, without error is:","".join(transmitted_msg))
    #32-bit error_generator, remove comments from below 2 lines to generate 32-bit error and comment other lines of code accordingly.
    #error_length = 32
    #transmitted_msg = msg+errorr
    #<32-bit error_generator, remove comments from below 3 lines to generate error less than 32-bit and comment other lines of code accordingly.
    for b in range(1505,1533):
        error_length = 27
        transmitted_msg[b] = str(random.randint(0,1))
    #>32-bit_error generator, remove comments from below 3 lines to generate error more than 32-bit and comment other lines of code accordingly.
    '''for b in range(1475,1533):
        error_len = 57
        transmitted_msg[b] = str(random.randint(0,1))'''
    print("message transmitted, with error of length:",error_length,"".join(transmitted_msg))
    error_checker(transmitted_msg,gen)
    
def error_checker(transmitted_msgg,gen):
    transmitted_msgg = list(transmitted_msgg)
    gen = list(gen)
    for p in range(len(transmitted_msgg)-len(gen)):
        if transmitted_msgg[p]== '1':
            for q in range (len(gen)):
                transmitted_msgg[p+q] = str((int(transmitted_msgg[p+q])+int(gen[q]))%2)
                
    error = (transmitted_msgg[-(len(gen)-1):])
    error = list(error)
    for m in range(len(error)):
         if error[m] == '1':
            global x
            x+=1
            print("since there is remainder, error has been detected","".join(error),"& it is in the frame no.",x)
            break
         elif m == (len(error)-1):
            print("there is No error")

for q in range(1000):
    rand_byte = []
    for p in range(1520):
        d = str(random.randint(0,1))
        rand_byte.append(d)

    rand_bit = "".join(rand_byte)
    new_gen = "100000100110000010001111110110001"
    new_gen_code = "0"*32
    
transmitter(rand_bit,new_gen,new_gen_code)
