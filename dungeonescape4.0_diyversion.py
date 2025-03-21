import turtle
import copy
import random
import time
import pygame

# -----------------------------------------------------------------
# 1.基本信息区，放置游戏相关的一些信息
# pygame.mixer.init()

size = 70
level_n = 1

from map import map_1
from map import map_2
from map import map_3
from map import map_4
from map import map_5
from map import map_6
from map import map_7
from map import map_8
from map import map_9
from map import map_10
from map import map_11

levels = [map_1.level1, map_2.level2, map_3.level3, map_4.level4, map_5.level5, map_6.level6, map_7.level7, map_8.level8, map_9.level9, map_10.level10, map_11.level11]
grid = copy.deepcopy(levels[level_n - 1])
width = len(grid[0])
height = len(grid)
origin_x = -(width-1) / 2 * size
origin_y = (height-1) / 2 * size
players = [[1, 1], [1, 3], [1, 1], [3, 5], [1, 1], [3, 2], [1, 2], [2, 1], [1, 6], [2, 1], [1, 1]]
player_x = players[level_n - 1][0]
player_y = players[level_n - 1][1]
result = 2
bgpic_count = 0
figure_count = 0
# bgm = pygame.mixer.Sound('bgm/bgm.mp3')
# bgm2 = pygame.mixer.Sound('bgm/bgm2.mp3')
# bgm3 = pygame.mixer.Sound('bgm/bgm3.mp3')
# bgm4 = pygame.mixer.Sound('bgm/bgm4.mp3')

# ------------------------------------------------------------
# 2.功能模块区，主要放置函数
'''
def music_4():
    global bgm, bgm2
    bgm4.stop()
    bgm4.play()
    bgm.stop()
    bgm2.stop()
    bgm3.stop()

def music_3():
    global bgm, bgm2
    bgm3.stop()
    bgm3.play()
    bgm.stop()
    bgm2.stop()
    bgm4.stop()

def music_2():
    global bgm, bgm2
    bgm2.stop()
    bgm2.play()
    bgm.stop()
    bgm3.stop()
    bgm4.stop()

def music_1():
    global bgm, bgm2
    bgm.stop()
    bgm.play()
    bgm2.stop()
    bgm3.stop()
    bgm4.stop()
'''
'''
def tf_figure():
    global figure, figure_count
    figure_count += 1
    if figure_count == 7:
        figure_count = 0

def tf_bgpic():
    global bgpic, bgpic_count
    turtle.bgpic(bgpic[bgpic_count])
    bgpic_count += 1
    if bgpic_count == 5:
        bgpic_count = 0
'''

def start_over():
    global level_n, result, level_n, grid, player_x, player_y, width, height, origin_x, origin_y, size
    level_n = 1

    result = 2
    grid = copy.deepcopy(levels[level_n - 1])
    width = len(grid[0])
    height = len(grid)
    origin_x = 0 - size * (width - 1) / 2
    origin_y = 0 + size * (height - 1) / 2
    player_x = players[level_n - 1][0]
    player_y = players[level_n - 1][1]

def blink11():
    global grid, player_x, player_y
    if player_x == 6 and player_y == 1:
        if level_n == 11:
            player_x = 6
            player_y = 3
    elif player_x == 6 and player_y == 3:
        if level_n == 11:
            player_x = 6
            player_y = 1

def blink5():
    global grid, player_x, player_y
    if player_x == 7 and player_y == 1:
        if level_n == 5:
            player_x = 7
            player_y = 3
    elif player_x == 7 and player_y == 3:
        if level_n == 5:
            player_x = 7
            player_y = 1

def force_the_previous_step():
    global level_n, result, level_n, grid, player_x, player_y, width, height, origin_x, origin_y, size
    level_n -= 1

    result = 2
    grid = copy.deepcopy(levels[level_n - 1])
    width = len(grid[0])
    height = len(grid)
    origin_x = 0 - size * (width - 1) / 2
    origin_y = 0 + size * (height - 1) / 2
    player_x = players[level_n - 1][0]
    player_y = players[level_n - 1][1]

def force_skips():
    global level_n, result, level_n, grid, player_x, player_y, width, height, origin_x, origin_y, size
    level_n += 1

    result = 2
    grid = copy.deepcopy(levels[level_n - 1])
    width = len(grid[0])
    height = len(grid)
    origin_x = 0 - size * (width - 1) / 2
    origin_y = 0 + size * (height - 1) / 2
    player_x = players[level_n - 1][0]
    player_y = players[level_n - 1][1]

def next_level():
    global result, level_n, grid, player_x, player_y, width, height, origin_x, origin_y, size
    if result == 1:
        level_n += 1

    result = 2
    grid = copy.deepcopy(levels[level_n - 1])
    width = len(grid[0])
    height = len(grid)
    origin_x = 0 - size * (width - 1) / 2
    origin_y = 0 + size * (height - 1) / 2
    player_x = players[level_n - 1][0]
    player_y = players[level_n - 1][1]

def show_result():
    global result, grid, player_x, player_y
    if grid[player_y][player_x] == 4:
        result = 0

    else:
        for i in grid:
            if 2 in i:
                result = 2
                break
        else:
            result = 1

def change_grid():
    global grid, player_x, player_y
    if grid[player_y][player_x] == 2:
        grid[player_y][player_x] = 3

    elif grid[player_y][player_x] == 3:
        grid[player_y][player_x] = 4

    elif grid[player_y][player_x] == 6:
        grid[player_y][player_x] = 3

    blink5()
    blink11()
    show_result()

def draw(pen, img, x, y):
    global  origin_x, origin_y, size
    pen.goto(origin_x + x * size, origin_y - y * size)
    pen.shape(img)
    pen.stamp()

def move_up():
    global player_x, player_y
    if result != 2:
        return

    player_y -= 1

    if player_y < 0:
        player_y = 0
        return

    elif grid[player_y][player_x] == 1:
        player_y += 1
        return

    change_grid()

def move_down():
    global player_x, player_y
    if result != 2:
        return

    player_y += 1

    if player_y >= height:
        player_y -= 1
        return

    elif grid[player_y][player_x] == 1:
        player_y -= 1
        return

    change_grid()

def move_left():
    global player_x, player_y
    if result != 2:
        return

    player_x -= 1

    if player_x < 0:
        player_x = 0
        return

    elif grid[player_y][player_x] == 1:
        player_x += 1
        return

    change_grid()

def move_right():
    global player_x, player_y
    if result != 2:
        return

    player_x += 1

    if player_x >= width:
        player_x -= 1
        return

    elif grid[player_y][player_x] == 1:
        player_x -= 1
        return

    change_grid()

# ------------------------------------------------------------
# 3.操作事件区，放置键鼠操作相关的内容

turtle.onkey(move_up, 'Up')
turtle.onkey(move_down, 'Down')
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(next_level, 'Return')
turtle.onkey(force_skips, 'e')
turtle.onkey(force_the_previous_step, 'r')
turtle.onkey(start_over, 'f')
# turtle.onkey(tf_bgpic, 'q')
# turtle.onkey(tf_figure, 'v')
# turtle.onkey(music_1, '1')
# turtle.onkey(music_2, '2')
# turtle.onkey(music_3, '3')
# turtle.onkey(music_4, '4')
turtle.listen()

# ------------------------------------------------------------
# 4.场景素材区，添加游戏画面相关的素材

tile_shapes = ['pic/img/空.gif', 'pic/img/墙壁2.gif', 'pic/img/空.gif', 'pic/img/目标.gif', 'pic/img/箱子.gif', 'pic/img/传送门.gif', 'pic/img/空.gif', 'pic/img/传送门.gif']
for i in tile_shapes:
    turtle.addshape(i)

figure = ['pic/figure/1.gif']
for i in figure:
    turtle.addshape(i)

result_shapes = ['pic/img/失败.gif', 'pic/img/成功.gif', 'pic/img/空.gif']
for i in result_shapes:
    turtle.addshape(i)

# ------------------------------------------------------------
# 5.画面绘制区，绘制场景用的画笔，绘制场景的代码

p = turtle.Pen()
p.penup()
p.hideturtle()
turtle.tracer(False)

while True:
    p.clear()
    for i in range(width):
        for j in range(height):
            draw(p, tile_shapes[grid[j][i]], i, j)

    draw(p, figure[figure_count], player_x, player_y)
    draw(p, result_shapes[result], (width - 1) / 2, (height - 1) / 2)

    # if level_n == 4 and player_x == 1 and player_y == 4:
    #     num = random.randint(1, 2)
    #     print(num)
    #
    #     if num == 1:
    #         force_skips()
    #
    #     else:
    #         move_right()
    #
    if level_n == 12:
        break

    turtle.update()

for i in range(300):
    turtle.tracer(False)
    p.backward(1)
    time.sleep(0.01)
    p.write('游戏结束！可退出程序重新游玩。', font=('Arial', 24, 'normal'))
    turtle.update()
    p.clear()

turtle.done()