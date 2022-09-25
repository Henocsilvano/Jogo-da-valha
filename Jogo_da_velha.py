import numpy as np

class JogoDaVelha:
    def __init__(self):
        self.jogador1 = False
        self.jogador2 = False
        self.jogo = ['_'] * 9

    # Função que inicia o jogo 
    def Iniciar(self):
        print('~'*40)
        print('BEM-VINDO AO JOGO DA VELHA'.center(40, '~'))
        print('~' *40)
        print('Marque a posição de acordo com os numeros\nque representam os espaços abaixo:\n')
        print('Posições:')
        print('1 2 3')
        print('4 5 6')
        print('7 8 9')
        while True:
            while True:
                confirmar = False
                for jogador in range(1, 3):
                    self.MostrarGrade()
                    continuar = self.lançarResultado()
                    if continuar == 1:
                        confirmar = True
                        break
                    print('~'*40)
                    jogada = self.validarJogada(jogador)
                    print('~'*40)
                    self.MarcarSimbolo(jogada, jogador)
                    self.verificarVencedor(self.jogo)
                    if self.jogador1 or self.jogador2:
                        break
                if confirmar:
                    break  
            break
    
    # Função que mostra os espaços (preenchidos/vazios)
    def MostrarGrade(self):
        for indice in range(len(self.jogo)):
            print(f'{self.jogo[indice]} ', end='')
            if indice == 2 or indice == 5 or indice == 8:
                print()

    # Função para validar jogada
    def validarJogada(self,jogador):
        valor = 10
        while True:
            try:
                if jogador == 1:
                    jogada = int(input(f'Jogador {jogador} [\033[32m⩙\033[m]: '))
                    valor = jogada -1
                elif jogador == 2:
                    jogada = int(input(f'Jogador {jogador} [\033[31mʘ\033[m]: '))
                    valor = jogada -1
            except:
                print('\033[32mMarque uma jogada entre 1 e 9\033[m')
                print('~'*40)
                continue
            else:
                break
        
        if valor < 0 or valor > 8:
            print('\033[32mJogada inválida!\033[m')
            print('~'*40)
            return self.validarJogada(jogador)
        else:
            for pos, elemento in enumerate(self.jogo):
                if pos == valor and elemento == '_':
                    return valor
                elif pos == valor and elemento != '_':
                    print('\033[32mPosição indisponivel!\033[m')
                    return self.validarJogada(jogador)

    # Função para marcar os sombolos apontados
    def MarcarSimbolo(self, jogda, jogador):
        simbolo = ''
        if jogador == 1:
            simbolo =  '\033[32m⩙\033[m'
        elif jogador == 2:
            simbolo =  '\033[31mʘ\033[m'
        self.jogo[jogda] = simbolo

    # Função para verificar o vencedor
    def verificarVencedor(self, jogo):
        s_X = '\033[32m⩙\033[m'
        s_O = '\033[31mʘ\033[m'
        l1 = jogo[0:3]
        l2 = jogo[3:6]
        l3 = jogo[6:]
        jog = np.array([l1,l2,l3])
        for linha in range(len(jog)):
            if not s_O in jog[linha,:] and not '_' in jog[linha,:]:
                self.jogador1 = True
            if not s_X in jog[linha,:] and not '_' in jog[linha,:]:
                self.jogador2 = True
        for coluna in range(len(jog)):
            if not s_O in jog[:,coluna] and not '_' in jog[:,coluna]:
                self.jogador1 = True
            if not s_X in jog[:,coluna] and not '_' in jog[:,coluna]:
                self.jogador2 = True
        if l1[0] == s_X and l2[1] == s_X and l3[2] == s_X:
            self.jogador1 = True
        if l1[2] == s_X and l2[1] == s_X and l3[0] == s_X:
            self.jogador1 = True
        if l1[2] == s_O and l2[1] == s_O and l3[0] == s_O:
            self.jogador2 = True
        if l1[0] == s_O and l2[1] == s_O and l3[2] == s_O:
            self.jogador2 = True

    def lançarResultado(self):
        if self.jogador1 or self.jogador2:
            print('~'*40)
            print('\033[32mFim do jogo!\033[m')
        if self.jogador1:
            print(f'\033[32mVitoria para o jogador 1!\033[m')
            return 1
        elif self.jogador2:
            print(f'\033[32mVitoria para o jogador 2!\033[m')
            return 1
        
        contador = self.jogo.count('_')
        if contador == 1:
            print('~'*40)
            res = ' '
            while res not in 'SN':
                res = str(input('\033[32mContinuar com o jogo? [S/N]:\033[m ')).strip().upper()[0]
            if res == 'N':
                print('~'*40)
                print('\033[32mJogo interronpido!\033[m')
                print('\033[32mSem vencedor!\033[m')
                return 1
            elif res == 'S':
                return 0
        elif contador == 2:
            print('~'*40)
            print('\033[32mRestam apenas 2 jogada possivel\033[m')
            res = ' '
            while res not in 'SN':
                res = str(input('\033[32mQuer continuar? [S/N]:\033[m ')).strip().upper()[0]
            if res == 'N':
                print('~'*40)
                print('\033[32mJogo terminado!\033[m')
                print('\033[32mSem vencedor!\033[m')
                return 1
            elif res == 'S':
                return 0
        elif contador == 0:
            print('~'*40)
            print('\033[32mFim do jogo!\033[m')
            print('\033[32mSem vencedor!\033[m')
            return 1 

def jogar():
    while True:
        jogo = JogoDaVelha()
        jogo.Iniciar()
        res = ' '
        while res not in 'SN':
            res = str(input('Quer jogar de novo? [S/N]: ')).strip().upper()[0]
        if res == 'N':
            break
