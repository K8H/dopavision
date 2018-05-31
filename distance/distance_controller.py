#!/usr/bin/env python3

import sys
import logging
import time
import datetime

sys.path.append('/home/pi/github/VL53L0X_rasp_python/python')
import VL53L0X

class DistanceController(object):

    def __init__(self):
        # Create a VL53L0X object
        logging.debug('Init distance controller')
        self.tof = VL53L0X.VL53L0X()
        self.dbTName = 'distance'
        self.dbColumnName = 'distance'
        
    def run(self, dbCursor):
        '''
        The core of obtaining a signal in while True loop.
        TODO: separate start and stop functions, according to threads.
        '''
        # Start ranging
        #dbCursor.execute('select * from %s' % self.dbTName)

        self.tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

        timing = self.tof.get_timing()
        if (timing < 20000):
            timing = 20000
        print ("Timing %d ms" % (timing/1000))

        insertQuery = 'insert into %s (%s) values ' % (self.dbTName, self.dbColumnName)

        count = 0
        while count < 100:
            count += 1
            distance = self.tof.get_distance()
            if (distance > 0):
                if distance > 1000:
                    distance = 1000     # max operation

                values = '(%d);' % (distance)
                dbCursor.execute(insertQuery + values)
                print ("%d %d mm" % (count, distance))

        self.tof.stop_ranging()
