import pandas as pd
import logging
import matplotlib.pyplot as plt


def csvAnalze(file):
	dfinit = pd.read_csv(file)
	dfcat = dfinit.groupby('Category').sum()
	dfcat.plot(kind='pie', subplots='True')
	labels = ['Grocery', 'Food', 'Others', 'Phone Exp', 'Travel Exp']
	plt.legend(labels)
	return dfcat


if __name__ == "__main__":
	logging.basicConfig(filename='analyzerlog.log', filemode='w', level=logging.DEBUG)
	logging.info('Started')
	ret = csvAnalze('JulyExp.csv')
	logging.debug(ret)
	plt.show()
