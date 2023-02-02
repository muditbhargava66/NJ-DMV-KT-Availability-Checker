# DMV Appointment Checker

---

## **Overview**

This script checks for available DMV appointment slots at specified locations and during specified times. It fetches appointment information from the NJ DMV website and alerts the user if a desired appointment slot is available.

## **Requirements**

- Python 3
- **`requests`** library
- **`BeautifulSoup`** library
- **`re`** library
- **`datetime`** library
- **`os`** library
- **`time`** library
- **`prettytable`** library

## **Constants**

- **`DMV_NAMES`**: A list of names of DMV locations in New Jersey
- **`START_DATE`**: The starting date for the appointment search
- **`END_DATE`**: The end date for the appointment search
- **`DESIRED_TIME`**: A list of desired appointment time range
- **`SLEEP_TIME`**: The number of seconds the code will wait before making another appointment search
- **`URL_BASE`**: The base URL of the NJMVC appointment page
- **`DMV_CODES`**: A list of DMV location codes
- **`ERROR_MSG`**: Error message displayed when an error is encountered

## **Execution**

1. Install the required libraries by running **`pip install -r requirements.txt`** in the terminal
2. Run the script **`python main.py`** in the terminal
3. The script will run indefinitely and check for desired appointment slots every **`SLEEP_TIME`** seconds
4. If a desired slot is available, the script will alert the user by printing the message to the terminal and using the built-in **`say`** function (Mac only).
5. If an error is raised during the script execution, the **`ERROR_MSG`** message will be printed to the terminal.

> **Note:**
This script was tested on a Mac machine and may not work on Windows or Linux systems without modification.
>