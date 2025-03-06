import pygame
from pygame.locals import * # O asterístico me diz que dentro do submódulo locals eu vou estar 
                            # inportando todas as funcoes e todas as constantes.
from sys import exit    # esse modulo vai servir pra quando eu fechar a janela do meu jogo, essa mesma função será chamado
from random import randint

# inciando todas as funções e variáveis da biblioteca pygame com o comando abaixo.
pygame.init()

# Variavel para coloca musica de fundo no jogo.
pygame.mixer.music.set_volume(0.05) # vara deixar o volume mais alto ou mais baixo no jogo.
musica_de_fundo = pygame.mixer.music.load('snake_game_python\snake_game_python\jogo_cobrinha\sons\som_de_fundo.wav')
pygame.mixer.music.play(-1)

# Variavel para receber o som da colisao.
som_colisao = pygame.mixer.Sound('snake_game_python\snake_game_python\jogo_cobrinha\sons\som_colisao.wav')

#Variaveis para definir a largura e altura da tela do meu jogo
larg = 640
alt =  480

# Variavel que vai controlar o movimento do meu retangulo.
x_cobra = int(larg / 2)    # essas duas variaveis divindo largura e altura por 2 vai fazer com que meu retangulo apareca no meio da tela.
y_cobra = int(alt / 2)

velocidade = 5
x_controle = velocidade
y_controle = 0

# essas duas variáveis em especifico, será atribuída ao meu objeto que será colidido, ele vai aparecer em algum lugar da tela, 
# por isso o modulo randint poque ai ele vai escolher onde o objeto vai parar.
x_maca = randint(40, 600)
y_maca = randint(40, 480)

# variavel para definir um texto na tela do jogo:
'''
    O primeiro parâmetro é o estlo do texto, 'arial' o segundo é o tamanho do texto '30' o terceiro parametro é 'True' caso voce queira
que o texto fique em negrito ou 'False' caso não queira e o quarto parâmetro é 'True' caso queira se o texto fique em italico ou
'false' caso nao queria.    
'''
fonte = pygame.font.SysFont('gabriola', 40, bold=True, italic=True)
pontos = 0

#Criando o objeto/ variavel que vai ser a tela do meu jogo. Definindo a largura e altura
tela_jogo = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('Jogo da Cobrinha') #Linha de codigo para dar um 'Titulo' para o jogo
relogio = pygame.time.Clock()   # uma variavel para controlar o tempo de frame do meu jogo

 # Lista para armazenar os valores da posisao que a cobra ja assumiu
lista_corpo_da_cobra = []

comprimento_inicial = 5
morte_cobra = False

# Funcao que vai desenhar o corpor da cobra
def crescimento_cobra(lista_corpo_da_cobra):
    for Xey in lista_corpo_da_cobra:
        pygame.draw.rect(tela_jogo, (0, 255, 0), (Xey[0], Xey[1], 20, 20))

def reiniciar_jogo():   # função criada para reiniciar o jogo jogo quando o usuário precisar.
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca_da_cobra, lista_corpo_da_cobra, x_maca, y_maca, morte_cobra
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(larg / 2)    
    y_cobra = int(alt / 2)
    lista_cabeca_da_cobra = []
    lista_corpo_da_cobra = []
    x_maca = randint(40, 600)
    y_maca = randint(40, 480)
    morte_cobra = False

''' 
    Criando o loop principal do jogo.
Todo jogo se passa dentro de um loop infinito ou um loop principal
a cada segundo que o jogo se passa ele tem que estar atualizando.

criando o loo do jogo, onde todo o scrit do jogo estara dentro desse lopp, ou quase todo.

'''
while True:
    relogio.tick(30) # aqui dentro do meu loop, eu coloco quantos frame por segundo eu quero que o meu jogo tenha
    tela_jogo.fill((0,0,0)) # esse comando deixa a minha tela toda preta.
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
     # loop 'for' vai ter a tarefa de checar cada iteração do meu loop principal se algum evento ocorreu
    for event in pygame.event.get():
        if event.type == QUIT:  # Condicao para saber se o usuário clicou em fechar a janela
            pygame.quit()
            exit()

        if event.type == KEYDOWN:   # condição para reconhecer quando o usuário aperta a tecla para o objto se mover ..
            if event.key == K_a:    # condcao para quando ser precionado a tecla a o objeto se mover para esquerda.
                if x_controle == velocidade:    # Condição para nao deixa mover para um sentido contrario do outro
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
                                
    ''' Desenhando um retângo na tela do jogo. o primeiro nome dentro dos parentes, é a tela_jogo
        seguido da virgula, e depois tenho mais dois parenteses() que na verdade se chama 'tuplas' dentro dessas tulpas eu vou definir
        as cores do meu retangulo sendo separado por virgulas também (255,0,0)
        depois tenho que colocar outra tupla() e dentro delas vai ser a posicao do meu retângulo, ou seja, tenho que passa o x e y
        em seguido da largura do retângulo e a altura do retângulo (200, 300, 40, 50)'''
    cobra = pygame.draw.rect(tela_jogo, (0,255,0), (x_cobra, y_cobra, 15, 15))
    # desenhando um circulo
    maca =  pygame.draw.circle(tela_jogo, (255,0, 0), (x_maca, y_maca), 9) # a diferena do circulo eh que no final dos parametros ele leva um raio,
                                                              # no exemplo eu coloquei raio de 40
    if cobra.colliderect(maca):  # essa condição vai verificar se o retângulo colidiui com o circulo
        x_maca = randint(40, 600)  # toda vez que o meu objeto colidir com o circulo ele vai parar um outro lugar
        y_maca = randint(40, 480)  # atraves do comando do randint
        pontos = pontos + 1
        som_colisao.play()
        comprimento_inicial = comprimento_inicial + 1

    # lista que vai armazenar os valores x e y da cabeca da cobra
    lista_cabeca_da_cobra = []
    lista_cabeca_da_cobra.append(x_cobra) # para armazenar o valor da posicao x da cobra
    lista_cabeca_da_cobra.append(y_cobra) # para armazenar o valor da posicao y da cobra

    lista_corpo_da_cobra.append(lista_cabeca_da_cobra)

    if lista_corpo_da_cobra.count(lista_cabeca_da_cobra) > 1:   # Condição para saber se a cobra encostou nela mesma
        fonte2 = pygame.font.SysFont('arial', 20, bold=True, italic=True)
        mensagem1 = "GAME OVER! PRECIONE a tecla R para jogar novamente."
        text_formatado = fonte2.render(mensagem1, True,(0,0,0))
        retangulo_text = text_formatado.get_rect()

        morte_cobra = True
        while morte_cobra:
            tela_jogo.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == quit:
                    pygame.quit
                    exit()
                if event.type == KEYDOWN:   # Condição para saber se o usuário clicou em alguma tecla
                    if event.key == K_r:    # Condição para saber se o usuário clicou na tecla R
                        reiniciar_jogo()    # função sendo chamada para reinicicar o jogo

            retangulo_text.center = (larg//2, alt//2)
            tela_jogo.blit(text_formatado, retangulo_text)
            pygame.display.update()

    if x_cobra > larg:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = larg
    if y_cobra > alt:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = alt

    if len(lista_corpo_da_cobra) > comprimento_inicial:
        del lista_corpo_da_cobra[0]

    crescimento_cobra(lista_corpo_da_cobra)

    tela_jogo.blit(texto_formatado, (10,20))
    pygame.display.update() # Essa linha de codigo faz com que cada iteração do loop principal do jogo ela atualiza a tela do jogo
                            # se não tiver essa linha de codigo, o jogo vai rodar apenas uma vez.
            