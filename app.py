import os, shutil, argparse
from pathlib import Path
from musicfile import MusicFile
import eyed3

dropFolderPath = "C:\\dev\\musicOrganizer\\drop"

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
    path = os.path.join("C:\\dev\\musicOrganizer", music_File.artist_name, music_File.album_name)
    create_directory(path)
    shutil.copy(music_File.full_file_name, path)

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--Source", help = "Source location where files are located", required=True)

args = parser.parse_args()

if args.Source:
    dropFolderPath = args.Source


files = os.listdir(dropFolderPath)

for file_name in files:
    if file_name == "ReadMe.md":
        continue
    
    print("Handling " + file_name)
    music_File = read_music_file(file_name)
    if music_File is not None:
        organize_music_file(music_File)

print("Done.")
