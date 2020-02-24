def boxPrint(symbol, w, h):
    if len(symbol != 1):
        raise Exception("symbol needs to be a string of length = 1")
    if (w < 2) or (h < 2)
        raise Exception("Width and height need to integers greater than 1.")

    print (symbol * w)
    
    for i in range (h - 2):
        print(symbol + (" "*(w-2)) + symbol)

    print (symbol * w)

# traceback management

import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was logged to error_log.txt.')

# assert, for sanity checks
# if the assert statement evaluates to false, the assert error is raised

assert False, "Error message"

k_21 = {'ns': 'green' 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys()
        if intersection[key] == 'green':
            intersection[key] == 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] == 'red'
        elif intersection[key] == 'red':
            intersection[key] == 'green'


    assert 'red' in intersection.values(), "Neither light is red" + str(intersection)

switchLights(k_21)

# assertions - unrecoverable programmer errors,
# exceptions - user errors that can ne recovered from
