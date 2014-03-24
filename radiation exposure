def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    epsilon = 0.01
    if (stop - start) <= epsilon:
        return 0
    elif start == stop:
        return f(start)
    else:
        return f(start) * step + radiationExposure(start + step, stop, step)

#559.2259707824549
