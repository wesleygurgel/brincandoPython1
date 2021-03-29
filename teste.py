# 576.73
# NOTAS:
# 5 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 1 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 1 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 1 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 2 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 3 moeda(s) de R$ 0.01

valor = float(input())
resto = valor
print('NOTAS:')
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

for valores in notas:
    valorInteiro = resto // valores
    resto = resto - valorInteiro * valores
    print('%d nota(s) de R$ %.2f' % (int(valorInteiro), valores))

print('MOEDAS:')

for valores in moedas:
    valorInteiro = resto // valores
    resto = resto - valorInteiro * valores
    print('%d moeda(s) de R$ %.2f' % (int(valorInteiro), valores))
