#Solicite ao usuário uma letra que represente a nota de um aluno: A,B,C,D ou F.
nota = input("Escolha uma nota A-B-C-D ou F: ").upper()
match nota:
    case "A":
        print("Excelente")
    case "B":
        print("Bom")   
    case "C":
        print("Regular")  
    case "D":
        print("Ruim")
    case "F":
        print("Reprovado")  
    case _:
        print("Opção inválida. Escolha A,B,C,D ou F.")  