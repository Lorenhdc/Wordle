import funciones
import colores

class Game():

    def wordle(num_letras, num_vidas):
        vidas = num_vidas
        palabra_adivinar = funciones.elegir_palabra(int(num_letras))
        count = 0

        respuesta = []
        funciones.instrucciones_wordle()
        print(f""" ¡Comienza el juego!
        
        La palabra seleccionada contine {len(palabra_adivinar)} letras""")

        while vidas > 0:

            palabra = input(f"Introduce una palabra: ")

            if len(palabra) == num_letras:
                if funciones.buscar(palabra) == "existe":
                    count += 1
                    if palabra == palabra_adivinar: 
                        print(count, ". ", colores.bcolors.VERDE + palabra.upper() + colores.bcolors.RESET)
                        print("Enhorabuena, acertaste!")

                        break
                
                    else: 
                        vidas -= 1
                        respuesta.clear()
                        for i,z in zip(palabra, palabra_adivinar): 
                            if i == z: 
                                respuesta.append(colores.bcolors.VERDE + i.upper()+ colores.bcolors.RESET)
                            elif i in palabra_adivinar: 
                                respuesta.append(colores.bcolors.AMARILLO + i.upper()+ colores.bcolors.RESET)
                            else: 
                                respuesta.append(i.upper())
                        salida = "".join(respuesta)
                        print(count, ". ", salida)
                else:
                    print(f"La palabra {palabra} no se haya en el diccionario")
            else:
                print(f"Por favor, introduce una palabra de {num_letras} letras")
        else: 
            print("Has perdido")
            print(f"la palabra que estabamos buscando es {palabra_adivinar}")

            
