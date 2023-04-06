#SEMAFORY PREKOD
## message creation
#message is list/string that contains UPPER A-Z, NUM, " " (space)  
# string otput = message #message to be used in part displaying semaphor

print("podaj komunikat do przekazania:\n (what do You want to transmit?)")
komunikat = str(input()).upper()

# definition of digits
#WSTAW DEFINICJE CYFR
#1-9 = a-i 0 = k
def encode_digit(value):
    global n
    if k == "0":
        n = "K"
    if k == "1":
        n = "A"
    if k == "2":
        n = "B"
    if k == "3":
        n = "C"
    if k == "4":
        n = "D"
    if k == "5":
        n = "E"
    if k == "6":
        n = "F"
    if k == "7":
        n = "G"
    if k == "8":
        n = "H"
    if k == "9":
        n = "I"
    return (n)

#KONIEC DEFINICJI CYFR
#end of digits definition 
# TO DO #with time change to list
#############################################

##############################
#klik lit gdy litery num gdy liczby
# 'klik' act as SWITCH to enter special sign when entering broadcast of digits or letters

global klik
klik = "lit"
#midlist
midlist = []

for k in komunikat:
    if k.isdigit() == False and klik == "lit":
        midlist.append(k)
        #print("warunek 1", k)
    if k.isdigit() == False and klik == "#":
        klik = "lit"
        midlist.append(klik)
        midlist.append(k)
        #print("warunek2", k)
    if k.isdigit() == True and klik == "#": # n zamiast k
        encode_digit(k)
        midlist.append(n)
        #print("warunek4", k, n)
    if k.isdigit() == True and klik == "lit": #n zamiast k
        klik = "#"
        midlist.append(klik)
        encode_digit(k)
        midlist.append(n)
        #print("warunek3", k,n)
    
#print("PRECODED:",midlist) #this is precoded message

#########################################################
#   encoding lit as flag J                              #
#   we use "J" to mark, that we end signaling digits    #
#   and following signals communicate letters           #
#########################################################
endlist = []
lit = "J"
for m in midlist:
    if m == "lit":
        endlist.append(lit)
    else:
        endlist.append(m)
#print("zakodowane:",endlist)

message = endlist
#############################
#   flag definitions        #
#############################

#a = #also = 1
def semafor_a ():
    print("")
    print("")
    print("")
    print("   O ")
    print("  /| ")
    print(" / |  ")
    print("#  # ")
    print("_______\n")

#b = 
def semafor_b ():
    print("")
    print("")
    print("")
    print("    O ")
    print("#---| ")
    print("    |  ")
    print("    # ")
    print("_______\n")

# c =
def semafor_c ():
    print("")
    print("#\\")
    print("  \\")
    print("   \\O ")
    print("    | ")
    print("    |  ")
    print("    # ")
    print("_______\n")

# d = 
def semafor_d ():
    print("  #|")
    print("   |")
    print("   | ")
    print("    O ")
    print("    | ")
    print("    |  ")
    print("    # ")
    print("_______\n")

# e =
def semafor_e ():
    print("")
    print("      /#")
    print("     /")
    print("    O ")
    print("    | ")
    print("    |  ")
    print("    # ")
    print("_______\n")

#f =
def semafor_f ():
    print("")
    print("")
    print("")
    print("    O---#")
    print("    | ")
    print("    |  ")
    print("    # ")
    print("_______\n")
#g=
def semafor_g ():
    print("")
    print("")
    print("")
    print("    O")
    print("    |\\ ")
    print("    | \\")
    print("    #  #")
    print("_______\n")

#h = 
def semafor_h ():
    print("")
    print("")
    print("")
    print("    O ")
    print("#---/ ")
    print("   /.   ")
    print("  # .  ")
    print("_______\n")

#i =
def semafor_i ():
    print("")
    print("#\\")
    print("  \\")
    print("    O ")
    print("    / ")
    print("   / .  ")
    print("  #  . ")
    print("_______\n")

#j = #letters LIT @
def semafor_j ():
    print("  #|")
    print("   |")
    print("   | ")
    print("    O---# ")
    print("    . ")
    print("    .  ")
    print("    . ")
    print("_______\n")

#k 
def semafor_k ():
    print("  #|")
    print("   |")
    print("   |")
    print("   O")
    print("  /.  ")
    print(" / .    ")
    print(" # .   ")
    print("_______\n")

#l 
def semafor_l ():
    print("")
    print("     /#")
    print("    /")
    print("   O ")
    print("  /.   ")
    print(" / .    ")
    print("#  .   ")
    print("_______\n")

#m 
def semafor_m ():
    print("")
    print("")
    print("")
    print("   O---# ")
    print("  /. ")
    print(" / .  ")
    print("#  . ")
    print("_______\n")

#n 
def semafor_n ():
    print("")
    print("")
    print("")
    print("   O ")
    print("  /.\\ ")
    print(" / . \\ ")
    print("#  .  #")
    print("_______\n")

#o 
def semafor_o ():
    print("")
    print(" #\\")
    print("   \\")
    print("#---0 ")
    print("    .  ")
    print("    . ")
    print("    . ")
    print("_______\n")

#p 
def semafor_p ():
    print("    #| ")
    print("     |")
    print("     |")
    print("#---O ")
    print("    .  ")
    print("    . ")
    print("    . ")
    print("_______\n")

#q 
def semafor_q ():
    print("")
    print("       /# ")
    print("      /")
    print("#---O ")
    print("    .  ")
    print("    . ")
    print("    . ")
    print("_______\n")

#r 
def semafor_r ():
    print("")
    print("")
    print("")
    print("#---O---# ")
    print("    .  ")
    print("    . ")
    print("    . ")
    print("_______\n")

#S 
def semafor_s ():
    print("")
    print("")
    print("")
    print("#---O ")
    print("    .\\  ")
    print("    . \\ ")
    print("    . #\\")
    print("_______\n")

#t
def semafor_t ():
    print("    #|") 
    print("#\\   |")
    print("  \\  |")
    print("   \\O ")
    print("    . ")
    print("    .  ")
    print("    . ")
    print("_______\n ")

#u 
def semafor_u ():
    print("")
    print("#\\     /#")
    print("  \\   /")
    print("   \\O/ ")
    print("    . ")
    print("    .  ")
    print("    . ")
    print("_______\n")

#v
def semafor_v ():
    print("   #| ")
    print("    |")
    print("    |")
    print("    O ")
    print("    .\\  ")
    print("    . \\")
    print("    . #\\")      
    print("_______\n")


#w 
def semafor_w ():
    print("")
    print("    /#")
    print("   /")
    print("  O---# ")
    print("  .   ")
    print("  .   ")
    print("  . ")
    print("_______\n")

#x print("_______")
def semafor_x ():
    print("")
    print("    /#")
    print("   /")
    print("  O ")
    print("  .\\   ")
    print("  . \\   ")
    print("  . #\\ ")
    print("_______\n")

#y print("_______")
def semafor_y ():
    print("     ")
    print("#\\")
    print("  \\")
    print("   \\O---#")
    print("    .")
    print("    .")
    print("    .")
    print("_______")

#z 
def semafor_z ():
    print("")
    print("")
    print("")
    print("    O---# ")
    print("    .\\  ")
    print("    . \\ ")
    print("    . #\\")
    print("_______\n")


#[space] print("_______")
def semafor_space ():
    print("")
    print("")
    print("")
    print("   O")
    print("  |.|")
    print("  |.|")
    print(" #|.|#")
    print("________\n")

#[numbers] 
def semafor_num ():
    print("      /# ")
    print("     /")
    print("    O---# ")
    print("    .  ")
    print("    . ")
    print("    . ")
    print("_______")

#[attention] #to be added
#[cancel] #to be added

#########################
#                       #
#   flag display code   #
#                       #
#########################

print("You should display following gestures:\n",message)
for c in message:
    #print(c) #uncomment to display letter alongside flag
    # to do: switch to turn on/off displaying letters
    if c == "A":
        semafor_a()
    if c == "B":
        semafor_b()
    if c == "C":
        semafor_c()
    if c == "D":
        semafor_d()
    if c == "E":
        semafor_e()
    if c == "F":
        semafor_f()
    if c == "G":
        semafor_g()
    if c == "H":
        semafor_h()
    if c == "I":
        semafor_i()
    if c == "J":
        semafor_j()
    if c == "K":
        semafor_k()
    if c == "L":
        semafor_l()
    if c == "M":
        semafor_m()
    if c == "N":
        semafor_n()
    if c == "O":
        semafor_o()
    if c == "P":
        semafor_p()
    if c == "Q":
        semafor_q()
    if c == "R":
        semafor_r()
    if c == "S":
        semafor_s()
    if c == "T":
        semafor_t()
    if c == "U":
        semafor_u()
    if c == "V":
        semafor_v()
    if c == "W":
        semafor_w()
    if c == "X":
        semafor_x()
    if c == "Y":
        semafor_y()
    if c == "Z":
        semafor_z()
    if c == " ":
        semafor_space()
    if c == "NUM":
        semafor_num()
    if c == "#":    #obejście problemu num
        semafor_num()
    if c == "@": # "LIT" = "J"
        semafor_j