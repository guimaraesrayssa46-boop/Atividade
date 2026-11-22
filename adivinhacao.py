palavra = "escola"
descobertas = []
erros = 0

while erros < 6:
    completa = True 

    print("Palavra:", end = "")

    for letra in palavra:
        if letra in descobertas:
            print(letra , end = " ")
        else:
            print("_", end = "")
            completa = False

        if completa:
            print("Você venceu!")
            break

    letra = input("Digite uma letra: ")

    if letra in palavra:
        descobertas.append(letra)
        print("Você acertou!")
    else:
        erros = erros + 1
        print("Você errou!")

    print("Quantidade de erros:" , erros)

if erros == 6:
    print("Você perdeu!")

print("A palavra era:", palvra) 






            
    

