#!/usr/bin/env python3

import logging
import time
import curses
import psycopg2

from distance import distance_controller, signal_processing

def db_connection(dbName='dopavision'):
    logging.debug('Connecting to database %s' % dbName)
    conn = psycopg2.connect(database=dbName, user='pi', password='dopavision')
    conn.autocommit = True
    cur = conn.cursor()
    return cur

def run():
    logging.debug('Run controller')
    cur = db_connection()
    
    # get data from sensor for specific number of iterations
    dist_ctrl = distance_controller.DistanceController()
    dist_ctrl.run(cur)

    signal_proc = signal_processing.SignalProcessing()
    signal_proc.calcMovingAvg(cur)

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
