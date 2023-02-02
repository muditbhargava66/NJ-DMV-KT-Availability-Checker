import re
import requests
from bs4 import BeautifulSoup
import datetime as dt
import os
import time
from prettytable import PrettyTable

# Constants
DMV_NAMES = ['Bayonne', 'Newark']
START_DATE = dt.date(2023, 2, 1)
END_DATE = dt.date(2023, 5, 6)
DESIRED_TIME = [dt.time(6, 0), dt.time(18, 0)]
SLEEP_TIME = 1
URL_BASE = 'https://telegov.njportal.com/njmvc/AppointmentWizard/19/'
DMV_CODES = ['270', '274']

# Error message
ERROR_MSG = "Error raised during the latest attempt"

# Initialize the table
table = PrettyTable(['DMV Name', 'Appointment Time'])

# Main loop
while True:
    for i, code in enumerate(DMV_CODES):
        for date in [START_DATE + dt.timedelta(days=x) for x in range((END_DATE - START_DATE).days + 1)]:
            DESIRED_DATE = [date, date]
            try:
                # Fetch URL
                url = URL_BASE + code
                try:
                    response = requests.get(url)
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching URL: {e}")
                    continue

                # Parse the page
                soup = BeautifulSoup(response.text, 'lxml')

                # Check for availability
                alert = soup.find('div', attrs={'class': 'alert-danger'})
                if alert:
                    print(f"No slot available at {DMV_NAMES[i]}")
                    continue

                # Get appointment date and time
                date_string = soup.find('div', attrs={'class': 'col-md-8'}).find('label', attrs={'class': 'control-label'}).text
                date_string = re.sub(r'Time of Appointment for ', '', date_string)
                date_string = re.sub(': ', '', date_string)

                time_strings = [re.search(r'\d{1,2}:\d{2}? [A|P]M', d.text).group(0)
                                for d in soup.find('div', attrs={'class': 'col-md-8'}).findAll('div', attrs={'class': 'col availableTimeslot'})]

                date_times = [dt.datetime.strptime(f"{date_string}, {time}", '%B %d, %Y, %I:%M %p')
                          for time in time_strings]

                # Check desired date and time
                for date_time in date_times:
                    if DESIRED_DATE[0] <= date_time.date() <= DESIRED_DATE[1] and DESIRED_TIME[0] <= date_time.time() <= DESIRED_TIME[1]:
                        #print(f"Slot available at {DMV_NAMES[i]}, {date_time}")
                        table.add_row([DMV_NAMES[i], date_time])
                    break
            except Exception:
                print(ERROR_MSG)

    # Printing the table
    print(table)

    # Sleep before next iteration
    time.sleep(SLEEP_TIME)