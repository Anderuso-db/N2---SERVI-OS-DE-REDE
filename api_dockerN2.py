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
    except Exception as e:
        print(f'Ocorreu algum erro durante o processo de criação do container. \nErro: {e}')
#-------------------------------------------------------------------------------------------------#
def removeContainer(containerId):
    container = client.containers.get(containerId)

    if container:
        try:
            container.remove(force=True)
            print(f'Container {container.name} removido com sucesso!')
        except Exception as e:
            print(f'Erro ao remover o container {container.name}. \nErro: {e}')

    else: print('Container não existe')
#-------------------------------------------------------------------------------------------------#
def removeAllContainers():
    containersToRemove = getAllContainers()

    if containersToRemove:
        for container in containersToRemove:
            try:
                container.remove(force=True)
                print(f'Container {container.name} removido com sucesso!')
            except Exception as e:
                print(f'Erro ao remover o container {container.name}. \nErro: {e}')
#-------------------------------------------------------------------------------------------------#
def listImages():
    imagesList =  client.images.list()
    if imagesList:
        print(' ---------// IMAGENS ENCONTRADAS //---------')
        for image in imagesList:
            print(image)

    return imagesList
#-------------------------------------------------------------------------------------------------#
def pullImage(image):
    try:
        image = client.images.pull(image)
        print(f'Imagem {image} obtida com sucesso!')
    except Exception as e:
        print(f'Erro ao obter a imagem. \nErro: {e}')
#-------------------------------------------------------------------------------------------------#
def removeImage(imageName):
    try: 
        image = client.images.remove(imageName)
        print(f'Imagem {image.id} removida com sucesso!')
    except Exception as e:
        print(f'Erro ao remnover imagem. \nErro: {e}')
#-------------------------------------------------------------------------------------------------#
def removeAllImages():
    imagesToRemove =  client.images.list()

    if imagesToRemove:
        for image in imagesToRemove:
            try:
                imageToRemove = client.images.remove(image.id)
                print(f'Imagem {imageToRemove} removida com sucesso!')
            except Exception as e:
                print(f'Erro ao remover a imagem {image}. \nErro: {e}')