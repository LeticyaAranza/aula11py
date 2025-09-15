

print("Bem-vindo!\n")
print("Escolha a opção para calcular:\n")
print("(1) área do retângulo")
print("(2) volume da esfera")
print("(3) sair\n")

opcao = int(input("opção: "))

while opcao != 3:

    match opcao:

        case 1:
            largura = float(input("\nlargura: "))
            altura = float(input("altura: "))
            area = largura * altura
            print(f"área: {area:.2f}\n")

        case 2:
            raio = float(input("\nraio: "))
            volume = (4 / 3) * 3.14159 * (raio ** 3)
            print(f"volume: {volume:.2f}\n")

        case _:
            print("\nopção inválida.\n")

    print("Escolha a opção para calcular:\n")
    print("(1) área do retângulo")
    print("(2) volume da esfera")
    print("(3) sair\n")
    opcao = int(input("opção: "))

print("fim.")

            

