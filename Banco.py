from time import sleep

nome = str(input('digite seu nome : ')).strip()

print('-=' * 11)
print('''Ola {}
Seja bem-vindo ao nosso banco '''.format(nome))
print('-=' * 11)
sleep(1)

print('''Nosso Banco so Trabalha com Emprestimos :
- Nos cobramos 5% de juros de nos Emprestimos
- Se o valor da Parcela do Emprestimo for maior que 30% do seu 
Salario o Emprestimo Sera NEGAOD''')
print('-=' * 11)
sleep(1)

emprestimo = int(input('Qual o valor da Emprestimo ? '))
salario = float(input('Qual o seu salario ? '))
anos = int(input('Em quantos anos você pretende pagar ? '))


salario1 = (salario * 30) / 100
tempo = anos * 12
juros = (emprestimo / tempo)*0.05
parcela1 = emprestimo / tempo
parcela = (emprestimo / tempo)*0.05 + parcela1
print('-=' * 11)
print('''Total de Parcelas {}
Valor do juros R${:.2f}
Valor da Parcelas com juros R${:.2f}
Valor da Parcelas sem juros R${:.2f}'''.format(parcela1,parcela,tempo,juros))
print('-=' * 11)
if salario1 > parcela:
    print('Emprestimo Aprovado')
else:
    print('Emprestimo Negado')
