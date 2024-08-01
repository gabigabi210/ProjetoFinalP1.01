from random import randint
import time
from time import sleep
from time import time
import os
import random
from ranking import atualizar_ranking_crescente, ver_ranking, atualizar_ranking_decrescente, ver_ranking_tentativas
import emoji
from random import choice
import palavras


################JogoDaVelha######################

'''login'''


def menu_login_jogador1():
    ########## login ##########
    nome_do_jogador1 = input('Digite o seu nickname: ').upper().strip()
    print()
    print('Carregando', end='')
    print('.', end='')
    print('.', end='')
    print('.')
    sleep(1)
    os.system('cls')
    return nome_do_jogador1
    ########## login ##########


def menu_login_jogador2():
    ########## login ##########
    nome_do_jogador2 = input('Digite o seu nickname: ').upper().strip()
    print()
    print('Carregando', end='')
    print('.', end='')
    print('.', end='')
    print('.')
    sleep(1)
    os.system('cls')
    return nome_do_jogador2
    ########## login ##########


def menu_inicio_jogo_da_velha():
    try:
        cont = 1
        while cont == 1:
            print(f'X{'O JOGO DA VELHA X':=^80}O')
            print()
            print('           TUTORIAL            JOGAR         RANKING       SAIR PARA O MENU')
            print('             [T]                [J]            [R]               [S]')
            print()
            comecar = input('DIGITE: ').upper().strip()
            if comecar == 'J':
                trava = 0
                while trava == 0:
                    os.system('cls')
                    print(f'X{'O JOGO DA VELHA X':=^80}O')
                    print()
                    opcao = input('Escolha um modo de jogo:\n\nPVP[A]\n\nPVE[B]\n\nDIGITE: ').upper().strip()
                    if opcao == 'A':
                        cont -= 1
                        trava = 1
                        Jogo_da_velha()
                    elif opcao == 'B':
                        cont -= 1
                        trava = 1
                        jogo_da_velha_maquina()
                    else:
                        print('Opção invalida!')
            elif comecar == 'T':
                os.system('cls')
                print('''Este é um jogo da velha comum onde seu objetivo é vencer, completando uma coluna, linha ou diagonal com a figura que lhe representa.

Você pode jogar contra um amigo ou contra o próprio computador.

Você jogará informando uma linha e uma coluna referente à posição que quer jogar.

Vamos jogar?[S/N]
                ''')
                resposta = input('DIGITE: ').upper().strip()
                os.system('cls')
                if resposta == 'N':
                    cont -= 1
                    # voltar para o menu principal
                    print('Saindo...')
                    sleep(2)
            elif comecar == 'S':
                cont -= 1
                os.system('cls')
                print('Saindo...')
                sleep(2)
                menu_todos_os_jogos()
                os.system('cls')
            elif comecar == 'R':
                os.system('cls')
                ver_ranking('Rank Jogo da Velha')
                print()
                voltar = input('Aperte enter para voltar')
                os.system('cls')
            else:
                print('Resposta inválida. Tente novamente!')
    except:
        if not KeyboardInterrupt:
            print('ERROR')
            menu_inicio_jogo_da_velha()


def Jogo_da_velha():
    try:

        tabuleiro = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

        print('Jogador 1')
        print()
        nick_jogador1 = menu_login_jogador1()
        print('Jogador 2')
        print()
        nick_jogador2 = menu_login_jogador2()
        jogada_geral = 0
        jogada_jogador1 = 0
        jogada_jogador2 = 0
        pontos_jogador1 = 0
        pontos_jogador2 = 0
        while ganhou(tabuleiro) == 0:
            os.system('cls')
            print(f'X{'O JOGO DA VELHA X':=^80}O')
            print()
            jogador = jogada_geral % 2 + 1
            print(f'Vez do jogador {jogador}')
            print()
            exibe(tabuleiro)
            print()
            jogada_linha = int(input('Linha: ')) - 1
            inicio = time()
            jogada_coluna = int(input('Coluna: ')) - 1
            if jogador == 1:
                jogada_jogador1 += 1
            elif jogador == 2:
                jogada_jogador2 += 1
            if tabuleiro[jogada_linha][jogada_coluna] == 0:
                if jogador == 1:
                    tabuleiro[jogada_linha][jogada_coluna] = 1
                else:
                    tabuleiro[jogada_linha][jogada_coluna] = -1
            else:
                print('Já foi ocupado!')
                jogada_geral -= 1
            if ganhou(tabuleiro) == 1:
                fim = time()
                tempo_partida = fim - inicio
                if jogador == 1:
                    if jogada_jogador1 <= 3:
                        pontos_jogador1 = 90
                    elif jogada_jogador1 > 3:
                        pontos_jogador1 = 30
                    if tempo_partida < 60:
                        pontos_jogador1 = pontos_jogador1 * 2
                    elif 60 < tempo_partida < 180:
                        pontos_jogador1 = pontos_jogador1 * 1.5
                    elif 180 < tempo_partida < 300:
                        pontos_jogador1 = pontos_jogador1 * 1.25
                    else:
                        pontos_jogador1 = pontos_jogador1
                elif jogador == 2:
                    if jogada_jogador2 <= 3:
                        pontos_jogador2 = 90
                    elif jogada_jogador2 > 3:
                        pontos_jogador2 = 30
                    if tempo_partida < 60:
                        pontos_jogador2 = pontos_jogador2 * 2
                    elif 60 < tempo_partida < 180:
                        pontos_jogador2 = pontos_jogador2 * 1.5
                    elif 180 < tempo_partida < 300:
                        pontos_jogador2 = pontos_jogador2 * 1.25
                    else:
                        pontos_jogador2 = pontos_jogador2
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador1, pontos_jogador1)
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador2, pontos_jogador2)
                exibe(tabuleiro)
                print(f'Parabéns Jogador {jogador}! Você ganhou após {jogada_geral + 1} rodadas.')
                print()
                print('Voltar para o menu?')
                print()
                print('[S]Sim\n\n[N]Não')
                print()
                resposta = input('Digite: ').upper().strip()
                if resposta == 'S':
                    os.system('cls')
                    menu_inicio_jogo_da_velha()
                elif resposta == 'N':
                    os.system('cls')
                    # voltar para o menu geral
                    print('Saindo...')
                    sleep(2)
            elif ganhou(tabuleiro) == 2:
                fim = time()
                pontos_jogador1 = 10
                pontos_jogador2 = 10
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador1, pontos_jogador1)
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador2, pontos_jogador2)
                exibe(tabuleiro)
                print(f'Velha! Ótima partida, pessoal.')
                print()
                print('Voltar para o menu?')
                print()
                print('[S]Sim\n\n[N]Não')
                print()
                resposta = input('Digite: ').upper().strip()
                if resposta == 'S':
                    os.system('cls')
                    menu_inicio_jogo_da_velha()
                elif resposta == 'N':
                    os.system('cls')
                    # voltar para o menu geral
                    print('Saindo...')
                    sleep(2)
            jogada_geral += 1
    except:
        if not KeyboardInterrupt:
            print('Error')
            print('Reiniciando...')
            menu_inicio_jogo_da_velha()


def ganhou(tabuleiro):
    # linhas
    if tabuleiro[0][0] + tabuleiro[0][1] + tabuleiro[0][2] == 3 or tabuleiro[0][0] + tabuleiro[0][1] + tabuleiro[0][
        2] == -3:
        return 1
    if tabuleiro[1][0] + tabuleiro[1][1] + tabuleiro[1][2] == 3 or tabuleiro[1][0] + tabuleiro[1][1] + tabuleiro[1][
        2] == -3:
        return 1
    if tabuleiro[2][0] + tabuleiro[2][1] + tabuleiro[2][2] == 3 or tabuleiro[2][0] + tabuleiro[2][1] + tabuleiro[2][
        2] == -3:
        return 1
    # colunas
    if tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][0] == 3 or tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][
        0] == -3:
        return 1
    if tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][1] == 3 or tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][
        1] == -3:
        return 1
    if tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][2] == 3 or tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][
        2] == -3:
        return 1
    # diagonais
    if tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2] == 3 or tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][
        2] == -3:
        return 1
    if tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0] == 3 or tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][
        0] == -3:
        return 1
    # empate
    cont = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] != 0:
                cont += 1
    if cont == 9:
        return 2

    return 0


def exibe(tabuleiro):
    for i in range(3):
        for j in range(3):
            if j == 0:
                if tabuleiro[i][j] == 0:
                    print('                                  _  ', end=' ')
                elif tabuleiro[i][j] == 1:
                    print('                                  X  ', end=' ')
                elif tabuleiro[i][j] == -1:
                    print('                                  O  ', end=' ')
            else:
                if tabuleiro[i][j] == 0:
                    print('  _  ', end=' ')
                elif tabuleiro[i][j] == 1:
                    print('  X  ', end=' ')
                elif tabuleiro[i][j] == -1:
                    print('  O  ', end=' ')
        print()
        print()


def jogo_da_velha_maquina():
    tabuleiro = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

    try:
        print('Jogador 1')
        print()
        nick_jogador1 = menu_login_jogador1()
        jogada_jogador1 = 0
        pontos_jogador1 = 0
        jogada_geral = 0
        while ganhou(tabuleiro) == 0:
            os.system('cls')
            print(f'X{'O JOGO DA VELHA X':=^80}O')
            print()
            jogador = jogada_geral % 2 + 1
            print(f'Vez do jogador {jogador}')
            exibe(tabuleiro)
            if jogador == 2:
                print('Pensando.', end='')
                sleep(1)
                print('.', end='')
                sleep(1)
                print('.')
                jogada_linha = randint(1, 3) - 1
                jogada_coluna = randint(1, 3) - 1
            else:
                if jogador == 1:
                    jogada_jogador1 += 1
                jogada_linha = int(input('Linha: ')) - 1
                inicio = time()
                jogada_coluna = int(input('Coluna: ')) - 1
            if tabuleiro[jogada_linha][jogada_coluna] == 0:
                if jogador == 1:
                    tabuleiro[jogada_linha][jogada_coluna] = 1
                else:
                    tabuleiro[jogada_linha][jogada_coluna] = -1
            else:
                print('Já foi ocupado!')
                jogada_geral -= 1
            if ganhou(tabuleiro) == 1:
                fim = time()
                tempo_partida = fim - inicio
                if jogador == 1:
                    if jogada_jogador1 <= 3:
                        pontos_jogador1 = 90
                    elif jogada_jogador1 > 3:
                        pontos_jogador1 = 30
                    if tempo_partida < 60:
                        pontos_jogador1 = pontos_jogador1 * 2
                    elif 60 < tempo_partida < 180:
                        pontos_jogador1 = pontos_jogador1 * 1.5
                    elif 180 < tempo_partida < 300:
                        pontos_jogador1 = pontos_jogador1 * 1.25
                    else:
                        pontos_jogador1 = pontos_jogador1
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador1, pontos_jogador1)
                exibe(tabuleiro)
                print(f'Parabéns Jogador {jogador}! Você ganhou após {jogada_geral + 1} rodadas.')
                print()
                print('Voltar para o menu?')
                print()
                print('[S]Sim\n\n[N]Não')
                print()
                resposta = input('Digite: ').upper().strip()
                if resposta == 'S':
                    os.system('cls')
                    menu_inicio_jogo_da_velha()
                elif resposta == 'N':
                    os.system('cls')
                    # voltar para o menu geral
                    print('Saindo...')
                    sleep(2)
            elif ganhou(tabuleiro) == 2:
                fim = time()
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador1, pontos_jogador1)
                pontos_jogador1 = 10
                pontos_jogador2 = 10
                exibe(tabuleiro)
                print(f'Velha! Ótima partida, pessoal.')
                print()
                print('Voltar para o menu?')
                print()
                print('[S]Sim\n\n[N]Não')
                print()
                resposta = input('Digite: ').upper().strip()
                if resposta == 'S':
                    os.system('cls')
                    menu_inicio_jogo_da_velha()
                elif resposta == 'N':
                    os.system('cls')
                    # voltar para o menu geral
                    print('Saindo...')
                    sleep(2)
            jogada_geral += 1
    except:
        if not KeyboardInterrupt:
            print('Error')
            print('Reiniciando...')
            menu_inicio_jogo_da_velha()


################JogoDosCopos######################


def jogo_dos_copos():
    # menu jogo dos copos e o jogo
    print('=' * 70)
    print('Bem Vindo ao Jogo dos Copos!!')
    print('Jogar = 1    Como Jogar = 2    Menu Principal = 3 ')
    print('Sua Escolha:  ', end='')
    resposta_menu = str(input())

    if resposta_menu == '1':
        os.system('cls')
        dificuldades_copos()

    elif resposta_menu == '2':
        os.system('cls')
        como_jogar_copos()
    elif resposta_menu == '3':
        menu_todos_os_jogos()
    else:
        os.system('')
        jogo_dos_copos()


def como_jogar_copos():
    # mostrar como jogar o jogo
    print('=' * 70)
    print('3 Copos:')
    sleep(1)
    print('São 3 copos, que vão ser embaralhados de acordo com as regras')
    sleep(1)
    print('Os movimentos de embaralhamento serão feitos pelo computador')
    sleep(1)
    print('Movimentos:')
    sleep(1)
    print('Movimento = 1 (Troca o Copo A com o Copo B)')
    sleep(1)
    print('Movimento = 2 (Troca o Copo B com o Copo C)')
    sleep(1)
    print('Movimento = 3 (Troca o Copo A com o Copo C)')
    sleep(1)
    print('')
    sleep(1)
    print('VOCÊ PRECISA DECORAR OS MOVIMENTOS!!!')
    print('')
    sleep(1)
    print('Ao final do embaralhamento você precisa escolher o copo que está com a bolinha!')
    sleep(1)
    print('')
    sleep(1)
    print('4 Copos:')
    sleep(1)
    print('São 4 copos, que vão ser embaralhados de acordo com as regras')
    sleep(1)
    print('Os movimentos de embaralhamento serão feitos pelo computador')
    sleep(1)
    print('Movimentos:')
    sleep(1)
    print('Movimento = 1 (Troca o Copo A com o Copo B)')
    sleep(1)
    print('Movimento = 2 (Troca o Copo B com o Copo C)')
    sleep(1)
    print('Movimento = 3 (Troca o Copo A com o Copo C)')
    sleep(1)
    print('Movimento = 4 (Troca o Copo D com o Copo A)')
    sleep(1)
    print('Movimento = 5 (Troca o Copo C com o Copo D)')
    sleep(1)
    print('Movimento = 6 (Troca o Copo D com o Copo B)')
    sleep(1)
    print('')
    sleep(1)
    print('VOCÊ PRECISA DECORAR OS MOVIMENTOS!!!')
    print('')
    sleep(1)
    print('Ao final do embaralhamento você precisa escolher o copo que está com a bolinha!')
    print('')
    print('Entendeu?')
    print('Voltar para o Menu = 1    Ler denovo = 2')
    print('Sua resposta:  ', end='')
    resposta_como_jogar = str(input())
    if resposta_como_jogar == '1':
        os.system('cls')
        jogo_dos_copos()
    else:
        os.system('cls')
        jogo_dos_copos()


def dificuldades_copos():
    # mostra as dificuldades e dificuldades funcionando
    print('=' * 70)
    print('Escolha a dificuldade:')
    print('')
    print('Jogar com 3 Copos = 1')
    print('Jogar com 4 Copos = 2')
    print('')
    print('Dificuldade:  ', end='')
    dificuldade = str(input())
    os.system('cls')

    if dificuldade == '1':
        os.system('cls')
        print('Quantas vezes você quer girar o copo? (1 - 20 vezes)')
        print('Sua resposta:  ', end='')
        numero_de_movimentos = int(input())
        if numero_de_movimentos in range(0, 20):
            os.system('cls')
            print('Em qual copo a bolinha vai iniciar? (A,B ou C)')
            print('Sua Resposta:  ', end='')
            posicao_inicial = str(input()).strip().upper()
            if posicao_inicial == 'A' or posicao_inicial == 'B' or posicao_inicial == 'C':
                posicao = posicao_inicial
                os.system('cls')

                # pegar o numero de movimentos e fazer a máquina fazer os movimentos
                for i in range(numero_de_movimentos):
                    print('...')
                    sleep(1)
                    movimento = random.randint(1, 3)
                    print(f'Movimento: {movimento}')
                    sleep(1)

                    # posição da moeda
                    if posicao == 'A' or posicao_inicial == 'a':
                        if movimento == 1:
                            moeda = 'B'
                            posicao = moeda
                        elif movimento == 2:
                            moeda = 'A'
                            posicao = moeda
                        elif movimento == 3:
                            moeda = 'C'
                            posicao = moeda

                    elif posicao == 'B' or posicao_inicial == 'b':
                        if movimento == 1:
                            moeda = 'A'
                            posicao = moeda
                        elif movimento == 2:
                            moeda = 'C'
                            posicao = moeda
                        elif movimento == 3:
                            moeda = 'B'
                            posicao = moeda

                    elif posicao == 'C' or posicao_inicial == 'c':
                        if movimento == 1:
                            moeda = 'C'
                            posicao = moeda
                        elif movimento == 2:
                            moeda = 'B'
                            posicao = moeda
                        elif movimento == 3:
                            moeda = 'A'
                            posicao = moeda
                print('...')
                print('')
                print('Em qual copo a bolinha esta?')
                resposta_bolinha = str(input())

                if resposta_bolinha == posicao:
                    print('')
                    print(f'Você acertou!! A bolinha enta na posição {posicao}')
                    print('')
                    print('Jogar novamente = 1    Voltar para o Menu = 2')
                    resposta_menu = str(input())
                    if resposta_menu == '1':
                        os.system('cls')
                        dificuldades_copos()
                    else:
                        os.system('cls')
                        jogo_dos_copos()

                else:
                    print('')
                    print(f'Voce errou!! A bolinha na verdade esta na posição {posicao}')
                    print('')
                    print('Jogar novamente = 1    Voltar para o Menu = 2')
                    resposta_menu = str(input())
                    if resposta_menu == '1':
                        os.system('cls')
                        dificuldades_copos()
                    else:
                        os.system('cls')
                        jogo_dos_copos()
            else:
                os.system('cls')
                dificuldades_copos()
        else:
            os.system('cls')
            dificuldades_copos()

    elif dificuldade == '2':
        os.system('cls')
        print('Quantas vezes você quer girar o copo? (1 - 20 vezes)')
        print('Sua resposta:  ', end='')
        numero_de_movimentos = int(input())
        if numero_de_movimentos in range(0, 20):
            os.system('cls')
            print('Em qual copo a bolinha vai iniciar? (A,B,C ou D)')
            print('Sua Resposta:  ', end='')
            posicao_inicial = str(input()).strip().upper()
            if (posicao_inicial == 'A' or posicao_inicial == 'B' or posicao_inicial == 'C'
                    or posicao_inicial == 'D'):
                posicao = posicao_inicial
                os.system('cls')

                for i in range(numero_de_movimentos):
                    print('...')
                    sleep(1)
                    movimento = random.randint(1, 6)
                    print(f'Movimento: {movimento}')
                    sleep(1)

                    if posicao == 'A' or posicao_inicial == 'a':
                        if movimento == 1:
                            moeda = 'B'
                            posicao = moeda
                        elif movimento == 2:
                            moeda = 'A'
                            posicao = moeda
                        elif movimento == 3:
                            moeda = 'C'
                            posicao = moeda
                        elif movimento == 4:
                            moeda = 'D'
                            posicao = moeda
                        elif movimento == 5:
                            moeda = 'A'
                            posicao = moeda
                        elif movimento == 6:
                            moeda = 'A'
                            posicao = moeda

                    elif posicao == 'B' or posicao_inicial == 'b':
                        if movimento == 1:
                            moeda = 'A'
                            posicao = moeda
                        elif movimento == 2:
                            moeda = 'C'
                            posicao = moeda
                        elif movimento == 3:
                            moeda = 'B'
                            posicao = moeda
                        elif movimento == 4:
                            moeda = 'B'
                            posicao = moeda
                        elif movimento == 5:
                            moeda = 'B'
                            posicao = moeda
                        elif movimento == 6:
                            moeda = 'D'
                            posicao = moeda

                    elif posicao == 'C' or posicao_inicial == 'c':
                        if movimento == 1:
                            moeda = 'C'
                            posicao = moeda
                        elif movimento == 2:
                            moeda = 'B'
                            posicao = moeda
                        elif movimento == 3:
                            moeda = 'A'
                            posicao = moeda
                        elif movimento == 4:
                            moeda = 'C'
                            posicao = moeda
                        elif movimento == 5:
                            moeda = 'D'
                            posicao = moeda
                        elif movimento == 6:
                            moeda = 'C'
                            posicao = moeda

                    elif posicao == 'D' or posicao_inicial == 'd':
                        if movimento == 1:
                            moeda = 'D'
                            posicao = moeda
                        elif movimento == 2:
                            moeda = 'D'
                            posicao = moeda
                        elif movimento == 3:
                            moeda = 'D'
                            posicao = moeda
                        elif movimento == 4:
                            moeda = 'A'
                            posicao = moeda
                        elif movimento == 5:
                            moeda = 'C'
                            posicao = moeda
                        elif movimento == 6:
                            moeda = 'B'
                            posicao = moeda
                print('...')
                print('')
                print('Em qual copo a bolinha esta?')
                resposta_bolinha = str(input())

                if resposta_bolinha == posicao:
                    print('')
                    print(f'Você acertou!! A bolinha enta na posição {posicao}')
                    print('')
                    print('Jogar novamente = 1    Voltar para o Menu = 2')
                    resposta_menu = str(input())
                    if resposta_menu == '1':
                        os.system('cls')
                        dificuldades_copos()
                    else:
                        os.system('cls')
                        jogo_dos_copos()

                else:
                    print('')
                    print(f'Voce errou!! A bolinha na verdade esta na posição {posicao}')
                    print('')
                    print('Jogar novamente = 1    Voltar para o Menu = 2')
                    resposta_menu = str(input())
                    if resposta_menu == '1':
                        os.system('cls')
                        dificuldades_copos()
                    else:
                        os.system('cls')
                        jogo_dos_copos()
            else:
                os.system('cls')
                dificuldades_copos()
        else:
            os.system('cls')
            dificuldades_copos()
    else:
        dificuldades_copos()


############JogoDeMemoria################


def jogo_de_memoria():
    # mostra o menu e o menu funcionando
    print('=' * 70)
    print('Bem Vindo ao Jogo da Mémoria Rápida!')
    print('')
    print('Jogar = 1    Como Jogar = 2    Menu Principal = 3    Rankings = 4'.rjust(20))
    print('Sua Escolha:  ', end='')
    resposta = str(input())

    if resposta == '1':
        os.system('cls')
        dificuldades()
    elif resposta == '2':
        os.system('cls')
        como_jogar()
    elif resposta == '3':
        os.system('cls')
        menu_todos_os_jogos()
    elif resposta == '4':
        os.system('cls')
        rankings()
    else:
        os.system('cls')
        jogo_de_memoria()


def dificuldades():
    # mostra a dificulade e as dificuldades funcioandno
    print('=' * 70)
    print('Escolha a dificuldade:\n1 = Fácil: 15 segundos para memorizar / n rodadas')
    print('2 = Normal: 10 segundos para memorizar / n rodadas')
    print('3 = Difícil: 5 segundos para memorizar / n rodadas')
    print('Dificuldade:  ', end='')
    dificuldade = str(input())
    os.system('cls')

    if dificuldade == '1':

        lista_palavras_cores = ['Amarelo', 'Rosa', 'Verde', 'Preto', 'Vermelho', 'Roxo', 'Azul',
                                'Laranja', 'Cinza', 'Branco']
        lista_palavras_animais = ['Gato', 'Cachorro', 'Guaxinim', 'Cobra', 'Baleia', 'Peixe', 'Lobo',
                                  'Arara', 'Esquilo', 'Tartaruga']
        lista_vazia_final_cores = []
        lista_vazia_final_animais = []

        print('Quantas rodadas você quer jogar? (3 - 10)')
        print('Rodadas:  ', end='')
        rodadas_pergunta = int(input())
        os.system('cls')

        # pega o numero de rodadas e sorteia as palavras da lista e adiciona em uma lista final
        # retirar a palavra da lista original para elas n serem sorteadas de novo
        if rodadas_pergunta in range(3, 11):
            for i in range(0, rodadas_pergunta):
                sorteado_1 = random.choice(lista_palavras_cores)
                lista_palavras_cores.remove(sorteado_1)
                lista_vazia_final_cores.append(sorteado_1)

                sorteado_2 = random.choice(lista_palavras_animais)
                lista_palavras_animais.remove(sorteado_2)
                lista_vazia_final_animais.append(sorteado_2)

                print(f'{sorteado_1.ljust(10)}- {sorteado_2.rjust(10)}')

            print('')
            print('O jogo começará em 15 segundos! Memorize!')
            sleep(12)
            print('3...')
            sleep(1)
            print('2...')
            sleep(1)
            print('1...')
            os.system('cls')
            print('Vamos lá!!!!')
            print('')
            tempo_inicio_jogo = time()

            # numero de rodadas de acordo com  a escolha
            for p in range(0, rodadas_pergunta):
                print(f'{lista_vazia_final_cores[p]}')
                print('Sua Resposta:  ', end='')
                resposta_0 = str(input())
                print('')
                # resposta certa = continuar
                if resposta_0 == lista_vazia_final_animais[p]:
                    print('...')
                    print('')
                    # resposta dinal = certa
                    if resposta_0 == lista_vazia_final_animais[rodadas_pergunta - 1]:
                        tempo_termino_jogo = time()
                        tempo_total = abs(tempo_termino_jogo - tempo_inicio_jogo)
                        print('Você Venceu! Parabéns')
                        print(f'Você terminou a dificuldade fácil em {tempo_total:.1f} segundos!')
                        print('Qual o seu nome?')
                        nome_jogador = str(input())
                        atualizar_ranking_decrescente('ranking_facil', nome_jogador, tempo_total)
                        print('Jogar Novamente = 1   Voltar para o Menu = Presione qualquer tecla')
                        resposta_jogo = str(input())
                        if resposta_jogo == '1':
                            os.system('cls')
                            dificuldades()
                            break
                        else:
                            os.system('cls')
                            jogo_de_memoria()
                            break
                else:
                    print(f'Você Errou! A resposta correta era: {lista_vazia_final_animais[p]} ')
                    print('Tentar Novamente = 1   Voltar para o Menu = Presione qualquer tecla')
                    resposta_jogo = str(input())
                    if resposta_jogo == '1':
                        os.system('cls')
                        dificuldades()
                    else:
                        os.system('cls')
                        jogo_de_memoria()
                        break
        else:
            os.system('cls')
            dificuldades()

    elif dificuldade == '2':

        lista_palavras_cores = ['Amarelo', 'Rosa', 'Verde', 'Preto', 'Vermelho', 'Roxo', 'Azul',
                                'Laranja', 'Cinza', 'Branco']
        lista_palavras_animais = ['Gato', 'Cachorro', 'Guaxinim', 'Cobra', 'Baleia', 'Peixe', 'Lobo',
                                  'Arara', 'Esquilo', 'Tartaruga']
        lista_vazia_final_cores = []
        lista_vazia_final_animais = []

        print('Quantas rodadas você quer jogar? (3 - 10)')
        print('Rodadas:  ', end='')
        rodadas_pergunta = int(input())
        os.system('cls')

        if rodadas_pergunta in range(3, 11):
            for i in range(0, rodadas_pergunta):
                sorteado_1 = random.choice(lista_palavras_cores)
                lista_palavras_cores.remove(sorteado_1)
                lista_vazia_final_cores.append(sorteado_1)

                sorteado_2 = random.choice(lista_palavras_animais)
                lista_palavras_animais.remove(sorteado_2)
                lista_vazia_final_animais.append(sorteado_2)

                print(f'{sorteado_1.ljust(10)}- {sorteado_2.rjust(10)}')

            print('')
            print('O jogo começará em 10 segundos! Memorize!')
            sleep(9)
            print('3...')
            sleep(1)
            print('2...')
            sleep(1)
            print('1...')
            os.system('cls')
            print('Vamos lá!!!!')
            print('')
            tempo_inicio_jogo = time()
            for p in range(0, rodadas_pergunta):
                print(f'{lista_vazia_final_cores[p]}')
                print('Sua Resposta:  ', end='')
                resposta_0 = str(input())
                print('')
                if resposta_0 == lista_vazia_final_animais[p]:
                    print('...')
                    print('')
                    if resposta_0 == lista_vazia_final_animais[rodadas_pergunta - 1]:
                        tempo_termino_jogo = time()
                        tempo_total = abs(tempo_termino_jogo - tempo_inicio_jogo)
                        print('Você Venceu! Parabéns')
                        print(f'Você terminou a dificuldade fácil em {tempo_total:.1f} segundos!')
                        print('Qual o seu nome?')
                        nome_jogador = str(input())
                        atualizar_ranking_decrescente('ranking_normal', nome_jogador, tempo_total)
                        print('Jogar Novamente = 1   Voltar para o Menu = Presione qualquer tecla')
                        resposta_jogo = str(input())
                        if resposta_jogo == '1':
                            os.system('cls')
                            dificuldades()
                        else:
                            os.system('cls')
                            jogo_de_memoria()
                else:
                    print(f'Você Errou! A resposta correta era: {lista_vazia_final_animais[p]} ')
                    print('Tentar Novamente = 1   Voltar para o Menu = Presione qualquer tecla')
                    resposta_jogo = str(input())
                    if resposta_jogo == '1':
                        os.system('cls')
                        dificuldades()
                    else:
                        os.system('cls')
                        jogo_de_memoria()
        else:
            os.system('cls')
            dificuldades()

    elif dificuldade == '3':

        lista_palavras_cores = ['Amarelo', 'Rosa', 'Verde', 'Preto', 'Vermelho', 'Roxo', 'Azul',
                                'Laranja', 'Cinza', 'Branco']
        lista_palavras_animais = ['Gato', 'Cachorro', 'Guaxinim', 'Cobra', 'Baleia', 'Peixe', 'Lobo',
                                  'Arara', 'Esquilo', 'Tartaruga']
        lista_vazia_final_cores = []
        lista_vazia_final_animais = []

        print('Quantas rodadas você quer jogar? (3 - 10)')
        print('Rodadas:  ', end='')
        rodadas_pergunta = int(input())

        if rodadas_pergunta in range(3, 11):
            for i in range(0, rodadas_pergunta):
                sorteado_1 = random.choice(lista_palavras_cores)
                lista_palavras_cores.remove(sorteado_1)
                lista_vazia_final_cores.append(sorteado_1)

                sorteado_2 = random.choice(lista_palavras_animais)
                lista_palavras_animais.remove(sorteado_2)
                lista_vazia_final_animais.append(sorteado_2)

                print(f'{sorteado_1.ljust(10)}- {sorteado_2.rjust(10)}')

            print('')
            print('O jogo começará em 5 segundos! Memorize!')
            sleep(4)
            print('3...')
            sleep(1)
            print('2...')
            sleep(1)
            print('1...')
            os.system('cls')
            print('Vamos lá!!!!')
            print('')
            tempo_inicio_jogo = time()

            for p in range(0, rodadas_pergunta):
                print(f'{lista_vazia_final_cores[p]}')
                print('Sua Resposta:  ', end='')
                resposta_0 = str(input())
                print('')
                if resposta_0 == lista_vazia_final_animais[p]:
                    print('...')
                    print('')
                    if resposta_0 == lista_vazia_final_animais[rodadas_pergunta - 1]:
                        tempo_termino_jogo = time()
                        tempo_total = abs(tempo_termino_jogo - tempo_inicio_jogo)
                        print('Você Venceu! Parabéns')
                        print(f'Você terminou a dificuldade fácil em {tempo_total:.1f} segundos!')
                        print('Qual o seu nome?')
                        nome_jogador = str(input())
                        atualizar_ranking_decrescente('ranking_dificil', nome_jogador, tempo_total)
                        print('Jogar Novamente = 1   Voltar para o Menu = Presione qualquer tecla')
                        resposta_jogo = str(input())
                        if resposta_jogo == '1':
                            os.system('cls')
                            dificuldades()
                        else:
                            os.system('cls')
                            jogo_de_memoria()
                else:
                    print(f'Você Errou! A resposta correta era: {lista_vazia_final_animais[p]} ')
                    print('Tentar Novamente = 1   Voltar para o Menu = Presione qualquer tecla')
                    resposta_jogo = str(input())
                    if resposta_jogo == '1':
                        os.system('cls')
                        dificuldades()
                    else:
                        os.system('cls')
                        jogo_de_memoria()
        else:
            os.system('cls')
            dificuldades()


def como_jogar():
    # mostra como jogar
    print('=' * 70)
    print('Como jogar:')
    sleep(1)
    print(f'Quando o jogo começar aparecerá na tela 4 palavras contendo nome de Cores')
    print(f'Relacinadas a outras 4 palavras contendo nome de Animais ')
    sleep(2)
    print(f'Você terá um tempo de x segundos para memorizar todas as relações de palavras')
    sleep(3)
    print('Após o tempo determinado o jogo começará e então o computador irá falar uma das palavras mostradas')
    print('E você terá que falar a palavra relacionada a ela')
    sleep(3)
    print('O jogo termina quando você arcetar todas as rodadas')
    print('')
    print('Entendeu?')
    print('1 = Sim, Começar a jogar     2 = Não, Mostrar De novo    Menu principal =  Pressione qualquer tecla')
    resposta_como_jogar = str(input())
    if resposta_como_jogar == '1':
        os.system('cls')
        dificuldades()
    elif resposta_como_jogar == '2':
        os.system('cls')
        como_jogar()
    else:
        os.system('cls')
        menu_todos_os_jogos()


def rankings():
    print('=' * 70)
    print('Qual ranking você deseja ver?')
    print('F = Fácil    N = Normal    D = Difícil')
    print('Sua escolha:  ', end='')
    escolha_ranking = str(input()).strip().upper()
    if escolha_ranking == 'F':
        ver_ranking('ranking_facil')
        print('')
        print('Voltar para o menu =  1    Ranking = 2')
        print('Sua resposta:  ', end='')
        pergunta_ranking = str(input())
        if pergunta_ranking == '1':
            os.system('cls')
            jogo_de_memoria()
        else:
            os.system('cls')
            rankings()
    elif escolha_ranking == 'N':
        ver_ranking('ranking_normal')
        print('')
        print('Voltar para o menu =  1    Ranking = 2')
        print('Sua resposta:  ', end='')
        pergunta_ranking = str(input())
        if pergunta_ranking == '1':
            os.system('cls')
            jogo_de_memoria()
        else:
            os.system('cls')
            rankings()
    elif escolha_ranking == 'D':
        ver_ranking('ranking_dificil')
        print('')
        print('Voltar para o menu =  1    Ranking = 2')
        print('Sua resposta:  ', end='')
        pergunta_ranking = str(input())
        if pergunta_ranking == '1':
            os.system('cls')
            jogo_de_memoria()
        else:
            os.system('cls')
            rankings()

    else:
        os.system('cls')
        rankings()

#####################MomentoCerto###########


pontuacao_momento = 0


def mostrar_instrucoes():
    print('''Como jogar:
    1. Quando o jogo começar, você será instruído a cronometrar um período específico de tempo.
    2. O objetivo é parar o cronômetro o mais próximo possível do tempo indicado.
    3. Você ganhará pontos com base na precisão do seu tempo:
       - Você começará com 10 pontos.
       - A cada décimo de segundo que você se desviar do tempo indicado, você perderá 0.1 pontos.
    4. Após parar o cronômetro, o jogo mostrará o tempo que você cronometrou e a sua pontuação.
    5. Você pode jogar várias vezes e seu total de pontos será atualizado.
    6. No final, seu nome e pontuação serão registrados no ranking.
    7. Escolha a opção "Ranking" para ver a classificação dos jogadores.
    ''')

def momento_perfeito(vez=0):
    lretorno = [True]
    # sistema de pontuação de acordo com o quão perto do tempo certo a pessoa acertou
    pontos_usuario = 0
    ja_falou_nome = False

    opcao = int(input('''[1] Play       [2] Como jogar?       [3] Ranking       [4] Sair
    Qual opcao desejada: '''))
    lretorno.append(opcao)

    # parte principal do jogo
    if opcao == 1:
        if vez == 0:
            lretorno.append(input('Qual o seu nome? '))
            ja_falou_nome = True
        else:
            lretorno.append(False)


        # escolhe de forma aleatória o tempo que o jogador deve acertar
        n = random.randint(300, 1300)/100
        print(f'Você deve cronometrar {n:.1f} segundos, boa sorte!')
        # inicia o cronômetro
        input('Pressione ENTER quando estiver pronto para começar')
        inicio = time()
        # para o cronômetro
        input('Pressione ENTER quando quiser parar o cronômetro')
        final = time()
        tempo_total = final - inicio
        diferenca = abs(tempo_total - n)
        print(f'{tempo_total:.1f} segundos')
        # utiliza a variável diferença para descobrir a pontuação do jogador
        if 10 - diferenca > 0:
            pontos_usuario += 10 - diferenca
        else:
            pontos_usuario = 0
        print(f'{pontos_usuario:.1f} pontos')
        lretorno.append(pontos_usuario)
        lretorno.append(ja_falou_nome)
    elif opcao == 2:
        mostrar_instrucoes()
    elif opcao == 3:
        ver_ranking('momento_ranking')
    elif opcao == 4:
        lretorno[0] = False
    return lretorno



############CampoMinado############

# bomba = -1
# lugar sem nada = 0
# 100 passa a representar 0 apos o jogador o encontrar
# -10 passa a representar bomba apos o jogador encontrar
# os outros serão multiplicados por 200 para diferenciar
# número de bombas aleatório//a medida que a dificuldade aumenta é randomizada entre menos números

'''login'''


def menu_login():
    ########## login ##########
    print('o' + '~' * 81 + 'o')
    print(
        f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
    print('o' + '~' * 81 + 'o')
    print()
    nome_do_jogador = input('Digite o seu nickname: ').upper().strip()
    print()
    print('Carregando', end='')
    print('.', end='')
    print('.', end='')
    print('.')
    sleep(2)
    os.system('cls')
    return nome_do_jogador
    ########## login ##########


'''TABULEIRO FÁCIL'''

tabuleiro_facil = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]]


# função que desenvolve o tabuleiro
def corpo_do_jogo_facil():
    tabuleiro_aleatorio_facil = [[0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0]]

    # aleatoriza as bombas do tabuleiro fácil
    for linha in range(0, 8):
        for quant in range(1):
            coluna = randint(0, 7)
            tabuleiro_aleatorio_facil[linha][coluna] = -1

    # transfere para o tabuleiro final fácil
    for linha in range(0, 8):
        for coluna in range(0, 8):
            if tabuleiro_aleatorio_facil[linha][coluna] == 0:
                tabuleiro_facil[linha][coluna] = 0
            elif tabuleiro_aleatorio_facil[linha][coluna] == -1:
                tabuleiro_facil[linha][coluna] = -1

    # posiciona as dicas do tabuleiro fácil
    for linha in range(0, 8):
        for coluna in range(len(tabuleiro_facil)):
            # teste de bombas
            soma = 0
            # linha de cima
            if linha == 0:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_facil[linha][coluna + 1] + tabuleiro_aleatorio_facil[linha + 1][
                        coluna] + \
                           tabuleiro_aleatorio_facil[linha + 1][coluna + 1]
                elif coluna == 7:
                    soma = tabuleiro_aleatorio_facil[linha][coluna - 1] + tabuleiro_aleatorio_facil[linha + 1][
                        coluna] + \
                           tabuleiro_aleatorio_facil[linha + 1][coluna - 1]
                elif 0 < coluna < 7:
                    soma = tabuleiro_aleatorio_facil[linha][coluna - 1] + tabuleiro_aleatorio_facil[linha + 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_facil[linha + 1][coluna] + \
                           tabuleiro_aleatorio_facil[linha + 1][coluna + 1] + tabuleiro_aleatorio_facil[linha][
                               coluna + 1]
            # linha de baixo
            elif linha == 7:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_facil[linha][coluna + 1] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna + 1] + \
                           tabuleiro_aleatorio_facil[linha - 1][coluna]
                elif coluna == 7:
                    soma = tabuleiro_aleatorio_facil[linha][coluna - 1] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_facil[linha - 1][coluna]
                elif 0 < coluna < 7:
                    soma = tabuleiro_aleatorio_facil[linha][coluna - 1] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_facil[linha - 1][coluna] + \
                           tabuleiro_aleatorio_facil[linha - 1][coluna + 1] + tabuleiro_aleatorio_facil[linha][
                               coluna + 1]
            # linhas do meio
            elif 0 < linha < 7:
                # coluna da esquerda
                if coluna == 0:
                    soma = tabuleiro_aleatorio_facil[linha - 1][coluna] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna + 1] + \
                           tabuleiro_aleatorio_facil[linha][coluna + 1] + \
                           tabuleiro_aleatorio_facil[linha + 1][coluna + 1] + tabuleiro_aleatorio_facil[linha + 1][
                               coluna]
                # coluna da direita
                elif coluna == 7:
                    soma = tabuleiro_aleatorio_facil[linha - 1][coluna] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_facil[linha][coluna - 1] + \
                           tabuleiro_aleatorio_facil[linha + 1][coluna - 1] + tabuleiro_aleatorio_facil[linha + 1][
                               coluna]
                # meio do tabuleiro
                else:
                    soma = tabuleiro_aleatorio_facil[linha - 1][coluna] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_facil[linha][coluna - 1] + \
                           tabuleiro_aleatorio_facil[linha + 1][coluna - 1] + tabuleiro_aleatorio_facil[linha + 1][
                               coluna] + \
                           tabuleiro_aleatorio_facil[linha + 1][coluna + 1] + \
                           tabuleiro_aleatorio_facil[linha][coluna + 1] + tabuleiro_aleatorio_facil[linha - 1][
                               coluna + 1]
            # quantidade de bombas
            if soma != 0 and tabuleiro_aleatorio_facil[linha][coluna] != -1:
                if soma == -1:
                    tabuleiro_facil[linha][coluna] = 1
                elif soma == -2:
                    tabuleiro_facil[linha][coluna] = 2
                elif soma == -3:
                    tabuleiro_facil[linha][coluna] = 3
                elif soma == -4:
                    tabuleiro_facil[linha][coluna] = 4
                elif soma == -5:
                    tabuleiro_facil[linha][coluna] = 5
                elif soma == -6:
                    tabuleiro_facil[linha][coluna] = 6
                elif soma == -7:
                    tabuleiro_facil[linha][coluna] = 7
                elif soma == -8:
                    tabuleiro_facil[linha][coluna] = 8


def exibe_tabuleiro_facil():
    for linha in range(0, 8):
        for coluna in range(0, 8):
            if linha == 0 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 1\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] == -10:
                    print(f'\033[0;31; m                 1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 1\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ',
                          end='')
                else:
                    print(f'\033[0;31; m                 1\033[m    -  ', end='')
            elif linha == 7 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 8\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] == -10:
                    print(f'\033[0;31; m                 8\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 8\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ',
                          end='')
                else:
                    print(f'\033[0;31; m                 8\033[m    -  ', end='')
            elif 0 < linha < 7 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] == -10:
                    print(f'\033[0;31; m                 {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(
                        f'\033[0;31; m                 {linha + 1}\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ',
                        end='')
                else:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_facil[linha][coluna] == -10:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'  {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def mostra_bomba_fim_facil():
    for linha in range(0, 8):
        for coluna in range(0, 8):
            if linha == 0 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 1\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] < 0:
                    print(f'\033[0;31; m                 1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 1\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ',
                          end='')
                else:
                    print(f'\033[0;31; m                 1\033[m    -  ', end='')
            elif linha == 7 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 8\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] < 0:
                    print(f'\033[0;31; m                 8\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 8\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ',
                          end='')
                else:
                    print(f'\033[0;31; m                 8\033[m    -  ', end='')
            elif 0 < linha < 7 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] < 0:
                    print(f'\033[0;31; m                 {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(
                        f'\033[0;31; m                 {linha + 1}\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ',
                        end='')
                else:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_facil[linha][coluna] < 0:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'  {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def jogo_facil_campo_minado():
    try:
        nick = menu_login()
        corpo_do_jogo_facil()
        game_over = 0
        tempo_inicial = time()
        while game_over == 0:
            os.system('cls')
            print('o' + '~' * 81 + 'o')
            print(
                f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
            print('o' + '~' * 81 + 'o')
            print()
            print()
            print('                     \033[0;31; m 1    2    3    4    5    6    7    8\033[m')
            print()
            exibe_tabuleiro_facil()
            linha = int(input('Linha: ')) - 1
            coluna = int(input('Coluna: ')) - 1
            # revela zeros próximos
            if linha == 0:
                if coluna == 0:
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                    if tabuleiro_facil[linha + 1][coluna + 1] == 0:
                        tabuleiro_facil[linha + 1][coluna + 1] = 100
                elif coluna == 7:
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                    if tabuleiro_facil[linha + 1][coluna - 1]:
                        tabuleiro_facil[linha + 1][coluna - 1] = 100
                elif 0 < coluna < 7:
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna - 1] == 0:
                        tabuleiro_facil[linha + 1][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                    if tabuleiro_facil[linha + 1][coluna + 1] == 0:
                        tabuleiro_facil[linha + 1][coluna + 1] = 100
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                # linha de baixo
            elif linha == 8:
                if coluna == 0:
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                    if tabuleiro_facil[linha - 1][coluna + 1] == 0:
                        tabuleiro_facil[linha - 1][coluna + 1] = 100
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100

                elif coluna == 7:
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha - 1][coluna - 1] == 0:
                        tabuleiro_facil[linha - 1][coluna - 1] = 100
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                elif 0 < coluna < 7:
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha - 1][coluna - 1] == 0:
                        tabuleiro_facil[linha - 1][coluna - 1] = 100
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                    if tabuleiro_facil[linha - 1][coluna + 1] == 0:
                        tabuleiro_facil[linha - 1][coluna + 1] = 100
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                # linhas do meio
            elif 0 < linha < 7:
                # coluna da esquerda
                if coluna == 0:
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                    if tabuleiro_facil[linha - 1][coluna + 1] == 0:
                        tabuleiro_facil[linha - 1][coluna + 1] = 100
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                    if tabuleiro_facil[linha + 1][coluna + 1] == 0:
                        tabuleiro_facil[linha + 1][coluna + 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                # coluna da direita
                elif coluna == 7:
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                    if tabuleiro_facil[linha - 1][coluna - 1] == 0:
                        tabuleiro_facil[linha - 1][coluna - 1] = 100
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna - 1] == 0:
                        tabuleiro_facil[linha + 1][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                # meio do tabuleiro
                else:
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                    if tabuleiro_facil[linha - 1][coluna - 1] == 0:
                        tabuleiro_facil[linha - 1][coluna - 1] = 100
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna - 1] == 0:
                        tabuleiro_facil[linha + 1][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                    if tabuleiro_facil[linha + 1][coluna + 1] == 0:
                        tabuleiro_facil[linha + 1][coluna + 1] = 100
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                    if tabuleiro_facil[linha - 1][coluna + 1] == 0:
                        tabuleiro_facil[linha - 1][coluna + 1] = 100
            if -2 < tabuleiro_facil[linha][coluna] < 10:
                if tabuleiro_facil[linha][coluna] == 0:
                    tabuleiro_facil[linha][coluna] = 100
                elif tabuleiro_facil[linha][coluna] == -1:
                    tabuleiro_facil[linha][coluna] = -10
                else:
                    tabuleiro_facil[linha][coluna] *= 200
            else:
                print(f'Você já jogou nessa posição.\nTente novamente!')
            teste_gameover_facil()
            if teste_gameover_facil() == 1:
                game_over = 1
            elif teste_gameover_facil() == 2:
                game_over = 2
        os.system('cls')
        print('o' + '~' * 81 + 'o')
        print(
            f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
        print('o' + '~' * 81 + 'o')
        print()
        print()
        print('                     \033[0;31; m 1    2    3    4    5    6    7    8\033[m')
        print()
        mostra_bomba_fim_facil()
        tempo_final = time()
        tempo_de_partida_facil = tempo_final - tempo_inicial
        print()
        print(f'TEMPO DE PARTIDA: {tempo_de_partida_facil:.2f}s')
        print()
        pontos_partida_facil = 0
        if game_over == 1:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_chorando:', language='pt')}Você perdeu!{emoji.emojize(':rosto_chorando:', language='pt')}')
        elif game_over == 2:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}Você Ganhou!{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}')
            pontos_partida_facil = 25
        print()
        # sistema de pontuação
        if tempo_de_partida_facil < 60:
            pontos_totais_facil = pontos_partida_facil * 2
        elif 60 < tempo_de_partida_facil < 180:
            pontos_totais_facil = pontos_partida_facil * 1.5
        elif 180 < tempo_de_partida_facil < 300:
            pontos_totais_facil = pontos_partida_facil * 1.25
        else:
            pontos_totais_facil = pontos_partida_facil
        # atualiza o rank
        atualizar_ranking_crescente('Rank_campo_minado', nome=nick, pontuacao=pontos_totais_facil)
        ########################################
        print('Voltar para o menu?')
        print()
        sim_nao = input('[S]Sim\n\n[N]Não\n\nDigite: ').upper()
        if sim_nao == 'S':
            os.system('cls')
            menu_campo_minado()
        else:
            print('Saindo...')
            print()
            sleep(3)
        ###################################3####
    except:
        if not KeyboardInterrupt:
            print('Error')
            os.system('cls')
            menu_campo_minado()


def teste_gameover_facil():
    quant_bombs = 0
    quant_jogadas = 0
    for linha in range(0, 8):
        for coluna in range(0, 8):
            if tabuleiro_facil[linha][coluna] == -1:
                quant_bombs += 1
            if tabuleiro_facil[linha][coluna] == -10:
                return 1
            if tabuleiro_facil[linha][coluna] >= 200 or tabuleiro_facil[linha][coluna] == 100:
                quant_jogadas += 1
    lugares_disponiveis = 64 - quant_bombs
    if lugares_disponiveis == quant_jogadas:
        return 2


'''TABULEIRO MÉDIO'''

tabuleiro_medio = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def corpo_do_jogo_medio():
    tabuleiro_aleatorio_medio = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # aleatoriza as bombas do tabuleiro medio
    for linha in range(0, 9):
        for quant in range(2):
            coluna = randint(0, 8)
            tabuleiro_aleatorio_medio[linha][coluna] = -1

    # transfere as bombas para o tabuleiro final facil
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if tabuleiro_aleatorio_medio[linha][coluna] == 0:
                tabuleiro_medio[linha][coluna] = 0
            elif tabuleiro_aleatorio_medio[linha][coluna] == -1:
                tabuleiro_medio[linha][coluna] = -1

    # posiciona as dicas do tabuleiro facil
    for linha in range(0, 9):
        for coluna in range(len(tabuleiro_medio)):
            # teste de bombas
            soma = 0
            # linha de cima
            if linha == 0:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_medio[linha][coluna + 1] + tabuleiro_aleatorio_medio[linha + 1][coluna] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna + 1]
                elif coluna == 8:
                    soma = tabuleiro_aleatorio_medio[linha][coluna - 1] + tabuleiro_aleatorio_medio[linha + 1][coluna] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna - 1]
                elif 0 < coluna < 8:
                    soma = tabuleiro_aleatorio_medio[linha][coluna - 1] + tabuleiro_aleatorio_medio[linha + 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna + 1] + tabuleiro_aleatorio_medio[linha][
                               coluna + 1]
            # linha de baixo
            elif linha == 8:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_medio[linha][coluna + 1] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna + 1] + \
                           tabuleiro_aleatorio_medio[linha - 1][coluna]
                elif coluna == 8:
                    soma = tabuleiro_aleatorio_medio[linha][coluna - 1] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha - 1][coluna]
                elif 0 < coluna < 8:
                    soma = tabuleiro_aleatorio_medio[linha][coluna - 1] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha - 1][coluna] + \
                           tabuleiro_aleatorio_medio[linha - 1][coluna + 1] + tabuleiro_aleatorio_medio[linha][
                               coluna + 1]
            # linhas do meio
            elif 0 < linha < 8:
                # coluna da esquerda
                if coluna == 0:
                    soma = tabuleiro_aleatorio_medio[linha - 1][coluna] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna + 1] + \
                           tabuleiro_aleatorio_medio[linha][coluna + 1] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna + 1] + tabuleiro_aleatorio_medio[linha + 1][
                               coluna]
                # coluna da direita
                elif coluna == 8:
                    soma = tabuleiro_aleatorio_medio[linha - 1][coluna] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha][coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna - 1] + tabuleiro_aleatorio_medio[linha + 1][
                               coluna]
                # meio do tabuleiro
                else:
                    soma = tabuleiro_aleatorio_medio[linha - 1][coluna] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha][coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna - 1] + tabuleiro_aleatorio_medio[linha + 1][
                               coluna] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna + 1] + \
                           tabuleiro_aleatorio_medio[linha][coluna + 1] + tabuleiro_aleatorio_medio[linha - 1][
                               coluna + 1]
            # quantidade de bombas
            if soma != 0 and tabuleiro_aleatorio_medio[linha][coluna] != -1:
                if soma == -1:
                    tabuleiro_medio[linha][coluna] = 1
                elif soma == -2:
                    tabuleiro_medio[linha][coluna] = 2
                elif soma == -3:
                    tabuleiro_medio[linha][coluna] = 3
                elif soma == -4:
                    tabuleiro_medio[linha][coluna] = 4
                elif soma == -5:
                    tabuleiro_medio[linha][coluna] = 5
                elif soma == -6:
                    tabuleiro_medio[linha][coluna] = 6
                elif soma == -7:
                    tabuleiro_medio[linha][coluna] = 7
                elif soma == -8:
                    tabuleiro_medio[linha][coluna] = 8


def exibe_tabuleiro_medio():
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if linha == 0 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 1\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] == -10:
                    print(f'\033[0;31; m                 1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 1\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ',
                          end='')
                else:
                    print(f'\033[0;31; m                 1\033[m    -  ', end='')
            elif linha == 8 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 9\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] == -10:
                    print(f'\033[0;31; m                 9\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 9\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ',
                          end='')
                else:
                    print(f'\033[0;31; m                 9\033[m    -  ', end='')
            elif 0 < linha < 8 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] == -10:
                    print(f'\033[0;31; m                 {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(
                        f'\033[0;31; m                 {linha + 1}\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ',
                        end='')
                else:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_medio[linha][coluna] == -10:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'  {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def mostra_bomba_fim_medio():
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if linha == 0 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 1\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] < 0:
                    print(f'\033[0;31; m                 1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 1\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ',
                          end='')
                else:
                    print(f'\033[0;31; m                 1\033[m    -  ', end='')
            elif linha == 8 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 9\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] < 0:
                    print(f'\033[0;31; m                 9\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 9\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ',
                          end='')
                else:
                    print(f'\033[0;31; m                 9\033[m    -  ', end='')
            elif 0 < linha < 8 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] < 0:
                    print(f'\033[0;31; m                 {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(
                        f'\033[0;31; m                 {linha + 1}\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ',
                        end='')
                else:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_medio[linha][coluna] < 0:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'  {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def jogo_medio_campo_minado():
    try:
        nick = menu_login()
        corpo_do_jogo_medio()
        game_over = 0
        tempo_inicial = time()
        while game_over == 0:
            os.system('cls')
            print('o' + '~' * 81 + 'o')
            print(
                f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
            print('o' + '~' * 81 + 'o')
            print()
            print()
            print('                     \033[0;31; m 1    2    3    4    5    6    7    8    9\033[m')
            print()
            exibe_tabuleiro_medio()
            linha = int(input('Linha: ')) - 1
            coluna = int(input('Coluna: ')) - 1
            # revela zeros próximos
            if linha == 0:
                if coluna == 0:
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                    if tabuleiro_medio[linha + 1][coluna + 1] == 0:
                        tabuleiro_medio[linha + 1][coluna + 1] = 100
                elif coluna == 8:
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                    if tabuleiro_medio[linha + 1][coluna - 1]:
                        tabuleiro_medio[linha + 1][coluna - 1] = 100
                elif 0 < coluna < 8:
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna - 1] == 0:
                        tabuleiro_medio[linha + 1][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                    if tabuleiro_medio[linha + 1][coluna + 1] == 0:
                        tabuleiro_medio[linha + 1][coluna + 1] = 100
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                # linha de baixo
            elif linha == 8:
                if coluna == 0:
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                    if tabuleiro_medio[linha - 1][coluna + 1] == 0:
                        tabuleiro_medio[linha - 1][coluna + 1] = 100
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100

                elif coluna == 8:
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha - 1][coluna - 1] == 0:
                        tabuleiro_medio[linha - 1][coluna - 1] = 100
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                elif 0 < coluna < 8:
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha - 1][coluna - 1] == 0:
                        tabuleiro_medio[linha - 1][coluna - 1] = 100
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                    if tabuleiro_medio[linha - 1][coluna + 1] == 0:
                        tabuleiro_medio[linha - 1][coluna + 1] = 100
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                # linhas do meio
            elif 0 < linha < 8:
                # coluna da esquerda
                if coluna == 0:
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                    if tabuleiro_medio[linha - 1][coluna + 1] == 0:
                        tabuleiro_medio[linha - 1][coluna + 1] = 100
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                    if tabuleiro_medio[linha + 1][coluna + 1] == 0:
                        tabuleiro_medio[linha + 1][coluna + 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                # coluna da direita
                elif coluna == 8:
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                    if tabuleiro_medio[linha - 1][coluna - 1] == 0:
                        tabuleiro_medio[linha - 1][coluna - 1] = 100
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna - 1] == 0:
                        tabuleiro_medio[linha + 1][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                # meio do tabuleiro
                else:
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                    if tabuleiro_medio[linha - 1][coluna - 1] == 0:
                        tabuleiro_medio[linha - 1][coluna - 1] = 100
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna - 1] == 0:
                        tabuleiro_medio[linha + 1][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                    if tabuleiro_medio[linha + 1][coluna + 1] == 0:
                        tabuleiro_medio[linha + 1][coluna + 1] = 100
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                    if tabuleiro_medio[linha - 1][coluna + 1] == 0:
                        tabuleiro_medio[linha - 1][coluna + 1] = 100
            if -2 < tabuleiro_medio[linha][coluna] < 10:
                if tabuleiro_medio[linha][coluna] == 0:
                    tabuleiro_medio[linha][coluna] = 100
                elif tabuleiro_medio[linha][coluna] == -1:
                    tabuleiro_medio[linha][coluna] = -10
                else:
                    tabuleiro_medio[linha][coluna] *= 200
            else:
                print(f'Você já jogou nessa posição.\nTente novamente!')
            teste_gameover_medio()
            if teste_gameover_medio() == 1:
                game_over = 1
            elif teste_gameover_medio() == 2:
                game_over = 2
        os.system('cls')
        print('                     \033[0;31; m 1    2    3    4    5    6    7    8    9\033[m')
        print()
        mostra_bomba_fim_medio()
        tempo_final = time()
        tempo_de_partida_medio = tempo_final - tempo_inicial
        print()
        print(f'TEMPO DE PARTIDA: {tempo_de_partida_medio:.2f}s')
        print()
        pontos_partida_media = 0
        if game_over == 1:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_chorando:', language='pt')}Você perdeu!{emoji.emojize(':rosto_chorando:', language='pt')}')
        elif game_over == 2:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}Você Ganhou!{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}')
            pontos_partida_media = 50
        print()
        # sistema de pontuação
        if tempo_de_partida_medio < 60:
            pontos_totais_medio = pontos_partida_media * 2
        elif 60 < tempo_de_partida_medio < 180:
            pontos_totais_medio = pontos_partida_media * 1.5
        elif 180 < tempo_de_partida_medio < 300:
            pontos_totais_medio = pontos_partida_media * 1.25
        else:
            pontos_totais_medio = pontos_partida_media
        # atualiza o rank
        atualizar_ranking_crescente('Rank_campo_minado', nome=nick, pontuacao=pontos_totais_medio)
        ########################################
        print('Voltar para o menu?')
        print()
        sim_nao = input('[S]Sim\n\n[N]Não\n\nDigite: ').upper()
        if sim_nao == 'S':
            os.system('cls')
            menu_campo_minado()
        else:
            print('Saindo...')
            print()
            sleep(3)
        #######################################
    except:
        if not KeyboardInterrupt:
            print('Error')
            os.system('cls')
            menu_campo_minado()


def teste_gameover_medio():
    quant_bombs = 0
    quant_jogadas = 0
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if tabuleiro_medio[linha][coluna] == -1:
                quant_bombs += 1
            if tabuleiro_medio[linha][coluna] == -10:
                return 1
            if tabuleiro_medio[linha][coluna] >= 200 or tabuleiro_medio[linha][coluna] == 100:
                quant_jogadas += 1
    lugares_disponiveis = 81 - quant_bombs
    if lugares_disponiveis == quant_jogadas:
        return 2


'''TABULEIRO DIFICIL'''

tabuleiro_dificil = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def corpo_do_jogo_difícil():
    tabuleiro_aleatorio_dificil = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # aleatoriza o tabuleiro dificil
    for linha in range(0, 10):
        for quant in range(3):
            coluna = randint(0, 9)
            tabuleiro_aleatorio_dificil[linha][coluna] = -1

    # transfere para o tabuleiro dificil final
    for linha in range(0, 10):
        for coluna in range(0, 10):
            if tabuleiro_aleatorio_dificil[linha][coluna] == 0:
                tabuleiro_dificil[linha][coluna] = 0
            elif tabuleiro_aleatorio_dificil[linha][coluna] == -1:
                tabuleiro_dificil[linha][coluna] = -1

    # posiciona as dicas do dificil
    for linha in range(0, 10):
        for coluna in range(0, 10):
            # teste de bombas
            soma = 0
            # linha de cima
            if linha == 0:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna + 1] + tabuleiro_aleatorio_dificil[linha + 1][
                        coluna] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna + 1]
                elif coluna == 9:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna - 1] + tabuleiro_aleatorio_dificil[linha + 1][
                        coluna] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna - 1]
                elif 0 < coluna < 9:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna - 1] + tabuleiro_aleatorio_dificil[linha + 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna + 1] + tabuleiro_aleatorio_dificil[linha][
                               coluna + 1]
            # linha de baixo
            elif linha == 9:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna + 1] + tabuleiro_aleatorio_dificil[linha - 1][
                        coluna + 1] + \
                           tabuleiro_aleatorio_dificil[linha - 1][coluna]
                elif coluna == 9:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna - 1] + tabuleiro_aleatorio_dificil[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha - 1][coluna]
                elif 0 < coluna < 9:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna - 1] + tabuleiro_aleatorio_dificil[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha - 1][coluna] + \
                           tabuleiro_aleatorio_dificil[linha - 1][coluna + 1] + tabuleiro_aleatorio_dificil[linha][
                               coluna + 1]
            # linhas do meio
            elif 0 < linha < 9:
                # coluna da esquerda
                if coluna == 0:
                    soma = tabuleiro_aleatorio_dificil[linha - 1][coluna] + tabuleiro_aleatorio_dificil[linha - 1][
                        coluna + 1] + \
                           tabuleiro_aleatorio_dificil[linha][coluna + 1] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna + 1] + tabuleiro_aleatorio_dificil[linha + 1][
                               coluna]
                # coluna da direita
                elif coluna == 9:
                    soma = tabuleiro_aleatorio_dificil[linha - 1][coluna] + tabuleiro_aleatorio_dificil[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna - 1] + tabuleiro_aleatorio_dificil[linha + 1][
                               coluna]
                # meio do tabuleiro
                else:
                    soma = tabuleiro_aleatorio_dificil[linha - 1][coluna] + tabuleiro_aleatorio_dificil[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna - 1] + tabuleiro_aleatorio_dificil[linha + 1][
                               coluna] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna + 1] + \
                           tabuleiro_aleatorio_dificil[linha][coluna + 1] + tabuleiro_aleatorio_dificil[linha - 1][
                               coluna + 1]
            # quantidade de bombas
            if soma != 0 and tabuleiro_aleatorio_dificil[linha][coluna] != -1:
                if soma == -1:
                    tabuleiro_dificil[linha][coluna] = 1
                elif soma == -2:
                    tabuleiro_dificil[linha][coluna] = 2
                elif soma == -3:
                    tabuleiro_dificil[linha][coluna] = 3
                elif soma == -4:
                    tabuleiro_dificil[linha][coluna] = 4
                elif soma == -5:
                    tabuleiro_dificil[linha][coluna] = 5
                elif soma == -6:
                    tabuleiro_dificil[linha][coluna] = 6
                elif soma == -7:
                    tabuleiro_dificil[linha][coluna] = 7
                elif soma == -8:
                    tabuleiro_dificil[linha][coluna] = 8


def teste_gameover_dificil():
    quant_bombs = 0
    quant_jogadas = 0
    for linha in range(0, 10):
        for coluna in range(0, 10):
            if tabuleiro_dificil[linha][coluna] == -1:
                quant_bombs += 1
            if tabuleiro_dificil[linha][coluna] == -10:
                return 1
            if tabuleiro_dificil[linha][coluna] >= 200 or tabuleiro_dificil[linha][coluna] == 100:
                quant_jogadas += 1
    lugares_disponiveis = 100 - quant_bombs
    if lugares_disponiveis == quant_jogadas:
        return 2


# exibe o tabuleiro
def exibe_tabuleiro_dificil():
    for linha in range(0, 10):
        for coluna in range(0, 10):
            if linha == 0 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            1\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] == -10:
                    print(f'\033[0;31; m            1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            1\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            1\033[m    -  ', end='')
            elif linha == 9 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            10\033[m   0  ', end='')
                elif tabuleiro_dificil[linha][coluna] == -10:
                    print(f'\033[0;31; m            10\033[m{emoji.emojize('   :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            10\033[m   {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            10\033[m   -  ', end='')
            elif 0 < linha < 9 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] == -10:
                    print(f'\033[0;31; m            {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(
                        f'\033[0;31; m            {linha + 1}\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ',
                        end='')
                else:
                    print(f'\033[0;31; m            {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_dificil[linha][coluna] == -10:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'  {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def mostra_bomba_fim_dificl():
    for linha in range(0, 10):
        for coluna in range(0, 10):
            if linha == 0 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            1\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] < 0:
                    print(f'\033[0;31; m            1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            1\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            1\033[m    -  ', end='')
            elif linha == 9 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            9\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] < 0:
                    print(f'\033[0;31; m            9\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            9\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            9\033[m    -  ', end='')
            elif 0 < linha < 9 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] < 0:
                    print(f'\033[0;31; m            {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(
                        f'\033[0;31; m            {linha + 1}\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ',
                        end='')
                else:
                    print(f'\033[0;31; m            {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_dificil[linha][coluna] < 0:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'  {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def jogo_dificil_campo_minado():
    try:
        nick = menu_login()
        corpo_do_jogo_difícil()
        game_over = 0
        tempo_inicial = time()
        while game_over == 0:
            os.system('cls')
            print('o' + '~' * 81 + 'o')
            print(
                f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
            print('o' + '~' * 81 + 'o')
            print()
            print()
            print('                \033[0;31; m 1    2    3    4    5    6    7    8    9    10\033[m')
            print()
            exibe_tabuleiro_dificil()
            linha = int(input('Linha: ')) - 1
            coluna = int(input('Coluna: ')) - 1
            # revela zeros próximos
            if linha == 0:
                if coluna == 0:
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                    if tabuleiro_dificil[linha + 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna + 1] = 100
                elif coluna == 8:
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                    if tabuleiro_dificil[linha + 1][coluna - 1]:
                        tabuleiro_dificil[linha + 1][coluna - 1] = 100
                elif 0 < coluna < 8:
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                    if tabuleiro_dificil[linha + 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                # linha de baixo
            elif linha == 8:
                if coluna == 0:
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100

                elif coluna == 8:
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                elif 0 < coluna < 8:
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                    if tabuleiro_dificil[linha - 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                # linhas do meio
            elif 0 < linha < 8:
                # coluna da esquerda
                if coluna == 0:
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                    if tabuleiro_dificil[linha - 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                # coluna da direita
                elif coluna == 8:
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                    if tabuleiro_dificil[linha - 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                # meio do tabuleiro
                else:
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                    if tabuleiro_dificil[linha - 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                    if tabuleiro_dificil[linha + 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna + 1] = 100
            if -2 < tabuleiro_dificil[linha][coluna] < 10:
                if tabuleiro_dificil[linha][coluna] == 0:
                    tabuleiro_dificil[linha][coluna] = 100
                elif tabuleiro_dificil[linha][coluna] == -1:
                    tabuleiro_dificil[linha][coluna] = -10
                else:
                    tabuleiro_dificil[linha][coluna] *= 200
            else:
                print(f'Você já jogou nessa posição.\nTente novamente!')
            teste_gameover_dificil()
            if teste_gameover_dificil() == 1:
                game_over = 1
            elif teste_gameover_dificil() == 2:
                game_over = 2
        os.system('cls')
        print('                \033[0;31; m 1    2    3    4    5    6    7    8    9    10\033[m')
        print()
        mostra_bomba_fim_dificl()
        tempo_final = time()
        tempo_de_partida_dificil = tempo_final - tempo_inicial
        print()
        print(f'TEMPO DE PARTIDA: {tempo_de_partida_dificil:.2f}s')
        print()
        pontos_partida_dificil = 0
        if game_over == 1:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_chorando:', language='pt')}Você perdeu!{emoji.emojize(':rosto_chorando:', language='pt')}')
        elif game_over == 2:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}Você Ganhou!{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}')
            pontos_partida_dificil = 100
        print()
        # sistema de pontuação
        if tempo_de_partida_dificil < 60:
            pontos_totais_dificil = pontos_partida_dificil * 2
        elif 60 < tempo_de_partida_dificil < 180:
            pontos_totais_dificil = pontos_partida_dificil * 1.5
        elif 180 < tempo_de_partida_dificil < 300:
            pontos_totais_dificil = pontos_partida_dificil * 1.25
        else:
            pontos_totais_dificil = pontos_partida_dificil
        # atualiza o rank
        atualizar_ranking_crescente('Rank_campo_minado', nome=nick, pontuacao=pontos_totais_dificil)
        ########################################
        print('Voltar para o menu?')
        print()
        sim_nao = input('[S]Sim\n\n[N]Não\n\nDigite: ').upper()
        if sim_nao == 'S':
            os.system('cls')
            menu_campo_minado()
        else:
            print('Saindo...')
            print()
            sleep(3)
        #######################################
    except:
        if not KeyboardInterrupt:
            print('Error')
            os.system('cls')
            menu_campo_minado()


'''MENU'''


def menu_campo_minado():
    try:
        cont = 1
        while cont == 1:
            print('o' + '~' * 81 + 'o')
            print(
                f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
            print('o' + '~' * 81 + 'o')
            print()
            print()
            print(' TUTORIAL          COMEÇAR A JOGAR          RANKING          VOLTAR PARA O INICIO')
            print('   [T]                   [J]                  [R]                    [I]')
            print()
            comecar = input('Digite: ').upper()
            os.system("cls")
            if comecar == 'J':
                print('o' + '~' * 81 + 'o')
                print(
                    f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
                print('o' + '~' * 81 + 'o')
                print()
                print()
                cont -= 1
                opcao = input(
                    'Qual a dificuldade em que você deseja jogar?\n\n[F]FÁCIL\n\n[M]MÉDIO\n\n[D]DIFÍCIL\n\n').upper()
                os.system('cls')
                if opcao == 'F':
                    os.system('cls')
                    jogo_facil_campo_minado()
                elif opcao == 'M':
                    os.system('cls')
                    jogo_medio_campo_minado()
                elif opcao == 'D':
                    os.system("cls")
                    jogo_dificil_campo_minado()
                else:
                    os.system('cls')
                    menu_campo_minado()
            elif comecar == 'T':
                os.system("cls")
                print('''O jogo é um campo minado simples, onde o seu objetivo é descobrir todas as posições sem bombas.

    O número que lhe aparecer mostra a quantidade de bombas presentes ao redor dele.

    Se você encontrar um número zero ele revelará outros números zeros que estejam ao redor dele. 

        Existem três dificuldades:
    FÁCIL: Tabuleiro 8x8 e 1 bomba por linha
    MÈDIO: Tabuleiro 9x9 e 2 bombas por linha
    DIFÌCIL: Tabuleiro 10x10 e 3 bombas por linha

    Vamos Jogar?
    ''')
                sim_nao = input('[S]Sim\n[N]Não\n\nDigite: ').upper()
                if sim_nao == 'S':
                    os.system('cls')
                else:
                    print('Saindo...')
                    # sair para o menu geral
            elif comecar == 'R':
                ver_ranking('Rank_campo_minado')
                print()
                voltar = input('Aperte enter para voltar')
                os.system('cls')
            elif comecar == 'I':
                cont -= 1
                print('Saindo...')
                sleep(3)
                menu_todos_os_jogos()
            else:
                print('Resposta inválida. Tente novamente!')
    except:
        if not KeyboardInterrupt:
            menu_campo_minado()

################QualaPalavra#############


def exibir_progresso(progresso):
    print(' '.join(progresso))

def qual_palavra(lista):
    # título do jogo e a categoria em que a pessoa vai jogar
    titulo = 'QUAL A PALAVRA?'
    print(f'{titulo:~^50}')
    print(f'A categoria da palavra que você deve descobrir será ', end='')
    for _ in range(3):
        sleep(0.2)
        print('.', end=' ')
    print(lista[0])

    escolhida = choice(lista[1:])
    progresso = ['_'] * len(escolhida)
    exibir_progresso(progresso)

    while True:
        # pergunta ao usuário se ele deseja adivinhar a palavra com aas letras já descobertas ou não
        opcao = input('''Você quer tentar adivinhar a palavra agora?
    [1] Sim, eu quero tentar
    [2] Não, eu quero descobrir mais letras antes
    Digite a sua escolha: ''')
        # caso a resposta for não, ele chama a função para descobrir mais letras
        if opcao == '2':
            progresso = tentativa_letra(escolhida, progresso)
            # caso nao tenha _ no progresso da palavra, significa que a pessoa já descobriu todas as letras
            if '_' not in progresso:
                print(f'Parabéns, a palavra era: {escolhida}')
                break
        # se a resposta for sim, ele pede ao usuário um palpite sobre qual a palavra
        elif opcao == '1':
            tentativa = input('Qual a sua tentativa? ')
            # Caso a pessoa acerte o programa parabeniza e se encerra
            if tentativa == escolhida:
                print('Acertou!')
                break
            else:
                # caso a pessoa erre ele fala qual era a palavra e se encerra
                print(f'Errou! A palavra era: {escolhida}')
                break
        else:
            print('Opção inválida. Por favor, digite 1 ou 2.')


def tentativa_letra(escolhida, progresso_palavra):
    # pedeao usuário uma letra
    jogada = input('Coloque uma letra: ')
    # checa se o usuário digitou realmente algo e se foi uma letra
    if len(jogada) != 1 or not jogada.isalpha():
        print('Por favor, insira apenas uma letra.')
    # tenta encontrar a letra digitada na palavra que foi escolhida
    if jogada in escolhida:
        # se encontrar a letra na palavra, descobre em que posição a letra está
        for i, letra in enumerate(escolhida):
            # quando descobre a posição que a letra está, atualiza o progresso da palavra
            if letra == jogada:
                progresso_palavra[i] = jogada
    else:
        # se não encontrar a letra ele informa
        print(f'A letra "{jogada}" não está na palavra.')
    # chama a função específica que exibe
    exibir_progresso(progresso_palavra)
    return progresso_palavra


def jogar_novamente():
    while True:
        # pergunta se a pessoa quer jogar novamente
        resposta = input("Você quer jogar novamente? (s/n): ").lower()
        # caso a pessoa escolha sim ele retorna True
        if resposta == 's':
            return True
        # caso a pessoa escolha não ele retorna False
        elif resposta == 'n':
            print("Obrigado por jogar!")
            return False
        else:
            print("Resposta inválida. Por favor, digite 's' ou 'n'.")


#############AdvinheMaisRapido#############

def selecionar_frase(categoria):
    frases = {
        'trava-linguas': [
            "O rato roeu a roupa do rei de Roma.",
            "A aranha arranha a rã, a rã arranha a aranha.",
            "O beijo da beata é o beijo da beata.",
            "Três pratos de trigo para três tigres tristes.",
            "Se o pombo não pousar, o passo não passa.",
            "A faca de casa corta com a ponta para baixo.",
            "O cinto de segurança do ciclista é de cinto sem cinto."
        ],
        'animais': [
            "O rápido raposo marrom pula sobre o cachorro preguiçoso.",
            "A girafa é o animal mais alto da savana.",
            "O elefante é conhecido por sua memória incrível.",
            "O leão é o rei da selva.",
            "O panda gigante se alimenta  principalmente de bambu.",
            "Os golfinhos são conhecidos por sua inteligência e habilidades sociais.",
            "A águia é um símbolo de força e visão aguçada."
        ],
        'engracadas': [
            "Eu não sou preguiçoso, só estou em modo de economia de energia.",
            "Eu ia te contar uma piada sobre um boomerang, mas vou ter que jogar de volta.",
            "Por que o computador foi ao médico? Porque estava com um vírus!",
            "Se você acha que ninguém se importa com você, tente faltar a um pagamento de conta.",
            "Eu não sou maluco, só sou um pouco fora do normal.",
            "Você sabe que está ficando velho quando os velhos te chamam de jovem.",
            "Minha vida é como um software, sempre precisando de atualizações."
        ],
        'historia': [
            "A história é um grande livro aberto onde aprendemos com o passado.",
            "Quem controla o passado controla o futuro.",
            "A história não se repete, mas rima.",
            "O estudo da história é o estudo da humanidade em si.",
            "O passado é um prólogo.",
            "História é a consciência do passado.",
            "Todo evento histórico é um reflexo dos valores da época em que ocorreu."
        ],
        'ciencia': [
            "A ciência é a chave para o futuro.",
            "Toda descoberta científica começa com uma pergunta.",
            "A ciência não conhece fronteiras, apenas oportunidades.",
            "O progresso científico é a maior conquista da humanidade.",
            "A curiosidade é o motor da ciência.",
            "A ciência é um meio de explorar os mistérios do universo.",
            "O conhecimento científico é um presente para a humanidade."
        ]
    }
    return random.choice(frases.get(categoria, ["Categoria não encontrada."]))
def jogo_digitacao():
    print('''===========================================
===========JOGO DA DITILOGRAFIA============
===========================================''')
    nome = input('Digite seu nome, jogador:').capitalize().strip()
    pontuacao = 0

    categorias = ['trava-linguas', 'animais', 'engracadas', 'historia', 'ciencia']
    dicas = {
        'trava-linguas': "Categoria: Trava-línguas",
        'animais': "Categoria: Animais",
        'engracadas': "Categoria: Engraçadas",
        'historia': "Categoria: História",
        'ciencia': "Categoria: Ciência"
    }
    contador = {
        'respostas_corretas': 0,
        'respostas_incorretas': 0,
        'tempo_total': 0.0
    }
    while True:
        categoria = random.choice(categorias)  # Escolhe uma categoria aleatória
        dica = dicas[categoria]
        frase = selecionar_frase(categoria)
        print(f"\nDica: {dica}\n")
        print(f"Frase para digitar: '{frase}'\n")
        input(f'\033[31mPressione ENTER quando estiver pronto para começar...')
        inicio = time()
        resposta = input("\033[mDigite a frase: ")
        fim = time()
        tempo = fim - inicio
        if resposta == frase:
            pontuacao = max(0, 100 - int(tempo))
            print(f"\nParabéns! Você digitou a frase corretamente em {tempo:.2f} segundos.")
            print(f"Sua pontuação: {pontuacao}")
            contador['respostas_corretas'] += 1
            contador['tempo_total'] += tempo
        else:
            print(f"\nVocê digitou a frase incorretamente. A frase correta era:\n'{frase}'")
            print(f"Seu tempo: {tempo:.2f} segundos.")
            contador['respostas_incorretas'] += 1
        r = input("Deseja continuar? [Sim/Não] ").strip().upper()
        if r == 'SIM':
            print(f'Oba, vamos jogar novamente {nome}!')
        else:
            print(f'Que pena, outro dia jogamos {nome}!')
            break
    atualizar_ranking_crescente('raking_frases', nome, pontuacao)
    if contador['respostas_corretas'] + contador['respostas_incorretas'] > 0:
        tempo_medio = contador['tempo_total'] / contador['respostas_corretas']
    else:
        tempo_medio = 0
    opcao = input('Você quer ver o ranking?[S/N]').strip().upper()[0]
    if opcao =='S':
        ver_ranking('raking_frases')
    else:
        print('')
    print("\nEstatísticas do Jogador:")
    print(f"Respostas Corretas: {contador['respostas_corretas']}")
    print(f"Respostas Incorretas: {contador['respostas_incorretas']}")
    print(f"Tempo Médio de Resposta: {tempo_medio:.2f} segundos")


############AdvinheONumero#############

def adivinhe_o_numero():

    r = 'S'
    print('''===========================================
========JOGO DE DESCOBRIR O NÚMERO=========
===========================================''')
    nome = input('Qual seu nome?')

    while True:
            dificuldade = str(input('Qual dificuldade vc quer jogar? [facil/medio/dificil]')).lower().strip()[0]
            if dificuldade == 'f':
                na = random.randint(0, 10)
                r = str(input('Vamos começar?(Sim/Não)')).upper().strip()[0]
                tentativas = 0
                if r == 'S':
                    print(f'Seja bem vindo,{nome}, vamos jogar')
                    n = int(input(f'Escreva um número:'))
                    while True:
                        tentativas += 1
                        if n > na:
                            print('Seu valor está muito alto')
                            n = int(input(f'\033[31mTente outra vez:'))
                        elif n < na:
                            print('Seu valor está muito baixo')
                            n = int(input(f'\033[31mTente outra vez:'))
                        else:
                            print(emoji.emojize(f'\033[34mParabéns :partying_face::partying_face: você conseguiu acerta o numero: {na} em {tentativas} tentativas'))
                            atualizar_ranking_decrescente('raking_numero', nome, tentativas)
                            opcao = input('Você quer ver o ranking?[S/N]').strip().upper()[0]
                            if opcao == 'S':
                                ver_ranking_tentativas('raking_numero')
                            else:
                                print('')
                            break
                else:
                    print(emoji.emojize('Na proxima jogamos :sad_but_relieved_face:'))
            if dificuldade == 'm':
                na = random.randint(10, 100)
                r = str(input('Vamos começar?(Sim/Não)')).upper().strip()[0]
                tentativas = 0
                if r == 'S':
                    print(f'Seja bem vindo,{nome}, vamos jogar')
                    n = int(input(f'Escreva um número:'))
                    while True:
                        tentativas += 1
                        if n > na:
                            print('Seu valor está muito alto')
                            n = int(input(f'\033[35mTente outra vez:'))
                        elif n < na:
                            print('Seu valor está muito baixo')
                            n = int(input(f'\033[35mTente outra vez:'))
                        else:
                            print(emoji.emojize(f'\033[32mParabéns :partying_face::partying_face: você conseguiu acerta o numero: {na} em {tentativas} tentativas' ))
                            atualizar_ranking_decrescente('raking_numero_m', nome, tentativas)
                            opcao = input('Você quer ver o ranking?[S/N]').strip().upper()[0]
                            if opcao == 'S':
                                ver_ranking_tentativas('raking_numero_m')
                            else:
                                print('')
                            break
                else:
                    print(emoji.emojize('Na proxima jogamos :sad_but_relieved_face:'))
            elif dificuldade == 'd':
                na = random.randint(0, 1000)
                r = str(input('Vamos começar?(Sim/Não)')).upper().strip()[0]
                tentativas = 0
                if r == 'S':
                    print(f'Seja bem vindo,{nome}, vamos jogar')
                    n = int(input(f'Escreva um número:'))
                    while True:
                        tentativas += 1
                        if n > na:
                            print('Seu valor está muito alto')
                            n = int(input(f'\033[33mTente outra vez:'))
                        elif n < na:
                            print('Seu valor está muito baixo')
                            n = int(input(f'\033[33mTente outra vez:'))
                        else:
                            print(emoji.emojize(
                                f'\033[33mParabéns :partying_face::partying_face: você conseguiu acerta o numero: {na} em {tentativas} tentativas'))
                            atualizar_ranking_decrescente('raking_numero_d', nome, tentativas)
                            opcao = input('Você quer ver o ranking?[S/N]').strip().upper()[0]
                            if opcao == 'S':
                                ver_ranking_tentativas('raking_numero_d')
                            else:
                                print('')
                            break
                else:
                    print(emoji.emojize('Na proxima jogamos :sad_but_relieved_face:'))
            r = input('\033[mQuer jogar novamente?(Sim/Não)').strip().capitalize()[0]
            if r == 'S':
                print('Escolha dentre as opções abaixo')
            else:
                print('OBRIGADO POR JOGAR,ATÉ UMA OUTRA HORA')
                break


############MenuPrincipal##############3
def menu_todos_os_jogos():
    print(f'{" MENU DE JOGOS ":~^70}', end='')
    print(f'{'~' * 10}')
    print(f'{" 1. Jogo de Memória ":<40}', end='')
    print(f'{" 2. Quem digita mais rápido?  ":>42}')
    print()
    print(f'{" 3. Advinhe o Número ":<40}', end='')
    print(f'{" 4. Campo Minado ":>29}')
    print('')
    print(f'{" 5. Jogo da Velha ":<40}', end='')
    print(f'{" 6. Jogo dos Copos ":>31}')
    print('')
    print(f'{" 7. Momento Certo":<40}', end='')
    print(f'{" 8. Qual a Palavra? ":>32}')
    print(f'{" 0. Sair":>38}')
    print('')
    print(f'{'~'*80}')


menu_todos_os_jogos()
opcao = int(input('Digite o que você deseja jogar: '))
jogar = True

while jogar:
    if opcao == 0:
        jogar = False
        break
    elif opcao == 1:
        os.system('cls')
        jogo_de_memoria()
    elif opcao == 2:
        os.system('cls')
        jogo_digitacao()
    elif opcao == 3:
        os.system('cls')
        adivinhe_o_numero()
    elif opcao == 4:
        os.system('cls')
        menu_campo_minado()
    elif opcao == 5:
        os.system('cls')
        menu_inicio_jogo_da_velha()
    elif opcao == 6:
        os.system('cls')
        jogo_dos_copos()
    elif opcao == 7:
        os.system('cls')
        vez = 0
        nome = ''
        while True:
            retorno = momento_perfeito(vez)
            if not retorno[0]:
                break
            else:
                if retorno[1] == 1:
                    vez += 1
                    if retorno[4]:
                        nome = retorno[2]
                    pontuacao_momento += retorno[3]
        if nome != '':
            atualizar_ranking_crescente('momento_ranking', nome, pontuacao_momento)
    elif opcao == 8:
        os.system('cls')
        print("Bem-vindo ao jogo de adivinhação de palavras!")
        while True:
            qual_palavra(choice(
                [palavras.animais, palavras.frutas, palavras.objetos, palavras.cores, palavras.sentimentos,
                 palavras.alimentos]))
            if not jogar_novamente():
                break

    os.system('cls')
    opcao = int(input('''Você deseja voltar para o menu principal?  
    [1] Sim
    [2] Não
DIGITE: '''))
    if opcao == 2:
        print('Obrigado por jogar, volte sempre!')
        break
    elif opcao == 1:
        os.system('cls')
        menu_todos_os_jogos()
        opcao = int(input('Digite o que você deseja jogar: '))


#########################MenuPrincipal###############

menu_todos_os_jogos()

