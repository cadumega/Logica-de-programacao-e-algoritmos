# ex1) Dois números inteiros e compara ambos
""" x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))
if (x>y) :
  print('O primeiro valor é maior que o segundo!')
else:
  print('O segundo valor que é maior do que o primeiro!')

"""

# ex2) par ou ímpar

""" x = int(input('Digite um valor inteiro: '))
if (x% 2 == 0):              #comparação lógica com ==
  print('O número é par!')
else:
  print('O número é ímpar!') """


""" #ex3)

x = True
y = False

print (not x)
print (not y)


#and
x = True
y = False
print (x and y)   #false , pois para ser true precisa de 2 value true

#or
x = True
y = False
print (x or y)  #true, pois preciso só de um value true
"""

# ex4)
# x = 10
# y = 1
# res = not x > y  # x>y é true... só que tenho not, tornando false a expressão
# print(res)

""" ex5)
x = 10
y = 1
z = 5.5
result = x > y and z == y  # true and false == false
print(result) """

# ex6) Aprovado é passar em todas as matérias, média = 7, aluno cursa 3 matérias somente. Algoritmo que leia a nota final do aluno em cada matéria e informe se passou ou não.

""" mat1 = float(input('Qual a nota na 1° matéria? '))
mat2 = float(input('Qual a nota na 2° matéria? '))
mat3 = float(input('Qual a nota na 3° matéria? '))

#escolha do operador lógico é fundamental, se tivesse or, a expressão altera
if mat1 >= 7 and mat2 >=7 and mat3 >=7:
  print('O aluno está aprovado nas 3 matérias, médias acima de 7!')
else:
  print('O aluno não passou de ano!') """


""" # ex 7)
print('Escolha o que deseja comprar:')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual a sua escolha? '))
qtd = int(input('Quantas unidades? '))

if(produto == 1):
    pagar = qtd * 2.3
    print('Você comprou {} maças. Total à pagar: {}' .format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd * 3.6
        print('Você comprou {} laranjas. Total à pagar: {}' .format(qtd, pagar))
    else:
        if (produto == 3):
            pagar = qtd * 1.85
            print('Você comprou {} bananas. Total à pagar: {}' .format(qtd, pagar))
        else:
            print('Produto inexistente!')
             """
             
# BOA PRÁTICA! ELIF Condicional de múltiplas escolhas, visa simplificar e ficar mais fácil de escrever o código.

# ex7.2)
""" print('Escolha o que deseja comprar:')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual a sua escolha? '))
qtd = int(input('Quantas unidades? '))

if (produto == 1):
    pagar = qtd * 2.3
    print('Você comprou {} maças. Total à pagar: {}' .format(qtd, pagar))
elif (produto == 2):
    pagar = qtd * 3.6
    print('Você comprou {} laranjas. Total à pagar: {}' .format(qtd, pagar))
elif (produto == 3):
    pagar = qtd * 1.85
    print('Você comprou {} bananas. Total à pagar: {}' .format(qtd, pagar))
else:
    print('Produto inexistente!') 
"""
    
# ex8)
nome = input ('Qual o seu nome? ')
idade = int(input ('Qual a sua idade? '))
if nome == 'Carlos':
  print('Olá, Carlos!')
elif idade < 18:
  print('Você não é o Carlos! Você também é menor de idade!')
elif idade >= 100:
  print('Mestre dos magos, com muita sabedoria!')
else:
  print('{} Você ainda é xovem!' . format(nome))