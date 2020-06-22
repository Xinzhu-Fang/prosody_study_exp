#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:43:54 2020

@author: xzfang
"""

#https://www.geeksforgeeks.org/convert-text-speech-python/
#https://pypi.org/project/gTTS/
# Import the required module for text
# to speech conversion
from gtts import gTTS
import pandas as pd
from pydub import AudioSegment


# This module is imported so that we can
# play the converted audio
import os

type = "computer-dry"
type = "computer-human" #manual

# dir_name ='audio_for_exp12_03_19_20'
dir_name = 'audio_for_exp14_06_19_20'

tQuestions = pd.read_csv(os.path.join(dir_name, 'tAll_questions.csv'))
os.mkdir(os.path.join(dir_name, 'original_mp3'))

if type == "computer-dry":
    os.mkdir(os.path.join(dir_name, 'constituents_mp3'))
    for iQ, iR in tQuestions.iterrows():
        words = iR.question_script.split(' ')
        myobj0 = gTTS(text=words[0], lang='en')
        myobj0.save(os.path.join(dir_name, 'constituents_mp3', words[0] + '.mp3'))
        song0 = AudioSegment.from_mp3(os.path.join(dir_name, 'constituents_mp3',  words[0]+ '.mp3' ))


        myobj1 = gTTS(text=words[1], lang='en')
        myobj1.save(os.path.join(dir_name, 'constituents_mp3', words[1] + '.mp3'))
        song1 = AudioSegment.from_mp3(os.path.join(dir_name, 'constituents_mp3', words[1]+ '.mp3' ))


        myobj2 = gTTS(text=words[2], lang='en')
        myobj2.save(os.path.join(dir_name, 'constituents_mp3', words[2] + '.mp3'))
        song2 = AudioSegment.from_mp3(os.path.join(dir_name, 'constituents_mp3', words[2]+ '.mp3' ))


        myobj3 = gTTS(text=words[3], lang='en')
        myobj3.save(os.path.join(dir_name, 'constituents_mp3', words[3] + '.mp3'))
        song3 = AudioSegment.from_mp3(os.path.join(dir_name, 'constituents_mp3', words[3]+ '.mp3' ))

        merged = song0 + song1 + song2 + song3
        merged.export(os.path.join(dir_name, 'original_mp3',  iR.question_file.replace('.wav', '.mp3')), format='mp3')

        print(iR.question_file.replace('.wav', '.mp3'))
else:
    for iQ, iR in tQuestions.iterrows():
        # print(iR)
        myobj = gTTS(text=iR.question_script, lang='es-us')
        myobj.save(os.path.join(dir_name, 'original_mp3',  iR.question_file.replace('.wav', '.mp3')))
