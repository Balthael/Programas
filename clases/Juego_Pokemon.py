from random import randint
import os


VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_CHARIZARD = 100
TAMAÑO_BARRA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_charizard= VIDA_INICIAL_CHARIZARD

while vida_pikachu > 0 and vida_charizard > 0 :
    input("Enter para continuar...\n\n")
    os.system("cls") #comando para limpiar pantalla

    print( "Turno de Pikachu")
    ataque_pikachu = randint (1,2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola voltio")
        vida_charizard -=10
    else:
        print("Pikachu ataca con onda trueno")
        vida_charizard -= 11

    if vida_pikachu <0:
        vida_pikachu = 0
    if vida_charizard <0 :
        vida_charizard = 0
    barras_de_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:       [{}{}] {}/{}".format("*" * barras_de_vida_pikachu," " * (TAMAÑO_BARRA-barras_de_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU))

    barras_de_vida_charizard = int(vida_charizard * TAMAÑO_BARRA / VIDA_INICIAL_CHARIZARD)
    print("Charizard:     [{}{}] {}/{}".format("*" * barras_de_vida_charizard," " * (TAMAÑO_BARRA-barras_de_vida_charizard),vida_charizard,VIDA_INICIAL_CHARIZARD))

    input("Enter para continuar...\n\n")

    print("Turno de Charizard")

    ataque_charizard = None

    while ataque_charizard != "A" and ataque_charizard != "C" and ataque_charizard != "G" and ataque_charizard !="N":

        ataque_charizard = input("Que ataque desea realizar? [A]rañazo, [C]orte, [G]olpe cabeza, [N]ada: ")
    if ataque_charizard == "A":
        print("Charizar ataca con Arañazo")
        vida_pikachu -= 10
    elif ataque_charizard == "C":
        print("Charizar ataca con Corte")
        vida_pikachu -= 12
    elif ataque_charizard == "G":
        print("Charizar ataca con Golpe de cabeza")
        vida_pikachu -= 9
    elif ataque_charizard == "N" :
        print("Charizard no hace nada")

    if vida_pikachu <0:
        vida_pikachu = 0
    if vida_charizard <0 :
        vida_charizard = 0

    barras_de_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:       [{}{}] {}/{}".format("*" * barras_de_vida_pikachu," " * (TAMAÑO_BARRA-barras_de_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU))

    barras_de_vida_charizard = int(vida_charizard * TAMAÑO_BARRA / VIDA_INICIAL_CHARIZARD)
    print("Charizard:     [{}{}] {}/{}".format("*" * barras_de_vida_charizard," " * (TAMAÑO_BARRA-barras_de_vida_charizard),vida_charizard,VIDA_INICIAL_CHARIZARD))

input("Enter para continuar...\n\n")
os.system("cls") #comando para limpiar pantalla
if vida_pikachu > vida_charizard:
    print("Pikachu gana")
else:
    print("Charizard gana")