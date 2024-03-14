#3- Para os itens abaixo, crie o código solicitado:
#solicitar ao usuário 2 valores com ponto flutuante e imprimir na tela o resultado da divisão de um pelo outro com 2 casas decimais
v1 = float(input("Primeiro valor: "))
v2 = float(input("Segundo valor: "))
v = v1/v2
vr = float("%.2f" % v)
print(vr)
#solicitar ao usuário 2 valores com ponto flutuante e imprimir na tela o resultado da divisão de um pelo outro com 3 casas decimais
valor1 = float(input("Digite o valor"))
valor2 = float(input("Digite outro valor"))
divisao = valor1/valor2
nvalor = float("%.3f" % divisao)
print(nvalor)
#solicitar ao usuário 2 valores com ponto flutuante e imprimir na tela o resultado da divisão de um pelo outro com 4 casas decimais
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
dnum = num1/num2
res = float("%.4f" % dnum)
print(res)