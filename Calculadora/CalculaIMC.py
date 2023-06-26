def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Peso insuficiente"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

print("Calculadora de Índice de Masa Corporal (IMC)")
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)
print("Tu Índice de Masa Corporal (IMC) es:", imc)
interpretacion = interpretar_imc(imc)
print("Interpretación del IMC:", interpretacion)
