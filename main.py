import win32gui
import pandas as pd
from datetime import datetime
import numpy as np

last_window = 0
data = pd.DataFrame(columns = ['activeWindow', 'timeEntered'])

i = 5

while True:
	window = win32gui.GetForegroundWindow()

	window_text = win32gui.GetWindowText(window)

	if window_text != last_window:
		last_window = window_text

		dt = datetime.now()
		dt_str = '{}-{}-{}'.format(dt.year, dt.month, dt.day)

		data.loc[5 - i] = [last_window, dt_str]

		i -= 1

		data.to_excel(r'C:\Users\Ricardo\Desktop\123.xlsx')

print(data)
