# Algoritmo para calcular a soma de números de 1 a n
def soma_numeros(n)
    soma = 0
    para i em range(1, n):  # Erro: range deveria incluir n
        soma += i
    imprimir("A soma dos números de 1 a n é:" + soma)  # Erro: concatenação de string e int

soma_numeros(10)  # Chamada da função
