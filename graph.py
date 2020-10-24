import os.path
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
filepath = os.path.dirname(__file__)

# Grafiki okna tytułowego
icon = pygame.image.load(os.path.join(filepath, "data\\pics\\icon.png"))
intro = pygame.image.load(os.path.join(filepath, "data\\introDev\\1x.png")).convert()
bg = pygame.image.load(os.path.join(filepath, "data\\pics\\intro.png")).convert()
kajdanki = [pygame.image.load(os.path.join(filepath, "data\\pics\\kajdanki.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\pics\\kajdanki1.png")).convert()]
pistol = [pygame.image.load(os.path.join(filepath, "data\\pics\\bron.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\pics\\bron1.png")).convert()]
nakladka_bg = pygame.image.load(os.path.join(filepath, "data\\sceny\\nakladka.png")).convert_alpha()

# Intro kafle

kafel = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel.png")).convert_alpha(),
         pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel1.png")).convert_alpha()]
kafel_2 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel2.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel2x.png")).convert_alpha()]
kafel_3 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel3.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel3x.png")).convert_alpha()]
kafel_4 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel4.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel4x.png")).convert_alpha()]
kafel_5 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel5.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel5x.png")).convert_alpha()]
kafel_6 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel6.png")).convert_alpha(),
           pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel6x.png")).convert_alpha()]
kafel_7 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel7.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel7x.png")).convert_alpha()]
kafel_8 = [pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel8.png")).convert_alpha(),
          pygame.image.load(os.path.join(filepath, "data\\introDev\\kafel8x.png")).convert_alpha()]

# Animacja logo

animated_Logo = [pygame.image.load(os.path.join(filepath, "data\\logo\\logo.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo1.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo2.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo3.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo4.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo5.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo6.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo7.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo8.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo9.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo10.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo11.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo12.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo13.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo14.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo15.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo16.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo17.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo18.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo19.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo20.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo21.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo22.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo23.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo24.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo25.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo26.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo27.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo28.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo29.png")),
                pygame.image.load(os.path.join(filepath, "data\\logo\\logo30.png"))]

# Nawigacja

press_Kariera = [pygame.image.load(os.path.join(filepath, "data\\navi\\kariera.png")).convert(),
                 pygame.image.load(os.path.join(filepath, "data\\navi\\kariera1.png")).convert()]
press_Enter = [pygame.image.load(os.path.join(filepath, "data\\navi\\enter.png")).convert(),
               pygame.image.load(os.path.join(filepath, "data\\navi\\enter1.png")).convert()]
press_Option = [pygame.image.load(os.path.join(filepath, "data\\navi\\info.png")).convert(),
                pygame.image.load(os.path.join(filepath, "data\\navi\\info1x.png")).convert()]
cofnij = [pygame.image.load(os.path.join(filepath, "data\\navi\\cofnij.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\cofnij1.png")).convert()]
press_Dalej = [pygame.image.load(os.path.join(filepath, "data\\navi\\dalej.png")).convert(),
               pygame.image.load(os.path.join(filepath, "data\\navi\\dalej1.png")).convert()]
silownia_N = [pygame.image.load(os.path.join(filepath, "data\\navi\\silownia.png")).convert(),
              pygame.image.load(os.path.join(filepath, "data\\navi\\silownia1.png")).convert()]
spacer_N = [pygame.image.load(os.path.join(filepath, "data\\navi\\spacer.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\navi\\spacer1.png")).convert()]
tak = [pygame.image.load(os.path.join(filepath, "data\\navi\\tak.png")).convert(),
       pygame.image.load(os.path.join(filepath, "data\\navi\\tak1.png")).convert()]
nie = [pygame.image.load(os.path.join(filepath, "data\\navi\\nie.png")).convert(),
       pygame.image.load(os.path.join(filepath, "data\\navi\\nie1.png")).convert()]
cela_nav = [pygame.image.load(os.path.join(filepath, "data\\navi\\cela.png")).convert(),
            pygame.image.load(os.path.join(filepath, "data\\navi\\cela1.png")).convert()]
miasto = [pygame.image.load(os.path.join(filepath, "data\\navi\\miasto.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\miasto1.png")).convert()]
zapisz = [pygame.image.load(os.path.join(filepath, "data\\navi\\zapisz.png")).convert(),
          pygame.image.load(os.path.join(filepath, "data\\navi\\zapisz1.png")).convert()]
zapisano = pygame.image.load(os.path.join(filepath, "data\\navi\\zapisano.png")).convert()
kontynuacja = [pygame.image.load(os.path.join(filepath, "data\\navi\\plusz.png")).convert(),
               pygame.image.load(os.path.join(filepath, "data\\navi\\plusz1.png")).convert()]
save_start = [pygame.image.load(os.path.join(filepath, "data\\navi\\continue.png")).convert(),
              pygame.image.load(os.path.join(filepath, "data\\navi\\continue1.png")).convert()]
ide = [pygame.image.load(os.path.join(filepath, "data\\navi\\ide.png")).convert(),
       pygame.image.load(os.path.join(filepath, "data\\navi\\ide1.png")).convert()]
