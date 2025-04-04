print('Ola mundo')

caixa='caneta'
print(caixa)

nome='Ana Clara'
idade= 16
altura= 1.62
estudante= True

print (f'Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudante: {estudante}') 

mensagem = "Python e divertido"

print (mensagem. strip())
print(mensagem. lower ())
print(mensagem. upper())

nome= input("qual é o seu nome? ")
print(f'Olá {nome}, seja bem-vindo a introducao python')

from datetime import datetime

nome = input("Qual é o seu nome? ")
agora = datetime.now()
hora_atual= agora.strftime("%H:%M")
print(f'Olá, {nome}! agora são {hora_atual}.')



