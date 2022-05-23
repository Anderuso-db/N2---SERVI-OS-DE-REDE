import docker
client = docker.from_env()
#-------------------------------------------------------------------------------------------------#
def getAllContainers():
    containerList = client.containers.list(all=True)
    #Se a chamada da api retornar os containers
    if containerList:
        print('------// CONTAINERS ENCONTRADOS //------')
        for container in containerList:
            print('Container Id:', container.id)
            print('Container Short Id', container.short_id)
            print('Container Name:', container.name)
            print()

    else: print('------// NENHUM CONTAINER ENCONTRADO //------')

    return containerList
#-------------------------------------------------------------------------------------------------#
def createContainer(image, containerName):
    try:
        container = client.containers.create(image=image, name=containerName)
        print(f'Container criado e iniciado com sucesso! Id: {container.id}')
        print()
    except Exception as e:
        print(f'Ocorreu algum erro durante o processo de criação do container. \nErro: {e}')
        print()
#-------------------------------------------------------------------------------------------------#
def removeContainer(containerId):
    container = client.containers.get(containerId)

    if container:
        try:
            container.remove(force=True)
            print(f'Container {container.name} removido com sucesso!')
            print()
        except Exception as e:
            print(f'Erro ao remover o container {container.name}. \nErro: {e}')
            print()

    else: print('Container não existe')
#-------------------------------------------------------------------------------------------------#
def removeAllContainers():
    containersToRemove = getAllContainers()

    if containersToRemove:
        for container in containersToRemove:
            try:
                container.remove(force=True)
                print(f'Container {container.name} removido com sucesso!')
                print()
            except Exception as e:
                print(f'Erro ao remover o container {container.name}. \nErro: {e}')
                print()
#-------------------------------------------------------------------------------------------------#
def listImages():
    imagesList =  client.images.list()
    if imagesList:
        print(' ---------// IMAGENS ENCONTRADAS //---------')
        for image in imagesList:
            print(image)
    else: print(' ---------// NENHUMA IMAGEM ENCONTRADA //---------')
    print()
    return imagesList
#-------------------------------------------------------------------------------------------------#
def pullImage(image):
    try:
        image = client.images.pull(image)
        print(f'Imagem {image} obtida com sucesso!')
        print()
    except Exception as e:
        print(f'Erro ao obter a imagem. \nErro: {e}')
        print()
#-------------------------------------------------------------------------------------------------#
def removeImage(imageName):
    try: 
        client.images.remove(imageName,force=True)
        print(f'Imagem removida com sucesso!')
        print()
    except Exception as e:
        print(f'Erro ao remover imagem. \nErro: {e}')
#-------------------------------------------------------------------------------------------------#
def removeAllImages():
    imagesToRemove =  client.images.list()
    
    if imagesToRemove:
        for image in imagesToRemove:
            try:
                client.images.remove(image.id, force=True)
                print(f'Imagem {str(image)} removida com sucesso!')
                print()
            except Exception as e:
                print(f'Erro ao remover a imagem {image}. \nErro: {e}')
                print()
