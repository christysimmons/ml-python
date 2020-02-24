import shutil

# straight copy

shutil.copy('.\\copy_from\\flaming_katy.txt', '.\\paste_to')

# copy and rename

shutil.copy('.\\copy_from\\flaming_katy.txt', '.\\paste_to\\christmas_cactus.txt')

#copy entire folder

shutil.copytree(".\\copy_from", '.\\copy_from_backup')

# move file

shutil.move('.\\paste_to\\christmas_cactus.txt', '.\\copy_from_backup')

# "renamimg" files (move to the same directory but with a new name)

shutil.move('.\\copy_from_backup\\christmas_cactus.txt', '.\\copy_from_backup\\roseum.txt')
