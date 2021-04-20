""" print(2+3)
a = 1
b = 5
number = a == b

print(number)
print(a+b)

print(min(34, 29, 31))

s1 = 'cod'
s2 = 'war'
s3 = 'zone'
print(s1 + ' ' + s2 + ' ' + s3)

"""
# Identificar as variáveis inicialmente
#________________________________________

# ex1)
""" 
price = float(input('Write one value off product R$: '))
p = float(input('Digite o percentual de desconto(0-100)%: '))

desconto = price * (p/100)
final = price - desconto

print('O preço do produto é de : {} . Teremos desconto de {}%.'  .format(price, p))
print ('Valor calculado de desconto: {} . Valor final do produto:R$ {} ' .format(desconto, final))
 
  """
  
# ex2)
""" 
km = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Quantos dias você utilizou o carro: '))

resdias = 60 * dias
reskm = 0.15 * km
price = 60 * dias + 0.15 * km

print('Como utilizou {} dias, o resultado cobrado pelos dias usados é de R$ {}'  .format(dias, resdias))
print('Assim é com a km percorrida{:.2f}, o resultado cobrado será de: R$ {:.2f}'  .format(km, reskm))
print('Somando você irá pagar {}' . format(price))
"""

# ex3)
frase = input('Digite uma frase: ')
tam = len(frase)

frase2 = frase [:int(tam/2)]
print(frase2)

print(frase2[-2:])   #manipulando índice

""" 
ex4)

name = input('Olá qual o seu nome? ')                  #função de entrada
year = input('Agora me diga a sua idade? ')

print('O seu nome é {} e a sua year é f{}. ' .format(name,year))


ex5)
s1 = 'Eu te'
s1 = s1 + ' Amo!'
print(s1)

 
ex6)
 
nota = 8.679
discipline = 'Algoritmos'
print('Você tirou {:.2f} na disciplina {}.' .format(nota, discipline))



"""
