from pico2d import *
import random

class Grass:
    # 생성사 함수 : 객체의 초기 상태
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Sball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        self.frame = 0
        self.y -= random.randint(0, 10)

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 21, 21, self.x, self.y)

class Bball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.frame = 0
        self.image = load_image('ball41x41.png')

    def update(self):
        self.frame = 0
        self.y -= random.randint(0, 10)

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 41, 41, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global ball
    global world

    running = True
    world = [] # world 리스트를 만들어 update_world 와 render_world를 고칠 필요가 없어짐

    grass = Grass() # 잔디 생성
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    sball = [Sball() for i in range(10)]
    world += sball

    bball = [Bball() for i in range(10)]
    world += bball

running = True

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
running = True
while running:
    # Game logic
    handle_events()
    update_world() # 상호작용 시뮬레이션
    render_world() # 결과 보여주기
    delay(0.05)

# finalization code
close_canvas()
