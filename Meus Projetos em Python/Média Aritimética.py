#DÁ AS BOAS VINDAS AO ALUNO
print("Olá aluno!")

#VARIAVEIS E ENTRADA DE DADOS
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
n4 = float(input('Digite a quarta nota:'))


#EXECUTA A SOMA DAS NOTAS
soma = n1 + n2 + n3 + n4

#DIVIDE AS NOTAS E OBTEM A MEDIA
media = soma / 5

#CONDIÇOES PARA DIZER SE O ALUNO FOI APROVADO OU NÃO
if media >= 5:
    print("Você foi aprovado!")
elif media <= 5:
    print("você foi reprovado")

#MOSTRA A SUA MEDIA E DIZ SE VOCE FOI APROVADO OU NÃO
print("A sua media final foi: {}".format(media))


