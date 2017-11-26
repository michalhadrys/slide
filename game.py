import os
import sys
import pygame
import random
import pickle


def dumbmenu(screen, menu, x_pos=100, y_pos=100, size=70, distance=1.4, exitAllowed=True):
	pygame.font.init
	myfont = pygame.font.SysFont("Courier", size, True)
	cursorpos = 0
	renderWithChars = False
	for i in menu:
		if cursorpos<9:
			text =  myfont.render(str(cursorpos + 1)+".  " + i, True, (255,255,255))
			textrect = text.get_rect()
			textrect = textrect.move(x_pos, (size // distance * cursorpos) + y_pos)
			screen.blit(text, textrect)
			pygame.display.update(textrect)
			cursorpos += 1
		else:
			text =  myfont.render(str(cursorpos + 1)+". " + i, True, (255,255,255))
			textrect = text.get_rect()
			textrect = textrect.move(x_pos, (size // distance * cursorpos) + y_pos)
			screen.blit(text, textrect)
			pygame.display.update(textrect)
			cursorpos += 1
	cursorpos = 0
	cursor = myfont.render(">", True, (255,0,0))
	cursorrect = cursor.get_rect()
	cursorrect = cursorrect.move(x_pos - (size // distance),
                 (size // distance * cursorpos) + y_pos)
	ArrowPressed = True
	exitMenu = False
	clock = pygame.time.Clock()
	filler = pygame.Surface.copy(screen)
	fillerrect = filler.get_rect()
	while True:
		clock.tick(30)
		if ArrowPressed == True:
			screen.blit(filler, fillerrect)
			pygame.display.update(cursorrect)
			cursorrect = cursor.get_rect()
			cursorrect = cursorrect.move(x_pos - (size // distance),
                         (size // distance * cursorpos) + y_pos)
			screen.blit(cursor, cursorrect)
			pygame.display.update(cursorrect)
			ArrowPressed = False
		if exitMenu == True:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return -1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE and exitAllowed == True:
					if cursorpos == len(menu) - 1:
						exitMenu = True
					else:
						cursorpos = len(menu) - 1; ArrowPressed = True
				if event.key == pygame.K_UP:
					ArrowPressed = True
					if cursorpos == 0:
						cursorpos = len(menu) - 1
					else:
						cursorpos -= 1
				elif event.key == pygame.K_DOWN:
					ArrowPressed = True
					if cursorpos == len(menu) - 1:
						cursorpos = 0
					else:
						cursorpos += 1
				elif event.key == pygame.K_KP_ENTER or \
					event.key == pygame.K_RETURN:
						exitMenu = True
	return cursorpos
def loadLvl(folder, lvl_num):
	matrix=[]
	levdir = os.curdir + os.sep + "levels" + os.sep + str(folder) + os.sep
	with open(levdir + 'level' + str(lvl_num) + '.txt', 'r') as lvl:
		for row in lvl.read().splitlines():
			matrix.append(list(row))
	return matrix
			
def drawlevel(matrix, lev_num):
	font = pygame.font.SysFont("Courier", 25, True)
	wall=pygame.image.load(gradir + "wall.png").convert()
	player=pygame.image.load(gradir + "player.png").convert()
	target=pygame.image.load(gradir + "target.png").convert()
	space=pygame.image.load(gradir + "space.png").convert()
	key=pygame.image.load(gradir + "key.png").convert()
	player_on_target=pygame.image.load(gradir + "player.png").convert()
	wall=pygame.transform.scale(wall, (53,53))
	player=pygame.transform.scale(player, (53,53))
	player_on_target=pygame.transform.scale(player_on_target, (53,53))
	target=pygame.transform.scale(target, (53,53))
	space=pygame.transform.scale(space, (53,53))
	key=pygame.transform.scale(key, (53,53))
	images = {'#': wall, ' ': space, 'X': target, '@': player, 'K': key, 'P':player_on_target}
	box_size = wall.get_width()
	for i in range (0,len(matrix)):
		for c in range (0,len(matrix[i])):
			screen.blit(images[matrix[i][c]], (c*box_size+8, i*box_size+4))
	text=font.render('Move: Cursors   Reset level: r   Quit to Main Menu: Escape', True, (255,255,255))
	textrect = text.get_rect()
	textrect = textrect.move(50, 650)
	screen.blit(text, textrect)
	font = pygame.font.SysFont("Courier", 45, True)
	text2=font.render(str(lev_num), True, (255,255,0))
	textrect2 = text2.get_rect()
	textrect2 = textrect2.move(15, 4)
	screen.blit(text2, textrect2)
	pygame.display.update()
def drawlevel_small(matrix, lev_num):
	font = pygame.font.SysFont("Courier", 25, True)
	wall=pygame.image.load(gradir + "wall.png").convert()
	player=pygame.image.load(gradir + "player.png").convert()
	target=pygame.image.load(gradir + "target.png").convert()
	space=pygame.image.load(gradir + "space.png").convert()
	key=pygame.image.load(gradir + "key.png").convert()
	player_on_target=pygame.image.load(gradir + "player.png").convert()
	wall=pygame.transform.scale(wall, (42,42))
	player=pygame.transform.scale(player, (42,42))
	player_on_target=pygame.transform.scale(player_on_target, (42,42))
	target=pygame.transform.scale(target, (42,42))
	space=pygame.transform.scale(space, (42,42))
	key=pygame.transform.scale(key, (42,42))
	images = {'#': wall, ' ': space, 'X': target, '@': player, 'K': key, 'P':player_on_target}
	box_size = wall.get_width()
	for i in range (0,len(matrix)):
		for c in range (0,len(matrix[i])):
			screen.blit(images[matrix[i][c]], (c*box_size+1, i*box_size+1))
	text=font.render('Move: Cursors   Reset level: r', True, (255,255,255))
	textrect = text.get_rect()
	textrect = textrect.move(50, 500)
	screen.blit(text, textrect)
	text2=font.render('Quit to Main Menu: Escape', True, (255,255,255))
	textrect2 = text2.get_rect()
	textrect2 = textrect2.move(50, 530)
	screen.blit(text2, textrect2)
	font = pygame.font.SysFont("Courier", 40, True)
	text3=font.render(str(lev_num), True, (255,255,0))
	textrect3 = text3.get_rect()
	textrect3 = textrect3.move(8, 3)
	screen.blit(text3, textrect3)
	pygame.display.update()
def getPlayerPosition(matrix):
	for i in range (0,len(matrix)):
		for c in range (0,len(matrix[i])):
			if matrix[i][c]=='@' or matrix[i][c]=='P':
				pozycja=[i,c]
	return pozycja
def getTargetPosition(matrix):
	for i in range (0,len(matrix)):
		for c in range (0,len(matrix[i])):
			if matrix[i][c]=='X':
				pozycja=[i,c]
	return pozycja
def countKeys(matrix):
	keys=0
	for i in range (0,len(matrix)):
		for c in range (0,len(matrix[i])):
			if matrix[i][c]=='K':
				keys=keys+1
	return keys
def showWin():
	font = pygame.font.SysFont("Courier", 175, True)
	text=font.render('EPIC WIN!', True, (255,255,0))
	if if_sound==0:
		pygame.mixer.music.load(sounddir+'win.wav')
		pygame.mixer.music.play(0)
	textrect = text.get_rect()
	screen.blit(text, textrect.move(75, 200))
	pygame.display.update()
	if if_sound==0:
		pygame.time.wait(5000)
	else:
		pygame.time.wait(2000)
def showWin_small():
	font = pygame.font.SysFont("Courier", 140, True)
	text=font.render('EPIC WIN!', True, (255,255,0))
	if if_sound==0:
		pygame.mixer.music.load(sounddir+'win.wav')
		pygame.mixer.music.play(0)
	textrect = text.get_rect()
	screen.blit(text, textrect.move(40, 150))
	pygame.display.update()
	if if_sound==0:
		pygame.time.wait(5000)
	else:
		pygame.time.wait(2000)
def leonardo():
	with open('background.txt', 'rb') as f:
		background_number = pickle.load(f)
	back = pygame.image.load(gradir + "background" + str(background_number) +".png").convert()
	back = pygame.transform.scale(back, [1024, 768])
	backrect = back.get_rect()
	screen.blit(back, backrect)
	font = pygame.font.SysFont("Courier", 80, True)
	text=font.render('Level set completed!', True, (255,255,0))
	textrect = text.get_rect()
	screen.blit(text, textrect.move(15, 10))
	leo_choice=random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
	leo = pygame.image.load(gradir + "complete" + str(leo_choice) +".png").convert()
	leo = pygame.transform.scale(leo, [1024, 668])
	leorect = leo.get_rect()
	screen.blit(leo, leorect.move(0,100))
	pygame.display.update()
	pygame.time.wait(5000)
def leonardo_small():
	with open('background.txt', 'rb') as f:
		background_number = pickle.load(f)
	back = pygame.image.load(gradir + "background" + str(background_number) +".png").convert()
	back = pygame.transform.scale(back, [800, 600])
	backrect = back.get_rect()
	screen.blit(back, backrect)
	font = pygame.font.SysFont("Courier", 60, True)
	text=font.render('Level set completed!', True, (255,255,0))
	textrect = text.get_rect()
	screen.blit(text, textrect.move(25, 10))
	leo_choice=random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
	leo = pygame.image.load(gradir + "complete" + str(leo_choice) +".png").convert()
	leo = pygame.transform.scale(leo, [800, 500])
	leorect = leo.get_rect()
	screen.blit(leo, leorect.move(0,100))
	pygame.display.update()
	pygame.time.wait(5000)
def movePlayer(direction,matrix, lev_num,win=False):
	with open('player_speed.txt', 'rb') as f:
		framerate = pickle.load(f)
	y=getPlayerPosition(matrix)[0]
	x=getPlayerPosition(matrix)[1]
	if direction == "L":
		while matrix[y][x-1] != "#" and win==False:
			if matrix[y][x-1] != 'X':
				if matrix[y][x]=='P':
					matrix[y][x-1]='@'
					matrix[y][x]='X'
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y][x-1]='@'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
			else:
				if countKeys(matrix)==1:
					matrix[y][x-1]='P'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y][x-1]='P'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
					win=True
					if x-2>=0:
						matrix[y][x-2]='#'
			x=x-1
	if direction == "R":
		while matrix[y][x+1] != "#" and win==False:
			if matrix[y][x+1] != 'X':
				if matrix[y][x]=='P':
					matrix[y][x+1]='@'
					matrix[y][x]='X'
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y][x+1]='@'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
			else:
				if countKeys(matrix)==1:
					matrix[y][x+1]='P'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y][x+1]='P'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
					win=True
					if x+2<=18:
						matrix[y][x+2]='#'
			x=x+1
	if direction == "U":
		while matrix[y-1][x] != "#" and win==False:
			if matrix[y-1][x] != 'X':
				if matrix[y][x]=='P':
					matrix[y-1][x]='@'
					matrix[y][x]='X'
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y-1][x]='@'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
			else:
				if countKeys(matrix)==1:
					matrix[y-1][x]='P'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y-1][x]='P'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
					win=True
					if y-2>=0:
						matrix[y-2][x]='#'
			y=y-1
	if direction == "D":
		while matrix[y+1][x] != "#" and win==False:
			if matrix[y+1][x] != 'X':
				if matrix[y][x]=='P':
					matrix[y+1][x]='@'
					matrix[y][x]='X'
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y+1][x]='@'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
			else:
				if countKeys(matrix)==1:
					matrix[y+1][x]='P'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y+1][x]='P'
					matrix[y][x]=' '
					drawlevel(matrix, lev_num)
					pygame.time.wait(framerate)
					win=True
					
					if y+2<=10:
						matrix[y+2][x]='#'
			y=y+1
	return win
def movePlayer_small(direction,matrix, lev_num, win=False):
	with open('player_speed.txt', 'rb') as f:
		framerate = pickle.load(f)
	y=getPlayerPosition(matrix)[0]
	x=getPlayerPosition(matrix)[1]
	if direction == "L":
		while matrix[y][x-1] != "#" and win==False:
			if matrix[y][x-1] != 'X':
				if matrix[y][x]=='P':
					matrix[y][x-1]='@'
					matrix[y][x]='X'
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y][x-1]='@'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
			else:
				if countKeys(matrix)==1:
					matrix[y][x-1]='P'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y][x-1]='P'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
					win=True
					if x-2>=0:
						matrix[y][x-2]='#'
			x=x-1
	if direction == "R":
		while matrix[y][x+1] != "#" and win==False:
			if matrix[y][x+1] != 'X':
				if matrix[y][x]=='P':
					matrix[y][x+1]='@'
					matrix[y][x]='X'
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y][x+1]='@'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
			else:
				if countKeys(matrix)==1:
					matrix[y][x+1]='P'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y][x+1]='P'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
					win=True
					if x+2<=18:
						matrix[y][x+2]='#'
			x=x+1
	if direction == "U":
		while matrix[y-1][x] != "#" and win==False:
			if matrix[y-1][x] != 'X':
				if matrix[y][x]=='P':
					matrix[y-1][x]='@'
					matrix[y][x]='X'
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y-1][x]='@'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
			else:
				if countKeys(matrix)==1:
					matrix[y-1][x]='P'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y-1][x]='P'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
					win=True
					if y-2>=0:
						matrix[y-2][x]='#'
			y=y-1
	if direction == "D":
		while matrix[y+1][x] != "#" and win==False:
			if matrix[y+1][x] != 'X':
				if matrix[y][x]=='P':
					matrix[y+1][x]='@'
					matrix[y][x]='X'
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y+1][x]='@'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
			else:
				if countKeys(matrix)==1:
					matrix[y+1][x]='P'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
				else:
					matrix[y+1][x]='P'
					matrix[y][x]=' '
					drawlevel_small(matrix, lev_num)
					pygame.time.wait(framerate)
					win=True
					
					if y+2<=10:
						matrix[y+2][x]='#'
			y=y+1
	return win
def play_random(songs):
	if if_sound==0:
		pygame.mixer.music.load(random.choice(songs))
		pygame.mixer.music.play(-1)

with open('window_size.txt', 'rb') as f:
    window_size = pickle.load(f)
if window_size==1:
	pygame.init()
	sounddir = os.curdir + os.sep + "sounds" + os.sep
	gradir = os.curdir + os.sep + "graphics" + os.sep
	levdir = os.curdir + os.sep + "levels" + os.sep
	screen = pygame.display.set_mode((1024,768))
	pygame.display.set_caption("Slide")
	with open('background.txt', 'rb') as f:
		background_number = pickle.load(f)
	back = pygame.image.load(gradir + "background" + str(background_number) +".png").convert()
	back = pygame.transform.scale(back, [1024, 768])
	backrect = back.get_rect()
	font = pygame.font.SysFont("Courier", 70, True)
	screen.blit(back, backrect)
	with open('theme_sound.txt', 'rb') as f:
		theme_sound = pickle.load(f)
	theme_sound_play=sounddir+str(theme_sound)+'.wav'
	with open('sound.txt', 'rb') as f:
		if_sound = pickle.load(f)
	level_dict={ 0:'First Steps', 1:'Take It Easy', 2:'In The Medium Of Nowhere', 3:'Die Hard', 4:'You Must Be Insane', 5:'Don\'t Even Try'}
	songs=[sounddir+'lev1.wav', sounddir+'lev2.wav', sounddir+'lev3.wav', sounddir+'lev4.wav']

	while True:
		if if_sound==0:
			if pygame.mixer.music.get_busy()==0:
				pygame.mixer.music.load(theme_sound_play)
				pygame.mixer.music.play(-1)
		screen.blit(back, backrect)
		pygame.display.update()
		dmval = dumbmenu(screen, (
		'Start Game',
		'Options',
		'Quit Game'), x_pos=300)
		if dmval == 2:
			if if_sound==0:
				pygame.mixer.music.load(sounddir+'exit.wav')
				pygame.mixer.music.play(-1)
			quit_screen=True
			screen.blit(back, backrect)
			font = pygame.font.SysFont("Courier", 80, True)
			text=font.render('Really? Quit?', True, (255,255,0))
			textrect = text.get_rect()
			screen.blit(text, textrect.move(15, 10))
			zaba_choice=random.choice([1,2,3,4])
			zaba = pygame.image.load(gradir + "smutnazaba" + str(zaba_choice) +".jpg").convert()
			zaba = pygame.transform.scale(zaba, [1024, 630])
			zabarect = zaba.get_rect()
			screen.blit(zaba, zabarect.move(0,100))
			font = pygame.font.SysFont("Courier", 35, True)
			text2=font.render('Yes: Y   No: N', True, (255,255,0))
			textrect2 = text2.get_rect()
			screen.blit(text2, textrect2.move(15, 725))
			pygame.display.update()
			while quit_screen==True:
				button_pressed="A"
				for event in pygame.event.get():
					if event.type == pygame.QUIT: sys.exit()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_n:
							button_pressed="N"
						elif event.key == pygame.K_y:
							button_pressed="Y"
				if button_pressed=="N":
					quit_screen=False
					pygame.mixer.music.stop()
					continue
				elif button_pressed=="Y":
					sys.stdout.write("Thanks for Playing the Game. Bye bye...\n")
					sys.exit()
		elif dmval==1:
			Menu4=True
			while Menu4==True:
				if if_sound==0:
					if pygame.mixer.music.get_busy()==0:
						pygame.mixer.music.load(theme_sound_play)
						pygame.mixer.music.play(-1)
				screen.blit(back, backrect)
				font = pygame.font.SysFont("Courier", 25, True)
				text=font.render('Note: Restart the game to update options', True, (255,255,255))
				textrect = text.get_rect()
				textrect = textrect.move(50, 700)
				screen.blit(text, textrect)
				pygame.display.update()
				dmval = dumbmenu(screen, (
				'Window size',
				'Sound',
				'Theme sound',
				'Background',
				'Player speed',
				'Back'), x_pos=300)
				if dmval==5:
					Menu4=False
					continue
				elif dmval==0:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 700)
						screen.blit(text, textrect)
						pygame.display.update()
						dmval = dumbmenu(screen, (
						'Small (800x600)',
						'Big (1024x768)',
						'Back'), x_pos=500, size=40)
						if dmval==2:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('window_size.txt', 'wb') as f:
								pickle.dump(dmval, f)
				elif dmval==1:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 700)
						screen.blit(text, textrect)
						pygame.display.update()
						dmval = dumbmenu(screen, (
						'Play',
						'Mute',
						'Back'), x_pos=500, size=40)
						if dmval==2:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('sound.txt', 'wb') as f:
								pickle.dump(dmval, f)
				elif dmval==2:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 700)
						screen.blit(text, textrect)
						pygame.display.update()
						sound_dict={0:'main', 1:'castle', 2:'rampart', 3:'tower', 4:'inferno', 5:'necropolis', 6:'dungeon', 7:'stronghold', 8:'fortress', 9:'conflux'}
						dmval = dumbmenu(screen, (
						'Main',
						'Castle',
						'Rampart',
						'Tower',
						'Inferno',
						'Necropolis',
						'Dungeon',
						'Stronghold',
						'Fortress',
						'Conflux',
						'Back'), x_pos=500, size=40)
						if dmval==10:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('theme_sound.txt', 'wb') as f:
								pickle.dump(sound_dict[dmval], f)
				elif dmval==3:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 700)
						screen.blit(text, textrect)
						pygame.display.update()
						dmval = dumbmenu(screen, (
						'Basic',
						'Cat',
						'Doge',
						'Back'), x_pos=500, size=40)
						if dmval==3:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('background.txt', 'wb') as f:
								pickle.dump(dmval+1, f)
				elif dmval==4:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 700)
						screen.blit(text, textrect)
						pygame.display.update()
						player_speed_dict={0:300, 1:200, 2:100, 3:60, 4:30}
						dmval = dumbmenu(screen, (
						'Very slow',
						'Slow',
						'Normal',
						'Fast',
						'Very fast',
						'Back'), x_pos=500, size=40)
						if dmval==5:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('player_speed.txt', 'wb') as f:
								pickle.dump(player_speed_dict[dmval], f)
		else:
			MainMenu4=True
			while MainMenu4==True:
				if if_sound==0:
					if pygame.mixer.music.get_busy()==0:
						pygame.mixer.music.load(theme_sound_play)
						pygame.mixer.music.play(-1)
				screen.blit(back, backrect)
				pygame.display.update()
				dmval = dumbmenu(screen, (
				'First Steps',
				'Take It Easy',
				'In The Medium Of Nowhere',
				'Die Hard',
				'You Must Be Insane',
				'Don\'t Even Try',
				'Back'), x_pos=325, size=40)
				if dmval == 6:
					MainMenu4=False
					continue
				elif dmval == 0:
					MainMenu3=True
					while MainMenu3==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						level_level=dmval
						screen.blit(back, backrect)
						pygame.display.update()
						lev_dmval = dumbmenu(screen, (
						'Level 1',
						'Level 2',
						'Level 3',
						'Level 4',
						'Level 5',
						'Back'), x_pos=500, size=40)
						if lev_dmval==5:
							MainMenu3=False
							continue
						else:
							start_dmval=lev_dmval
							MainMenu=True
							win=False
							while MainMenu==True and MainMenu3==True:
								play_random(songs)
								screen.blit(back, backrect)
								matrix=loadLvl(level_dict[level_level], lev_dmval+1)
								drawlevel(matrix, lev_dmval+1)
								MainMenu2=True
								direction="A"
								begin_target=getTargetPosition(matrix)
								while MainMenu==True and MainMenu2==True:
									for event in pygame.event.get():
										if event.type == pygame.QUIT: sys.exit()
										elif event.type == pygame.KEYDOWN:
											if event.key == pygame.K_ESCAPE:
												MainMenu=False
												pygame.mixer.music.stop()
												continue
											elif event.key == pygame.K_r:
												MainMenu2=False
												continue
											elif event.key == pygame.K_LEFT:
												direction="L"
											elif event.key == pygame.K_RIGHT:
												direction="R"
											elif event.key == pygame.K_DOWN:
												direction="D"
											elif event.key == pygame.K_UP:
												direction="U"
									if direction!="A":
										movePlayer(direction,matrix,lev_dmval+1)
									direction="A"
									if countKeys(matrix)==0 and getPlayerPosition(matrix)==begin_target:
										showWin()
										if lev_dmval==4:
											if start_dmval==0:
												leonardo()
											MainMenu=False
											pygame.mixer.music.stop()
											continue
										else:
											lev_dmval=lev_dmval+1
											MainMenu2=False
											continue
					

				else:
					MainMenu3=True
					while MainMenu3==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						level_level=dmval
						screen.blit(back, backrect)
						pygame.display.update()
						lev_dmval = dumbmenu(screen, (
						'Level 1',
						'Level 2',
						'Level 3',
						'Level 4',
						'Level 5',
						'Level 6',
						'Level 7',
						'Level 8',
						'Level 9',
						'Level 10',
						'Back'), x_pos=500, size=40)
						if lev_dmval==10:
							MainMenu3=False
							continue
						else:
							start_dmval=lev_dmval
							MainMenu=True
							win=False
							while MainMenu==True and MainMenu3==True:
								play_random(songs)
								screen.blit(back, backrect)
								matrix=loadLvl(level_dict[level_level], lev_dmval+1)
								drawlevel(matrix, lev_dmval+1)
								MainMenu2=True
								direction="A"
								begin_target=getTargetPosition(matrix)
								while MainMenu==True and MainMenu2==True:
									for event in pygame.event.get():
										if event.type == pygame.QUIT: sys.exit()
										elif event.type == pygame.KEYDOWN:
											if event.key == pygame.K_ESCAPE:
												MainMenu=False
												pygame.mixer.music.stop()
												continue
											elif event.key == pygame.K_r:
												MainMenu2=False
												continue
											elif event.key == pygame.K_LEFT:
												direction="L"
											elif event.key == pygame.K_RIGHT:
												direction="R"
											elif event.key == pygame.K_DOWN:
												direction="D"
											elif event.key == pygame.K_UP:
												direction="U"
									if direction!="A":
										movePlayer(direction,matrix, lev_dmval+1)
									direction="A"
									if countKeys(matrix)==0 and getPlayerPosition(matrix)==begin_target:
										showWin()
										if lev_dmval==9:
											if start_dmval==0:
												leonardo()
											MainMenu=False
											pygame.mixer.music.stop()
											continue
										else:
											lev_dmval=lev_dmval+1
											MainMenu2=False
											continue
elif window_size==0:
	pygame.init()
	sounddir = os.curdir + os.sep + "sounds" + os.sep
	gradir = os.curdir + os.sep + "graphics" + os.sep
	levdir = os.curdir + os.sep + "levels" + os.sep
	screen = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Slide")
	with open('background.txt', 'rb') as f:
		background_number = pickle.load(f)
	back = pygame.image.load(gradir + "background" + str(background_number) +".png").convert()
	back = pygame.transform.scale(back, [800, 600])
	backrect = back.get_rect()
	font = pygame.font.SysFont("Courier", 70, True)
	screen.blit(back, backrect)
	with open('theme_sound.txt', 'rb') as f:
		theme_sound = pickle.load(f)
	theme_sound_play=sounddir+str(theme_sound)+'.wav'
	with open('sound.txt', 'rb') as f:
		if_sound = pickle.load(f)
	level_dict={ 0:'First Steps', 1:'Take It Easy', 2:'In The Medium Of Nowhere', 3:'Die Hard', 4:'You Must Be Insane', 5:'Don\'t Even Try'}
	songs=[sounddir+'lev1.wav', sounddir+'lev2.wav', sounddir+'lev3.wav', sounddir+'lev4.wav']

	while True:
		if if_sound==0:
			if pygame.mixer.music.get_busy()==0:
				pygame.mixer.music.load(theme_sound_play)
				pygame.mixer.music.play(-1)
		screen.blit(back, backrect)
		pygame.display.update()
		dmval = dumbmenu(screen, (
		'Start Game',
		'Options',
		'Quit Game'), x_pos=300, size=40)
		if dmval == 2:
			pygame.mixer.music.load(sounddir+'exit.wav')
			pygame.mixer.music.play(-1)
			quit_screen=True
			screen.blit(back, backrect)
			font = pygame.font.SysFont("Courier", 60, True)
			text=font.render('Really? Quit?', True, (255,255,0))
			textrect = text.get_rect()
			screen.blit(text, textrect.move(15, 10))
			zaba_choice=random.choice([1,2,3,4])
			zaba = pygame.image.load(gradir + "smutnazaba" + str(zaba_choice) +".jpg").convert()
			zaba = pygame.transform.scale(zaba, [800, 480])
			zabarect = zaba.get_rect()
			screen.blit(zaba, zabarect.move(0,80))
			font = pygame.font.SysFont("Courier", 30, True)
			text2=font.render('Yes: Y   No: N', True, (255,255,0))
			textrect2 = text2.get_rect()
			screen.blit(text2, textrect2.move(15, 560))
			pygame.display.update()
			while quit_screen==True:
				button_pressed="A"
				for event in pygame.event.get():
					if event.type == pygame.QUIT: sys.exit()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_n:
							button_pressed="N"
						elif event.key == pygame.K_y:
							button_pressed="Y"
				if button_pressed=="N":
					quit_screen=False
					pygame.mixer.music.stop()
					continue
				elif button_pressed=="Y":
					sys.stdout.write("Thanks for Playing the Game. Bye bye...\n")
					sys.exit()
		elif dmval==1:
			Menu4=True
			while Menu4==True:
				if if_sound==0:
					if pygame.mixer.music.get_busy()==0:
						pygame.mixer.music.load(theme_sound_play)
						pygame.mixer.music.play(-1)
				screen.blit(back, backrect)
				font = pygame.font.SysFont("Courier", 25, True)
				text=font.render('Note: Restart the game to update options', True, (255,255,255))
				textrect = text.get_rect()
				textrect = textrect.move(50, 500)
				screen.blit(text, textrect)
				pygame.display.update()
				dmval = dumbmenu(screen, (
				'Window size',
				'Sound',
				'Theme sound',
				'Background',
				'Player speed',
				'Back'), x_pos=350, size=40)
				if dmval==5:
					Menu4=False
					continue
				elif dmval==0:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 500)
						screen.blit(text, textrect)
						pygame.display.update()
						dmval = dumbmenu(screen, (
						'Small (800x600)',
						'Big (1024x768)',
						'Back'), x_pos=350, size=40)
						if dmval==2:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('window_size.txt', 'wb') as f:
								pickle.dump(dmval, f)
				elif dmval==1:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 500)
						screen.blit(text, textrect)
						pygame.display.update()
						dmval = dumbmenu(screen, (
						'Play',
						'Mute',
						'Back'), x_pos=350, size=40)
						if dmval==2:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('sound.txt', 'wb') as f:
								pickle.dump(dmval, f)
				elif dmval==2:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 500)
						screen.blit(text, textrect)
						pygame.display.update()
						sound_dict={0:'main', 1:'castle', 2:'rampart', 3:'tower', 4:'inferno', 5:'necropolis', 6:'dungeon', 7:'stronghold', 8:'fortress', 9:'conflux'}
						dmval = dumbmenu(screen, (
						'Main',
						'Castle',
						'Rampart',
						'Tower',
						'Inferno',
						'Necropolis',
						'Dungeon',
						'Stronghold',
						'Fortress',
						'Conflux',
						'Back'), x_pos=350, size=40)
						if dmval==10:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('theme_sound.txt', 'wb') as f:
								pickle.dump(sound_dict[dmval], f)
				elif dmval==3:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 500)
						screen.blit(text, textrect)
						pygame.display.update()
						dmval = dumbmenu(screen, (
						'Basic',
						'Cat',
						'Doge',
						'Back'), x_pos=350, size=40)
						if dmval==3:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('background.txt', 'wb') as f:
								pickle.dump(dmval+1, f)
				elif dmval==4:
					Menu5=True
					while Menu5==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						screen.blit(back, backrect)
						font = pygame.font.SysFont("Courier", 25, True)
						text=font.render('Note: Restart the game to update options', True, (255,255,255))
						textrect = text.get_rect()
						textrect = textrect.move(50, 500)
						screen.blit(text, textrect)
						pygame.display.update()
						player_speed_dict={0:300, 1:200, 2:100, 3:60, 4:30}
						dmval = dumbmenu(screen, (
						'Very slow',
						'Slow',
						'Normal',
						'Fast',
						'Very fast',
						'Back'), x_pos=350, size=40)
						if dmval==5:
							Menu5=False
							continue
						else:
							Menu5=False
							with open('player_speed.txt', 'wb') as f:
								pickle.dump(player_speed_dict[dmval], f)
		else:
			MainMenu4=True
			while MainMenu4==True:
				if if_sound==0:
					if pygame.mixer.music.get_busy()==0:
						pygame.mixer.music.load(theme_sound_play)
						pygame.mixer.music.play(-1)
				screen.blit(back, backrect)
				pygame.display.update()
				dmval = dumbmenu(screen, (
				'First Steps',
				'Take It Easy',
				'In The Medium Of Nowhere',
				'Die Hard',
				'You Must Be Insane',
				'Don\'t Even Try',
				'Back'), x_pos=300, size=28)
				if dmval == 6:
					MainMenu4=False
					continue
				elif dmval == 0:
					MainMenu3=True
					while MainMenu3==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						level_level=dmval
						screen.blit(back, backrect)
						pygame.display.update()
						lev_dmval = dumbmenu(screen, (
						'Level 1',
						'Level 2',
						'Level 3',
						'Level 4',
						'Level 5',
						'Back'), x_pos=400, size=28)
						if lev_dmval==5:
							MainMenu3=False
							continue
						else:
							start_dmval=lev_dmval
							MainMenu=True
							win=False
							while MainMenu==True and MainMenu3==True:
								play_random(songs)
								screen.blit(back, backrect)
								matrix=loadLvl(level_dict[level_level], lev_dmval+1)
								drawlevel_small(matrix, lev_dmval+1)
								MainMenu2=True
								direction="A"
								begin_target=getTargetPosition(matrix)
								while MainMenu==True and MainMenu2==True:
									for event in pygame.event.get():
										if event.type == pygame.QUIT: sys.exit()
										elif event.type == pygame.KEYDOWN:
											if event.key == pygame.K_ESCAPE:
												MainMenu=False
												pygame.mixer.music.stop()
												continue
											elif event.key == pygame.K_r:
												MainMenu2=False
												continue
											elif event.key == pygame.K_LEFT:
												direction="L"
											elif event.key == pygame.K_RIGHT:
												direction="R"
											elif event.key == pygame.K_DOWN:
												direction="D"
											elif event.key == pygame.K_UP:
												direction="U"
									if direction!="A":
										movePlayer_small(direction,matrix, lev_dmval+1)
									direction="A"
									if countKeys(matrix)==0 and getPlayerPosition(matrix)==begin_target:
										showWin_small()
										if lev_dmval==4:
											if start_dmval==0:
												leonardo_small()
											MainMenu=False
											pygame.mixer.music.stop()
											continue
										else:
											lev_dmval=lev_dmval+1
											MainMenu2=False
											continue
					

				else:
					MainMenu3=True
					while MainMenu3==True:
						if if_sound==0:
							if pygame.mixer.music.get_busy()==0:
								pygame.mixer.music.load(theme_sound_play)
								pygame.mixer.music.play(-1)
						level_level=dmval
						screen.blit(back, backrect)
						pygame.display.update()
						lev_dmval = dumbmenu(screen, (
						'Level 1',
						'Level 2',
						'Level 3',
						'Level 4',
						'Level 5',
						'Level 6',
						'Level 7',
						'Level 8',
						'Level 9',
						'Level 10',
						'Back'), x_pos=400, size=28)
						if lev_dmval==10:
							MainMenu3=False
							continue
						else:
							start_dmval=lev_dmval
							MainMenu=True
							win=False
							while MainMenu==True and MainMenu3==True:
								play_random(songs)
								screen.blit(back, backrect)
								matrix=loadLvl(level_dict[level_level], lev_dmval+1)
								drawlevel_small(matrix, lev_dmval+1)
								MainMenu2=True
								direction="A"
								begin_target=getTargetPosition(matrix)
								while MainMenu==True and MainMenu2==True:
									for event in pygame.event.get():
										if event.type == pygame.QUIT: sys.exit()
										elif event.type == pygame.KEYDOWN:
											if event.key == pygame.K_ESCAPE:
												MainMenu=False
												pygame.mixer.music.stop()
												continue
											elif event.key == pygame.K_r:
												MainMenu2=False
												continue
											elif event.key == pygame.K_LEFT:
												direction="L"
											elif event.key == pygame.K_RIGHT:
												direction="R"
											elif event.key == pygame.K_DOWN:
												direction="D"
											elif event.key == pygame.K_UP:
												direction="U"
									if direction!="A":
										movePlayer_small(direction,matrix, lev_dmval+1)
									direction="A"
									if countKeys(matrix)==0 and getPlayerPosition(matrix)==begin_target:
										showWin_small()
										if lev_dmval==9:
											if start_dmval==0:
												leonardo_small()
											MainMenu=False
											pygame.mixer.music.stop()
											continue
										else:
											lev_dmval=lev_dmval+1
											MainMenu2=False
											continue