income = float(input("Entre com os rendimentos "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else: 
    income >= 85528
    tax = round(0)

print("A taxa é:", tax, "thalers")

print("\nPressione Enter para finalizar o programa.")
input()
print("Posso descansar finalmente...")
