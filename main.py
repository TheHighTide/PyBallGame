import pygame,sys,pymunk,keyboard
from pymunk.vec2d import Vec2d

# Player Options
player_speed = 250
player_slowrate = 0.15
player_jumppower = 375

# World Options
gravity_scale = 500

# Game Options
game_title = "HighTide's Ball Game"

# Window Setup
game_icon = pygame.image.load('icon.png')
pygame.display.set_caption(game_title)
pygame.display.set_icon(game_icon)

# Game Setup
player_slowrate = 1.0 - player_slowrate


def create_circle(space):
    body = pymunk.Body(1, 50, body_type = pymunk.Body.DYNAMIC)
    body.position = (400, 0)
    body.friction = 500
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape


def create_static_square(space, posx, posy, height, width):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (posx, posy)
    body.friction = 5000
    shape = pymunk.Poly.create_box(body, (width, height))
    space.add(body, shape)
    return shape


def draw_circles(circles):
    for circle in circles:
        pos_x = int(circle.body.position.x)
        pos_y = int(circle.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 80)


def draw_squares(squares):
    for square in squares:
        pos_x = int(square.body.position.x)
        pos_y = int(square.body.position.y)
        pygame.draw.poly(screen, (0, 0, 0), (pos_x, pos_y), 80)

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, gravity_scale)
circles = []
circles.append(create_circle(space))

main_circle = circles[0]

ismoving_left = False
ismoving_right = False
canjump = False

while True: # Game Loop & Game Code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and canjump:
            main_circle.body.velocity = (0, -player_jumppower)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ismoving_right = True
            elif event.key == pygame.K_a:
                ismoving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ismoving_right = False
            elif event.key == pygame.K_a:
                ismoving_left = False


    if main_circle.body.position >= (main_circle.body.position.x, 719):
        canjump = True
    elif main_circle.body.position < (main_circle.body.position.x, 719):
        canjump = False


    if ismoving_left and ismoving_right:
        main_circle.body.velocity = (main_circle.body.velocity.x * 0.9, main_circle.body.velocity.y)
    elif ismoving_right:
        main_circle.body.velocity = (player_speed, main_circle.body.velocity.y)
    elif ismoving_left:
        main_circle.body.velocity = (-player_speed, main_circle.body.velocity.y)

    
    screen.fill((217, 217, 217))

    if not ismoving_left and not ismoving_right:
        main_circle.body.velocity = (main_circle.body.velocity.x * player_slowrate, main_circle.body.velocity.y)
    create_static_square(space, 400, 850, 100, 800)
    create_static_square(space, 400, -50, 100, 800)
    create_static_square(space, 850, 400, 800, 100)
    create_static_square(space, -50, 400, 800, 100)
    draw_circles(circles)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)