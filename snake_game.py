import random
import curses


s= curses.initscr() # initializa the screen
curses.curs_set(0) # the cursor will not show up on the screen
sh, sw = s.getmaxyx() #get width and height
w = curses.newwin(sh, sw, 0, 0) #create new window using the defined height and width
w.keypad(1) #Excepts keypad input
w.timeout(100) #refresh the screen every 100 milli seconds

snk_x = sw/4 #snakes initial position
snk_y = sh/2 

snake = [
			[snk_y, snk_x],
			[snk_y, snk_x-1],
			[snk_y, snk_x-2],
	
		]

food = [sh/2, sw/2] #centre of the screen
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT #tell the snake where to go initially

while True: # To snart infinite movement for the every action of the snake
	next_key = w.getch()
	key = key if next_key == -1 else next_key
	if snake[0][0] in [0, sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]: #checking whether the person has lost the game or not
		curses.endwin() # kill the window 
		quit()

	new_head = [snake[0][0], snake[0][1]]
	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_LEFT:
		new_head[1] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1
	snake.insert(0, new_head)

	if snake[0] == food:
		food = None
		while food is None:
			nf = [
					random.randint(1, sh-1),
					random.randint(1, sw-1)
				 ]
			food = nf if nf not in snake else None
		w.addch(food[0], food[1], curses.ACS_PI)
	else:
		tail = snake.pop()
		w.addch(tail[0], tail[1], ' ')
	
	w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

