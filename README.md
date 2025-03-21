# 操作逻辑：

enter：重置关卡（重新开始），并在显示通关时进入下一关。

Up：向上移动。

Down：向下移动。

Left：向左移动。

Right：向右移动。

e：强制进入下一关。

r：强制进入上一关。

f：重新开始所有关卡。



为了避免版权原因本游戏全部素材均为最简单的图片。

如需更改素材图片只需将原图片删除在按照原本的图片大小和名称放入即可。



代码更改。

一：更改角色，只需将以下代码取消注释并在==pic\figure==文件夹中放入其他角色图片（gif格式）。

1.

~~~python
turtle.onkey(tf_figure, 'v')
~~~

2.

~~~python
def tf_figure():  
    global figure, figure_count  
    figure_count += 1  
    if figure_count == 7:  #按照figure文件夹内图片个数填写（默认为7）
        figure_count = 0
~~~

3.（需要再此列表中添加图片的路径和名称）

~~~python
figure = ['pic/figure/1.gif']#需要输入相对路径路径+图片名
~~~

完成后可通过==v==键更换角色

二：更改背景，只需将以下代码取消注释并在==pic\background==文件夹中放入背景图片（gif格式）。
1.

~~~python
turtle.onkey(tf_bgpic, 'q')
~~~

2.

~~~python
def tf_bgpic():  
    global bgpic, bgpic_count  
    turtle.bgpic(bgpic[bgpic_count])  
    bgpic_count += 1  
    if bgpic_count == 5:  #按照background文件夹内图片个数填写（默认为5）
        bgpic_count = 0
~~~

3.（添加一个列表并将路径和图片名称填入）

~~~python
bgpic = ['pic/background/图片名']#需要输入相对路径路径+图片名
~~~

完成后可通过==q==键更换背景

三：添加背景音乐，只需将以下代码取消注释并在==bgm==文件夹中放入背音乐（至少4首，并均为MP3格式并命名为bgm、bgm2、bgm3、bgm4）。
1.
~~~python
turtle.onkey(music_1, '1')  
turtle.onkey(music_2, '2')  
turtle.onkey(music_3, '3')  
turtle.onkey(music_4, '4')
~~~

2.

~~~python
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
~~~

3.

~~~python
pygame.mixer.init()
bgm = pygame.mixer.Sound('bgm/bgm.mp3')  
bgm2 = pygame.mixer.Sound('bgm/bgm2.mp3')  
bgm3 = pygame.mixer.Sound('bgm/bgm3.mp3')  
bgm4 = pygame.mixer.Sound('bgm/bgm4.mp3')
~~~

四：更换砖块，只需将准备好的70 * 70大小的砖块图片（gif格式）放入==pic\img==并将需要替换的文件删除，再将需要替换的文件名称命名新文件。