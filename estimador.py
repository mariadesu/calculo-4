from sympy import Symbol
n = Symbol('n')

#a)
def estimador(an, N):
    soma = 0
    for i in range(1, N + 1):
        soma += an.subs(n, i)
    return soma

#Teste (a)
an = 1/n**3

print("Letra a)")
print("Considerando a série", an)
for i in range(1,4):
    print("A aproximação é", estimador(an,10**i).evalf(), "para a soma dos", 10**i,"primeiros termos.")
    print("O erro dessa aproximação é", abs(1/((10**i)+1)**3))
    print()


#b)
def num_termos(valor_busca, precisao):
    i = 1
    soma = 1
    while(abs(soma-valor_busca)>precisao):
        i +=  1
        soma += 1/i**2
    return i


#Teste (b)
bn = 1/n**2
valor_busca = 1.644934
precisao = 1e-6

print("Letra b)")
print("Considerando", bn, "e a aproximação x =", valor_busca)
print("O menor número de termos necessários para ter a mesma aproximação que x é", num_termos(valor_busca, precisao))