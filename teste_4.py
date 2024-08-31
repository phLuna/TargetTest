states = [
    {"state": 'SP', "value": 67836.43},
    {"state": 'RJ', "value": 36678.66},
    {"state": 'MG', "value": 29229.88},
    {"state": 'ES', "value": 27165.48},
    {"state": 'Outros', "value": 19849.53}
]

#Soma o total dos valores.
total_value = sum(state["value"] for state in states)

#Calcula o percentual de cada esatdo.
def calculate_percentual(value, total):
    percentage = (value / total) * 100
    return percentage

#Imprime o percentual de cada estado.
for state in states:
    percentual = calculate_percentual(state["value"], total_value)
    print(f'O percentual de representação de {state["state"]} é de {percentual:.2f}%.')