while True:
    number1 = input("Digita un numero\n")
    number2 = input("Digita un numero\n")

    try:

        result = int(number1)/int(number2)
        print(f"El resultado es: {result}")

    # except ValueError:
    #   print("Por favor solo ingrese numeros")

    # except ZeroDivisionError:
    #   print("El segundo numero evita que sea 0")

    except Exception as e:
        print(F"Se produjo un error del tipo {e}")

    finally:
        print("El programa ha terminado")
        