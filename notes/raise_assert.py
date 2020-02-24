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
