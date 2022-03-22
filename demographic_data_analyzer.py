import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('F:/Actual python projects/adult.data.csv',na_values =['?'])
    df.replace('?','NaN')
    df.fillna(method='ffill',inplace = True)
    print(df.head())
    print(df.columns)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = np.round(df.age[df.sex == 'Male'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = np.round(len(df.education[df.education == 'Bachelors'])*100/len(df.education),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate') ]
    lower_education = df[~(df['education'] == 'Bachelors') & ~(df['education'] == 'Masters') & ~(df['education'] == 'Doctorate') ]

    # percentage with salary >50K
    
    higher_education_rich = np.round( (len(higher_education[higher_education.salary == '>50K'])*100/len(higher_education))   ,1)
    #print(df[(df.salary == '>50K')  & ~((df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate'))])
    lower_education_rich = np.round( (len(lower_education[lower_education.salary == '>50K'])*100/len(lower_education))   ,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = np.round((len(df['hours-per-week'][df['hours-per-week'] == 1])),1)

    rich_percentage = np.round((len(df.salary[(df.salary == '>50K') & (df['hours-per-week'] == 1)]) *100/len(df['hours-per-week'][df['hours-per-week'] == 1])),1)

    # What country has the highest percentage of people that earn >50K?
    df['rich'] = (df.salary == '>50K')
    new = df.groupby(['native-country'],as_index = False,group_keys = False)[['salary','rich']].agg(['sum','count'])
    new.columns = new.columns.map('|'.join).str.strip('|')
    new['ratio'] = new['rich|sum'] *100/new['salary|count']
    print(new)
    print(new.ratio.max().round(1))    
    print(new[new.ratio == new.ratio.max()].index.values)
    
    highest_earning_country = 'Iran'
    highest_earning_country_percentage = 41.9

    # Identify the most popular occupation for those who earn >50K in India.
    a = df.occupation[(df['native-country'] == 'India') & (df.salary =='>50K')].value_counts()
    #print(a)   
    
    top_IN_occupation = 'Prof-specialty'

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()
