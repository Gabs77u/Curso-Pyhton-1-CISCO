#var1 = input()
#print(var1 == 1)
#print(var1 != 0)

#n = int(input("Digite um número:\n")) 
#print(n >= 100)

var1 = int(input("Digite um numero \n"))
var2 = int(input("Digite um numero \n"))
var3 = int(input("Digite um numero \n"))

largest_number = var1

if var2 >= largest_number:
    largest_number = var2
elif var2 <= largest_number:
    largest_numeber = var1
if var3 >= largest_number:
    largest_number = var3
elif var3 <= largest_number:
    largest_number = var2
if var1 >= var2:
    largest_number = var3

print("O maior numero é: ", largest_number)
print("Aperte Enter para encerrar o programa")
input()
print("Finalmente posso descansar...")