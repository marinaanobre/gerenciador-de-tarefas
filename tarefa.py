tarefas = []

while True:
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print()

    elif opcao == "2":
        for i, tarefa in enumerate(tarefas):
            print(i + 1, "-", tarefa)
            print()

    elif opcao == "3":
        for i, tarefa in enumerate(tarefas):
            print(i + 1, "-", tarefa)
            
        numero = input("Qual tarefa deseja remover? ")
        numero = int(numero)
        tarefas.pop(numero - 1)
        print()

    elif opcao == "4":
        break
    


