#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('ViewingActivity.csv')


# In[2]:


df.shape 


# In[ ]:


# Indicates that our data set has 200 rows, and 10 columns.


# In[4]:


df.head() # Prints the first five rows.


# In[6]:


# Dropping unnecessary columns (focused on Start Time, Duration, Title)

df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)

df.head(1)


# In[19]:


#Converting Strings to Date-time and Timedelta in Pandas - first have to see what format the data is being stored in
df.dtypes


# In[14]:


# Let's convert. Makin sure the time zone is uniform to convert to EST time zone.
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df.dtypes


# In[15]:


# change the Start Time column into the dataframe's index
df = df.set_index('Start Time')

# convert from UTC timezone to eastern time
df.index = df.index.tz_convert('US/Eastern')

# reset the index so that Start Time becomes a column again
df = df.reset_index()

#double-check that it worked
df.head(1)


# In[16]:


df['Duration'] = pd.to_timedelta(df['Duration'])
df.dtypes


# In[20]:


#Filtering Strings by substring in Pandas using str.contains - we want to filter for views of only 'Office'


# create a new dataframe called office that that takes from df
# only the rows in which the Title column contains 'The Office (U.S.)'
office = df[df['Title'].str.contains('The Office (U.S.)', regex=False)]


# In[21]:


office.shape


# In[22]:


office['Duration'].sum()


# In[28]:


#Let's focus on when and what day I watch a particular show?
import matplotlib

office['weekday'] = office['Start Time'].dt.weekday
office['hour'] = office['Start Time'].dt.hour

#Check to make sure the columns were added correctly

office.head()


# In[29]:


# set our categorical and define the order so the days are plotted Monday-Sunday
office['weekday'] = pd.Categorical(office['weekday'], categories=
    [0,1,2,3,4,5,6],
    ordered=True)

# create office_by_day and count the rows for each weekday, assigning the result to that variable
office_by_day = office['weekday'].value_counts()

# sort the index using our categorical, so that Monday (0) is first, Tuesday (1) is second, etc.
office_by_day = office_by_day.sort_index()

# optional: update the font size to make it a bit larger and easier to read
matplotlib.rcParams.update({'font.size': 22})

# plot office_by_day as a bar chart with the listed size and title
office_by_day.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Day')


# In[30]:


# set our categorical and define the order so the hours are plotted 0-23

office['hour'] = pd.Categorical(office['hour'], categories=
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    ordered=True)

# create office_by_hour and count the rows for each hour, assigning the result to that variable

office_by_hour = office['hour'].value_counts()

# sort the index using our categorical, so that midnight (0) is first, 1 a.m. (1) is second, etc.

office_by_hour = office_by_hour.sort_index()

# plot office_by_hour as a bar chart with the listed size and title

office_by_hour.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Hour')

