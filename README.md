ExPerceive
------------------

ExPerceive analyzes and visualizes Expense Data. Pandas and Matplotlib are used for the same.

This project started with a necessity of keeping track of monthly expenditure and to curb over-spending. 
The spreadsheet of monthly expenses serves as the Data to this project. 
Certain categories have been indroduced as an additional column in the sheet in order to categorize expenses better.

Visuals
---------------
Viz1: Expenditure by each category:

This Visual provides a pictoral representation of Percentage spent on each Category.

![Viz1](/Figure_1.png)


Viz2: Comparison with Forecast:

The Forecast sheet created during the start of the month is compared with the Actual expenses. It can help the user understand the discrepancy and thus forecast better for the next month.

![Viz2](/Figure_2.png)


Conclusions:
------------------------------------------

1. Amount spent: Bills > Food > Misc > Grocery.
2. Expenditure on Food > Allocated Budget.
3. Good Savings: Transport, Bills, Grocery. 
4. Over-Spending: Food, Misc expenses


Requirements:
--------------------
- Python 2.7
- Matplotlib
- Pandas
- Numpy 

Road-Map
------------

 - [x] Category-wise expenditure - a Visual Representation
 - [x] Comparison with the initial Forecast/Budget
 - [x] Obtain Excel sheet parameters from command line
 - [ ] Capability to analyze multiple sheet i.e. expenses over 6 months/1 year
 
 To-do
 --------

 - [x] Category-wise seggregation
 - [x] Meaningful labels to the charts. 
 - [x] Categorize the expenses sheet to get a more granular approach.
 - [x] Improvise the matplotlib charts.
 - [x] Refine the README file - requirements, explanation, each category description.
