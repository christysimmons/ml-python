#walking directory trees
# using for loops to apply some piece of code to all docs in a file tree
# the nature of code and storage is that all the things you think happen simultaneousy,
# actually just happen, very, very fast

# to walk a file tree:
# python givues us a simpl function in the os library

import os
for filename in os.walk('c://users/user/file'):
    print(f'The file name is {filename}' ) 
