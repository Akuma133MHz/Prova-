#Guilherme Monteiro e Iago Rodrigues

#Questão 1
def nome(texto):

    if len(texto) > 5:
       return "Verdadeiro"

usuario = input("Digite um nome: ")
nome(usuario)

#Questão 4
def idade(A,B):
     return A-B

ano_nascimento = int(input("digite o ano de nascimento: "))
ano_atual = int(input("digite o ano de atual: "))

idade(ano_atual, ano_nascimento)

#Questão 3
def viagem(a,b):
    if a <= 100:
      return 1.50 * b
    else:
      return 2 * b

distancia = int(input("Digite a distância: "))
peso = int(input("Digite o valor do peso: "))

viagem(distancia, peso)
#Questão 2
def senha(A):
    if len(A) <= 3:
        return "senha deve possuir mais de 3 caracteres"
    elif len(A) > 100:
        return "por favor digite uma senha menor que 100"
    else:
        return "senha valida"

(outro arquivo:)

import aula

passoword = input("digite a senha:")
aula.senha(passoword)
