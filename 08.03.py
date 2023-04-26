#print("Pętle")

# for i in range (10) :  #numerowanie zaczyna się od 0, <0,10) 
#     print(i) 

# for i in range (2,15) :
#     print(i)

# for i in range (0,22,2) :   #start/stop/krok
#     print(i)

# for i in range (60,20,-3) :
#     print(i)


# for i in range(1,4):
#     for j in range(1,5):
#         print("To jest",i, "wykonanie zewnętrznej pętli i",j, "wewnętrznej pętli")


# cyfra = 0             #start
# while cyfra != 10:    #warunek końca
#     print(cyfra)
#     cyfra += 1        #krok, sposób dążenia do końca

# znak = ""                         #pętla nieskończona
# print("aby zakończyć program wciśnij \"q\"")
# while znak != "q" : 
#     print("nie wcisnąłeś \"q\"")
#     znak = input()

# print("aby zakończyć program wciśnij \"q\"")
# while True : 
#     znak = input()
#     if znak != "q":
#         print("nie wcisnąłeś \"q\"")
#     else:
#         break 


# print("aby zakończyć program wciśnij \"q\"")
# while True : 
#     znak = input()
#     if znak == "q":
#          break
#     print("nie wcisnąłeś \"q\"") 


# while True: 
#     print("aby zakończyć program wciśnij \"q\"")
#     print("aby wyświetlić imię autora wciśnij \"i\"")
#     print("aby wyświetlić nazwę przedmiotu i kieunku wciśnij \"n\"")
#     print("aby wyświetlić ulubiony kolor autora wciśnij \"f\"")
#     znak = input()
#     if znak == "i": 
#         print("Milena")
#     elif znak == "n":
#         print("Programowanie na Kogni")
#     elif znak == "f":
#         print("Fioletowy")
#     elif znak == "q":
#         break
#     else :
#         print("Ja niepaniemajuu")


# import os          #importy muszą być na górze kodu 
# os.system("cls")  #czyści terminal

# import os 
# print("to nie będzie widoczne")
# os.system("cls")
# print("to będzie widoczne")


# import os 
# while True: 
#     print("aby zakończyć program wciśnij \"q\"")
#     print("aby wyświetlić imię autora wciśnij \"i\"")
#     print("aby wyświetlić nazwę przedmiotu i kieunku wciśnij \"n\"")
#     print("aby wyświetlić ulubiony kolor autora wciśnij \"f\"")
#     znak = input()
#     os.system("cls")
#     if znak == "i": 
#         print("Milena")
#     elif znak == "n":
#         print("Programowanie na Kogni")
#     elif znak == "f":
#         print("Fioletowy")
#     elif znak == "q":
#         break
#     else :
#         print("Ja niepaniemajuu")

# print("podaj 2 liczby")
# while True : 
#     liczba1 = int(input())
#     liczba2 = int(input())
#     print("Wybierz rodzaj operacji")
#     print("aby zakończyć program wciśnij\"q\"") 
#     operacja = input()
#     if operacja == "mnożenie": 
#         print(liczba1 * liczba2)
#     elif operacja == "dodawanie": 
#         print(liczba1 + liczba2)
#     elif operacja == "dzielenie": 
#         print(liczba1 / liczba2)
#     elif operacja == "odejmowanie": 
#         print(liczba1 - liczba2) 
#     elif operacja == "q": 
#         break 
#     else :
#         print("Błąd")


    
# suma= 0 
# for i in range(0,51):
#     suma+= i                 # i = 0 suma = 0, i = 2 suma = 0+1+2
# print(suma)
