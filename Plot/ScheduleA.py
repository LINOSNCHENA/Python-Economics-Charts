# imports fpr HTML schedule

import plotly
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.DataFrame([
    dict(Task="Preparation Works", Start='2021-02-01',
         Finish='2021-07-01', Resource="First Semester"),

    dict(Task="Data Gathering", Start='2021-07-01',
         Finish='2021-12-01', Resource="Second Semester"),
    dict(Task="Data Gathering", Start='2022-03-01',
         Finish='2022-05-01', Resource="Third Semester"),

    dict(Task="Publication Works", Start='2021-09-01',
         Finish='2021-10-01', Resource="Second Semester"),
    dict(Task="Publication Works", Start='2022-09-01',
         Finish='2022-10-01', Resource="Fouth Semester"),

    dict(Task="Presenting Works", Start='2021-06-01',
         Finish='2021-07-01', Resource="First Semester"),
    dict(Task="Presenting Works", Start='2021-11-01',
         Finish='2021-12-01', Resource="Second Semester"),
    dict(Task="Presenting Works", Start='2022-06-01',
         Finish='2022-07-01', Resource="Third Semester"),
    dict(Task="Presenting Works", Start='2022-11-01',
         Finish='2022-12-01', Resource="Fouth Semester"),

    dict(Task="Reporting Works", Start='2021-02-01',
         Finish='2021-07-01', Resource="First Semester"),
    dict(Task="Reporting Works", Start='2021-09-01',
         Finish='2022-01-01', Resource="Second Semester"),
    dict(Task="Reporting Works", Start='2022-02-01',
         Finish='2022-07-01', Resource="Third Semester"),
    dict(Task="Reporting Works", Start='2022-09-01',
         Finish='2023-02-01', Resource="Fouth Semester")
])

fig = px.timeline(df, x_start="Start", x_end="Finish",
                  y="Task", color="Resource",
                   color_discrete_sequence=["brown","gray", "purple","olive","magenta","olive" ,"cyan", "goldenrod"],
title="Automation: An empirical study using advanced ML algorithms")
fig.update_yaxes(autorange="reversed")
plotly.offline.plot(fig, filename='ScheduleA.html')

print('===============================|Completed page 50|================================')

