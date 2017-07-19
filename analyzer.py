import pandas as pd
import logging
import matplotlib.pyplot as plt


def csvAnalze(file):
	dfinit = pd.read_csv(file)
	dfcat = dfinit.groupby('Category').sum()
	labels = ['Grocery', 'Food', 'Others', 'Phone Exp', 'Travel Exp']
	dfcat.plot(kind='pie', subplots='True', autopct='%1.1f%%', 
		labels=labels, shadow=True, startangle=90)
	return dfcat


if __name__ == "__main__":
	logging.basicConfig(filename='analyzerlog.log', filemode='w', level=logging.DEBUG)
	logging.info('Started')
	ret = csvAnalze('JulyExp.csv')
	logging.debug(ret)
	plt.show()
