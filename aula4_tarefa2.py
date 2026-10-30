#Solicite um número de 1 a 7 e mostre o dia correspondente da semana.
dia = int(input("Escolha um número entre 1 e 7: "))
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")   
    case 3:
        print("Terça-feira")  
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")  
    case 7:
        print("Sábado")   
    case _:
        print("Opção inválida. Escolha entre 1 e 7.")   