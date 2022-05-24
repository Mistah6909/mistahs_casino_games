import pygame

class entities(pygame.sprite.Sprite):
  def __init__(self,pos,image):
    super().__init__()
    self.image = image
    self.image =  pygame.transform.scale(pos,image)
    self.rect = self.image.get_rect()
