#!/usr/bin/env python

import speech_recognition as sr
from sound_play.libsoundplay import SoundClient
import time

speaker = SoundClient()
ear = sr.Recognizer()

def hear_color():

	speaker.say("What color is the object?")
	time.sleep(2)
	with sr.Microphone() as source:
		ear.adjust_for_ambient_noise(source)
		print("Retriving Red or Green")
		audio = ear.listen(source,timeout=4)

	try:

		text = ear.recognize_google(audio)
		if text == "red":
			print(text)
			return text
		elif text == "green":
			print(text)
			return text

	except:
		
		print("I did not hear")
		text = raw_input("red or green: ")
		return str(text)



		
def hear_size():

	speaker.say("What size is the object?")
	time.sleep(2)
	with sr.Microphone() as source:
		ear.adjust_for_ambient_noise(source)
		print("Retriving Small or Large")
		audio = ear.listen(source,timeout=4)

	try:

		text = ear.recognize_google(audio)
		if text == "small":
			print(text)
			return text
		elif text == "large":
			print(text)
			return text

	except:
		
		print("I did not hear")
		text = raw_input("small or large: ")
		return str(text)

def confirm_rs():

	speaker.say("Is the object red and small?")
	time.sleep(2)
	with sr.Microphone() as source:
		ear.adjust_for_ambient_noise(source)
		print("Retriving Y/N")
		audio = ear.listen(source,timeout=4)

	try:

		text = ear.recognize_google(audio)
		if text == "yes":
			print(text)
			return text
		elif text == "no":
			print(text)
			return text

	except:
		
		print("I did not hear")
		text = raw_input("yes or no: ")
		return str(text)


def confirm_rl():

	speaker.say("Is the object red and large?")
	time.sleep(2)
	with sr.Microphone() as source:
		ear.adjust_for_ambient_noise(source)
		print("Retriving Y/N")
		audio = ear.listen(source,timeout=4)

	try:

		text = ear.recognize_google(audio)
		if text == "yes":
			print(text)
			return text
		elif text == "no":
			print(text)
			return text

	except:
		
		print("I did not hear")
		text = raw_input("yes or no: ")
		return str(text)


def confirm_gs():

	speaker.say("Is the object green and small?")
	time.sleep(2)
	with sr.Microphone() as source:
		ear.adjust_for_ambient_noise(source)
		print("Retriving Y/N")
		audio = ear.listen(source,timeout=4)

	try:

		text = ear.recognize_google(audio)
		if text == "yes":
			print(text)
			return text
		elif text == "no":
			print(text)
			return text

	except:
		
		print("I did not hear")
		text = raw_input("yes or no: ")
		return str(text)


def confirm_gl():

	speaker.say("Is the object green and large?")
	time.sleep(2)
	with sr.Microphone() as source:
		ear.adjust_for_ambient_noise(source)
		print("Retriving Y/N")
		audio = ear.listen(source,timeout=4)

	try:

		text = ear.recognize_google(audio)
		if text == "yes":
			print(text)
			return text
		elif text == "no":
			print(text)
			return text

	except:
		
		print("I did not hear")
		text = raw_input("yes or no: ")
		return str(text)
















