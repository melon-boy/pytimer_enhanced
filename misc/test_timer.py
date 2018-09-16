#!/usr/bin/python

'''
Test for Enhanced Timer class

@author Marco Espinosa
@version $Revision 1.0
@date 2018/09/12 09:00:00
  
'''

import pytimer_enhanced.version
from time import sleep
from pytimer_enhanced.timer import EnhancedTimer, EventTimer



def timerTerminated():
    '''
    Function that executes at timer termination
    '''
    print "Terminated OK"        
    
def main():
    
    print "Test timer"
    print "========================================"
    print "Version: %s" % (pytimer_enhanced.version.__version__)
    print "Revision: %s" % (pytimer_enhanced.version.__revision__)
    print "Author: %s" % (pytimer_enhanced.version.__author__)
    print "========================================"
    timer = EnhancedTimer(3.0, True)
    timer.start()
    timer.addEventHandler(timerTerminated, EventTimer.TERMINATED_EVENT)
    sleep(2)
    print "Elapsed_time: %.2f " % (timer.elapsed_time)
    sleep(10)
    
    timer.stop()
    
           
if __name__ == '__main__':
    main()
    


