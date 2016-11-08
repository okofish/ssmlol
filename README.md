# SSMLOL

SSMLOL is an MP3 file validator for Alexa SSML `<audio>` tags. Amazon is very particular about the files it lets you play, and with terse error messages, testing them can be quite a hassle. SSMLOL is a command-line tool written in Python that can check your files for all known current Alexa requirements.

## Use

Using SSMLOL is pretty simple! Just install the requirements (see below), copy the files you want to validate to the directory you downloaded SSMLOL to, and run `python ssmlol.py myfile.mp3`. It should instantly spit out a report on your file (with pretty colors if you installed colored!)

## Requirements

The only package SSMLOL requires is the eyeD3 audio file metadata parser. It also supports colored for the report outputs, but it isn't absolutely required. You can install both with this pip command (you might have to run it with sudo):

    pip install eyed3 colored