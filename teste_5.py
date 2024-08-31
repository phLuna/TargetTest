def reverse_sentence(string):
    return string[::-1]  # Retorna a string invertida

#Recebe a entrada do usuário.
phrase = input('Insira uma frase: ')

#Inverte a frase usando a função.
reverse_phrase = reverse_sentence(phrase)

print(f'Ao contrário, a frase é: {reverse_phrase}')