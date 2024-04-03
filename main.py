import js as p5

print('Assignment #7 (Final Project)')

bg = p5.loadImage('weather/rain_bg.png')

class Opening():
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
    self.opimg1=p5.loadImage('opening/opening_1.png')
    self.opimg2=p5.loadImage('opening/opening_2.png')
    self.playimg1=p5.loadImage('opening/play_1.png')
    self.playimg2=p5.loadImage('opening/play_2.png')
#^^^^^   
  def draw(self):
    global game_state
    if game_state=='opening':
      if p5.millis()%1000<500:
        p5.image(self.opimg1,0,0,self.opimg1.width/2,self.opimg1.height/2)
      if p5.millis()%1000>500:
        p5.image(self.opimg2,0,0,self.opimg2.width/2,self.opimg2.height/2)
      if p5.mouseX>240 and p5.mouseX<300 and p5.mouseY>200 and p5.mouseY<270:
          p5.image(self.playimg1,0,0,self.playimg1.width/2,self.playimg1.height/2)
      else:
        p5.image(self.playimg2,0,0,self.playimg2.width/2,self.playimg2.height/2)

#^^^^^   
opening=Opening()
game_state='opening'

class Character:
  x = 150
  y = 150
  state = 'standing'

  def update(self):
    if (self.state == 'moving_right'):
      if (self.x < 200):
        self.x += 1
      else:
        self.state = 'moving_up'
    elif (self.state == 'moving_up'):
      if (self.y < 200):
        self.y += 1
        

#-------------------------------------------------------------
class Intro():
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
    self.font1=p5.loadFont('PressStart2P.otf')
    self.intro1=p5.loadImage('intro/introbase.png')
    self.character=p5.loadImage('intro/character.gif')
#^^^^^  
  def draw(self):
    global game_state, intro_state
    if game_state=='intro':
      p5.image(self.intro1,0,0,self.intro1.width/2,self.intro1.height/2)
      p5.image(self.character,75,70,self.character.width*4,self.character.height*4)
#^^^^^      
  def text(self):
    global game_state, intro_state
    if game_state=='intro':
      p5.textFont(self.font1)
      p5.fill(0)
      p5.textSize(15)
      if intro_state==0:
        p5.text('Hi, welcome to the village!',70,300)
      elif intro_state==1:
        p5.text('In this place, you can ',70,290)
        p5.text('freely build houses, plant, ',70,320)
        p5.text('change the look of trees...',70,350)
      elif intro_state==2:
        p5.text('...and even change the...',70,300)
      elif intro_state==3:
        p5.text('...and even change the...',70,300)
        p5.textSize(20)
        p5.text('weather!',70,330)
      elif intro_state==4:
        p5.text('for the rest, I will let',70,300)
        p5.text('you explore.',70,330)
      elif intro_state==5:
        p5.text('Good luck!',70,300)
#^^^^^   
intro=Intro()
intro_state=0

#-------------------------------------------------------------
class Scene():
  def __init__(self,x=0,y=0,Cx1=0,Cx2=0):
    self.x=x
    self.y=y
    self.Cx1=Cx1
    self.Cx2=Cx2
    self.sce1=p5.loadImage('scene/scene_1.png')
    self.sce2=p5.loadImage('scene/scene_2.png')
    self.eleCat1=p5.loadImage('elements/cat1.gif')
    self.eleCat2=p5.loadImage('elements/cat2.gif')
    self.cloudL=p5.loadImage('elements/cloud_l.png')
    self.cloudR=p5.loadImage('elements/cloud_r.png')
    self.plant1=p5.loadImage('field/plant1.png')
    self.plant2=p5.loadImage('field/plant2.png')
    self.plant3=p5.loadImage('field/plant3.png')
    self.plant4=p5.loadImage('field/plant4.png')
    self.plant1_1=p5.loadImage('field/plant1_1.png')
    self.plant1_2=p5.loadImage('field/plant1_2.png')
    self.plant1_3=p5.loadImage('field/plant1_3.png')
    self.field1=p5.loadImage('field/field1.png')
    self.field2=p5.loadImage('field/field2.png')
    self.field3=p5.loadImage('field/field3.png')
    self.field4=p5.loadImage('field/field4.png')
    self.field1_1=p5.loadImage('field/field1_1.png')
    self.field2_1=p5.loadImage('field/field2_1.png')
    self.field3_1=p5.loadImage('field/field3_1.png')
    self.field4_1=p5.loadImage('field/field4_1.png')
    self.house1=p5.loadImage('house/house1.png')
    self.house2=p5.loadImage('house/house2.png')
    self.house3=p5.loadImage('house/house3.png')
    self.house4=p5.loadImage('house/house4.png')
    self.house5=p5.loadImage('house/house5.png')
    self.rest=p5.loadImage('scene/rest.png')
    self.character=p5.loadImage('scene/character.gif')
    
    
#^^^^^
  def draw(self):
    global game_state
    if game_state=='scene':
      if p5.millis()%1000<500:
        p5.image(self.sce1,self.x,0,self.sce1.width/2,self.sce1.height/2)
      elif p5.millis()%1000>500:
        p5.image(self.sce2,self.x,0,self.sce2.width/2,self.sce2.height/2)
      if p5.mouseX>scene.x+280 and p5.mouseX<scene.x+340 and p5.mouseY>285 and p5.mouseY<305:
        p5.image(self.eleCat2,self.x-20,0,self.eleCat2.width/2,self.eleCat2.height/2)
      else:
        p5.image(self.eleCat1,self.x-20,0,self.eleCat1.width/2,self.eleCat1.height/2)
      p5.image(self.rest,self.x+590,0,self.rest.width/
      2,self.rest.height/2)
      p5.image(self.character,scene.x+600,320,self.character.width/
      2,self.character.height/2)
#^^^^^
  def cloud_op(self):
    global game_state
    if game_state=='scene':
      
      self.Cx1-=3
      self.Cx2+=3
      p5.image(self.cloudL,self.Cx1,0,self.cloudL.width/2,self.cloudL.height/2)
      p5.image(self.cloudR,self.Cx2,0,self.cloudR.width/2,self.cloudR.height/2)
  
#^^^^^
  def field(self):
    global game_state,plant1,plant2
    if game_state=='scene':
      p5.image(self.plant1,self.x,0,self.plant1.width/2,self.plant1.height/2)
      p5.image(self.plant2,self.x,0,self.plant2.width/2,self.plant2.height/2)
      p5.image(self.field1,self.x,0,self.field1.width/2,self.field1.height/2)
      p5.image(self.field2,self.x,0,self.field2.width/2,self.field2.height/2)
      p5.image(self.field3,self.x,0,self.field3.width/2,self.field3.height/2)
      p5.image(self.field4,self.x,0,self.field4.width/2,self.field4.height/2)
      

#^^^^^
  def click(self):
    global game_state, scene_state, house1,house2,house3,house4
    if game_state=='scene':
      if p5.mouseX>self.x+70 and p5.mouseX<self.x+180 and p5.mouseY>310 and p5.mouseY<340:         p5.image(self.plant3,self.x,0,self.plant3.width/2,self.plant3.height/2)
      if p5.mouseX>self.x+420 and p5.mouseX<self.x+530 and p5.mouseY>310 and p5.mouseY<340: 
        p5.image(self.plant4,self.x,0,self.plant4.width/
        2,self.plant4.height/2)
      if p5.mouseX>self.x+70 and p5.mouseX<self.x+180 and p5.mouseY>140 and p5.mouseY<260: 
        p5.image(self.field1_1,self.x,0,self.field1.width/
        2,self.field1.height/2)
      if p5.mouseX>self.x+330 and p5.mouseX<self.x+440 and p5.mouseY>50 and p5.mouseY<170:
        p5.image(self.field2_1,self.x,0,self.field2.width/
        2,self.field2.height/2)
      if p5.mouseX>self.x+490 and p5.mouseX<self.x+600 and p5.mouseY>50 and p5.mouseY<170: 
        p5.image(self.field3_1,self.x,0,self.field3.width/
        2,self.field3.height/2)
      if p5.mouseX>self.x+640 and p5.mouseX<self.x+750 and p5.mouseY>50 and p5.mouseY<170: 
        p5.image(self.field4_1,self.x,0,self.field4.width/
        2,self.field4.height/2)

  #^^^^^
  def plants(self):
    if plant1==1:
      p5.image(self.plant1_1,self.x+60,0,self.plant1_1.width/
      2,self.plant1_1.height/2)
    elif plant1==2:
      p5.image(self.plant1_2,self.x+60,0,self.plant1_2.width/
      2,self.plant1_2.height/2)
    elif plant1==3:
      p5.image(self.plant1_3,self.x+60,0,self.plant1_3.width/
      2,self.plant1_3.height/2)
    if plant2==1:
      p5.image(self.plant1_1,self.x+410,0,self.plant1_1.width/
      2,self.plant1_1.height/2)
    elif plant2==2:
      p5.image(self.plant1_2,self.x+410,0,self.plant1_2.width/
      2,self.plant1_2.height/2)
    elif plant2==3:
      p5.image(self.plant1_3,self.x+410,0,self.plant1_3.width/
      2,self.plant1_3.height/2)
#^^^^^
  def house(self):
    if house1==1:
      p5.image(self.house1,self.x,0,self.house1.width/
      2,self.house1.height/2)
    elif house1==2:
      p5.image(self.house2,self.x,0,self.house2.width/
        2,self.house2.height/2)
    elif house1==3:
      p5.image(self.house3,self.x+312,0,self.house3.width/
        2,self.house3.height/2)
    elif house1==4:
      p5.image(self.house4,self.x+312,0,self.house4.width/
        2,self.house4.height/2)
    elif house1==5:
      p5.image(self.house5,self.x+312,0,self.house5.width/
        2,self.house5.height/2)
#---------------------------
    if house2==1:
      p5.image(self.house1,self.x+155,0,self.house1.width/
      2,self.house1.height/2)
    elif house2==2:
      p5.image(self.house2,self.x+155,0,self.house2.width/
        2,self.house2.height/2)
    elif house2==3:
      p5.image(self.house3,self.x+467,0,self.house3.width/
      2,self.house3.height/2)
    elif house2==4:
      p5.image(self.house4,self.x+467,0,self.house4.width/
      2,self.house4.height/2)
    elif house2==5:
      p5.image(self.house5,self.x+467,0,self.house5.width/
      2,self.house5.height/2)
#---------------------------
    if house3==1:
      p5.image(self.house1,self.x+305,0,self.house1.width/
        2,self.house1.height/2)
    elif house3==2:
      p5.image(self.house2,self.x+305,0,self.house2.width/
      2,self.house2.height/2)
    elif house3==3:
      p5.image(self.house3,self.x+617,0,self.house3.width/
      2,self.house3.height/2)
    elif house3==4:
      p5.image(self.house4,self.x+617,0,self.house4.width/
      2,self.house4.height/2)
    elif house3==5:
      p5.image(self.house5,self.x+617,0,self.house5.width/
      2,self.house5.height/2)
#---------------------------
    if house4==1:
      p5.image(self.house1,self.x-263,94,self.house1.width/
      2,self.house1.height/2)
    elif house4==2:
      p5.image(self.house2,self.x-263,94,self.house2.width/
        2,self.house2.height/2)
    elif house4==3:
      p5.image(self.house3,self.x+49,90,self.house3.width/
      2,self.house3.height/2)
    elif house4==4:
      p5.image(self.house4,self.x+49,90,self.house4.width/
      2,self.house4.height/2)
    elif house4==5:
      p5.image(self.house5,self.x+49,90,self.house5.width/
      2,self.house5.height/2)

#---------------------------
scene=Scene()
house1=0
house2=0
house3=0
house4=0
plant1=0
plant2=0
#-------------------------------------------------------------
class Control():
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
    self.sys1_x = 500
    self.left=p5.loadImage('control/left.png')
    self.right=p5.loadImage('control/right.png')
    self.sys=p5.loadImage('control/sys.png')
    self.sys1=p5.loadImage('control/sys1.png')
    self.sys_1=p5.loadImage('control/sys_1.png')
    
#^^^^^
  def function(self):
    global sys_state
    if game_state=='scene':
      p5.image(self.left,350,350,self.left.width/4,self.left.height/4)
      p5.image(self.right,450,350,self.right.width/4,self.right.height/4)
      p5.image(self.sys,470,15,self.sys.width/1.5,self.sys.height/1.5)
      if p5.mouseX>470 and p5.mouseX<510 and p5.mouseY>15 and p5.mouseY<55: 
        p5.image(self.sys_1,470,15,self.sys.width/1.5,self.sys.height/1.5)
      if sys_state==1:
        if self.sys1_x > 390:
          self.sys1_x -= 5
        p5.image(self.sys1,self.sys1_x,80,self.sys1.width/2,self.sys1.height/2)
      if sys_state==0:
        if self.sys1_x >= 390:
          self.sys1_x += 5
          if self.sys1_x>=535:
            self.sys1_x=535
        p5.image(self.sys1,self.sys1_x,80,self.sys1.width/2,self.sys1.height/2)

#^^^^^
sys_state=0
control=Control()
#-------------------------------------------------------------

class Select():
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
    self.sle1=p5.loadImage('select/select.gif')
    self.tree1=p5.loadImage('tree/tree1.png')
    self.tree2=p5.loadImage('tree/tree2.png')
    self.tree3=p5.loadImage('tree/tree3.png')
    self.tree2_1=p5.loadImage('tree/tree2_1.png')
    self.tree2_2=p5.loadImage('tree/tree2_2.png')
    self.tree2_3=p5.loadImage('tree/tree2_3.png')
    self.tree3_1=p5.loadImage('tree/tree3_1.png')
    self.tree3_2=p5.loadImage('tree/tree3_2.png')
    self.tree3_3=p5.loadImage('tree/tree3_3.png')
#^^^^^
  def sle(self):
    global game_state,tree1_state,tree2_state,tree3_state
    #print(tree1_state)
    if game_state=='scene':
      if p5.mouseX>scene.x+320 and p5.mouseX<scene.x+395 and p5.mouseY>200 and p5.mouseY<300: 
        p5.image(self.sle1,scene.x+340,145)
      if p5.mouseX>scene.x+410 and p5.mouseX<scene.x+490 and p5.mouseY>180 and p5.mouseY<300:
        p5.image(self.sle1,scene.x+435,135)
      if p5.mouseX>scene.x+500 and p5.mouseX<scene.x+540 and p5.mouseY>220 and p5.mouseY<300:
        p5.image(self.sle1,scene.x+500,170)
        
#^^^^^
  def tree(self):
    global game_state,tree1_state,tree2_state,tree3_state
    if tree1_state==1:
      p5.image(self.tree1,scene.x+312,181,self.tree1.width/
      2,self.tree1.height/2)
    elif tree1_state==2:
      p5.image(self.tree2,scene.x+312,181,self.tree1.width/
      2,self.tree1.height/2)
    elif tree1_state==3:
      p5.image(self.tree3,scene.x+312,181,self.tree1.width/
      2,self.tree1.height/2)
    if tree2_state==1:
      p5.image(self.tree2_1,scene.x+406.5,0,self.tree2_1.width/
      2,self.tree2_1.height/2)
    elif tree2_state==2:
      p5.image(self.tree2_2,scene.x+406.5,0,self.tree2_1.width/
      2,self.tree2_1.height/2)
    elif tree2_state==3:
      p5.image(self.tree2_3,scene.x+406.5,0,self.tree2_1.width/
      2,self.tree2_1.height/2)
    if tree3_state==1:
      p5.image(self.tree3_1,scene.x+494,0,self.tree3_1.width/
      2,self.tree3_1.height/2)
    elif tree3_state==2:
      p5.image(self.tree3_2,scene.x+494,0,self.tree3_1.width/
      2,self.tree3_1.height/2)
    elif tree3_state==3:
      p5.image(self.tree3_3,scene.x+494,0,self.tree3_1.width/
      2,self.tree3_1.height/2)


select=Select()
tree1_state=0
tree2_state=0
tree3_state=0
#-------------------------------------------------------------
class Rain():
  def __init__(self,x=150,y=150):
    self.x=x
    self.y=y
    self.speed=int(p5.random(1,5))
    self.rain=p5.loadImage('weather/rain.png')
    self.rain_bg=p5.loadImage('weather/rain_bg.png')
    

  def draw_rain(self):
    p5.image(self.rain,self.x,self.y,self.rain.width/
    8,self.rain.height/8)

  def update_rain(self):
    if self.y<320:
      self.y+=self.speed
    else:
      self.y=-50

  def tint(self):
    global scene_state
    #if scene_state=='rain':
      #p5.image(self.rain_bg,0,0,self.rain_bg.width/
      #2,self.rain_bg.height/2)
      

#-------------------------------------------------------------
class Sun():
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
    self.sun1=p5.loadImage('weather/sun_1.png')
    self.sun2=p5.loadImage('weather/sun_2.png')
    self.sun3=p5.loadImage('weather/sun_3.png')
    
  def draw(self):
    global game_state,scene_state
    if scene_state=='sun':
      if p5.millis()%1000<330:
        p5.image(self.sun1,scene.x+self.x,self.y,self.sun1.width/
        1,self.sun1.height/2)
      elif 660>p5.millis()%1000>330:
        p5.image(self.sun2,scene.x+self.x,self.y,self.sun2.width/
        1,self.sun2.height/2)
      elif 1000>p5.millis()%1000>660:
        p5.image(self.sun3,scene.x+self.x,self.y,self.sun3.width/
        1,self.sun3.height/2)
    
  

sun=Sun()
#-------------------------------------------------------------
rain=Rain(150,150)
rain_list=[]
scene_state='none'

def setup():
  p5.createCanvas(540, 400)  

def draw():
  global scene_state,rain
  p5.background(0)   
  p5.fill(255)  
  

  opening.draw()
  intro.draw()
  intro.text()
  
  scene.draw()
  scene.field()
  scene.cloud_op()
  scene.click()
  if game_state=='scene':
    scene.house()
    scene.plants()
    select.tree()
    select.sle()
    sun.draw()
  if game_state=='scene' and scene_state=='rain':
    rain.tint()
    p5.image(bg,0,0,540,800)
    i=0
    #p5.loadImage(rain_bg,0,0,rain_bg.width/2,rain_bg.height/2)
    while i<len(rain_list):
      rain=rain_list[i]
      rain.update_rain()
      rain.draw_rain()
      i+=1
    
  
  control.function()
  #cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  #p5.text(cursor_xy, 10, 20)  # cursor (x, y) 

  
# event function below need to be included,
# even if they don't do anything
#-------------------------------------------------------------

def keyPressed(event):
  pass
      

def keyReleased(event):
  #print('keyReleased.. ' + str(p5.key))
  pass

def mousePressed(event):
  global game_state,intro_state,sys_state,tree1_state,tree2_state,tree3_state,house1,house2,house3,house4,scene_state,plant1,plant2
  #print(scene_state)
#^^^^^rain:
  if scene_state=='rain':
    rain=Rain(p5.mouseX,p5.mouseY)
    rain_list.append(rain)
  else:
    rain_list.clear()
#^^^^^star the game:
  if p5.mouseX>240 and p5.mouseX<300 and p5.mouseY>200 and p5.mouseY<270:
    if game_state=='opening':
      game_state='intro'
      intro_state=0
#^^^^^introduction:
  elif p5.mouseX>50 and p5.mouseX<500 and p5.mouseY>250 and p5.mouseY<380:
    if int(intro_state)<5:
      intro_state+=1
    elif int(intro_state)>=5:
      intro_state=5
      game_state='scene'
#^^^^^move the scene:
  if game_state=='scene':
    if p5.mouseX>350 and p5.mouseX<400 and p5.mouseY>360 and p5.mouseY<380:
      if scene.x==0:
        scene.x=scene.x
      else:
        scene.x+=50
    if p5.mouseX>450 and p5.mouseX<500 and p5.mouseY>360 and p5.mouseY<380:
      if scene.x<=-250:
        scene.x=-250
      else:
        scene.x-=50
#^^^^^field/house interactions:
    if p5.mouseX>scene.x+330 and p5.mouseX<scene.x+440 and p5.mouseY>50 and p5.mouseY<170:
      house1+=1
      if house1==6:
        house1=0
    if p5.mouseX>scene.x+490 and p5.mouseX<scene.x+600 and p5.mouseY>50 and p5.mouseY<170: 
      house2+=1
      if house2==6:
        house2=0
    if p5.mouseX>scene.x+640 and p5.mouseX<scene.x+750 and p5.mouseY>50 and p5.mouseY<170: 
      house3+=1
      if house3==6:
        house3=0
    if p5.mouseX>scene.x+70 and p5.mouseX<scene.x+180 and p5.mouseY>140 and p5.mouseY<260: 
      house4+=1
      if house4==6:
        house4=0
    if p5.mouseX>scene.x+70 and p5.mouseX<scene.x+180 and p5.mouseY>310 and p5.mouseY<340:         
      plant1+=1
      if plant1==4:
        plant1=0
    if p5.mouseX>scene.x+420 and p5.mouseX<scene.x+530 and p5.mouseY>310 and p5.mouseY<340: 
      plant2+=1
      if plant2==4:
        plant2=0
#^^^^^sys button:
    if p5.mouseX>470 and p5.mouseX<510 and p5.mouseY>15 and p5.mouseY<55: 
      if sys_state==0:
        sys_state=1
      else:
        sys_state=0
    if sys_state==1 and p5.mouseX>460 and p5.mouseX<515 and p5.mouseY>130 and p5.mouseY<180:
      if scene_state!='rain':
        scene_state='rain'
      else:
        scene_state='none'
    if sys_state==1 and p5.mouseX>405 and p5.mouseX<450 and p5.mouseY>130 and p5.mouseY<180:
      if scene_state!='sun':
        scene_state='sun'
      else:
        scene_state='none'
    if sys_state==1 and p5.mouseX>405 and p5.mouseX<515 and p5.mouseY>220 and p5.mouseY<245:
      game_state='opening'
    if sys_state==1 and p5.mouseX>405 and p5.mouseX<515 and p5.mouseY>190 and p5.mouseY<210:
      sys_state=0
#^^^^^tree interaction:
    if p5.mouseX>scene.x+320 and p5.mouseX<scene.x+395 and p5.mouseY>200 and p5.mouseY<300: 
      tree1_state+=1
      if tree1_state==4:
        tree1_state=0
    if p5.mouseX>scene.x+410 and p5.mouseX<scene.x+490 and p5.mouseY>180 and p5.mouseY<300:
      tree2_state+=1
      if tree2_state==4:
        tree2_state=0
    if p5.mouseX>scene.x+500 and p5.mouseX<scene.x+540 and p5.mouseY>220 and p5.mouseY<300:
      tree3_state+=1
      if tree3_state==4:
        tree3_state=0
      

def mouseReleased(event):
  #print('mouseReleased..')
  pass


  
