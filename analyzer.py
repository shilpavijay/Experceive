import pandas as pd
import logging

def csvAnalze(file):
	dfinit = pd.read_csv(file)
	dfcat = dfinit.groupby('Category').sum()
	return dfcat

if __name__ == "__main__":
	logging.basicConfig(filename='analyzerlog.log', filemode='w', level=logging.DEBUG)
	logging.info('Started')
	ret = csvAnalze('JulyExp.csv')
	logging.debug(ret)
