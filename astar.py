class Node():
    
    def __init__(self, parente = None, posiçao = None):
        self.parente = parente
        self.posiçao = posiçao

        self.f = 0
        self.g = 0
        self.h = 0 #Será utilizado Distância de Manhattan

    def __eq__(self, other):
        return self.posiçao == other.posiçao
    
def astar(mapa, começo, final):
    #parâmetros iniciais
    node_inicial = Node(None, começo)
    node_inicial.f = node_inicial.g = node_inicial.h = 0

    node_final = Node(None, final)
    node_final.f = node_final.g = node_final.h = 0

    lista_aberta = []
    lista_fechada = []

    lista_aberta.append(node_inicial)

    #pega um node
    while len(lista_aberta) > 0:
        node_atual = lista_aberta[0]
        index_atual = 0
        for index, item in enumerate(lista_aberta):
            if item.f < node_atual.f:
                node_atual = item
                index_atual = index

        lista_aberta.pop(index_atual)
        lista_fechada.append(node_atual)

    #verifica se já chegou no final
        if node_atual == node_final:
            caminho = []
            atual = node_atual
            while atual is not None:
                caminho.append(atual.posiçao)
                atual = atual.parente

            return caminho[::-1]

    #gera os vizinhos adjacentes
        vizinhos=[]

        for nova_posiçao in [(0,-1), (-1, 0), (0,1), (1, 0), (-1, 1), (-1, -1), (1, 1), (1,-1)]:
        #pega a posição de um node
            posiçao_node = (node_atual.posiçao[0] + nova_posiçao[0], node_atual.posiçao[1] + nova_posiçao[1])
        #verificando se está dentro do alcance
            if posiçao_node[0] > (len(mapa) - 1) or posiçao_node[0] < 0 or posiçao_node[1] > (len(mapa[len(mapa)-1])-1) or posiçao_node[1]<0:
                continue
        #verificando se o caminho está liberado
            if mapa[posiçao_node[0]][posiçao_node[1]] != 0:
                continue
        #cria um novo node
            novo_node = Node(node_atual, posiçao_node)

            vizinhos.append(novo_node)

        for vizinho in vizinhos:
            for vizinho_fechado in lista_fechada:
                if vizinho == vizinho_fechado:
                    continue


    #Criar os valores para f, g e h para cada vizinho
            vizinho.g = node_atual.g + 1 #pesquisa os vizinhos com base nas posições permitidas

            vizinho.h = heuristic(vizinho.posiçao, node_final.posiçao)

            vizinho.f = vizinho.g + vizinho.h

            for node_aberto in lista_aberta:
                if vizinho == node_aberto and vizinho.g > node_aberto.g:
                    continue


            lista_aberta.append(vizinho)


def heuristic(node1, node2):
    dx = abs(node1[0] - node2[0])
    dy = abs(node1[1] - node2[1])
    return (dx+dy)


def main():
    começo = (0, 0)
    final = (21, 5)
    mapa = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]]


    caminho = astar(mapa, começo, final)
    print(caminho)


    

if __name__ == '__main__':
    main()
