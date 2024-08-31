#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53
#
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

states = [
    {"state": 'SP', "value": 67836.43},
    {"state": 'RJ', "value": 36678.66},
    {"state": 'MG', "value": 29229.88},
    {"state": 'ES', "value": 27165.48},
    {"state": 'Outros', "value": 19849.53}
]

total_value = 0
for state in states:
    total_value += state["value"]


def calculate_total(state_value, total_value):
    percentage = (state_value / total_value) * 100
    return percentage