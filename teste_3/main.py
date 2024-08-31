import json

def calculate_billing(dados):
    #Filtra os dias com faturamento bigger que 0.
    billings = [day['value'] for day in dados['faturamento'] if day['value'] > 0]

    #Calcula o minor e o bigger valor de faturamento.
    minor_billing = min(billings)
    bigger_billing = max(billings)

    #Calcula a média mensal.
    monthly_average = sum(billings) / len(billings)

    #Calcula o número de dias com faturamento superior à média.
    days_above_average = len([f for f in billings if f > monthly_average])

    return minor_billing, bigger_billing, days_above_average



with open('teste_3/faturamento.json', 'r') as file:
    dados_faturamento = json.load(file)

minor, bigger, days_above_average = calculate_billing(dados_faturamento)

print(f"Menor valor de faturamento ocorrido em um dia do mês: R$ {minor:.2f}")
print(f"bigger valor de faturamento ocorrido em um dia do mês: R$ {bigger:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {days_above_average} dias")