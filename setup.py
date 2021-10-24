import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Temperature", y="Ice-cream Sales( ₹ )")
        fig.show()
        
def getDataSource(data_path):
  marks_in_percentages = []
  days_present = []
  with open(data_path) as csv file:
    csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    marks_in_percentages = append(float(row["Marks in Percentage"]))
    days_present = append(float(row["Days Present']))
         
  return ("x":marks_in_percentages, "y" : days_present)
                                    
                                    
def findCorrelation(dataSource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])        
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup:
    data_path = "./data/Student Marks vs Days Present.csv"
                               
dataSource = getDataSource(data_path)
findCorrelation(dataSource)
                                    
setup()
