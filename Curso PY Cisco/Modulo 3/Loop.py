largest_number = -999999999

number = int(input("Digite um número ou digite 0 para parar: "))

while number != 0:
    
    if number > largest_number:
       
        largest_number = number
    
    number = int(input("Digite um número ou digite 0 para parar: "))
 
print("O maior número é:", largest_number)
print("\nPressione Enter para finalizar o programa.")
input()
print("Posso descansar finalmente...")