import os
import shutil

def save_backup(path):
    os.makedirs(path + "/backup")
    shutil.copy(path + '/citadel_gc_english.txt', path + '/backup/citadel_gc_english.txt')
    shutil.copy(path + '/citadel_gc_russian.txt', path + '/backup/citadel_gc_russian.txt')

save_backup('C:/Users/Stas/Desktop/game')