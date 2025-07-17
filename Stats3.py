import statistics
import math
from collections import Counter

stats = ("Mean",
         "Median",
         "Mode",
         "Sum",
         "Variance",
         "Standard Deviation (SD)",
         "Coefficient of Variation (CV)",
         "Class Limits (CL)",
         "Class Width (CW)",
         "Frequency",
         "Frequency distribution (FD)")
data = [200,
        239,
        155,
        252,
        384,
        165,
        296,
        405,
        303,
        400,
        307,
        241,
        256,
        315,
        330,
        317,
        352,
        266,
        276,
        345,
        238,
        306,
        290,
        271,
        345
]


def mean(mean):
    mean = round(statistics.mean(data))
    print(f"{mean:.2f}")

def median(median):
    median = statistics.median(data)
    print(f"{median:.2f}")

def mode(mode):
    mode = statistics.mode(data)
    print(f"{mode:.2f}")
   
def total_sum(sum1):
    sum1 = sum(data)
    print(f"{sum1:.2f}")
    
def variance(variance):
    variance = statistics.variance(data)
    print(f"{variance:.2f}")

def standard_deviation(standard_deviation):
    standard_deviation = statistics.stdev(data)
    print(f"{standard_deviation:.2f}")

def coefficient_variation(coefficient_variation):
    coefficient_variation = (statistics.stdev(data) / (statistics.mean(data)))
    print(f"{coefficient_variation:.2f}")
    
def classLimits(data):
    mini = min(data)
    maxi = max(data)    
    print("The lower class Limit is:", mini)
    print("The upper class Limit is: ", maxi)

def classWidth(data):
    num_classes = int(input("Enter number of classes: "))
    sorted_data = sorted(data)
    data_range = max(sorted_data) - min(sorted_data)
    class_width = round(data_range / num_classes)
    print("The class width is", class_width)
    return class_width

def frequency(data):
    data = sorted(data)
    print(dict(Counter(data)))
    
def frequency_distribution(data):
    num_classes = int(input("Enter number of classes: "))
    sorted_data = sorted(data)
    data_range = max(sorted_data) - min(sorted_data)
    class_width = math.ceil(data_range / num_classes)

    min_val = min(sorted_data)
    frequency = {}

    for i in range(num_classes):
        lower = min_val + i * class_width
        upper = lower + class_width - 1
        # Count elements within the bin range
        count = sum(lower <= x < upper for x in sorted_data)
        frequency[f"{lower}-{upper}"] = count

    print("The frequency distribution is:", frequency)
    return frequency
  

statF = {
    "Mean" : mean,
    "Median" : median,
    "Mode" : mode,
    "Sum" : total_sum,
    "Variance" : variance,
    "SD" : standard_deviation,
    "Standard Deviation" : standard_deviation,
    "CV" : coefficient_variation,
    "Coefficient Variation" : coefficient_variation,
    "CL" : classLimits,
    "Class Limits" : classLimits,
    "Frequency" : frequency,
    "FD" : frequency_distribution,
    "Frequency Distribution" : frequency_distribution,
    "CW" : classWidth
}


print("Hello, let's work on your statistics homework together. Type 'Exit' at any time to stop.")
print(stats)
print()

while True:
    choice = input("Which statistical function do you wish to execute?: ").capitalize()
    if choice == "Exit":
        print("Let's take a break.")
        break
    elif choice in statF:
        statF[choice](data)
        print()
    else:
        print("Invalid entry, try again.")
