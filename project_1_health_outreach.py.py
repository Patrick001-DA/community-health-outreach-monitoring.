"""
Project 1: Community Health Outreach Monitoring

Practice task for an aspiring Monitoring, Evaluation and Learning (MEL) Officer.
All records are fictional and created for learning. Do not treat them as real programme findings.
"""

import pandas as pd
import numpy as np

# TODO: Create the DataFrame from the records below.
# Tip: records is a list of dictionaries; the first dictionary gives the column names.
records = [
    {'event_id': 'E001', 'county': 'Kajiado', 'target_attendance': 100, 'actual_attendance': 92, 'people_referred': 18, 'followups_completed': 14},
    {'event_id': 'E002', 'county': 'Nairobi', 'target_attendance': 120, 'actual_attendance': 135, 'people_referred': 22, 'followups_completed': 20},
    {'event_id': 'E003', 'county': 'Machakos', 'target_attendance': 80, 'actual_attendance': 64, 'people_referred': 12, 'followups_completed': 8},
    {'event_id': 'E004', 'county': 'Kiambu', 'target_attendance': 110, 'actual_attendance': 101, 'people_referred': 20, 'followups_completed': 17},
    {'event_id': 'E005', 'county': 'Nakuru', 'target_attendance': 90, 'actual_attendance': 95, 'people_referred': 15, 'followups_completed': 13},
    {'event_id': 'E006', 'county': 'Kajiado', 'target_attendance': 105, 'actual_attendance': 88, 'people_referred': 16, 'followups_completed': 12},
    {'event_id': 'E007', 'county': 'Nairobi', 'target_attendance': 130, 'actual_attendance': 119, 'people_referred': 24, 'followups_completed': 21},
    {'event_id': 'E008', 'county': 'Machakos', 'target_attendance': 85, 'actual_attendance': 91, 'people_referred': 14, 'followups_completed': 12},
    {'event_id': 'E009', 'county': 'Kiambu', 'target_attendance': 115, 'actual_attendance': 98, 'people_referred': 19, 'followups_completed': 15},
    {'event_id': 'E010', 'county': 'Nakuru', 'target_attendance': 95, 'actual_attendance': 103, 'people_referred': 17, 'followups_completed': 16},
]
# 1. Load the data into a pandas DataFrame and display the first five rows ,rows, columns, and data types.
df = pd.DataFrame(records)

print("First five rows:")
print(df.head())

print("\nData shape:")
print(df.shape)

print("\nData types:")
print(df.dtypes)
#Check for missing values and duplicate event IDs.
print("\nMissing values:")
print(df.isna().sum())

print("\nduplicates:")
print(df["event_id"].duplicated().sum())

# 4. Create attendance_rate_pct = actual_attendance / target_attendance * 100.
print("\nattendance rate percentage ")

df["attendance_rate_pct"]=(df["actual_attendance"]/ df["target_attendance"]*100).round(1)

print(df.columns)


# 5. Create followup_rate_pct = followups_completed / people_referred * 100.
print("\nfollowup rate percentage")
df["followup_rate_pct"]=(df["followups_completed"]/ df["people_referred"]* 100).round(1)
print(df.columns)
# 6. Which events met or exceeded their attendance target?
print("\nevents which exceeded their attendance target")
print(df[df["actual_attendance"]>=df["target_attendance"]])

# 7. Calculate the overall attendance rate using totals, not the mean of event percentages.
print("\noverall attendance rate using total")
print(df["actual_attendance"].sum()/df["target_attendance"].sum()*100)


# 8. Summarise attendance and follow-up rates by county.


summary = df.groupby('county')[['target_attendance','actual_attendance','people_referred','followups_completed']].sum()
summary['attendance_rate_pct'] = (summary['actual_attendance'] / summary['target_attendance'] * 100).round(1)
summary['followup_rate_pct'] = (summary['followups_completed'] / summary['people_referred'] * 100).round(1)
print(summary.to_string())
summary.to_csv("summary.csv")
# 9. Identify the three events with the lowest follow-up rates.
print(df.sort_values("followup_rate_pct").head(3))
# 10. Write three evidence-based recommendations for the programme team.
# 1) Prioritise follow-up support in Kajiado (76.5%) and Machakos (76.9%), about 13 points
#    below Nakuru (90.6%); all three weakest events (E003, E006, E001) come from these counties.
# 2) Review target-setting and mobilisation in Kajiado (87.8%) and Kiambu (88.4%), where every
#    event fell below target, and learn from Nakuru, which exceeded target with the best follow-up.

