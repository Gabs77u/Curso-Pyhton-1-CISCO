year = int(input("Digite um ano: "))

if year < 1582:
 print("Não pertence ao periodo do calendario gregoriano")
else:
   if year % 4 != 0:
     print("Ano Comum")
   elif year % 100 != 0:
     print("Ano Bissexto")
   elif year % 400 != 0:
     print("Ano Comum")
   else:
     print("Ano Bissexto")

print("\nPressione Enter para finalizar o programa.")
input()
print("Posso descansar finalmente...")