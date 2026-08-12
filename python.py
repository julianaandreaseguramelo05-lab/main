def main():
    #NOTA: JULIANA ANDREA SEGURA MELO 
    #SIENDO SINCERA NO PUDE RESOLVER LA MAYORIA DE EJERCICIOS SOLA, YO VI PROGRAMACION CUANDO ENTRE A LA UNIVERSIDAD DEL
    # RESTO NO TENIA CONOCIMIENTO PREVIO Y PUES VOY EN CUARTO SEMESTRE Y COMO SOY DE ESTADISTICA SOLO PROGRAME EN R Y MUCHAS COSAS 
    # SE ME OLVIDARON PERO CON ESTA PRUEBA INTENTE REPASAR TODOS LOS CONCEPTOS Y PUES TENGO VARIOS AMIGOS DE SISTEMAS QUE ME EXPLICARON
    # RECORDE MUCHAS Y PUES POR INTENTE HACER TODO Y CORREGIR LOS ERRORES Y VARIOS BUCLES INFINITOS QUE SE ME PRESENTARON.
    #punto 1
    n = int(input("ingrese un numero:"))
    if n > 0:
        print("el numero es positivo")
    elif n < 0:
        print("el numero es negativo")
    else:
        print("el numero es cero")
    #punto 2
    if n < 0:
        print("el numero no es de fibonacci")
    else:
        a=0
        b=1
        while b < n:
            c = a + b
            a = b
            b = c
        if n==0 or n==b:
            print("el numero pertenece a la secuencia es de fibonacci")
        else:
            print("el numero no pertenece a la secuencia es de fibonacci")

    #punto 3
    if  n <=  1:
        print("el numero no es primo")

    else:
        di=2
        while di < n and n % di != 0:
            di=di + 1
        if di == n:
           print("el numero si es primo")
        else:
            print("el numero no es primo")
            
    #punto 4
    n2= int(input("ingrese un numero:"))
    if n <= n2:
        s=0
        i= n + 1
        while i < n2:
            s = s + i
            i = i + 1

    else:
        s=0
        i= n2 + 1
        while i < n:
            s= s + i
            i= i + 1
    print("la suma der su intermendios es : ", s)

    #punto 5 (no estaba segura de crear otras 2 variables entonces use las mismas del inicio )
    if n < 0 and n2 < 0:
        r = n * n2
        print("La multiplicación es:", r)
    else:
        r = n + n2
        print("La suma es:", r)

    #punto 6

    if n % 2 == 0 and n2 % 2 == 0:
        print("El cubo de", n, "es:", n ** 3)
        print("El cubo de", n2, "es:", n2 ** 3)

    elif n % 2 != 0 and n2 % 2 != 0:
        print("El cuadrado de", n, "es:", n ** 2)
        print("El cuadrado de", n2, "es:", n2 ** 2)

    else:
        print("Un número es par y el otro es impar.")


    # punto 7 
    id = input("Ingrese el ID: ")

    dia = int(input("Ingrese el día: "))

    mes = input("Ingrese el mes: ")

    año = int(input("Ingrese el año: "))


    #punto 8 
    fecha = [dia, mes, año, id]
    print(fecha)


    # punto 9 
    v = ["a", "e", "i", "o", "u"]
    for letra in mes:


        if letra in v:
            print(letra, "Es vocal")
        else:
            print(letra, "Es consonante")
    # punto 10 
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
              "n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

    i = 0
    while i < len(mes):
        j = 0
        while j < len(abecedario):
            if mes[i] == abecedario[j]:
                print(mes[i], "esta en la posicion del abecedario", j + 1)
            j = j + 1
        i = i + 1
main()