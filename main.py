'''001
Escreva um programa que pergunte para o usuário seu nome e depois seu 
sobrenome e exiba a seguinte mensagem: 
Seja bem-vindo ao INFNET, [Nome] [Sobrenome]
'''

first_name = input("What's your first name?").strip()
last_name = input("What's your last name?").strip()

print("Seja bem-vindo ao INFNET, ", first_name + " " + last_name)

'''002
Crie um programa que receba um parágrafo e diga quantas palavras existe 
nesse texto. Considere que só existe exatamente um espaço entre as palavras.
'''
text = input("Escreva seu texto aqui: ").strip()

text = text.count(" ") + 1

print(text)

'''003
Crie um programa que recebe um número inteiro N > 1 e gere uma risada 
“kkkk” com a quantidade de “k” iguais ao valor de N. Por exemplo, se N = 5 ele deve gerar a risada kkkkk
'''
x = input("Quantas vezes você quer repetir?")
x = int(x)

print("k" * x)

'''004
A long time ago in a galaxy far, far away...
No exemplo acima, a palavra far é repetida duas vezes. No entanto, 
gostaríamos de repeti-lo exatamente vezes sem alterar o resto da frase. Deve 
haver uma vírgula logo após cada ocorrência, exceto a última.
Dado N, você consegue produzir a frase corretamente?
'''
x = input("Quantas vezes você quer repetir?")
x = int(x)

x_new = x - 1
time = "far, " * x_new


print("A long time ago in a galaxy " + time + "far away")

'''05
Você conhece uma família com três filhos. Suas idades formam uma sequência aritmética, isto é, a diferença de idade entre o filho do meio e o filho mais novo é a mesma que a diferença de idade entre o filho mais velho e o filho do meio. Por exemplo, suas idades podem ser 5, 10 e 15, já que ambos os pares adjacentes têm uma diferença de 5 anos. Dadas as idades dos filhos mais novo e do meio, qual é a idade do filho mais velho'''
#Input do usuario
filho_03 = input("Qual a idade do filho mais novo?")
filho_02 = input("Qual a idade do filho do meio?")
#Transformando em integer
kid_03 = int(filho_03)
kid_02 = int(filho_02)
#Calculando
dif = kid_02 - kid_03

kid_01 = kid_02 + dif

print("O filho mais velho tem", kid_01, "anos")

'''06
"Ugh, tem estado tão quente ultimamente, por que tem que estar 32 graus... 32 graus? Isso é congelar'''
fahr = input("Qual a temperatura em Fahrenheit?")

new_temp = int(fahr)

celcius = (5 / 9) * (new_temp - 32)

new_celcius = int(celcius)


print("A temperatura em celcius é: ", new_celcius)

'''07
Quanto dinheiro James ganhará para a Equipe Rocket no total, com suas 
vendas de emblemas e sobras de tinta quando P = 14, B = 3 e N=10?'''

#Quantidade de tinta
P = 14
#Tinta usada por tampa
B = 3
#Valor de cada tampa(insignia)
N = 10

#Calculo de tampas
badges = (P // B) * 10
leftover = (P % B) * 1

#Valor arrecadado
pokemoney = badges + leftover

print(pokemoney)

''' 08
Você está ajudando seu sobrinho a estudar matemática na escola. Ele está 
aprendendo divisão e você precisa conferir se a tarefa dele está correta. Como ele ainda não estudou os números reais você precisa verificar se ele calculou corretamente o quociente e o resto das divisões (divisão inteira). Para evitar erros você decide escrever um programa que pergunta para o usuário o dividendo e o divisor e mostra na tela o quociente e o resto da operação. '''

dividendo = input("Qual o dividendo?")
divisor = input("Qual o divisor?")

quociente = int(dividendo) // int(divisor)
resto = int(dividendo) % int(divisor)

print("O quociente é: ", quociente, " e o resto é: ", resto)

'''09 
Três amigos foram para um restaurante. O primeiro gastou 60 reais, o segundo gastou 1,5 vezes mais que o primeiro e o último a média entre o primeiro e o segundo. Faça um programa que calcula o total da conta do restaurante.
'''
a_01 = 60
a_02 = a_01 + (a_01 * 1.5)
a_03 = (a_01 + a_02) / 2

bill = round(a_01 + a_02 + a_03)
print("R$", bill)

'''10
Faça um programa que recebe do usuário o tamanho dos dois catetos de um 
triângulo retângulo e retorna qual o tamanho da hipotenusa. (Lembre do 
teorema de Pitágoras a**2 = b**2 + c**2). Será necessário pesquisar como 
calcular raiz quadrada em Python'''
import math

b = int(input("Qual o valor de b? "))
c = int(input("Qual o valor de c? "))

bc = (b**2) + (c**2)

a = math.sqrt(bc)

print(round(a))

'''11 
Faça um programa que pergunta para o usuário o nome completo do mesmo 
e imprime quantas letras existem no nome dele completo e quantas letras 
existem no primeiro nome dele. Considere que o usuário sempre vai escrever o seu nome completo, isto é, sempre vai ter pelo menos um espaço na string para separar os nomes'''
#tirando todos os espaços do nome
def count_letters(name):
  return len(name.replace(" ", ""))

#Pegando o input do usuario
full_name = input("Qual o seu nome?").strip()

#Dividindo o nome
names = full_name.split()
first_name = names[0]
#utilizar o -1 para lidar com nomes maiores que 2 unidades
#caso nao tenha, ficara em branco
last_name = names[-1] if len(names) > 1 else ""

#contando as letras
first_name_counting = count_letters(first_name)
last_name_counting = count_letters(last_name)

print(f"O seu primeiro nome, {first_name}, tem {first_name_counting} letras")
print(f"O seu último nome, {last_name}, tem {last_name_counting} letras")

'''12) 
Escreva um programa que dado uma palavra de entrada do usuário retorna 
quantas letras essa palavra possui.'''

def count_letters(palavra):
  return len(palavra.replace(" ", ""))

entrada = input("Qual a palavra que você gostaria de verificar? ").strip()

counting = count_letters(entrada)

print(f"A sua palavra, {entrada}, possui {counting} letras.")

'''13)
Escreva um programa que dado a quantidade de resultados N e a quantidade de resultados por página P calcule a quantidade de páginas necessárias para mostrar todos os produtos'''

results = input("Quantos resultados deu a sua procura? ").strip()
per_page = input("Quantos resultados devem ser mostrados por página? ").strip()

total_pages = int(results) // int(per_page)

print(f"Serão mostrados {total_pages} resultados por página.")

'''13)
Escreva um programa que dado a quantidade de resultados N e a quantidade de resultados por página P calcule a quantidade de páginas necessárias para mostrar todos os produtos'''

results = int(input("Quantos resultados deu a sua procura? "))
per_page = int(input("Quantos resultados devem ser mostrados por página? "))

total_pages = int(results) // int(per_page)
#garantindo que se o número for quebrado, uma pagina extra será adicionada
if results % per_page != 0:
  total_pages += 1

print(f"Serão mostrados {total_pages} resultados por página.")
