#!/usr/bin/python

'''
Test for Enhanced Timer class

@author Marco Espinosa
@version $Revision 1.0
@date 2018/09/12 09:00:00
  
'''

from pytimer_enhanced.timer import EnhancedTimer, EventTimer
from time import sleep

def timerTerminated():
    print "Terminated"

def otherfunc():
    print "Time elapsed demanded!"
    
def main():
    
    print "Test for own Timer"
    t = EnhancedTimer(3.0)
    t.start()
    t.AddEventHandler(timerTerminated, EventTimer.TERMINATED_EVENT)
    
    
    sleep(1)
    print "Elapsed time: %.0f" % t.elapsed_time
    t.RemoveEventHandler(timerTerminated)
    t.RemoveAllEventHandlers()
    
    
if __name__ == '__main__':
    main()
