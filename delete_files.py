import os, shutil, send2trash

# delete via os module
os.unlink('.\\delete_me.txt')

# delete empty folder
os.rmdir('.\\emptyfolder')

# delete folder and all of its contents

shutil.rmtree('.\\folder_with_stuff')

# use caution when deleting. Break things you can.

# eg. 
for filename in os.listdir():
    if filename.endswith('.rxt') # note typo
    # perform a dry run by commenting out delete functions and doing a print call
    # os.unlink(filename)
    print(filename)


# the send2trash module sends files to your machine's recycling bin insteadt of fully deleting, and is a good option for danger reduction

send2trash.send2trash('.\\delete_me.txt")S
