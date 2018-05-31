#!/usr/bin/env python3

import logging
import time
import curses
import psycopg2

from distance import distance_controller, moving_average

def db_connection(dbName='dopavision'):
    logging.debug('Connecting to database %s' % dbName)
    conn = psycopg2.connect(database=dbName, user='pi', password='dopavision')
    conn.autocommit = True
    cur = conn.cursor()
    return cur

def run():
    logging.debug('Run controller')
    cur = db_connection()
    
    while False:
        dist_ctrl = distance_controller.DistanceController()
        dist_ctrl.run(cur)

    moving_avg = moving_average.MovingAverage()
    moving_avg.calcMovingAvg(cur)

    while False:
        damn = curses.initscr()
        d_thread = distance_thread.DistanceThread()
        distance_t = threading.Thread(name="distance_controller", 
                                       target=d_thread.run)

        distance_t.start()
        
        while True:
            if damn.getch() == 113:
                logging.debug('The thread will be terminated')
                distance_t.join()
                logging.debug('The thread was terminated')
