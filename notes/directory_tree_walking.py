#walking directory trees
# using for loops to apply some piece of code to all docs in a file tree
# the nature of code and storage is that all the things you think happen simultaneousy,
# actually just happen, very, very fast

# to walk a file tree:
# python givues us a simpl function in the os library

import os
for filename in os.walk('c://users/user/file'):
    print(f'The file name is {filename}' ) 

for subfolder in os.walk('c://users/user/file'):
    if "grant" in subfolder:
        os.rmdir(subfolder)

for folderName, file in os.walk('c://users/user/file'):
    if file.endswith('.py')
        shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')
