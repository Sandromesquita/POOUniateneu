numero_secreto = 30.0
diferenca = 0

for i in range(3, 0, -1):
  numero = input("Digite um numero: ")
  try:
    numero = int(numero)
  except:
    print("Digite somente numeros inteiros!")
    continue
  
  if numero == numero_secreto:
    print("Parabens voce acertou!")
    break
  else:
    print("Voce errou e tem", i-1, "chance" )
    
    if numero > numero_secreto:
      diferenca = numero - numero_secreto
      print(numero, "e maior que o numero secreto")
    else:
      diferenca = numero_secreto - numero
      print(numero, "e menor que o numero secreto")
    
    if diferenca > 30:
      print("Voce esta gelado!")
    elif diferenca > 20:
      print("Voce esta frio!")
    elif diferenca > 10:
      print("Voce esta quente!")
    else:
      print("Voce esta muito quente!")
