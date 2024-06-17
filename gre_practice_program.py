# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:49:15 2024

@author: Francisco Pizzi
UC DAVIS 
UNLP
"""
#%%
import random
import time
import csv
import math
import datetime
import os
#CHANGE DIRECTORY (use r in the begining of the path)
os.chdir(r"C:\...)


#%%
def gre_practice_program():
    print("First, focus on effectiveness. Then, on reducing the time.")
    nombre = input("Name: ")
    
    fecha  = datetime.datetime.now()
    start = time.time()
    correcta = 0 
    incorrecta = 0  
    numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137]
    q_numeros_primos = len(numeros_primos)
    
    equis = random.randint(50,60)
    for x in range(0,equis):     
        tipo_ejercicio = random.randint(1,8)    
        
        # Ejercicio multiplicacion
        if tipo_ejercicio == 1:
            a = random.randint(2, 100) 
            b = random.randint(2, 100) 
            axb = str(a * b)
            enunciado = f"Product between {a} and {b} is: "    
            respuesta_alumno = input(enunciado)
            if respuesta_alumno == axb:
                print("Correct answer")
                correcta += 1 
            else:
                print("Incorrect, answer was", axb)
                incorrecta += 1  

        # Ejercicio suma
        if tipo_ejercicio == 2:
            a = random.randint(2, 100) 
            b = random.randint(2, 100)
            c = random.randint(2, 100)
            d = random.randint(2, 100)
            e = random.randint(2, 100)
            amasb = str(a + b + c + d + e)
            enunciado = f"The sum of {a} + {b} + {c} + {d} + {e} is:"    
            respuesta_alumno = input(enunciado)
            if respuesta_alumno == amasb:
                print("Correct answer")
                correcta += 1 
            else:
                print("Incorrect, answer was", amasb)
                incorrecta += 1          

        # Ejercicio resta
        if tipo_ejercicio == 3:
            a = random.randint(101, 500) 
            b = random.randint(2, 100)
            amenosb = str(a - b)
            enunciado = f"The difference between {a} and {b} is:"    
            respuesta_alumno = input(enunciado)
            if respuesta_alumno == amenosb:
                print("Correct answer")
                correcta += 1 
            else:
                print("Incorrect, answer was", amenosb)
                incorrecta += 1  

        # Ejercicio Division
        if tipo_ejercicio == 4: 
            a = random.randint(50, 1000)
            b = random.randint(2, 40)
            quotient = str(a // b) 
            resto = str(a % b)      
            enunciado1 = f"Division {a} by {b}. Quotient (integer) is: " 
            enunciado2 = "while the remainder is: "  
            respuesta_alumno = input(enunciado1)
            respuesta_alumno2 = input(enunciado2)
            if respuesta_alumno == quotient and respuesta_alumno2 == resto:
                print("Correct answer")
                correcta += 1 
            else:
                print("Incorrect answer: Quotient is: ", quotient, "and the remainder is: ", resto)
                incorrecta += 1      

        # Ejercicio numeros primos
        if tipo_ejercicio == 5: 
            objeto_lista_primos = random.randint(1, q_numeros_primos - 2)
            numero_p = str(numeros_primos[objeto_lista_primos])
            numero_pmas1 = str(numeros_primos[objeto_lista_primos + 1])
            enunciado1 = f"What is the next prime number after {numero_p}:"
            respuesta_alumno = input(enunciado1)
            if respuesta_alumno == numero_pmas1:
                print("Correct answer")
                correcta += 1 
            else:
                print("Incorrect, answer was", numero_pmas1)
                incorrecta += 1

        # Ejercicio multiplicacion decimales
        if tipo_ejercicio == 6:
            round_a = random.randint(1, 2)
            round_b = random.randint(1, 2)
            a = round(random.randint(1, 4) * random.random(), round_a) 
            b = round(random.random(), round_b)
            axb = str(round(a * b, 4))
            enunciado = f"The multiplication between  {a} and  {b} rounded to a maximum of 4 decimal places is: "    
            respuesta_alumno = input(enunciado)
            if respuesta_alumno == axb:
                print("Correct answer")
                correcta += 1 
            else:
                print("Incorrect, answer was", axb)
                incorrecta += 1 

        # Ejercicio sumar Fracciones 
        if tipo_ejercicio == 7: 
            lista = [random.randint(2, 30) for _ in range(6)]
            suma_fracciones = str(round(lista[0] / lista[1] + lista[2] / lista[3] + lista[4] / lista[5]))
            enunciado = f"The sum of the 3 fractions:  {lista[0]}/{lista[1]} + {lista[2]}/{lista[3]} + {lista[4]}/{lista[5]} rounded to the nearest integer:"
            respuesta_alumno = input(enunciado)
            if respuesta_alumno == suma_fracciones:
                print("Correct answer")
                correcta += 1 
            else:
                print("Incorrect, answer was", suma_fracciones)
                incorrecta += 1                    

        # Ejercicio tripletes 
        if tipo_ejercicio == 8:
            lista_base = [1, 1, 3, 5, 8, 7]
            lista_altura = [1, round(math.sqrt(3), 2), 4, 12, 15, 24]
            lista_hipotenusa = [round(math.sqrt(2), 2), 2, 5, 13, 17, 25]
            nro_triplete = random.randint(0, 5)
            k = random.randint(1, 4)
            base = k * lista_base[nro_triplete]
            altura = k * lista_altura[nro_triplete]
            hipotenusa = k * lista_hipotenusa[nro_triplete]
            enunciado1 = f"In a right triangle with a base of {base} and height of {altura}, the hypotenuse is (if decimal, rounded to two decimal places):"
            enunciado2 = f"In a right triangle with a height of {base} and base of {altura}, the hypotenuse is (if decimal, rounded to two decimal places):"
            lista_enunciados = [enunciado1, enunciado2]
            opcion = random.randint(0, 1)
            enunciado = lista_enunciados[opcion]
            respuesta_alumno = input(enunciado)
            if respuesta_alumno == str(hipotenusa):
                print("Correct aFrannswer")
                correcta += 1 
            else:
                print("Incorrect, answer was", str(hipotenusa))
                incorrecta += 1

    # Resultados Generales            
    tardaste = round((time.time() - start), 2) 
    porcentaje = round(100 * correcta / equis, 2) 
    promedio = round((tardaste / equis), 2)

    print("Number of questions: ", correcta)   
    print("Correct: ", correcta)
    print("Incorrect: ", incorrecta)    
    print("Percentage: ", porcentaje, " effectivenes")
    print("Total time: ", tardaste, " seconds")
    print("Average time: ", promedio, " seconds per answer")

    # List to store results
    results = [nombre, fecha.strftime("%x"), fecha.strftime("%X"), equis, correcta, incorrecta, porcentaje, promedio, tardaste]

    # Column names for the CSV
    column_names = ["Name", "Date", "Time", "Questions", "Correct", "Incorrect", "Percentage", "Average time per q", "Total Time"]
    file_name = "results.csv"
    file_exists = os.path.isfile(file_name)
    
    with open(file_name, 'a', newline='') as f_object:
        writer_object = csv.writer(f_object)
        if not file_exists:
            writer_object.writerow(column_names)            
        writer_object.writerow(results)
        
#%%
# Run the exercise function
gre_practice_program()
#%%


