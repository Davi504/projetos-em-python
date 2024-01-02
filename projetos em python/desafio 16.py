import math

# Função para ler um ângulo em graus
def ler_angulo():
    while True:
        try:
            angulo = float(input("Digite o valor do ângulo em graus: "))
            return angulo
        except ValueError:
            print("Por favor, digite um número válido.")

# Função para calcular e exibir o seno, cosseno e tangente do ângulo
def calcular_seno_cosseno_tangente(angulo):
    # Converter o ângulo para radianos
    angulo_radianos = math.radians(angulo)

    # Calcular seno, cosseno e tangente
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    
    # Verificar se o ângulo é diferente de 90 graus para evitar divisão por zero
    if angulo % 90 != 0:
        tangente = math.tan(angulo_radianos)
        print(f"Seno: {seno:.2f}")
        print(f"Cosseno: {cosseno:.2f}")
        print(f"Tangente: {tangente:.2f}")
    else:
        print(f"Seno: {seno:.2f}")
        print(f"Cosseno: {cosseno:.2f}")
        print("Tangente não definida para ângulo de 90 graus.")

# Programa principal
angulo = ler_angulo()
calcular_seno_cosseno_tangente(angulo)
