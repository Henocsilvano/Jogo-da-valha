class JogoDaVelha:
    def __init__(self):
        self.parar = False
        self.jogo = ['_'] * 9

    # Função que inicia o jogo 
    def Iniciar(self):
        print('~'*40)
        print(f"\033[32m{'BEM-VINDO AO JOGO DA VELHA.':^40}\033[m")
        print('~' *40)
        print('Marque a posição de acordo com os numeros\nque representam os espaços abaixo:\n')
        print('Posições:')
        print('1 2 3')
        print('4 5 6')
        print('7 8 9')
        while True:
            self.MostrarGrade()
            while True:
                confirmar = False
                for jogador in range(1, 3):
                    simbolo = '\033[32m⩙\033[m' if jogador == 1 else '\033[31mʘ\033[m'
                    print('~'*40)
                    jogada = self.validarJogada(jogador)
                    print('~'*40)
                    self.MarcarSimbolo(jogada, jogador)
                    self.verificarVencedor(self.jogo, jogada, simbolo)
                    self.MostrarGrade()
                    continuar = self.lançarResultado(jogador)
                    if continuar:
                        confirmar = True
                        break
                if confirmar:
                    break  
            break
    
    # Função que mostra os espaços (preenchidos/vazios)
    def MostrarGrade(self):
        for linha in [self.jogo[i*3:(i+1)*3] for i in range(3)]:
            print(*linha)
            
    # Função para validar jogada
    def validarJogada(self,jogador):
        valor = 10
        simbolo = "\033[32m⩙\033[m" if jogador == 1 else "\033[31mʘ\033[m"
        while True:
            try:
                jogada = int(input(f'Jogador {simbolo}: '))
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
        simbolo = '\033[32m⩙\033[m' if jogador == 1 else '\033[31mʘ\033[m'
        self.jogo[jogda] = simbolo

    # Função para verificar o vencedor
    def verificarVencedor(self, jogo, jogada, simbolo):
        linha_ind = jogada // 3
        linha = jogo[linha_ind*3: (linha_ind+1)*3]
        if all([simb == simbolo for simb in linha]):
            self.parar = True

        col_ind = jogada % 3
        coluna = [jogo[col_ind+i*3] for i in range(3)]
        if all([simb == simbolo for simb in coluna]):
            self.parar = True
        
        if jogada % 2 == 0:
            diagonal1 = [jogo[i] for i in [0,4,8]]
            if all([simb == simbolo for simb in diagonal1]):
                self.parar = True
            diagonal2 = [jogo[i] for i in [2,4,6]]
            if all([simb == simbolo for simb in diagonal2]):
                self.parar = True
   
   #Função para lançar o resultado do jogo
    def lançarResultado(self, jogador):
        if self.parar:
            print('~'*40)
            print('\033[32mFim do jogo!\033[m')
            print(f'\033[32mVitoria para o jogador [{"⩙" if jogador == 1 else "ʘ"}]!\033[m')
            return True
        
        contador = self.jogo.count('_')
        if contador == 0:
            print('~'*40)
            print('\033[32mFim do jogo!\033[m')
            print('\033[32mSem vencedor!\033[m')
            return True

# Função para iniciar o jogo
def jogar():
    while True:
        jogo = JogoDaVelha()
        jogo.Iniciar()
        res = ' '
        while res not in 'SN':
            res = str(input('Quer jogar de novo? [S/N]: ')).strip().upper()[0]
        if res == 'N':
            break

if __name__ == '__main__':
    jogar()