from starbucks import Starbucks
from graph import Graph
import pandas as pd
import random
import sys
import heapq

dados_planilha = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Pilha/main/directory.csv", encoding="UTF-8")

quant_linhas = len(dados_planilha)
print("Quantidade de linhas do dataframe é {}.\n".format(quant_linhas))

grafo = Graph()

def menu():
    quant_vertices = int(input("Digite a quantidade de vértices:\n"))
    
    for i in range(quant_vertices):
        indice_linha_aleatoria = random.randint(0, quant_linhas)-1
        linha_dataframe = dados_planilha.iloc[indice_linha_aleatoria]
        starbucks_linha = Starbucks(linha_dataframe)
        # AQUI chame a função para adicionar as linhas no grafo
        grafo.add_vertex(starbucks_linha, starbucks_linha.store_number)

    for j in grafo:
        j_id = j.get_id()
        for k in grafo:
            k_id = k.get_id()
            peso = random.randint(0, quant_vertices)
            grafo.add_edge(j_id, k_id, peso)

    for v in grafo:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    no_inicial = input()
    no_final = input()

    grafo_no_inicial = grafo.get_vertex(no_inicial)
    grafo_no_final = grafo.get_vertex(no_final)

    grafo.short_path(grafo_no_inicial, grafo_no_final)
    # print(grafo_no_inicial, grafo_no_final)


    # target = grafo.get_vertex(grafo_no_final)
    # path = [target.get_id()]
    # grafo.shortest(target, path)
    # print ('The shortest path : %s' %(path[::-1]))
    
    menu()
menu()