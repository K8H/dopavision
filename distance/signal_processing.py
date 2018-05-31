#!/usr/bin/env python3

class SignalProcessing(object):

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
        withQuery = 'with new_values as'
        selectQuery = 'select id, avg(dist.%s) over(order by dist.%s rows between %s preceding and current row) as %s from %s dist' % (self.dbDistanceColumnName, self.dbTimestampColumnName, self.avgTimeMinLen, self.dbColumnName, self.dbTableName)
        updateQuery = 'update %s as dist set %s = nv.%s from new_values nv where nv.id = dist.id;' % (self.dbTableName, self.dbColumnName, self.dbColumnName)        
        query = withQuery + ' (' + selectQuery + ') ' + updateQuery
        dbCursor.execute(query)
