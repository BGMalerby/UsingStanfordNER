from platform import system
IS_WINDOWS = True if system() == 'Windows' else False

import os

if 'JAVAHOME' not in os.environ:
	currentJavaVersionPath = r'C:\Program Files\Java\jre1.8.0_151\bin'
	# r'' like above reads the text in quotes as raw so \b is not read as a word boundry
	if os.path.isdir(currentJavaVersionPath):
		os.environ['JAVAHOME'] = os.path.join(currentJavaVersionPath)
	else:
		javaBinDir = ''
		while not os.path.isdir(javaBinDir): javaBinDir = input('Enter Java bin directory path: ')
		os.environ['JAVAHOME'] = os.path.join(javaBinDir)

import nltk
from nltk.tag import StanfordNERTagger

currentNERPath = r'.\stanford-ner-2017-06-09'
if os.path.isdir(currentNERPath):
	ner_root = currentNERPath
else:
	ner_root = ''
	while not os.path.isdir(ner_root): ner_root = input('Enter Stanford NER Folder Path: ')

if IS_WINDOWS:
	ner_class = 'classifiers\english.all.3class.distsim.crf.ser.gz'
	ner_jar = 'stanford-ner.jar'
else:
	ner_class = 'classifiers/english.all.3class.distsim.crf.ser.gz'
	ner_jar = 'stanford-ner.jar'
	
S_NER_Tagger = StanfordNERTagger(os.path.join(ner_root,ner_class),os.path.join(ner_root,ner_jar))

print(S_NER_Tagger.tag('Rami Eid is studying at Stony Brook University in NY'.split()))


