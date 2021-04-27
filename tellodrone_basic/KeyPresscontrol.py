import pygame

def init():
    pygame.init()
    win= pygame.display.set_mode((400,400))

def get_key(keyname):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyname))
    # K_{LEFT}

    if keyInput[myKey]:
        ans = True

    pygame.display.update()

    return ans

def main():
    #print(get_key("a"))
    if get_key("LEFT"):
        print("left key pressed")
    if get_key("RIGHT"):
        print("right key pressed")


if __name__ == '__main__':
    init()
    while True:
        main()