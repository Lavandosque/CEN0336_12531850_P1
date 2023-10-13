import sys


def calcular_area(a, b):
    return a * b / 2


def main():
    if len(sys.argv) != 3:
        print("Uso: python script_area.py a b")
        sys.exit(1)


    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])


        if a < 1 or a >= 500 or b < 1 or b >= 500:
            print("Os valores de a e b devem ser inteiros positivos menores que 500.")
        else:
            area = calcular_area(a, b)
            print(f"A área do triângulo retângulo com lados a={a} e b={b} é {area:.2f}")
    except ValueError:
        print("Certifique-se de fornecer dois números inteiros válidos.")


if __name__ == "__main":
    main()

