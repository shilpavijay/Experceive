import pandas as pd
import numpy as np
import logging
import matplotlib.pyplot as plt


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
	
	N = 5
	# forecast = ()
	return dfbudget.head()


if __name__ == "__main__":
	logging.basicConfig(filename='analyzerlog.log', filemode='w', 
						level=logging.DEBUG)
	logging.info('Experceive')
	budget = Analysis('JulyExp.csv','JulyForecast.csv')
	logging.debug(budget)
	# plt.show()
