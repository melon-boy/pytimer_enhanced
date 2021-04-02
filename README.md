# Enhanced Timer for Python



This package intends to be a flexible user-friendly wrapper for the python timer. 


### Table of content

- [Installation](##Installation)
- [Documentation](##Documentation)
- [API](##API)
- [Examples](##Examples)



## Installation


**pytimer_enhanced** can be installed from one of the following methods:

### From PIP:
```
$>pip install pytimer_enhanced
```

### From Pypi.python.org:

* Download package from [pytimer_enhanced](http://pypi.python.org/pytimer_enhanced).
* Uncompress it:
	
		$>tar zxvf pytimer_enhanced-x.x.x.tar.gz
		
* Install:

		$>cd pytimer_enhanced
		$>python setup.py install
		
### From Github repository [pytimer_enhanced](https://github.com/melon-boy/pytimer_enhanced):

* Clone the git repository into the local filesystem:

		$>git clone https://github.com/melon-boy/pytimer_enhanced

* Change working directory to the project directory and run install script:

		$>cd pytimer_enhanced
		$>python setup.py install
	
## Documentation

The **pytimer_enhanced** package gives the developper an interface to the native Python Timer from *threading* module. This implementation provides the next functionalities:

* Create a single execution of a timer.
* Create a repeated execution of a timer.
* Start, stop or restart the current timer.
* Access to its status.
* Handle a terminated timer event.

## API

### Class EventTimer

This class contains the events that can be handler.

**TERMINATED_EVENT** - Event raised when timer is terminated.

### Class TimerEnhanced

This class contains the enhanced timer implementation. 

#### Constructor

*TimerEnhanced(timeout, repeat=False)*

This constructor can take two arguments:

* **timeout** - (Mandatory) - Timer time.
* **repeat** - (Optional) - If True, tells timer to repeat indefinitly. This parameter is False by default.

#### Properties

* **status** - Returns True if timer is running. False otherwise.
* **elapsed_time** - Returns the elapsed timer running time.
* **terminated** - Returns True if timer has terminated. False otherwise.

#### Public Methods

*start()* - Starts the timer execution.

*stop()* - Stops the timer execution.

*restart()* - Restarts timer execution.

#### Event Handlers

*addEventHandler(notifier, event_type)* - register an event handler to a particular event.

* **notifier** - Function to execute when event *event_type* raised.
* **event_type** - Event to register.

*removeEventHandler(notifier)* - unregister an event handler.

* **notifier** - Function to be unregistered from the timer event handler system.

*removeAllEventHandlers()* - unregister all event hanlders.

## Examples

### Example 1: Launching a one time timer

This example launch a timer of 2 seconds.

	>>> from pytimer_enhanced.timer import EnhancedTimer
	>>> t = EnhacedTimer(2.0)
	>>> t.start()

### Example 2: Registering for the timer terminated event

This exemple initialize a timer of 2 seconds and register the function *foo* to be executed when *TERMINATED* timer event raised.

	>>> from pytimer_enhanced.timer import EnhancedTimer, EventTimer
	>>> t = EnhacedTimer(2.0)
	>>> t.addEventHandler(foo, EventTimer.TERMINATED_EVENT)

	
### Example 3: Getting timer status 

	>>> from pytimer_enhanced.timer import EnhancedTimer, EventTimer
	>>> t = EnhacedTimer(2.0)
	>>> if t.status():
	>>>	     print "Timer is running!"
	>>> else:
	>>>     print "Timer stopped." 

### Example 4: Getting elapsed time

	>>> from pytimer_enhanced.timer import EnhancedTimer, EventTimer
	>>> t = EnhacedTimer(10.0)
	>>> t.start()
	>>>	print "Elapsed time: %.2f " % t.elapsed_time()     

### Example 4: Unregistering an event handler

From the code of exemple 2, we can unregister an event handler as follows:

	>>> t.removeEventHandler(foo)

### Example 5: Launching a repeated timer

This example launch a timer that executes every 2 seconds until it is programmatically stopped.

	>>> from pytimer_enhanced.timer import EnhancedTimer
	>>> t = EnhacedTimer(2.0, True)
	>>> t.start()

### Example 6: Stopping a timer

From the code of exemple 5, we can stop a timer as follows:

	>>> t.stop()


### Example 7: Restarting a timer

From the code of exemple 1, we can restart a timer as follows:

	>>> t.restart()

## Credits

Developed with [Eclipse IDE](https://www.eclipse.org).

Marco Espinosa *(melon-boy)* © 2018 (hi@marcoespinosa.es)

