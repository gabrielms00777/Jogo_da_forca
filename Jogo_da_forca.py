print('----Bem vindo ao jogo da forca----\n')

secreta = input('Escolha um númuro: 1, 2, 3: ')

if secreta == "1":
  palavra_secreta = 'sorvete'
elif secreta == '2':
  palavra_secreta = 'caracol'
elif secreta == '3':
  palavra_secreta = 'espelho'
else:
  palavra_secreta = 'indefinido'

digitadas = []
chances = 3
while True:
  if chances <= 0:
    print('Você perdeu, tente de novo!')
    break

  letra = input('Digite uma letra: ')

  if len(letra) > 1:
    print("Ahh por favor digite apenas uma letra.")
    continue

  digitadas.append(letra)

  if letra in palavra_secreta:
    print(f'UHUUU a letra {letra} esta na palavra secreta!')
  else:
    print(f'AFFFzzz a letra {letra} NÃO esta na palavra secreta.')
    digitadas.pop()

  secreto_temp = ''

  for letra_secreta in palavra_secreta:
    if letra_secreta in digitadas:
      secreto_temp += letra_secreta
    else:
      secreto_temp += '*'

  if secreto_temp == palavra_secreta:
    print(f'Quel legal, VOCÊ GANHOU!!! A palavra era {palavra_secreta}')
    break
  else:
    print(f'A palavra secreta esta assim: {secreto_temp}')

  if letra not in palavra_secreta:
    chances -= 1

  print(f'Você ainda tem {chances} chances.\n')