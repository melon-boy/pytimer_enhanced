#!/usr/bin/python

'''
Test for Enhanced Timer class

@author Marco Espinosa
@version $Revision 1.0
@date 2018/09/12 09:00:00
  
'''

from time import sleep
from pytimer_enhanced.timer import EnhancedTimer, EventTimer

def timerTerminated():
    '''
    Function that executes at timer termination
    '''
    print "Terminated OK"        
    
def main():
    
    print "Test timer"
    timer = EnhancedTimer(3.0, True)
    timer.start()
    timer.addEventHandler(timerTerminated, EventTimer.TERMINATED_EVENT)
    
    sleep(10)
    timer.stop()
    
           
if __name__ == '__main__':
    main()
    


