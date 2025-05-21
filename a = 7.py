while True:
    try:    
        a = float(input("ingresa un valor 'a' aquí: "))
        b = float(input("ingresa un valor 'b'aquí: "))
        if a and b !=0:
            break
        else:
            print("No se puede dividir por cero!")
    except ValueError:
        print("Valor invalido!")
    except ZeroDivisionError:
        print("No se puede dividir por cero!")
    except SyntaxError:
        print("Ingrese valores numericos!")

print(a + b) # mostrar el resultado de la suma aquí
print(a - b) # mostrar el resultado de la resta aquí
print(a * b) # mostrar el resultado de la multiplicación aquí
print(a / b) # mostrar el resultado de la división aquí

print("\n¡Eso es todo, amigos!")