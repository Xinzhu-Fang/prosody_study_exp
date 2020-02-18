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
  
# This module is imported so that we can  
# play the converted audio 
import os 
dir_name ='audio_for_exp10_02_17_20'
tQuestions = pd.read_csv(os.path.join(dir_name, 'tAll_questions.csv'))
#os.mkdir(os.path.join(dir_name, 'original_mp3'))
for iQ, iR in tQuestions.iterrows():

      
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=iR.question_script, lang='en', slow=False) 
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save(os.path.join(dir_name, 'original_mp3', iR.question_file.replace('.wav', '.mp3')))
