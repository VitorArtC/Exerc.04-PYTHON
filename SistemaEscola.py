
notas01 = float(input("Nota do 1 Bimestre: "))
notas02 = float(input("Nota do 2 Bimestre: "))
notas03 = float(input("Nota do 3 Bimestre: "))
notas04 = float(input("Nota do 4 Bimestre: "))

media = (notas01 + notas02 + notas03 + notas04)/4


if media >= 7:
    print("Aprovado =D sua média é: {:.1f}".format(media))

elif 5 <= media <= 6.9:
    print("Recuperaçao =( sua média é : {:.1f}".format(media))

else:
     print("Reprovado!! Você vai estudar com o Tijolo, sua média é: {:.1f}".format(media))