#!/usr/bin/env python3

import keyboard

def keypress():
    while True:
        try:
            if keyboard.is_pressed('q'):
                print('The key was pressed')
                break
            else:
                pass

if __name__=='__main__':
    keypress()
