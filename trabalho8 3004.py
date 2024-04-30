# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:06:19 2024

@author: 202309151855
"""

#def imprimir_info(nome, idade, cidade, sep=' - ', end='\n'):
 #   print(f'Nome: {nome}{sep}Idade: {idade}{sep}Cidade: {cidade}!', end=end)

# Exemplo de uso:
#imprimir_info('Maria Clara', 20, 'Rio de Janeiro')

#def calcular():
    #num1 = float(input("Digite o primeiro número: "))
    #num2 = float(input("Digite o segundo número: "))
    #operacao = input("Digite a operação desejada (+, -, *, /): ")

    #if operacao == '+':
      #  resultado = num1 + num2
    #elif operacao == '-':
      #  resultado = num1 - num2
    #elif operacao == '*':
  #      resultado = num1 * num2
   # elif operacao == '/':
     #   if num2 != 0:
    #        resultado = num1 / num2
      #  else:
         #   print("Erro: Divisão por zero!")
            #return
    #else:
      #  print("Operação inválida!")
      #  return

   # print(f"O resultado de {num1} {operacao} {num2} é {resultado}.")

# Exemplo de uso:
#calcular()

def criar_lista_de_compras():
    # Pedir ao usuário para digitar os itens da lista de compras
    entrada = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Dividir a entrada do usuário em uma lista de itens
    itens = entrada.split(',')

    # Imprimir os itens em linhas separadas usando um laço
    #print("Lista de compras:")
    #for item in itens:
       # print(item.strip())  # Remover espaços em branco extras

#def celsius_para_fahrenheit(celsius):
    # Converter Celsius para Fahrenheit usando a fórmula
  # fahrenheit = (celsius * 9/5) + 32
    #return fahrenheit

# Solicitar ao usuário a temperatura em Celsius
#celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converter Celsius para Fahrenheit e imprimir o resultado
#fahrenheit = celsius_para_fahrenheit(celsius)
#print("A temperatura em Fahrenheit é:", fahrenheit)

def pedir_nomes():
    nomes = []  # Lista para armazenar os nomes digitados

    while True:
        nome = input("Digite um nome ou 'sair' para terminar: ")
        if nome.lower() == 'sair':
            break  # Encerra o loop se 'sair' for digitado
        nomes.append(nome)  # Adiciona o nome à lista

    # Imprime todos os nomes digitados em linhas separadas
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Chamada da função
pedir_nomes()