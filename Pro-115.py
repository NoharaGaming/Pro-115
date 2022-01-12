import pandas as pd
import csv 
import statistics

df = pd.read_csv("medium_data.csv")
readingtime = df["reading_time"].to_list()
responses = df["responses"].to_list()

mean = statistics.mean(readingtime)
print(mean)

std = statistics.stdev(readingtime)

print(std)

