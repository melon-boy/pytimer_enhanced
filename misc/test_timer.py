#!/usr/bin/python

'''
Test for Enhanced Timer class

@author Marco Espinosa
@version $Revision 1.0
@date 2018/09/12 09:00:00
  
'''

from pytimer_enhanced.timer import EnhancedTimer, EventTimer
from unittest import TestCase, main


class TestTimer(TestCase):
    '''
    Class to test enhanced timer functionalities
    '''
    def run(self):
        '''
        Execute all tests
        '''
        self.__testTerminatedEvent(4.0)
        self.__testPropertiesTimer(4.0)

    def __timerTerminated(self):
        '''
        Function that executes at timer termination
        '''
        print "Terminated OK"
        
    def __testTerminatedEvent(self,timeout):
        '''
        Test terminated event
        '''
        print "Test timer terminated event"
        timer = EnhancedTimer(timeout)
        self.assertTrue(timer)
        
        timer.start()
        timer.AddEventHandler(self.__timerTerminated, EventTimer.TERMINATED_EVENT)
        
    def __testPropertiesTimer(self, timeout):
        '''
        Test properties
        '''
        print "Test timer properties"
        timer = EnhancedTimer(timeout)
        self.assertTrue(timer)
        
        status = timer.status
        self.assertTrue(status)
        
        print "Status: %s" % (status)
        
        timer.start()
        
        status = timer.status
        self.assertTrue(status)
        
        print "Status: %s" % (status)
        
    
def main():
    t = TestTimer
    t.run()
           
if __name__ == '__main__':
    main()
    


