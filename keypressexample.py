import curses

damn = curses.initscr()
damn.nodelay(1)

while True:
    if damn.getch() == 113:
        print('The key was pressed')
        break


