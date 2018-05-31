#!/usr/bin/env python3

class MovingAverage(object):

    def __init__(self, avgTimeMinLen=20):
        '''
        sizeOfWindow defines the time period within which the average is calculated. 
        '''
        self.avgTimeMinLen = avgTimeMinLen
        self.dbTableName = 'distance'
        self.dbTimestampColumnName = 'created_at'
        self.dbDistanceColumnName = 'distance'
        self.dbColumnName = 'moving_average'

    def calcMovingAvg(self, dbCursor):
        '''
        Calculates average in defined time period and writes a result into datatable.
        '''
        query = 'insert into %s (moving_average) values (select avg(dist.%s) over(order by dist.%s rows between %s preceding and current row) as %s from %s dist)' % (self.dbTableName, self.dbDistanceColumnName, self.dbTimestampColumnName, self.avgTimeMinLen, self.dbColumnName, self.dbTableName)
        #print(query)
        dbCursor.execute(query)
        rows = dbCursor.fetchall()
        print(len(rows))
        
