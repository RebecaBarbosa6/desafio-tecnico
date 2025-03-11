# Questão 1
indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)

# Questão 2
def pertence_fib(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

numero = int(input("Informe o número a ser verificado: "))
print(f"O número {numero} pertence à sequência de Fibonacci" 
      if pertence_fib(numero) 
      else f"O número {numero} não pertence à sequência de Fibonacci")

# Questão 3
import json
import xml.etree.ElementTree as ET

def ler_arquivo_json(caminho="dados.json"):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def ler_arquivo_xml(caminho="dados.xml"):
    tree = ET.parse(caminho)
    root = tree.getroot()
    return [{'dia': int(row.find('dia').text), 'valor': float(row.find('valor').text)} for row in root.findall('row')]

dados_json = ler_arquivo_json()
dados_xml = ler_arquivo_xml()

def analisar_faturamento(dados):
    valores = [d['valor'] for d in dados if d['valor'] > 0]
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    acima_media = sum(1 for v in valores if v > media)
    return menor, maior, acima_media

menor, maior, acima_media = analisar_faturamento(dados_json)
print(f"   Menor faturamento: R$ {menor:.2f}")
print(f"   Maior faturamento: R$ {maior:.2f}")
print(f"   Dias com faturamento acima da média: {acima_media}")

# Questão 4
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_estados.values())
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# Questão 5
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string_original = input("Informe uma string para inverter: ")
print("Questão 5 - String invertida:", inverter_string(string_original))
