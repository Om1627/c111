import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import pandas as pd 
import csv
import random
import statistics
df = pd.read_csv("medium_data.csv")
poplist = df["reading_time"].to_list()

popmean = statistics.mean(poplist)
print("Population Mean {}".format(popmean))
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(poplist)-1)
        value = poplist[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
def showFig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([poplist],["Population"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "Mean"))
    fig.show()
mean_list = []
def setUp():
    
    for i in range(0,100):
        SetOfMean = randomSetOfMean(30)
        mean_list.append(SetOfMean)
    showFig(mean_list)
    mean = statistics.mean(mean_list)
    print("Sampling mean: ", mean)

setUp()

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)



first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)




fig = ff.create_distplot([mean_list], ["sampling mean"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 START"))

fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

fig.show()

mean_of_sample1 = statistics.mean(poplist)
print("Mean of sample1:- ",mean_of_sample1)
#finding the z score using the formula
z_score = (mean_of_sample1 - mean)/std_deviation
print("The z score is = ",z_score)