#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Main_Hello_World.py
#  
#  Copyright 2021 Matt Evans <mbevans@Buddy-Ubuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
def argumentParsing():
	parser = argparse.ArgumentParser()
	parser.add_argument("name", type=str,
		help="Your name")
	parser.add_argument("freq", type=float,
		help="The frequency or sample rate of the data")
	parser.add_argument("-d", "--debugLevel", type=int, choices=[0,1,2], default=0,
		help="The debug level of the output; 0 for quiet, 1 for informational data only, 2 for most verbose(informational and debug).")
	args=parser.parse_args()
	return args

def main(args):
	commandArgs=argumentParsing()
	print(f'Hello World, {commandArgs.name}')
	if commandArgs.debugLevel == 2:
		print(f"The sample rate for the data is {commandArgs.freq} Hz")
	elif commandArgs.debugLevel == 1:
		print(f"Sampe rate = {commandArgs.freq} Hz")
	else:
		print(f"{commandArgs.freq} Hz")
	return 0

if __name__ == '__main__':
	import sys
	import argparse
	sys.exit(main(sys.argv))
