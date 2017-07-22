""" analyze.py:  File that performs analysis and visualizes the data 

This file takes as an input two csv sheets with expenses in one 
with the following format:
Data, Amount, Category, Comments

The other csv contains the Forecast/Budget with the format:
Category, Amount, Details

"""

import pandas as pd
import numpy as np
import logging
import matplotlib.pyplot as plt


__author__ = "Shilpa Amberker"
__copyright__ = "Copyright 2017, Experceive"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "shilpa.amberker@gmail.com"
__status__ = "Development"


def Analysis(exp,budget):
	dfinit = pd.read_csv(exp)
	dfcat = dfinit.groupby('Category').sum()
	logging.info(dfcat)
	labels = ['Grocery', 'Food', 'Others', 'Phone Exp', 'Transport']
	explode = (0, 0.05, 0, 0, 0)
	colors = ['#b64b50', '#f46e6e', '#f69a9a', '#4dc9ba', '#afd2e7']

	dfcat.plot(kind='pie', subplots='True', autopct='%1.1f%%', labels=labels, 
				shadow=True, startangle=90, explode=explode, colors=colors, legend=None)

	plt.subplots_adjust(left=0.13, bottom=0.09, right=0.78, top=0.9, 
						wspace=0.2, hspace=0.2)

	# plt.title('Experceive', bbox={'facecolor' : '0.9', 'pad' : 3})


	# Comaparing with the Forecast Sheet
	dfbudget = pd.read_csv(budget)	
	a = dfbudget.Category
	
	N = 5
	loc = np.arange(N)       # no. of locations for the groups
	width = 0.35              # width of each bar
	fig, ax = plt.subplots()
	forecast_val = [int(dfbudget[a == 'BB'].Amount[0]), 
					int(dfbudget[a == 'P'].Amount[1]), 
					int(dfbudget[a == 'T'].Amount[2]), 
					int(dfbudget[a == 'F'].Amount[3]),
					int(dfbudget[a == 'O'].Amount[6])]
	forecast_std = (1, 1, 2, 1, 2)
	forecast = ax.bar(loc, forecast_val, width, color='#692b50', yerr=forecast_std)


	#actual values from exp.csv
	actual_val = [dfcat.Amount[0], dfcat.Amount[3], dfcat.Amount[4], dfcat.Amount[1], dfcat.Amount[2]]				
	actual_std = (2, 5, 2, 3, 3)  
	actuals = ax.bar(loc + width + 0.02, actual_val, width, color='#2b6944', yerr=actual_std)

	#text for the labels, title and axes ticks
	ax.set_ylabel('Amount')
	ax.set_xticks(loc + width / 2)
	ax.set_xticklabels(('Grocery', 'Phone', 'Transport', 'Food', 'Others'))
	ax.set_title('Amount by Categories')

	ax.legend((forecast[0], actuals[0]), ('Forecast', 'Actuals'))


	def autolabel(rects):
		"""
		Attach a text label above each bar displaying its height
		"""
		for rect in rects:
			height = rect.get_height()
			ax.text(rect.get_x() + rect.get_width()/2., 1*height,
					'%d' % int(height),
					ha='center', va='bottom')

	autolabel(forecast)
	autolabel(actuals)
	return forecast_val


if __name__ == "__main__":
	logging.basicConfig(filename='analyzerlog.log', filemode='w', 
						level=logging.DEBUG)
	logging.info('Experceive')
	expsheet = raw_input('Expense sheet: ')
	forecast = raw_input('Forecast sheet: ')
	budget = Analysis(expsheet, forecast)
	logging.debug(budget)
	plt.show()
