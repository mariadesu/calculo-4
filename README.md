# calculo-4
Calculus 4 assignments.

# Indice

1. Limite
2. Estimador

## Limite

_LIMITE DE UMA SEQUÊNCIA_

- Biblioteca sympy
Caso dê o erro de compilação "ModuleNotFoundError: No module named 'sympy'", digite pip install sympy no terminal.
limit -> calcula o limite de uma função
Symbol -> formalizar a variável n da sequência
oo -> infinito
im -> retorna a parte imaginária de um número

- função limite(seq)

lim = limit(seq, n, oo)
Primeiro calculamos o limite da sequencia quando n tende ao infinito.

1) if lim == oo or lim == -oo:
Verifica se o limite tende ao mais infinito ou ao menos infinito.
Se for aplicável, retorna a mensagem "O limite da sequência tende ao infinito."

2) elif im(lim) == 0:
Verifica se o limite é um número real através da verificação dele não possuir parte imaginária.
Se for aplicável, retorna a mensagem "O limite da sequência é o número real" com o valor do limite até 2 casas decimais
        
3) else:
O limite não existe. Retorna a mensagem "O limite da sequência não existe."

- Testes
Testamos a função com 3 sequências e encontramos os seguintes resultados:

seq1 = (2*n+1)/n  "O limite da sequência é o número real 2.0"
seq2 = 2**n  "O limite da sequência tende ao infinito."
seq3 = (-1)**n  "O limite da sequência não existe."


## Estimador

_ESTIMADOR DA SOMA DE UMA SÉRIE_

- Bibliotecas
Caso dê o erro de compilação "ModuleNotFoundError: No module named 'sympy'", digite pip install sympy no terminal.
Symbol -> formalizar a variável n da sequência

a) função estimador
Recebe como parâmetro a série que deseja estimar a soma e o valor correspondente aos N primeiros termos (1 até N) que devem ser somados.
Retorna a soma dos N primeiros termos da série an.

O erro foi calculado considerando o "Termo Remanescente" (erro <= |a(n+1)|).

- teste
A saída do teste é:

Considerando a série n**(-3)
A aproximação é 1.19753198567419 para a soma dos 10 primeiros termos.
O erro dessa aproximação é 0.0007513148009015778

A aproximação é 1.20200740065968 para a soma dos 100 primeiros termos.
O erro dessa aproximação é 9.705901479276445e-07

A aproximação é 1.20205640365934 para a soma dos 1000 primeiros termos.
O erro dessa aproximação é 9.97005990014979e-10


b) função num_termos
Recebe como parâmetros o valor da aproximação x (1.644934) e a precisao (1e-6).
Considerando as variáveis i como o número de termos e soma como a soma dos termos da série,
enquanto a diferença entre a soma e o valor de aproximação buscado for maior que a precisão (0,000001),
continua-se a soma de termos. [while(abs(soma-valor_busca)>precisao)]
Quando encontramos o valor que satisfaça a precisão, retornamos o número de termos. 


- Teste
A saída do teste é:

Considerando n**(-2) e a aproximação x = 1.644934
O menor número de termos necessários para ter a mesma aproximação que x é 937340