'''
1. import  file
2. remove formatting of the text

'''

# import all packages
import webvtt
import re

for caption in webvtt.read('captions_text.vtt'):
    print(caption.start)
    print(caption.end)
    print(caption.text)

# formatting


