import pygame,os

SCALE=3
TITLE='Super Mario Bros. 3'
SCREEN_SIZE=SCREEN_WIDTH,SCREEN_HEIGHT=256*SCALE,224*SCALE
FPS=60

CURRENT_PATH=os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH=os.path.join(CURRENT_PATH,'image')