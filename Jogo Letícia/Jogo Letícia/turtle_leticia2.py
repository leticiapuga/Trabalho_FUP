#Universidade Federal do Ceará
#Ciência_da_computação_2022.2
#Fundamentos_de_programação
#Professor: Rafael Fernandes Ivo
#Aluna: Letícia de Miranda Puga
#Matrícula: 541559

#Biblioteca
import turtle
import random

#Criar janela
janela = turtle.Screen() #Tela do jogo
janela.tracer(0)

#Variáveis principais
string_dragao = 'Dragon_fup_le.gif'
string_flecha = 'Flecha_fup_le.gif'
string_princesa = 'Princesa_fup_le2.gif'
string_cenario = 'Caminho_pedra_fup_le.gif'
string_arvore = 'Arvore_fup_le.gif'
string_borda = 'Borda_marrom_fup_le2.gif'

#Criar shapes
janela.addshape(string_dragao)
janela.addshape(string_flecha)
janela.addshape(string_princesa)
janela.addshape(string_cenario)
janela.addshape(string_arvore)
janela.addshape(string_borda)


#Dimensão da tela
janela.setup(750, 600)  #Tamanho da tela
janela.bgpic('Caminho_pedra_fup_le.gif') #Imagem de fundo

#Criação das arvores

offset_y = 2 #Deslocamento_do_y

arvore = turtle.Turtle()
arvore2 = turtle.Turtle()
arvore3 = turtle.Turtle()
arvore4 = turtle.Turtle()
arvore5 = turtle.Turtle()
arvore6 = turtle.Turtle()

#Personagem dragão
dragao = turtle.Turtle()
dragao.shape(string_dragao)
dragao.penup()
dragao.goto(0,-100)

#Princesa/Combustível
princesa = turtle.Turtle()
princesa.shape(string_princesa)
princesa.penup()
princesa.goto(random.randint(-100, 100),300)
princesa.right(90)

#Flecha/Obstáculo
flecha = turtle.Turtle()
flecha.shape(string_flecha)
flecha.penup()
flecha.goto(random.randint(-100, 100),300)
flecha.right(90)

#Gameover
gameover = turtle.Turtle()
gameover.penup()
gameover.ht()  #Esconder a tartaruga
gameover.color('yellow')
gameover.goto(-145,0)

#Pontuação do jogo
pontuacao = turtle.Turtle()
pontuacao.color('white')
pontuacao.penup()
pontuacao.hideturtle()
pontuacao.goto(-360,200)

gasolina = 20  #Medidor de combustível
distancia = 0  #Medidor da distância

#Bordas da tela
borda_direita = turtle.Turtle()
borda_direita.penup()
borda_direita.goto(350,0)
borda_direita.color('white')
borda_direita.shape(string_borda)

borda_esquerda = turtle.Turtle()
borda_esquerda.penup()
borda_esquerda.goto(-350,0)
borda_esquerda.color('white')
borda_esquerda.shape(string_borda)

def arvores():  #Função que define as posições das arvores

    #arvore = turtle.Turtle()
    arvore.penup()
    arvore.goto(280, 300)
    arvore.shape(string_arvore)

    #arvore2 = turtle.Turtle()
    arvore2.penup()
    arvore2.goto(250, 50)
    arvore2.shape(string_arvore)

    #arvore3 = turtle.Turtle()
    arvore3.penup()
    arvore3.goto(290, -200)
    arvore3.shape(string_arvore)

    #arvore4 = turtle.Turtle()
    arvore4.penup()
    arvore4.goto(-250, -250)
    arvore4.shape(string_arvore)

    #arvore5 = turtle.Turtle()
    arvore5.penup()
    arvore5.goto(-280, -75)
    arvore5.shape(string_arvore)

    #arvore6 = turtle.Turtle()
    arvore6.penup()
    arvore6.goto(-290, 220)
    arvore6.shape(string_arvore)

arvores()

def movimento_arvores(offset):

    if arvore.ycor() < -250:
        arvore.sety(520)
    arvore.sety(arvore.ycor() - offset)

    if arvore2.ycor() < -250:
        arvore2.sety(520)
    arvore2.sety(arvore2.ycor() - offset)

    if arvore3.ycor() < -250:
        arvore3.sety(520)
    arvore3.sety(arvore3.ycor() - offset)

    if arvore4.ycor() < -250:
        arvore4.sety(520)
    arvore4.sety(arvore4.ycor() - offset)

    if arvore5.ycor() < -250:
        arvore5.sety(520)
    arvore5.sety(arvore5.ycor() - offset)

    if arvore6.ycor() < -250:
        arvore6.sety(520)
    arvore6.sety(arvore6.ycor() - offset)

#Funções de movimento
def dragao_esquerda():
    dragao.back(5)

def dragao_direita():
    dragao.forward(5)

#Limites das bordas
def barreira():
    if dragao.xcor() >= 200:
        gameover.write('GAME OVER', font=('Courier', 40, 'bold'))
        turtle.done()
    if dragao.xcor() <= -200:
        gameover.write('GAME OVER', font=('Courier', 40, 'bold'))
        turtle.done()

def placar():
    global distancia  #Habilitar variável distancia
    global gasolina   #Habilitar variável gasolina

    gasolina -= 0.02
    distancia += 0.02

    if gasolina <= 0: #Finaliza o jogo ao zerar o combustível
        gameover.write('GAME OVER', font=('Courier', 40, 'bold'))
        turtle.done()

    if princesa.xcor() + 15 >= dragao.xcor() - 15 and princesa.xcor() - 15 <= dragao.xcor() + 15 and princesa.ycor() + 15 >= dragao.ycor() - 15 and princesa.ycor() - 15 <= dragao.ycor() + 15:
        princesa.goto(random.randint(-100, 100), 300)
        gasolina += 10

    pontuacao.clear()
    pontuacao.write(f'DISTÂNCIA: {int(distancia)}\nGASOLINA: {int(gasolina)}',font=('Consolas', 15))

#Movimentos do obstáculo e do combustível
def mover_flecha_princesa():
    flecha.forward(5)
    princesa.forward(4)

    if flecha.ycor() <= -600:
        flecha.goto(random.randint(-100, 100),300)

    if flecha.xcor() + 15 >= dragao.xcor() - 15 and flecha.xcor() - 15 <= dragao.xcor() + 15 and flecha.ycor() + 15 >= dragao.ycor() - 15 and flecha.ycor() - 15 <= dragao.ycor() + 15:
        gameover.write('GAME OVER', font=('Courier', 40, 'bold'))
        turtle.done() #Colisão do Dragão com o obstáculo finaliza o jogo

    if princesa.ycor() <= -600:
        princesa.goto(random.randint(-100, 100), 300)

def movimentos():

    mover_flecha_princesa()
    movimento_arvores(offset_y)
    placar()
    barreira()

    janela.onkeypress(dragao_esquerda, 'a') #Movimento do personagem à esquerda
    janela.onkeypress(dragao_direita, 'd')  #Movimento do personagem à direita

    janela.listen()  #Para seguir os comandos

    janela.update()  #Para manter a tela aberta
    turtle.ontimer(movimentos, 1000//60) #Temporizador FPS

def reset():
    global gasolina
    global distancia

    gameover.clear()

    dragao.goto(0,-200)
    flecha.goto(random.randint(-100, 100), 300)
    princesa.goto(random.randint(-100, 100), 300)

    gasolina = 20
    distancia = 0

    pontuacao.clear() #Para limpar o placar

    movimentos()  #Função dos movimentos

janela.onkeypress(reset, 'space') #Inicia o jogo com a tecla espaço
janela.listen()   #Para seguir os comandos
janela.mainloop() #Para exibir a tela