#trabajo de promoción de gestión de software
#crear un programa de preguntas con opciones de respuesta a cerca de python, cada respuesta correcta suma 2 puntos
#informar si el alumno aprobó o desaprobó
preguntas=["1) ¿Qué función cumple el bucle while?","2) ¿Cuál de las siguientes opciones crea una lista?",
           "3) ¿Qué opción me muestra el 2do elemento de mi lista?","4) Si quiero poner mas de una condición en un if, ¿Qué operador debo usar?",
           "5) ¿Qué función cumple el método .upper()?"]
respuestas=["b","a","c","a","b"]
opciones=["\na) Repite una acción la cantidad de veces que ordene el usuario \nb) Repite una acción mientras se cumpla una cierta condición \nc) Permite que el programa tome decisiones en base a una condición",
          "\na) Lista=[] \nb) Lista==[] \nc) []=Lista","\na) Print(lista(2)) \nb) Print(lista[2]) \nc) Print(lista[1])","\na) And \nb) Y \nc) Plus",
          "\na) Sirve para converir el contenido del string a minúsculas \nb) Sirve para convertir el contenido del string a mayúsculas \nc) Sirve para convertir la primer letra del string a mayúsculas "]
nota=0
print("""\t\t\t\t\t\t Exámen de promoción directa
      \t\t\t\t\t\t    Gestión de software 1""")
for x in range (len(preguntas)):
    print("\n",preguntas[x])
    print(opciones[x])
    opcion=input("\nEscriba la respuesta seleccionada: ")
    opcion1=opcion.lower()
    while opcion != "a" and opcion != "b" and opcion != "c":
            print("\nPor favor ingrese una respuesta válida")
            opcion=input("\nEscriba la respuesta seleccionada: ")
            opcion1=opcion.lower()
    if opcion1==respuestas[x]:
        nota+=2
        print("\n¡Respuesta correcta!, sumas dos puntos")
    else:
        print("\nOh, respuesta incorrecta, la respuesta correcta era la opcion",respuestas[x]) 
print("""\n\n\n\t\t\t\t\t¡Felicitaciones! ¡Ha finalizado el exámen!
    \nRecuerde que: un exámen es parte del proceso de aprendizaje, si aprueba significa que logro apropiarse de los contenidos.\nsi no aprobó, ¡no se desanime! Es solo un examen, aprenda de los errores cometidos, repase lo aprendido en clase e intentelo \nde nuevo. No importa cuantas veces nos caigamos, sino cuantas nos levantemos, éxitos.""")
if nota>=6:
    print("\n¡Aprobaste! \nTu nota es de",nota)
else:
    print("\nNo aprobaste \nTu nota es un",nota)