# Questão 1 

indice = 13
soma = 0
k=0

while(k<indice):
    k+=1
    soma += k 
print("Ao final do processamento, a variável soma armazenará o valor:", soma)

# Questão 2

def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if n in fib:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."
        
numero = int(input("Digite um número: "))
resultado = fibonacci(numero)
print(resultado)

# Questão 3

faturamento_medio = [
    5234.50, 6789.20, 0.00, 7890.45, 3456.30, 9821.10, 6234.70, 0.00, 8990.65, 4500.85,
    6700.95, 8123.75, 2345.60, 0.00, 5432.15, 7865.25, 6345.10, 3450.90, 8921.30, 0.00,
    7894.45, 6200.30, 9123.15, 4578.70, 5634.25, 0.00, 2340.65, 8765.40, 3123.20, 5678.50
]

def minimo(array):
    valor_min=array[0]
    for i in range(1, len(array)): 
        if array[i] < valor_min and array[i] != 0:
            valor_min = array[i]
    return valor_min
    
def maximo(array):
    valor_max=array[0]
    for i in range(1, len(array)): 
        if array[i] > valor_max:
            valor_max = array[i]
    return valor_max
    
def media_valores_sem_zeros (array):
    media = 0
    faturamento_total = 0
    dias_faturados = 0
    for i in range (0, len(array)):
        faturamento_total += array[i]
        if(array[i] != 0):
            dias_faturados += 1
    
    media = faturamento_total/dias_faturados
    return media
    
def dias_faturamento_acima_da_media(array):
    media = media_valores_sem_zeros(array)
    dias_acima_da_media = 0
    for i in range(0, len(array)):
        if(array[i] > media):
            dias_acima_da_media += 1
    return dias_acima_da_media
        

maior_valor = maximo(faturamento_medio)
menor_valor = minimo(faturamento_medio)
valor_medio = media_valores_sem_zeros(faturamento_medio)
dias_acima = dias_faturamento_acima_da_media(faturamento_medio)
print(f"O menor valor foi {menor_valor}, o maior valor foi {maior_valor}")
print(f"O valor medio foi {valor_medio}, {dias_acima} dias foram registrados com valores acima da media")

# Questão 4

def calcular_percentuais(faturamentos):

    faturamento_total = sum(faturamentos.values())
    
    for estado, faturamento in faturamentos.items():
        percentual = (faturamento / faturamento_total) * 100
        print(f"Faturamento de {estado}: {percentual:.2f}%")

faturamentos = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

calcular_percentuais(faturamentos)

#Questão 5:

def inverter_string():
    
    string_original = input("Digite a string que deseja inverter: ")
    
    string_invertida = string_original[::-1]
    
    print(f"String invertida: {string_invertida}")

inverter_string()
