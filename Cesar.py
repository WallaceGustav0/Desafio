import random
import string

def gerar_senha(tamanho):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(tamanho))

def criptografar_senha(senha, deslocamento=3):
    letras1 = string.ascii_lowercase
    letras2 = string.ascii_uppercase
    numeros = string.digits

    senha_criptografada = []
    for caractere in senha:
        if caractere in letras1:
            posicao = (letras1.index(caractere) + deslocamento) % 26
            senha_criptografada.append(letras1[posicao])
        elif caractere in letras2:
            posicao = (letras2.index(caractere) + deslocamento) % 26
            senha_criptografada.append(letras2[posicao])
        elif caractere in numeros:
            posicao = (numeros.index(caractere) + deslocamento) % 10
            senha_criptografada.append(numeros[posicao])
        else:
            senha_criptografada.append(caractere)

    return ''.join(senha_criptografada)

tamanho_senha = 7
senha = gerar_senha(tamanho_senha)
senha_criptografada = criptografar_senha(senha)

print(f'Senha gerada: {senha}')
print(f'Senha criptografada: {senha_criptografada}')