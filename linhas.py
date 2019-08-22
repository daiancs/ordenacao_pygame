"""Ordena um vetor de inteiros aleatório e exibe de forma gráfica utilizando a biblioteca PyGame"""
import pygame
import random
import time
from pygame.locals import *

LARGURA = 400
ALTURA = 600
ESPESSURA = 2
PROG_NOME = "Linhas aleatórias"


def exibe_lista(posicao_inicial, lista):
    for pos_atual, valor in enumerate(lista, posicao_inicial):
        desenha_linha_no_canvas(screen, pos_atual * ESPESSURA, valor)


def quicksort(posicao_inicial, lista):
    if len(lista) <= 1:
        return lista
    else:
        menores = []
        maiores = []
        pivot = lista.pop(len(lista) // 2)
        for valor in lista:
            if valor < pivot:
                menores.append(valor)
            else:
                maiores.append(valor)

        exibe_lista(posicao_inicial, menores + [pivot] + maiores)
        return quicksort(
            posicao_inicial, menores[:]) + \
            [pivot] + \
            quicksort(len(menores) + posicao_inicial + 1, maiores[:])


def indice_menor_valor(lista):
    menor_valor = lista[0]
    indice_menor = 0
    for indice in range(1, len(lista)):
        if lista[indice] < menor_valor:
            menor_valor = lista[indice]
            indice_menor = indice
    return indice_menor


def selectionsort(lista):
    lst_ordenada = []
    for i in range(len(lista)):
        menor = indice_menor_valor(lista)
        valor = lista.pop(menor)
        lst_ordenada.append(valor)

        desenha_linha_no_canvas(screen, i * ESPESSURA, valor)
        time.sleep(0.01)
    return lst_ordenada


def bubblesort(lista):
    trocou = True
    while trocou:
        trocou = False
        for i, vl in enumerate(lista[1:], 1):
            if vl < lista[i-1]:
                trocou = True
                vl_temp = lista[i-1]
                lista[i-1] = vl
                lista[i] = vl_temp
                exibe_lista(i-1, lista[i-1:i+1])
    return lista


def gera_lista_aleatoria():
    lista_aleatoria = []
    for _ in range(LARGURA):
        lista_aleatoria.append(random.randint(1, ALTURA))
    return lista_aleatoria


def criar_canvas():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA * ESPESSURA, ALTURA))
    pygame.display.set_caption(PROG_NOME)
    pygame.display.update()
    return screen


def desenha_linha_no_canvas(screen, posicao_linha, altura_linha):
    posicao_linha += (ESPESSURA // 2)
    pygame.draw.line(screen, (0, 0, 0), (posicao_linha, 0), (posicao_linha, ALTURA), ESPESSURA)
    pygame.draw.line(screen, (250, 250, 250), (posicao_linha, ALTURA - altura_linha), (posicao_linha, ALTURA),
                     ESPESSURA)
    pygame.display.update()


if __name__ == "__main__":
    # Cria tela do PyGame
    screen = criar_canvas()

    lista_aleatoria = gera_lista_aleatoria()
    print(lista_aleatoria)
    pygame.display.set_caption(PROG_NOME + " - Aleatório")
    exibe_lista(0, lista_aleatoria)
    time.sleep(2)

    # Quicksort
    pygame.display.set_caption(PROG_NOME + " - Quick Sort")
    lista_ordenada = quicksort(0, lista_aleatoria[:])
    #print(lista_ordenada)

    time.sleep(2)
    pygame.display.set_caption(PROG_NOME + " - Aleatório")
    exibe_lista(0, lista_aleatoria)
    time.sleep(2)

    # Selection Sort
    pygame.display.set_caption(PROG_NOME + " - Selection Sort")
    lista_ordenada = selectionsort(lista_aleatoria[:])
    #print(lista_ordenada)

    time.sleep(2)
    pygame.display.set_caption(PROG_NOME + " - Aleatório")
    exibe_lista(0, lista_aleatoria)
    time.sleep(2)

    # Bubble Sort
    pygame.display.set_caption(PROG_NOME + " - Bubble Sort")
    lista_ordenada = bubblesort(lista_aleatoria[:])
    #print(lista_ordenada)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
