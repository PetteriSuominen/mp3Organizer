import os, shutil, argparse
from pathlib import Path
from musicfile import MusicFile
import eyed3

parser = argparse.ArgumentParser()
parser.add_argument("--source", required=True)
parser.add_argument("--destination", required=True)

args = parser.parse_args()

dropFolderPath = args.source
destinationPath = args.destination

def read_music_file(file_name):
    full_file_name = os.path.join(dropFolderPath, file_name)
    audiofile = eyed3.load(full_file_name)

    if audiofile is None:
        print("File " + file_name  + " is not supported, skipping the file.")
        return None

    artist = audiofile.tag.artist
    album = audiofile.tag.album
    return MusicFile(artist, album, full_file_name)

def create_directory(path):
    print("Creating directory path: " + path)
    Path(path).mkdir(parents=True, exist_ok=True)

def organize_music_file(music_file):
    path = os.path.join(destinationPath, music_file.artist_name, music_file.album_name)
    create_directory(path)
    shutil.copy(music_file.full_file_name, path)

files = os.listdir(dropFolderPath)

for file_name in files:    
    print("Handling " + file_name)
    music_File = read_music_file(file_name)
    if music_File is not None:
        organize_music_file(music_File)

print("Done.")
