#-------------------------------------------------------------------------
# AUTHOR: Josephine Nguyen
# FILENAME: naive_bayes.py
# SPECIFICATION: This program reads the weather_training.csv and weather_test.csv to use clf to train the model and run test data. The program outputs all classficiations of the test data who's confidence level is above 75%
# FOR: CS 4210- Assignment #2
# TIME SPENT: 40min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv


# Outlook: Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# Temp: Hot = 1, Mild = 2, Cool = 3,
# Humidity: High = 1, Normal = 2,
# Wind: Weak = 1, Strong = 2
def parseAttributes(dataList):
    twoDArray = []

    for attribute in dataList:
        currRow = []
        for valueIndex in range(len(attribute)):
            value = attribute[valueIndex]

            #Check Outlook values:
            if valueIndex == 1:
                if value == "Sunny":
                    currRow.append(1)
                elif value == "Overcast":
                    currRow.append(2)
                elif value == "Rain":
                    currRow.append(3)
                else:
                    print("something went wrong")

            # Check Temp values:
            elif valueIndex == 2:
                if value == "Hot":
                    currRow.append(1)
                elif value == "Mild":
                    currRow.append(2)
                elif value == "Cool":
                    currRow.append(3)
                else:
                    print("something went wrong")

            # Check Humidity values:
            elif valueIndex == 3:
                if value == "High":
                    currRow.append(1)
                elif value == "Normal":
                    currRow.append(2)
                else:
                    print("something went wrong")

            # Check Wind values:
            elif valueIndex == 4:
                if value == "Weak":
                    currRow.append(1)
                elif value == "Strong":
                    currRow.append(2)
                else:
                    print("something went wrong")

        twoDArray.append(currRow)
    return twoDArray


#reading the training data
dsTraining = []

with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dsTraining.append(row)


#transform the original training features to numbers and add to the 4D array X. For instance
X = parseAttributes(dsTraining)

#transform the original training classes to numbers and add to the vector Y.
Y = []
for instance in dsTraining:
        value = instance[5]            #get only the value for the playTennies attribute
        # Check Rec Lenses values:
        if value == "Yes":
            Y.append(1)
        elif value == "No":
            Y.append(2)
        else:
            print("something went wrong")


#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
dsTest = []

with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dsTest.append(row)

all_tests = parseAttributes(dsTest)

confident_days = []
#use your test samples to make probabilistic predictions.
for i, test_instance in enumerate(all_tests):
    predicted = clf.predict_proba([test_instance])[0]
    class_predicted = clf.predict([test_instance])[0]

    #if confidence level is good enough
    if predicted[0] >= 0.75:

        #Update the classification under playTennis
        instance_str = dsTest[i]
        if class_predicted == 1:
            instance_str[5] = "Yes"
        else:
            instance_str[5] = "No"

        #appead the confidence level to print it later
        dsTest[i].append(predicted[0])
        confident_days.append(dsTest[i])


# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))
for instance in confident_days:
    print(str(instance[0]).ljust(15) + str(instance[1]).ljust(15) +str(instance[2]).ljust(15) + str(instance[3]).ljust(15) + str(instance[4]).ljust(15) + str(instance[5]).ljust(15) + str(instance[6]).ljust(15))