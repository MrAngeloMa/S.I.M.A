# Mapa.py
import pygame

class Porta: # Cria a classe das Portas
    def __init__(self, x, y, largura, altura, id=-1):
       self.x = x
       self.y = y
       self.altura = altura
       self.largura = largura
       self.id = id

class Sala: # Cria a classe das Salas
    def __init__(self, x, y, largura, altura):
       self.x = x
       self.y = y
       self.altura = altura
       self.largura = largura
       self.nmax = 0

class Corredor: # Cria a classe dos corredores
    def __init__(self, x, y, largura, altura):
       self.x = x
       self.y = y
       self.altura = altura
       self.largura = largura
       self.porta = []

    def addPorta(self, porta): # Adiciona a porta
        self.porta.append(porta)    

    def VerificaPorta(self, player): # Verifica se o player passou pela porta
      for porta in self.porta: 
        rectporta = pygame.Rect((porta.x + self.x, porta.y + self.y, porta.largura, porta.altura))
        if player.colliderect(rectporta):
            return porta.id
      return None

class Mapa: # Cria a classe dos Bots
    def __init__(self, start_x, start_y, id):
       self.start_x = start_x
       self.start_y = start_y
       self.id = id
       self.salas = []
       self.corredores = []

    def addSala(self, sala): # Adiciona a sala
        self.salas.append(sala)    

    def addCorredor(self, corredor): # Adiciona o corredor
        self.corredores.append(corredor)

def DesenhaMapa(Mapa, screen): # Desenha o mapa atual com suas salas e corredores
    for sala in Mapa.salas: # Desenha as salas do mapa
        pygame.draw.rect(screen, (211, 211, 211), (sala.x, sala.y, sala.largura, sala.altura))

    for corredor in Mapa.corredores: # Desenha os corredores da sala
        pygame.draw.rect(screen, (169, 169, 169), (corredor.x, corredor.y, corredor.largura, corredor.altura))
        for porta in corredor.porta: # Desenha as portas dos corredores
            pygame.draw.rect(screen, (211, 211, 211), (porta.x + corredor.x, porta.y + corredor.y, porta.largura, porta.altura))

def MudaMapa(player, mapa_atual, bot_atual, sala_atual, TMapas, TBots, TSalas): # Muda o Mapa atual
    for corredor in mapa_atual.corredores:
        porta_id = corredor.VerificaPorta(pygame.Rect((player.x, player.y, player.raio, player.raio)))
        if porta_id != None:
            id = porta_id - 1
            mapa_novo = TMapas[id]      # Atualiza o mapa atual
            bot_novo = TBots[id]        # Atualiza a lista de bot atual
            sala_nova = TSalas[id]      # Atualiza a sala atual

            # Muda a posição do player ao avançar um mapa
            if mapa_atual.id < porta_id:
                player.x = 1200 - player.x
            
            # Muda a posição do player ao retornar um mapa
            if mapa_atual.id > porta_id:
                player.x = 1200 - (player.raio + 5) - player.x

        else:
            mapa_novo = mapa_atual
            bot_novo = bot_atual
            sala_nova = sala_atual
                
        return[mapa_novo, bot_novo, sala_nova]
