#LIST COMPHERENSION

import seaborn as sns
df = sns.load_dataset('car_crashes')
df.dtypes


### TASK 1

liste =['NUM_'+i.upper() if df[i].dtype in ['float64','int64'] else i.upper() for i in df.columns]

df.columns=liste

### TASK 2

liste = [i.upper()+'_FLAG' if not 'no' in i else i.upper() for i in df.columns]

### TASK3

liste = [i for i in df.columns if not i in ['abbrev','no_previous']]
new_df=df[liste]


#PANDAS

#TASK1

import seaborn as sns

df=sns.load_dataset('titanic')

#TASK2

female = df[df['sex'] == 'female'].shape[0]


male = df[df['sex'] == 'male'].shape[0]
f'MALE : {male}'
f'FEMALE : {female}'

#TASK3

df.nunique()

#TASK4

df.pclass.nunique()

#TASK5

df[['pclass','parch']].nunique()

#TASK6

df['embarked']=df['embarked'].astype('category')
df['embarked'].dtype

df.dtypes

#TASK7

df[(df['embarked'] == 'C')]

#TASK8

df[df['embarked'] != 'S']

#TASK9

df[(df['age']<30) & (df['sex']=='female')]

#TASK10

df[(df['fare']>500) & (df['age']>70)]

#TASK11

df.isnull().sum()

#TASK12

df.drop('who',axis=1,inplace=True)

#TASK13

df['deck'].fillna(df['deck'].mode()[0],inplace=True)

#TASK14

df['age'].fillna(df['age'].median(),inplace=True)

#TASK15

df.groupby(['pclass','sex'])['survived'].agg(['sum','count','mean'])

#TASK16

def funct(arr):
    if arr['age']<30:
        return 1
    else:
        return 0

df['age_flag']=df.apply(lambda arr : funct(arr),axis=1)

df

#TASK17

df = sns.load_dataset('tips')

#TASK18

df.groupby('time')['total_bill'].agg(['min', 'max', 'mean'])

#TASK19

df.groupby(['day','time'])['total_bill'].agg(['min', 'max', 'mean'])

#TASK20

df_lunch_female = df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')]
result_20 = df_lunch_female.groupby('day')['total_bill', 'tip'].agg(['sum', 'min', 'max', 'mean'])

#TASK21

result_21 = df.loc[(df['size'] < 3) & (df['total_bill'] > 10), 'total_bill'].mean()

#TASK22

df['totalbill_tip_sum']=df['total_bill']+df['tip']
df

#TASK23

sorted_df = df.sort_values('totalbill_tip_sum', ascending=False)
result_23 = sorted_df.head(30).copy()







