#Calculadora de IMC Felipe Gomes

peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))
imc = peso / (pow(altura, 2))

print(f'Seu imc é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 24.9:print('Obesidade grau 1')
elif 35 <= imc < 39.9:
    print('Obesidade grau 2')
    print('Peso nomal')
elif 25 <= imc < 29.9:
    print('Sobrepeso')
elif 30 <= imc < 34.9:
    print('Obesidade grau 1')
elif 35 <= imc < 39.9:
    print('Obesidade grau 2')
else:
    print('Obedisade grau 3 ou Mórbida')
    