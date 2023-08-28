from datetime import date

print('-=' * 15)
print('     ALISTAMENTO MILITAR')
print('-=' * 15)

dia = int(input('Dia do Nacimento: '))
mes = int(input('Mês do Nacimento: '))
ano = int(input('Ano do Nacimento: '))

print('-=' * 15)
print('Data de Nacimento: {}/{}/{}'.format(dia,mes,ano))
idade = date.today().year - ano
print('Idade : {}'.format(idade))
print('-=' * 15)


if idade < 18:
    print('''Não e hora de se Alistar =( 
Você tem {} anos
Ainda Falta {} anos'''.format(idade,18 - idade))

elif idade == 18:
    print('''Já está na hora de se Alistar =D
Você tem {} anos'''.format(idade))

else:
    print('''Já Passou {} anos de se Alistar =(
Vá a uma Junta Militar Para Realiza o Alistamento
e Pagar a Multa do Valor de R$5.76 '''.format(idade - 18))
