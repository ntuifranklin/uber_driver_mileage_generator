
from datetime import date
from random import randint
from calendar import monthrange
import csv

LEAST_DAILY_MILEAGE = 100
# Assume the person cannot drive more than 100 miles per day
MAX_DAILY_MILEAGE = 327
START_MILEAGE = 0
END_MILEAGE = 0
YEAR_TOTAL_MILEAGE = 119000 # Total number of miles driven.
weekDays = ("Monday","Tuesday","Wednesday",
"Thursday","Friday","Saturday","Sunday")
JANUARY_DAYS=MARCH_DAYS=APRIL_DAYS=MAY_DAYS=31
JULY_DAYS=AUGUST_DAYS=OCTOBER_DAYS=DECEMBER_DAYS=JANUARY_DAYS
APRIL_DAYS=JUNE_DAYS=SEPTEMBER_DAYS=NOVEMBER_DAYS=30

YEAR = 2020 # The current year we are trying to get csv data for
FEBRUARY_DAYS= monthrange(YEAR, 2)[1] # num_days in the month of february 2020
ALL_MONTHS=(JANUARY,FEBRUARY,MARCH,APRIL,MAY,JUNE,JULY,AUGUST,SEPTEMBER, \
OCTOBER,NOVEMBER,DECEMBER) = (1,2,3,4,5,6,7,8,9,10,11,12)

NO_OF_DAYS_EACH_MONTH=(JANUARY_DAYS,FEBRUARY_DAYS,MARCH_DAYS, \
APRIL_DAYS,MAY_DAYS,JUNE_DAYS,JULY_DAYS,AUGUST_DAYS,SEPTEMBER_DAYS, \
OCTOBER_DAYS,NOVEMBER_DAYS,DECEMBER_DAYS)

MONTH_NAMES=("JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE", \
"JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")

data = []
sum_mileage = 0
for month in ALL_MONTHS:
    month_index = month-1
    days_in_the_month = NO_OF_DAYS_EACH_MONTH[month_index]
    line = []
    for day in range(0,days_in_the_month):
        date_of_the_year = date(YEAR,month,(day+1))
        day_in_the_week = date_of_the_year.weekday()

        # This person does not drive on Sundays
        # If they drives every day
        # then place a condition that wll allwasy be true
        REST_DAY = (len(weekDays)-1)
        if ( weekDays[day_in_the_week] != weekDays[REST_DAY])  :

            date_column = weekDays[day_in_the_week] + " " + str(MONTH_NAMES[month_index]).capitalize() + " " + str((day + 1)) + " " + str(YEAR)
            mileage_generated = randint(LEAST_DAILY_MILEAGE,MAX_DAILY_MILEAGE)
            END_MILEAGE = START_MILEAGE + mileage_generated

            data.append( [date_column,str(START_MILEAGE),str(END_MILEAGE), str(mileage_generated)])
            START_MILEAGE = END_MILEAGE
            sum_mileage += mileage_generated
            # print("Now sum mileage is ", sum_mileage) # was meant for debugging


mileage_difference = YEAR_TOTAL_MILEAGE - sum_mileage

#If we havent gotten a sum mileage
# of 119000 we add some more random miles to the random mileage
while (sum_mileage < YEAR_TOTAL_MILEAGE) :
    mileage_difference = YEAR_TOTAL_MILEAGE - sum_mileage
    #generate random mileage numbers for the number of days in the year
    #and add to the values stored
    totalDays = 52 * 6
    additional = int(mileage_difference/totalDays) + 1
    lower,upper = abs(additional-3),(additional+3)
    end_mileage = 0
    #Now we add random number generated
    index = 0
    for l in data:
        if lower <= upper :
            a = randint(lower,upper)
        else :
            a = randint(upper,lower)
        if index == 0 :
            #start_mileage = int(l[1])
            end_mileage = int(l[2])
            mileage_generated = int(l[3])
            mileage_generated += a
            end_mileage += mileage_generated
            l[2] = str(end_mileage)
            l[3] = str(mileage_generated)
        else :
            start_mileage = end_mileage
            l[1] = str(start_mileage) #we  update the start mileage
            # we add the old saved mileage genegrated to
            # the new generated random additional mileage
            mileage_generated = a + int(l[3])
            #We use the previous
            end_mileage = start_mileage + mileage_generated
            l[2] = str(end_mileage) # update the end mileage
            l[3] = str(mileage_generated) # we update the mileage generated

        # now we update our sum_mileage
        sum_mileage += a

        #print("Now sum mileage is ", sum_mileage)
        if sum_mileage == YEAR_TOTAL_MILEAGE :
            break

first_name = "John"
last_name = "Smith"
customer_full_name = first_name + " " + last_name
csv_file_name = customer_full_name.replace(" ","_").upper() + \
'_DAILY_MILEAGE_TRACKING_FOR_' + str(YEAR) + '.csv'
with open(csv_file_name, mode='w') as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow([ customer_full_name +  " Daily Mileage Track for Year " + str(YEAR) ])
    file_writer.writerow(["Dates Worked","Start Mileage","End Mileage", "Sub total Mileage Driven"])
    for l in data:
        file_writer.writerow(l)
    file_writer.writerow(["Total Mileage Driven For " + str(YEAR),
    " :,  " + str(sum_mileage) ])
