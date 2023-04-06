#SEMAFORY PREKOD
# A-Z, NUM, " "
# string otput = message #message będzie użyte w części kodu wyświetlającej semafory

print("podaj komunikat do przekazania")
komunikat = input()
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

#klik lit gdy litery num gdy liczby
global klik
klik = "lit"
#midlist
midlist = []
for k in komunikat:
    if k.isdigit() == False and klik == "lit":
        midlist.append(k)
    if k.isdigit() == False and klik == "num":
        klik = "lit"
        midlist.append(klik)
        midlist.append(k)
    if k.isdigit() == True and klik == "num": # n zamiast k
        encode_digit(k)
        midlist.append(n) #was condition 4 should be 3
    
    if k.isdigit() == True and klik == "lit": #n zamiast k
        klik = "num"
        midlist.append(klik)
        encode_digit(k)
        midlist.append(n) #was condition 3 should be 4
    

print(midlist)

#ALE czemu to nie działa?
