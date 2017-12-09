def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Divisão por zero!")
    else:
        print("Resultado:", result)
    finally:
        print("Executando o bloco finally")

# divide(2,2)