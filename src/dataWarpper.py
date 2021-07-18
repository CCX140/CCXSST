#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy
from candle import Candle

class DataWarpper :

	def __init__(self,period):
	    print("DataWarpper initialisation...")
	    self.cursor = 0
	    self.data = []
	    self.period = period

	def load_csv(self,path):
		print("Loading ",path,"...")
		try :
			with open(path,"r") as f:
				lines = f.readlines()
				for line in lines:
					split = line.split(",")
					self.data.append(Candle(float(split[1]),float(split[2]),float(split[3]),float(split[4])))

			print("Loaded lol")		
		except :
			print("Error : cant load file",path)


	def ma(self,nb_periods,cursor,source='C'):
		if cursor-nb_periods < 0:
			return -1
		if cursor>=self.length():
			return -1
		ma = 0
		for i in range(cursor-nb_periods,cursor):
			if source == "O":
				ma += self.data[i].open
			elif source == "H":
				ma += self.data[i].high
			elif source == "L":
				ma += self.data[i].low
			elif source == "C":
				ma += self.data[i].close

		return ma/nb_periods

	def ema(self,nb_periods,cursor,source='C'):
		ema = 0
		return ema

	def rsi(self,nb_periods,cursor,source='C'):
		if cursor-nb_periods < 0:
			return -1
		if cursor>=self.length():
			return -1
		rsi = 0

		return rsi

	def price(self,cursor,source='C'):
		if cursor>=self.length():
			return -1
		if cursor < 0:
			return -1
		if source == "O":
			return self.data[cursor].open
		elif source == "H":
			return self.data[cursor].high
		elif source == "L":
			return self.data[cursor].low
		elif source == "C":
			return self.data[cursor].open


	#nombre de bougies verte
	#nombre de bougies apres un cross de ma
	#bougie de ravalement
	#bougie verte ou rouge
	#direction des ma
	#
	#
	#

	def print_data(self):
		for candle in self.data:
			print("Open =",candle.open,"High =",candle.high,"Low =",candle.low,"Close =",candle.close)

	def current_cursor(self):
		return self.cursor

	def length(self):
		return len(self.data)



