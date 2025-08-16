def conocer():
    print("Bienvenido al programa, usuario. Vamos a comenzar por conocer su nombre")
    global nombre 
    nombre = input("Soy:")
    sexo = input("Y soy:").strip().lower()
    if sexo == "hombre":
        print("Encantado de conocerte, Sr.", nombre)
    elif sexo == "mujer":
        print("Encantado de conocerte, Sra.", nombre)
    else:
        while sexo not in ["hombre", "mujer"]:
            print("Por favor, ingrese 'hombre' o 'mujer'.")
            sexo = input("Soy:").strip().lower()
        
    edad = input("Cuántos años tienes? Solo menciona los años\nTengo:")
    
    sino_ocu = input("Tiene alguna ocupación? (Si/No): ").strip().lower()
    if sino_ocu.lower() == "si":
        ocupacion = input("Y cuál es?\nSoy:")
    elif sino_ocu.lower() == "no":
        ocupacion = "ninguna"
        
    extra = input("Algo más que quieras contar sobre tí?").strip().lower()
    if extra == "no":
        print("Oh, ok")
    else:
        print("Oh, interesante", nombre)
        
    print("Veamos como queda tu ficha", nombre)
    print("Nombre:", nombre)
    print("Sexo:", sexo)   
    print("Edad:", edad)
    if sino_ocu.lower() == "si":
        print("Ocupación:", ocupacion)
    if extra != "no":
        print("Información adicional:", extra)
        
    print("Gracias por compartir tu información,", nombre)
    
conocer()

def juego():
    import random
    print("Juguemos a un juego simple de adivinar un número, te parece ", nombre, "?")
    jusino = input("Si/No\n").strip().lower()
    if jusino == "si":
        print("Perfecto\nQ u e   e m p i e c e   e l   j u e g o\njaja")
        nu1 = random.randint(1, 100)
        nu2 = random.randint(1, 100)
        if nu1 > nu2:
            mayor = nu1
            menor = nu2
        else:
            mayor = nu2
            menor = nu1
        nu3 = random.randint(menor, mayor)
        nuser = 0
        nuser1 = 0
        nuser2 = 0 
        nuser3 = 0
        intentos = 0
        punto1 = 0
        punto2 = 0
        punto3 = 0
        while nuser != nu3:
            print("Tienes que adivinar los 3 números, 2 representan el intervalo dentro del cual se encuentra el tercero")
            nuser = int(input("El número: "))
            if nuser < menor or nuser > mayor:
                print("El número está fuera del intervalo, sigue intentando")
            elif nuser > menor:
                print("El número está dentro del intervalo, vas bien")
            elif nuser == nu1:
                print("Has adivinado el menor número, sigue intentando")
                nuser1 = nu1
                punto1 = 1
            elif nuser == nu2:
                print("Has adivinado el mayor número, sigue intentando")
                nuser2 = nu2
                punto2 = 1
            elif nuser == nu3:
                print("Has adivinado el tercer número, has ganado el juego")
                nuser3 = nu3
                punto3 = 1
            intentos += 1
        print("genial, veamos los resultados", nombre)
        Puntaje = punto1 + punto2 + punto3
        print("Adivinaste")
        if nuser1 != 0:
            print("El menor número:", nuser1)  
        if nuser2 != 0:
            print("El mayor número:", nuser2)
        if nuser3 != 0: 
            print("El tercer número:", nuser3)
        print("Tu puntaje es:", Puntaje)
        print("Has necesitado", intentos, "intentos para adivinar los números")
        if Puntaje == 3:
            print("Felicidades, lo hiciste perfecto")
        
        
    elif jusino == "no":
        print("Está bien, no hay problema. Hasta luego", nombre)
        return 0    