import random
import colores
import os
os.chdir(os.path.dirname(__file__))

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def instrucciones_wordle():

    print("""Bienvenido al simulador de Wordlee\nComo jugar:\n\t - Adivina la palabra oculta en el número de intentos definas.\n\t - Cada intento debe ser una palabra de la misma longitud que la palabra definidia.\n\t - Después de cada intento el color de las letras cambia para mostrar qué tan cerca estás de acertar la palabra.\nEjemplos:\n""")


    print(colores.bcolors.VERDE + "G" + colores.bcolors.RESET + "ATOS")
    print(colores.bcolors.VERDE + "La letra G está en la palabra y en la posición correcta." + colores.bcolors.RESET)

    print("VO" + colores.bcolors.AMARILLO + "C" + colores.bcolors.RESET + "AL")
    print(colores.bcolors.AMARILLO+ "La letra C está en la palabra pero en la posición incorrecta." + colores.bcolors.RESET)

    print("CANTO")
    print("Ninguna de las letras está en la palabra definida\n")

    print("Puede haber letras repetidas.")



def elegir_palabra(x):
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]
    letra = random.choice(abecedario)
    c = "dics/" + letra + ".txt"
    abrir = open(c)
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    lista_de_palabra = []
    for line in abrir:
        line = line.replace(" ","")
        line = line.replace("\n","")
        for letter in line:
            if  letter in numeros:
                index_number = line.index(letter)
                line = line[:index_number]
            if "," in line:
                index_colom =line.index(",")
                line = line[:index_colom]
        if len(line)== x: 
            lista_de_palabra.append(line) 
    palabra = random.choice(lista_de_palabra)
    palabra_normalizada = normalize(palabra)
    return palabra_normalizada


def buscar(a):
    c = "dics/" + a[0] + ".txt"
    abrir = open(c)
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    for line in abrir:
        line = line.replace(" ","")
        line = line.replace("\n","")
        for letter in line:
            if  letter in numeros:
                index_number = line.index(letter)
                line = line[:index_number]
            if "," in line:
                index_colom =line.index(",")
                line = line[:index_colom]
        palabra_normalizada = normalize(line)
        
        if a != palabra_normalizada:
            continue
        return "existe"
