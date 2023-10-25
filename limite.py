from sympy import limit, Symbol, oo, im
n = Symbol('n')


def limite(seq):

    lim = limit(seq, n, oo) #Calcula o valor do limite da sequencia quando n tende ao infinito

    if lim == oo or lim == -oo: #Compara o valor para ver tende ao mais infinito ou menos infinito
        print("O limite da sequência tende ao infinito.") #Retorna que o resultado tende ao infinito
        
    elif im(lim) == 0: #Verifica se o valor é um número real
        print("O limite da sequência é o número real", round(float(lim), 2)) #Retorna o valor do limite com apenas 2 casas decimais
        
    else:
        print("O limite da sequência não existe.")
    

#Testes

seq1 = (2*n+1)/n
print("Teste 1:", seq1)
limite(seq1)
print()

seq2 = 2**n
print("Teste 2:", seq2)
limite(seq2)
print()

seq3 = (-1)**n
print("Teste 3:", seq3)
limite(seq3)