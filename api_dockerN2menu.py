import api_dockerN2 as api

def menu():
    exit = False

    while not exit:
        option = input(
            '1 - Obter todos os containers\n' +
            '2 - Criar Container\n' +
            '3 - Remover Container\n' +
            '4 - Remover Todos os Containers\n' +
            '5 - Mostrar Imagens\n' + 
            '6 - Enviar Imagem\n' +
            '7 - Excluir Imagem\n' +
            '8 - Remover todas as Imagens\n'
            '9 - Sair\n' 
        )

        if option == '1':
            api.getAllContainers()
        elif option == '2':
            image = input('Digite o nome da imagem para o container:\n')
            containerName = input('Digite o nome do container a ser criado:\n')
            api.createContainer(image, containerName)
        elif option == '3':
            containerId = input('Insira o id do container a ser removido:\n ')
            api.removeContainer(containerId)
        elif option == '4':
            api.removeAllContainers()
        elif option == '5':
            api.listImages()
        elif option == '6':
            imageName = input('Digite o nome imagem que deseja obter:\n')
            api.pullImage(imageName)
        elif option == '7':
            imageName = input('Digite o nome da imagem que deseja excluir:\n')
            api.removeImage(imageName)
        elif option == '8':
            api.removeAllImages()
        else: exit = True

menu()
