horas = int(input("Hora de início (horas): "))
mins= int(input("Hora de início (minutos): "))
dur = int(input("Duração do evento (minutos): "))

#Estrutura de Horas e Minutagem

mins = mins + dur 
horas = horas + mins // 60 
mins = mins % 60 
horas = horas % 24 
print(horas, ":", mins, sep='')

print("\nPressione Enter para finalizar o programa.")
input()
print("Posso descansar finalmente...")