#!/usr/bin/python

'''
Enhanced Timer python package

@author Marco Espinosa
@version $Revision 1.0
@date 2018/09/12 09:00:00
  
'''

from threading import Timer
from time import sleep
from time import time


class EventTimer:
    '''
    Event timer definitions
    '''
    TERMINATED_EVENT = 0


class EnhancedTimer:
    '''
    Timer class to handle an own implementation of a Python Timer
    '''
    
    def __init__(self, seconds, repeat=False):
        '''
        Constructor
        '''
        self._seconds = seconds
        self._running = False
        self._start_time = 0.0
        self._elapsed_time = 0.0
        self._terminated = False
        self._repeat = repeat
        
        self.__configure_event_handlers()
    
    # #  Public methods    
        
    def start(self):
        '''
        Starts the timer with the constructor parameters
        '''
        if not self._running:
            self._timer = Timer(self._seconds, self.__terminated)
            self._timer.start()
            self._start_time = time()
            self._elapsed_time = 0.0
            self._terminated = False
            self._running = True
        
    def stop(self):
        '''
        Stops the timer
        '''
        if self._running:
            self._timer.cancel()
        
        self.__init_variables()
        
    def restart(self):
        '''
        Restarts the timer
        '''
        self.stop()
        sleep(1)
        self.start()
    
    # #  Event Handlers
    
    def addEventHandler(self, notifier, event_type):
        '''
        Attach a function to callback for terminated notifications
        '''
        if event_type == EventTimer.TERMINATED_EVENT:
            self._terminated_event_handlers.add(notifier)

    def removeEventHandler(self, notifier):
        '''
        Detach a function to callback for terminated notifications
        '''
        for handler in self._event_handlers:
            handler.discard(notifier)
            print "Event handler %s removed" % repr(notifier)

    def removeAllEventHandlers(self):
        '''
        Detach all event handlers
        '''
        for handler in self._event_handlers:
            print "Event handler %s removed" % repr(handler)
            handler = None
    
    # #  Properties
    
    @property    
    def status(self):
        '''
        Returns the status of the timer
        '''
        return self._running
    
    @property
    def elapsed_time(self):
        '''
        Returns elapsed time from a running Timer
        '''
        self._notify_others()
        
        if self._running:
            return time() - self._start_time
        else:
            return self._start_time
        
    @property
    def terminated(self):
        '''
        Returns terminated status of the timer
        '''
        return self._terminated 
    
    # #  Private methods
    
    def __configure_event_handlers(self):
        '''
        Configure notifiable objects
        '''
        self._terminated_event_handlers = set()
        self._event_handlers = []
        self._event_handlers.append(self._terminated_event_handlers)
        
    def __notify_terminated(self):
        '''
        Launch terminated event to event handlers
        '''
        for notifier in self._terminated_event_handlers:
            notifier()
        
    def __init_variables(self):
        '''
        Variables initialization
        '''
        self._start_time = 0.0
        self._elapsed_time = 0.0
        self._running = False
        
    def __terminated(self):
        '''
        Function called when timer terminated event raised
        '''
        self._terminated = True
        self.__init_variables()
        self.__notify_terminated()
        
        if self._repeat:
            # Restart timer
            self.start()

