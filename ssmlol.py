#!/usr/bin/env python
import argparse
from eyed3 import mp3

try:
    from colored import fg, attr
except ImportError:
    fg = lambda *_: ''
    attr = fg

parser = argparse.ArgumentParser(description='Validate an MP3 file for use in an Alexa SSML <audio> tag.')
parser.add_argument('file', help='MP3 file to check')
args = parser.parse_args()

info = mp3.Mp3AudioFile(args.file).info
valid = True

def test_true(statement, description):
    global valid
    if statement == True:
        print(u'{0}\u2713 {description[0]} is {description[1]}{1}'.format(fg('green'), attr('reset'), description=description))
    else:
        print(u'{0}\u2715 {description[0]} should be {description[1]} (it\'s {description[2]}){1}'.format(fg('red'), attr('reset'), description=description))
        valid = False

print('Starting Alexa audio test...')
test_true(info.mp3_header.version == 2.0, ('MP3 version', 2, int(info.mp3_header.version)))
test_true(info.vbri_header == None, ('Bit rate', 'constant', 'variable'))
test_true(info.bit_rate[1] == 48, ('Bit rate', '48 kbps', info.bit_rate[1]))
test_true(info.sample_freq == 16000, ('Sample rate', '16 khz', info.sample_freq / 1000))

if valid == True:
    # only do this if everything else is right because otherwise eyeD3 tends to give a wildly inaccurate value
    test_true(info.time_secs <= 90, ('File length', '90 seconds or less', info.time_secs))

if valid == True:
    print('Result: {0}Pass!{1} Your file should work with Alexa.'.format(fg('green'), attr('reset')))
else:
    print('Result: {0}Failure.{1}'.format(fg('red'), attr('reset')))