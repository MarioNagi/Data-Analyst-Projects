# Project: Investigate a Dataset (No Show Appointments )

## Table of Contents
<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#wrangling">Data Wrangling</a></li>
<li><a href="#eda">Exploratory Data Analysis</a></li>
<li><a href="#conclusions">Conclusions</a></li>
</ul> 

<a id='intro'></a>
## Introduction

This dataset collects information
from 110k medical appointments in
Brazil and is focused on the question
of whether or not patients show up
for their appointment. A number of
characteristics about the patient are
included in each row, we will try in this anaylsis to know What are the factors that
important in order to
predict if a patient will
show up for their
scheduled
appointment?

<a id='wrangling'></a>
## Data Wrangling

>  In this section of the report, data will be loaded, checked for cleanliness, and then trimed and cleaned to be prepared for analysis.

### Inital Observations:

- The dataset size is 14 columns by 110527 rows, there are neither null nor duplicated values
- All of the columns names need to be in lower case and to be corrected from slight mistakes
- Changing the columns type to correct type e.g. scheduled_day to datetime
- Age:we have alot of young patients(age 0,1) but the rest of the patients age is distributed evenly with less patients older than 60 years.
- Alcoholism: Most of the patients are not alcoholics.
- Handicap: There are 4 handicap categories but most of the patients aren't handicapted
- Diabetes: Most of the patients don't have diabetes but it slightly more than alcoholics ratio and handicap.
- Scholarship:Most of the patients didn't receive Scholarship but it slightly more than alcoholics ratio and handicap
- fixing age outliers (Age<0&>100) and changing handicap to bool

> In the next section, data will be cleaned as per the above observations to get it ready for anaylsis


<a id='eda'></a>
## Exploratory Data Analysis

>  Now that the data is cleaned, it is ready for exploration. if we looked at the different columns, we can see 3 categories 
- 1-Demographics Features(Gender,Age,Neighoburhood)
- 2-Dieases / chronic or harmful Personal Features
- 3-Season / time Feature

Any of the above features could have affected the missed appointments ratio
For example, a certain hour/day of the week or certain location might be the reason, in the following section we will explore all of these questions. but before that, lets first find the total number of the missed appointments


<a id='conclusions'></a>
## Conclusions

After cleaning and doing data exploratory analysis, I can list the most important finding as below: 

- Out off 110K only 22K didn’t show up in the period from 29-4-16 till 8-6-16
- out of the 22K, 14.5k are females and 7.7K are males (as seen in pie chart)
- The columns -Features- can be divided into 3 section (Demographics Features, alignment Personal Features and Season / time Feature )
- Most of the patients aren't alcoholics. (Only 3% are alcoholics)
- Most of the patients doesn't have handicap. (Only 2% suffer from handicap)
- The younger the age, the higher the ratio of no-show but it gets uniformed as the age goes up
- Either the patient has chronic disease or not, 80% will go to the appointments
- Some neighborhoods are higher than other like JARDIM CAMBURI (Bar chart)
- If we looked at the time of the missed Appointments, will find that most of them was in the early morning (7 am to 11 am) (bar chart) -To help in this issue, maybe we can add more staff in morning shift or make the clinic work longer hour-

> Limitations:
>
>- The dataset duration (2 months) which is too small to get any conclusive and accurate data from, also any model built from this set won’t have high accuracy
>- Appointment time wasn't given, which could add more insights to the dataset
>- This dataset only covers Vitória, not all of Brazil. Covering more than one state in Brazil would've been better.
>- Also, the data is too old -4 years old-, maybe adding more data for the following years, could help to shed some light in understanding the elements which affect the missed Appointments
>- The handicap category wasn't clear in the dataset, had to look for it in the discussions
https://www.kaggle.com/joniarroba/noshowappointments/discussion/32174
>- Looking over the dates, most of the missed Appointments are in certain days in May 2016, during this month there were many political events like the president impeachment (which may have impacted the no-show ratio)
 https://en.wikipedia.org/wiki/2016_in_Brazil#May




Any of the above features could have affected the missed appointments ratio
For example, a certain hour/day of the week or certain location might be the reason, in the following section we will explore all of these questions. but before that, lets first find the total number of the missed appointments
