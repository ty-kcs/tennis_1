import pyxel

def court():
 #コートの描画
        pyxel.cls(1)
        # 四角形を描画、引数は(左上の点の座標x, y, 幅w, 高さh, 色)
        pyxel.rect(70, 0, 360, 390, 2)
        pyxel.rect(247, 0, 6, 200, 7)
        pyxel.rect(115, 200 , 270, 6, 7)
        pyxel.rect(115,0, 6, 390, 7) #シングルス左
        pyxel.rect(385, 0, 6, 390, 7)#シングルス右
        pyxel.rect(430, 0, 6, 390, 7)
        pyxel.rect(430, 0, 6, 390, 7)
        pyxel.rect(70, 390, 366, 6, 7)
        pyxel.rect(70, 0, 6, 390, 7)
        pyxel.rect(247, 380, 6, 10, 7)



class Racquet:
    
    def __init__(self, height, width, color):
        self.h = height
        self.center_x = pyxel.mouse_x
        self.center_y = 420
        self.w = width
        self.color = color
        self.angle = 0
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.angle += 7
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.angle -= 7
    def draw(self):
        pyxel.line(self.center_x - self.w/2 * pyxel.cos(self.angle) - self.h/2 * pyxel.sin(self.angle),self.center_y + self.w/2 * pyxel.sin(self.angle) - self.h/2 * pyxel.cos(self.angle),self.center_x - self.w/2 * pyxel.cos(self.angle) + self.h/2 * pyxel.sin(self.angle),self.center_y + self.w/2 * pyxel.sin(self.angle) + self.h/2 * pyxel.cos(self.angle), self.color) #左の縦線
         
        pyxel.line(self.center_x + self.w/2 * pyxel.cos(self.angle) - self.h/2 * pyxel.sin(self.angle),self.center_y - self.w/2 * pyxel.sin(self.angle) - self.h/2 * pyxel.cos(self.angle),self.center_x + self.w/2 * pyxel.cos(self.angle) + self.h/2 * pyxel.sin(self.angle),self.center_y - self.w/2 * pyxel.sin(self.angle) + self.h/2 * pyxel.cos(self.angle), self.color)#右の縦線
        
        pyxel.line(self.center_x - self.w/2 * pyxel.cos(self.angle) - self.h/2 * pyxel.sin(self.angle),self.center_y + self.w/2 * pyxel.sin(self.angle) - self.h/2 * pyxel.cos(self.angle),self.center_x + self.w/2 * pyxel.cos(self.angle) - self.h/2 * pyxel.sin(self.angle),self.center_y - self.w/2 * pyxel.sin(self.angle) - self.h/2 * pyxel.cos(self.angle), self.color)#上の横線
        
        pyxel.line(self.center_x - self.w/2 * pyxel.cos(self.angle) + self.h/2 * pyxel.sin(self.angle),self.center_y + self.w/2 * pyxel.sin(self.angle) + self.h/2 * pyxel.cos(self.angle),self.center_x + self.w/2 * pyxel.cos(self.angle) + self.h/2 * pyxel.sin(self.angle),self.center_y - self.w/2 * pyxel.sin(self.angle) + self.h/2 * pyxel.cos(self.angle), self.color)#下の横線
        
    def hit(self, ball):
        #座標が一致していれば
        if (ball.y >= 418 and ball.x >= self.center_x - self.w/2 and ball.x <= self.center_x + self.w/2):
            return True
        #そうでなければ
        else:
            return False
        
class Ball:
        r = 5
        color = 10

        def __init__(self):
            self.restart()
            self.points = 0
            self.speed = self.points + 3
        
        def move(self):
            self.speed = self.points + 3
            self.x += self.vx * self.speed
            self.y += self.vy * self.speed
        
        def restart(self):
            self.x = pyxel.rndi(115, 385)
            self.y = 0
            if self.x <=110:
                self.angle = 90
            elif self.x >= 380:
                self.angle = 90
            else:
                self.angle = pyxel.rndi(75, 105)
            self.vx = pyxel.cos(self.angle)
            self.vy = pyxel.sin(self.angle)
            
        def draw(self):
            pyxel.circ(self.x, self.y, Ball.r, Ball.color)

class Target:
    length = 50
    height = 5
    color = 4
    
    def __init__(self):
        self.restart()
        
    def restart(self):
        self.x = pyxel.rndi(70, 360)
        self.y = 5
    
    def draw(self):
        pyxel.rect(self.x, self.y, Target.length, Target.height, Target.color)
    
    def hit(self, ball):
        #座標が一致していれば
        if (ball.y <= 7 and ball.x >= self.x and ball.x <= self.x + Target.length):
            return True
        #そうでなければ
        else:
            return False

class Clock:
  # 最初の位置と色を(x,y,c)で指定してインスタンス生成
  def __init__(self,x,y,c):
    self.x = x
    self.y = y
    self.c = c
    self.sec = 0
    self.min = 0

  # 更新ごとに経過秒数を設定する
  def update(self):
    # フレームカウントを30で割って経過秒数を得て、それを内部時間の変数self.tに代入
    # 小数点以下を切り捨てるため、//を使う
    self.sec = pyxel.frame_count // 30
    self.min = self.sec // 60
  def draw(self):
    pyxel.text(self.x,self.y,"Time: %02d:%02d" % (self.min,self.sec%60),self.c)

    

class App:
    def __init__(self):
        self.game_over = False
        pyxel.init(500, 500)
        org_colors = pyxel.colors.to_list() # 表示色リストの取得
        pyxel.colors[1] = 0x6c935c # 緑色
        pyxel.colors[2] = 0x3c638e # 青色  
        self.racquet = Racquet(10, 40, 4)
        self.ball = Ball()
        self.ball_hit = False
        self.target = Target()
        self.clock = Clock(250,480,7)
        pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.run(self.update, self.draw)
        
        
        
    def update(self):
        if self.clock.sec >= 60:
            self.game_over = True
        if self.game_over:
            return
        self.racquet.center_x = pyxel.mouse_x
        self.racquet.update()
        self.ball.move()
        self.clock.update()
        if self.ball.x < 0 or self.ball.x > 500 or self.ball.y < 0 or self.ball.y > 500:
            self.ball.restart()
        if self.racquet.hit(self.ball): #ラケットに当たったら
            self.ball.angle = self.racquet.angle 
            self.ball.vy = pyxel.cos(self.ball.angle) * -1
            self.ball.vx = pyxel.sin(self.ball.angle) * -1
        if self.target.hit(self.ball): #ターゲットに当たったら
            self.target.restart()
            pyxel.play(0, 0)
            self.ball.points += 1
        
    def draw(self):
        pyxel.cls(0)
        court()
        self.racquet.update()
        
        # ラケットの描画
        self.racquet.draw()
        #ボールの描画
        self.ball.draw()
        #ターゲットの描画
        self.target.draw()
        #時間の描画
        self.clock.draw()
        #ポイントの描画
        pyxel.text(10, 10, "points:" + str(self.ball.points), 7)
        
        if self.game_over >= 60:
            pyxel.text(250, 250, "GAME FINISHED!!", 7)
            pyxel.stop()
        
app = App()