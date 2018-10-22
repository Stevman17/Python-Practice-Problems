import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#counts how many views came from each ad source
print (ad_clicks\
 .groupby('utm_source').user_id.  count()\
 .reset_index()
      )
#creates a new column to show when someone clicked on an ad, when ad_click_timestamp is not null
ad_clicks['is_click'] = ~ad_clicks\
  .ad_click_timestamp\
  .isnull()

#creates a variable to show the percent of peple who clicked on ads from each source
clicks_by_source = ad_clicks\
  .groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id')
print clicks_pivot
#Creates a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True]+ clicks_pivot[False])
print clicks_pivot

print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())

print(ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(index = 'experimental_group', columns = 'is_click', values = 'user_id').reset_index())

#creates two data frames to separate the percent of users who clicked on either ad, A or B, by the day of the week
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(index = 'day', columns = 'is_click', values = 'user_id').reset_index()

#adds a new column
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])

print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(index = 'day', columns = 'is_click', values = 'user_id').reset_index()

#adds a new column
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])
print(b_clicks_pivot)
