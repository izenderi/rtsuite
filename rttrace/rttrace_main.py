import pandas as pd
import numpy as np
import math
import re

import plotly.figure_factory as ff
from datetime import datetime, timedelta

# from task import Task

__author__ = "Ziliang(Johnson)"
__copyright__ = "Copyright 2023, Ziliang(Johnson)"
__license__ = "MIT"
__maintainer__ = "Ziliang(Johnson)"
__email__ = "ziliang.zhang@email.ucr.edu"
__version__ = "1.0"

# def rttrace(csv_path=None):
#     """
#     This version is mutually exclusive with the one down
#     It is using the start_rt and finish_rt columns of the csv 
#     (relative time to start of the program)
#     """
#     # Sample DataFrame with relative start and finish times in milliseconds
#     df = pd.read_csv(csv_path)
#     # Convert relative time in ms to a datetime object
#     # Assuming that the reference start time is the current time
#     reference_time = datetime.now()

#     # # Convert the timestamp strings to datetime objects
#     # df['Start'] = pd.to_datetime(df['start_ts'])
#     # df['Finish'] = pd.to_datetime(df['finish_ts'])

#     # Convert strings to integers and then to timedeltas added to the reference time
#     df['Start'] = df['start_rt'].astype(int).apply(lambda x: reference_time + timedelta(microseconds=x))
#     df['Finish'] = df['finish_rt'].astype(int).apply(lambda x: reference_time + timedelta(microseconds=x))

#     # Create a Gantt chart
#     fig = ff.create_gantt(df, index_col='Task', show_colorbar=True, group_tasks=True, showgrid_x=True, showgrid_y=True)

#     # Show the figure
#     fig.show()

def rttrace(csv_path=None):
    """
    This version is mutually exclusive with the one up
    It is using the start_tp and finish_tp columns of the csv 
    (time stamp of the each log. Max Precision: millisec)
    """
    df = pd.read_csv(csv_path)

    # Convert the timestamp strings to datetime objects
    df['Start'] = pd.to_datetime(df['start_ts'])
    df['Finish'] = pd.to_datetime(df['finish_ts'])

    # Prepare the data for Plotly Gantt chart
    df_gantt = df[['Task', 'Start', 'Finish']]
    df_gantt = df_gantt.rename(columns={'Start': 'Start', 'Finish': 'Finish', 'Task': 'Task'})

    # Create a Gantt chart
    fig = ff.create_gantt(df_gantt, index_col='Task', show_colorbar=True, group_tasks=True, showgrid_x=True, showgrid_y=True)

    # Show the figure
    fig.show()