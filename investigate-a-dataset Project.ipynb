{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project: No-Show Appointmensts\n",
    "\n",
    "## Table of Contents\n",
    "<ul>\n",
    "<li><a href=\"#intro\">Introduction</a></li>\n",
    "<li><a href=\"#wrangling\">Data Wrangling</a></li>\n",
    "<li><a href=\"#eda\">Exploratory Data Analysis</a></li>\n",
    "<li><a href=\"#conclusions\">Conclusions</a></li>\n",
    "</ul>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='intro'></a>\n",
    "## Introduction\n",
    "\n",
    "> The dataset I have selected is [No-Show Appointmensts](https://www.kaggle.com/datasets/joniarroba/noshowappointments) from [Kaggle](https://www.kaggle.com/)\n",
    ">\n",
    ">This dataset collects information from **100k** medical appointments in **Brazil** and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row\n",
    ">\n",
    ">- 01 - PatientId: Identification of a patient\n",
    ">\n",
    ">- 02 - AppointmentID: Identification of each appointment\n",
    ">\n",
    ">- 03 - Gender: 'M' for Male or 'F' for Female\n",
    ">\n",
    ">- 04 - ScheduledDay: tells us on what day the patient set up their appointment, this is before appointment of course\n",
    ">\n",
    ">- 05 - AppointmentDay: The day someone called or registered the appointment\n",
    ">\n",
    ">- 06 - Age: How old is the patient in years\n",
    ">\n",
    ">- 07 - Neighbourhood: Where the appointment takes place or indicates the location of the hospital\n",
    ">\n",
    ">- 08 - Scholarship: indicates whether or not the patient is enrolled in Brasilian welfare program [Bolsa Família](https://en.wikipedia.org/wiki/Bolsa_Fam%C3%ADlia) (zero for not enrolled and 1 for enrolled)\n",
    ">\n",
    ">- 09 - Hipertension: True or False\n",
    ">\n",
    ">- 10 - Diabetes: True or False\n",
    ">\n",
    ">- 11 - Alcoholism: True or False\n",
    ">\n",
    ">- 12 - Handcap: True or False\n",
    ">\n",
    ">- 13 - SMS_received: 1 or more messages sent to the patient.\n",
    ">\n",
    ">- 14 - No-show: True or False (**Be careful about the encoding of the last column: it says ‘No’ if the patient showed up to their appointment, and ‘Yes’ if they did not show up.**)\n",
    ">\n",
    "\n",
    "At the end, I will ask and answer some quaestions:\n",
    "<ul>\n",
    "<li><a href=\"#q1\">1- What are the general statistical results for whole columns?</a></li>\n",
    "\n",
    "<li><a href=\"#q2\">2- How far does the gender affect the attending of the appointment?</a></li>\n",
    "\n",
    "<li><a href=\"#q3\">3- Is there any relationship between age and the attending the appointment?</a></li>\n",
    "\n",
    "<li><a href=\"#q4\">4- Is the enrollment in Brasilian welfare program have an effect on attending the appointment?</a></li>\n",
    "</ul>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use this cell to set up import statements for all of the packages that you\n",
    "#   plan to use.\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Remember to include a 'magic word' so that your visualizations are plotted\n",
    "#   inline with the notebook. See this page for more:\n",
    "#   http://ipython.readthedocs.io/en/stable/interactive/magics.html\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='wrangling'></a>\n",
    "## Data Wrangling\n",
    "\n",
    " **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you document your steps carefully and justify your cleaning decisions.\n",
    "\n",
    "1- load csv file to a Pandas DataFrame using *resd_csv* function\n",
    "\n",
    "2- show the first 5 rows by *head*\n",
    "\n",
    "3- show the number of columns and rows by *shape*\n",
    "\n",
    ">- 110527 rows and 14 columns\n",
    ">\n",
    "\n",
    "4- show overall information by *info*\n",
    ">- There isn't any NaN values, This is good but there may be unlogic values or undesired columns\n",
    ">\n",
    ">- Also some column dtypes need some change\n",
    ">\n",
    "\n",
    "5- show sum of all NaN values by *isnull*\n",
    ">- zero NaN values\n",
    ">\n",
    "\n",
    "6- check for duplicates by *duplicated*\n",
    ">- zero duplicated rows\n",
    ">\n",
    "\n",
    "### General Properties"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PatientId</th>\n",
       "      <th>AppointmentID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>ScheduledDay</th>\n",
       "      <th>AppointmentDay</th>\n",
       "      <th>Age</th>\n",
       "      <th>Neighbourhood</th>\n",
       "      <th>Scholarship</th>\n",
       "      <th>Hipertension</th>\n",
       "      <th>Diabetes</th>\n",
       "      <th>Alcoholism</th>\n",
       "      <th>Handcap</th>\n",
       "      <th>SMS_received</th>\n",
       "      <th>No-show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.987250e+13</td>\n",
       "      <td>5642903</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T18:38:08Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>62</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.589978e+14</td>\n",
       "      <td>5642503</td>\n",
       "      <td>M</td>\n",
       "      <td>2016-04-29T16:08:27Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.262962e+12</td>\n",
       "      <td>5642549</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T16:19:04Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>62</td>\n",
       "      <td>MATA DA PRAIA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.679512e+11</td>\n",
       "      <td>5642828</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T17:29:31Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>8</td>\n",
       "      <td>PONTAL DE CAMBURI</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8.841186e+12</td>\n",
       "      <td>5642494</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T16:07:23Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      PatientId  AppointmentID Gender          ScheduledDay  \\\n",
       "0  2.987250e+13        5642903      F  2016-04-29T18:38:08Z   \n",
       "1  5.589978e+14        5642503      M  2016-04-29T16:08:27Z   \n",
       "2  4.262962e+12        5642549      F  2016-04-29T16:19:04Z   \n",
       "3  8.679512e+11        5642828      F  2016-04-29T17:29:31Z   \n",
       "4  8.841186e+12        5642494      F  2016-04-29T16:07:23Z   \n",
       "\n",
       "         AppointmentDay  Age      Neighbourhood  Scholarship  Hipertension  \\\n",
       "0  2016-04-29T00:00:00Z   62    JARDIM DA PENHA            0             1   \n",
       "1  2016-04-29T00:00:00Z   56    JARDIM DA PENHA            0             0   \n",
       "2  2016-04-29T00:00:00Z   62      MATA DA PRAIA            0             0   \n",
       "3  2016-04-29T00:00:00Z    8  PONTAL DE CAMBURI            0             0   \n",
       "4  2016-04-29T00:00:00Z   56    JARDIM DA PENHA            0             1   \n",
       "\n",
       "   Diabetes  Alcoholism  Handcap  SMS_received No-show  \n",
       "0         0           0        0             0      No  \n",
       "1         0           0        0             0      No  \n",
       "2         0           0        0             0      No  \n",
       "3         0           0        0             0      No  \n",
       "4         1           0        0             0      No  "
      ]
     },
     "execution_count": 202,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load your data and print out a few lines. Perform operations to inspect data\n",
    "#   types and look for instances of missing or possibly errant data.\n",
    "df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(110527, 14)"
      ]
     },
     "execution_count": 203,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 110527 entries, 0 to 110526\n",
      "Data columns (total 14 columns):\n",
      " #   Column          Non-Null Count   Dtype  \n",
      "---  ------          --------------   -----  \n",
      " 0   PatientId       110527 non-null  float64\n",
      " 1   AppointmentID   110527 non-null  int64  \n",
      " 2   Gender          110527 non-null  object \n",
      " 3   ScheduledDay    110527 non-null  object \n",
      " 4   AppointmentDay  110527 non-null  object \n",
      " 5   Age             110527 non-null  int64  \n",
      " 6   Neighbourhood   110527 non-null  object \n",
      " 7   Scholarship     110527 non-null  int64  \n",
      " 8   Hipertension    110527 non-null  int64  \n",
      " 9   Diabetes        110527 non-null  int64  \n",
      " 10  Alcoholism      110527 non-null  int64  \n",
      " 11  Handcap         110527 non-null  int64  \n",
      " 12  SMS_received    110527 non-null  int64  \n",
      " 13  No-show         110527 non-null  object \n",
      "dtypes: float64(1), int64(8), object(5)\n",
      "memory usage: 11.8+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 205,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 206,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['AppointmentID'].duplicated().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Data Cleaning\n",
    "<ul>\n",
    "<li><a href=\"#change_names\">1- Change cloumns' names to lowercase, splitted by _ and correct spilling</a></li>\n",
    "<li><a href=\"#correct_dtypes\">2- Correct dtypes of columns</a></li>\n",
    "<li><a href=\"#check\">3- Check whole information by *info*</a></li>\n",
    "<li><a href=\"#data_overview\">4- Data Overview (show overall numbers about data in each column) by *describe*, *value_counts*</a></li>\n",
    "<li><a href=\"#delete_row\">5- Delete row including (age = -1)</a></li>\n",
    "<li><a href=\"#edit_handicap\">6- Edit values of handicap > 1 to equal 1</a></li>\n",
    "<li><a href=\"#check_duplicate\">7- check for duplicates</a></li>    \n",
    "<li><a href=\"#delete_col\">8- Delete some columns according to my insight</a></li>\n",
    "<li><a href=\"#save_clean\">9- Save a clean CSV</a></li>\n",
    "<li><a href=\"#import_clean\">10- Import the clean CSV and show the first 5 rows by *head*</a></li>\n",
    "\n",
    "</ul>\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='change_names'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>patient_id</th>\n",
       "      <th>appointment_id</th>\n",
       "      <th>gender</th>\n",
       "      <th>schedule_day</th>\n",
       "      <th>appointment_day</th>\n",
       "      <th>age</th>\n",
       "      <th>neighbourhood</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "      <th>no_show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.987250e+13</td>\n",
       "      <td>5642903</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-04-29T18:38:08Z</td>\n",
       "      <td>2016-04-29T00:00:00Z</td>\n",
       "      <td>62</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     patient_id  appointment_id gender          schedule_day  \\\n",
       "0  2.987250e+13         5642903      F  2016-04-29T18:38:08Z   \n",
       "\n",
       "        appointment_day  age    neighbourhood  scholarship  hypertension  \\\n",
       "0  2016-04-29T00:00:00Z   62  JARDIM DA PENHA            0             1   \n",
       "\n",
       "   diabetes  alcoholism  handicap  sms_received no_show  \n",
       "0         0           0         0             0      No  "
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Change names of columns to be lowercase, Split any two word by _, correct names of two columns to hypertension and handicap \n",
    "df.columns = df.columns.str.lower()\n",
    "df.rename(columns={'patientid':'patient_id',\n",
    "                  'appointmentid': 'appointment_id',\n",
    "                  'scheduledday': 'schedule_day',\n",
    "                  'appointmentday': 'appointment_day',\n",
    "                   'hipertension': 'hypertension',\n",
    "                   'handcap': 'handicap',\n",
    "                  'no-show':'no_show'}, inplace=True)\n",
    "df.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='correct_dtypes'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Change type of PatientId Dtype from float to int to trim the digits then to string as this is more logic\n",
    "df['patient_id'] = df['patient_id'].apply(int)\n",
    "df['patient_id'] = df['patient_id'].apply(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Change type of AppointmentID from int to str as as this is more logic (same as PatientId)\n",
    "df['appointment_id'] = df['appointment_id'].apply(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Change type of ScheduledDay and AppointmentDay to datetime for more control\n",
    "df['schedule_day'] = pd.to_datetime(df['schedule_day']).dt.date\n",
    "df['appointment_day'] = pd.to_datetime(df['appointment_day']).dt.date"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='check'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 110527 entries, 0 to 110526\n",
      "Data columns (total 14 columns):\n",
      " #   Column           Non-Null Count   Dtype \n",
      "---  ------           --------------   ----- \n",
      " 0   patient_id       110527 non-null  object\n",
      " 1   appointment_id   110527 non-null  object\n",
      " 2   gender           110527 non-null  object\n",
      " 3   schedule_day     110527 non-null  object\n",
      " 4   appointment_day  110527 non-null  object\n",
      " 5   age              110527 non-null  int64 \n",
      " 6   neighbourhood    110527 non-null  object\n",
      " 7   scholarship      110527 non-null  int64 \n",
      " 8   hypertension     110527 non-null  int64 \n",
      " 9   diabetes         110527 non-null  int64 \n",
      " 10  alcoholism       110527 non-null  int64 \n",
      " 11  handicap         110527 non-null  int64 \n",
      " 12  sms_received     110527 non-null  int64 \n",
      " 13  no_show          110527 non-null  object\n",
      "dtypes: int64(7), object(7)\n",
      "memory usage: 11.8+ MB\n"
     ]
    }
   ],
   "source": [
    "# This to show the change done to dtypes of some columns\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='data_overview'></a>\n",
    "#### Data Overview (This section is to check whether there are any unlogic or misleading value or not)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "      <td>110527.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>37.088874</td>\n",
       "      <td>0.098266</td>\n",
       "      <td>0.197246</td>\n",
       "      <td>0.071865</td>\n",
       "      <td>0.030400</td>\n",
       "      <td>0.022248</td>\n",
       "      <td>0.321026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>23.110205</td>\n",
       "      <td>0.297675</td>\n",
       "      <td>0.397921</td>\n",
       "      <td>0.258265</td>\n",
       "      <td>0.171686</td>\n",
       "      <td>0.161543</td>\n",
       "      <td>0.466873</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>37.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>55.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>115.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 age    scholarship   hypertension       diabetes  \\\n",
       "count  110527.000000  110527.000000  110527.000000  110527.000000   \n",
       "mean       37.088874       0.098266       0.197246       0.071865   \n",
       "std        23.110205       0.297675       0.397921       0.258265   \n",
       "min        -1.000000       0.000000       0.000000       0.000000   \n",
       "25%        18.000000       0.000000       0.000000       0.000000   \n",
       "50%        37.000000       0.000000       0.000000       0.000000   \n",
       "75%        55.000000       0.000000       0.000000       0.000000   \n",
       "max       115.000000       1.000000       1.000000       1.000000   \n",
       "\n",
       "          alcoholism       handicap   sms_received  \n",
       "count  110527.000000  110527.000000  110527.000000  \n",
       "mean        0.030400       0.022248       0.321026  \n",
       "std         0.171686       0.161543       0.466873  \n",
       "min         0.000000       0.000000       0.000000  \n",
       "25%         0.000000       0.000000       0.000000  \n",
       "50%         0.000000       0.000000       0.000000  \n",
       "75%         0.000000       0.000000       1.000000  \n",
       "max         1.000000       4.000000       1.000000  "
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Describe the statisical results for numerical data\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "F    71840\n",
       "M    38687\n",
       "Name: gender, dtype: int64"
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# show some little number about Gender\n",
    "df['gender'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2016-05-03    4238\n",
       "2016-05-02    4216\n",
       "2016-05-16    4120\n",
       "2016-05-05    4095\n",
       "2016-05-10    4024\n",
       "              ... \n",
       "2016-04-16       1\n",
       "2016-01-28       1\n",
       "2015-11-10       1\n",
       "2016-03-19       1\n",
       "2016-03-05       1\n",
       "Name: schedule_day, Length: 111, dtype: int64"
      ]
     },
     "execution_count": 214,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# show some little number about Schedule Day\n",
    "df['schedule_day'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2016-06-06    4692\n",
       "2016-05-16    4613\n",
       "2016-05-09    4520\n",
       "2016-05-30    4514\n",
       "2016-06-08    4479\n",
       "2016-05-11    4474\n",
       "2016-06-01    4464\n",
       "2016-06-07    4416\n",
       "2016-05-12    4394\n",
       "2016-05-02    4376\n",
       "2016-05-18    4373\n",
       "2016-05-17    4372\n",
       "2016-06-02    4310\n",
       "2016-05-10    4308\n",
       "2016-05-31    4279\n",
       "2016-05-05    4273\n",
       "2016-05-19    4270\n",
       "2016-05-03    4256\n",
       "2016-05-04    4168\n",
       "2016-06-03    4090\n",
       "2016-05-24    4009\n",
       "2016-05-13    3987\n",
       "2016-05-25    3909\n",
       "2016-05-06    3879\n",
       "2016-05-20    3828\n",
       "2016-04-29    3235\n",
       "2016-05-14      39\n",
       "Name: appointment_day, dtype: int64"
      ]
     },
     "execution_count": 215,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# show some little number about Appointment Day\n",
    "df['appointment_day'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "JARDIM CAMBURI                 7717\n",
       "MARIA ORTIZ                    5805\n",
       "RESISTÊNCIA                    4431\n",
       "JARDIM DA PENHA                3877\n",
       "ITARARÉ                        3514\n",
       "                               ... \n",
       "ILHA DO BOI                      35\n",
       "ILHA DO FRADE                    10\n",
       "AEROPORTO                         8\n",
       "ILHAS OCEÂNICAS DE TRINDADE       2\n",
       "PARQUE INDUSTRIAL                 1\n",
       "Name: neighbourhood, Length: 81, dtype: int64"
      ]
     },
     "execution_count": 216,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# show some little number about Neighbourhood\n",
    "df['neighbourhood'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     88208\n",
       "Yes    22319\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 217,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Show some little numbers about attendence No == Attend Appointment , Yes == Not Attend Appointment\n",
    "df['no_show'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='delete_row'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>patient_id</th>\n",
       "      <th>appointment_id</th>\n",
       "      <th>gender</th>\n",
       "      <th>schedule_day</th>\n",
       "      <th>appointment_day</th>\n",
       "      <th>age</th>\n",
       "      <th>neighbourhood</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "      <th>no_show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>99832</th>\n",
       "      <td>465943158731293</td>\n",
       "      <td>5775010</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-06-06</td>\n",
       "      <td>2016-06-06</td>\n",
       "      <td>-1</td>\n",
       "      <td>ROMÃO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            patient_id appointment_id gender schedule_day appointment_day  \\\n",
       "99832  465943158731293        5775010      F   2016-06-06      2016-06-06   \n",
       "\n",
       "       age neighbourhood  scholarship  hypertension  diabetes  alcoholism  \\\n",
       "99832   -1         ROMÃO            0             0         0           0   \n",
       "\n",
       "       handicap  sms_received no_show  \n",
       "99832         0             0      No  "
      ]
     },
     "execution_count": 218,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# I have noticed that the minimum value of age is -1 and this is unlogic so\n",
    "# I will serach for row of age = min and delete this row\n",
    "df[df['age'] == df['age'].min()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "99832"
      ]
     },
     "execution_count": 219,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "row_to_delete_index = df[df['age'] == df['age'].min()].index[0]\n",
    "row_to_delete_index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(index=row_to_delete_index, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(110526, 14)"
      ]
     },
     "execution_count": 221,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='edit_handicap'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>patient_id</th>\n",
       "      <th>appointment_id</th>\n",
       "      <th>gender</th>\n",
       "      <th>schedule_day</th>\n",
       "      <th>appointment_day</th>\n",
       "      <th>age</th>\n",
       "      <th>neighbourhood</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "      <th>no_show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>91820</th>\n",
       "      <td>9251878146849</td>\n",
       "      <td>5789549</td>\n",
       "      <td>M</td>\n",
       "      <td>2016-06-08</td>\n",
       "      <td>2016-06-08</td>\n",
       "      <td>15</td>\n",
       "      <td>DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98538</th>\n",
       "      <td>497246337172194</td>\n",
       "      <td>5760621</td>\n",
       "      <td>M</td>\n",
       "      <td>2016-06-01</td>\n",
       "      <td>2016-06-03</td>\n",
       "      <td>19</td>\n",
       "      <td>SÃO PEDRO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104268</th>\n",
       "      <td>758189466958349</td>\n",
       "      <td>5697136</td>\n",
       "      <td>F</td>\n",
       "      <td>2016-05-13</td>\n",
       "      <td>2016-06-02</td>\n",
       "      <td>9</td>\n",
       "      <td>ITARARÉ</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             patient_id appointment_id gender schedule_day appointment_day  \\\n",
       "91820     9251878146849        5789549      M   2016-06-08      2016-06-08   \n",
       "98538   497246337172194        5760621      M   2016-06-01      2016-06-03   \n",
       "104268  758189466958349        5697136      F   2016-05-13      2016-06-02   \n",
       "\n",
       "        age neighbourhood  scholarship  hypertension  diabetes  alcoholism  \\\n",
       "91820    15      DA PENHA            0             0         0           0   \n",
       "98538    19     SÃO PEDRO            0             0         0           0   \n",
       "104268    9       ITARARÉ            0             0         0           0   \n",
       "\n",
       "        handicap  sms_received no_show  \n",
       "91820          4             0      No  \n",
       "98538          4             0      No  \n",
       "104268         4             1     Yes  "
      ]
     },
     "execution_count": 222,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check how many handicap values > 1 and set these values to 1 \n",
    "df[df['handicap'] == df['handicap'].max()]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "So, I found that there are 3 rows of handicap equal 4 but This is unlogic so I will make every value of 4 to be 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['handicap'].replace({4:1,3:1,2:1}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 224,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['handicap'][df['handicap'] > 1].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id= 'check_duplicate'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 225,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check again for duplicates and now we for whole DataFrame and for appointment_id column also\n",
    "df['appointment_id'].duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 226,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='delete_col'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Delete columns of patient_id, appointment_id, schedule_day, appointment_day as I will not include them in my insight\n",
    "df.drop(columns=['patient_id', 'appointment_id', 'schedule_day', 'appointment_day'], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>neighbourhood</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "      <th>no_show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>F</td>\n",
       "      <td>62</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>62</td>\n",
       "      <td>MATA DA PRAIA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>F</td>\n",
       "      <td>8</td>\n",
       "      <td>PONTAL DE CAMBURI</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>F</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  age      neighbourhood  scholarship  hypertension  diabetes  \\\n",
       "0      F   62    JARDIM DA PENHA            0             1         0   \n",
       "1      M   56    JARDIM DA PENHA            0             0         0   \n",
       "2      F   62      MATA DA PRAIA            0             0         0   \n",
       "3      F    8  PONTAL DE CAMBURI            0             0         0   \n",
       "4      F   56    JARDIM DA PENHA            0             1         1   \n",
       "\n",
       "   alcoholism  handicap  sms_received no_show  \n",
       "0           0         0             0      No  \n",
       "1           0         0             0      No  \n",
       "2           0         0             0      No  \n",
       "3           0         0             0      No  \n",
       "4           0         0             0      No  "
      ]
     },
     "execution_count": 228,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='save_clean'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save a clean CSV \n",
    "df.to_csv('clean_no_show_appointment_data.csv', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='import_clean'></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>neighbourhood</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "      <th>no_show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>F</td>\n",
       "      <td>62</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>62</td>\n",
       "      <td>MATA DA PRAIA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>F</td>\n",
       "      <td>8</td>\n",
       "      <td>PONTAL DE CAMBURI</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>F</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  age      neighbourhood  scholarship  hypertension  diabetes  \\\n",
       "0      F   62    JARDIM DA PENHA            0             1         0   \n",
       "1      M   56    JARDIM DA PENHA            0             0         0   \n",
       "2      F   62      MATA DA PRAIA            0             0         0   \n",
       "3      F    8  PONTAL DE CAMBURI            0             0         0   \n",
       "4      F   56    JARDIM DA PENHA            0             1         1   \n",
       "\n",
       "   alcoholism  handicap  sms_received no_show  \n",
       "0           0         0             0      No  \n",
       "1           0         0             0      No  \n",
       "2           0         0             0      No  \n",
       "3           0         0             0      No  \n",
       "4           0         0             0      No  "
      ]
     },
     "execution_count": 230,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import the clean CSV and show the first 5 rows by *head*\n",
    "df = pd.read_csv('clean_no_show_appointment_data.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(110526, 10)"
      ]
     },
     "execution_count": 231,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 110526 entries, 0 to 110525\n",
      "Data columns (total 10 columns):\n",
      " #   Column         Non-Null Count   Dtype \n",
      "---  ------         --------------   ----- \n",
      " 0   gender         110526 non-null  object\n",
      " 1   age            110526 non-null  int64 \n",
      " 2   neighbourhood  110526 non-null  object\n",
      " 3   scholarship    110526 non-null  int64 \n",
      " 4   hypertension   110526 non-null  int64 \n",
      " 5   diabetes       110526 non-null  int64 \n",
      " 6   alcoholism     110526 non-null  int64 \n",
      " 7   handicap       110526 non-null  int64 \n",
      " 8   sms_received   110526 non-null  int64 \n",
      " 9   no_show        110526 non-null  object\n",
      "dtypes: int64(7), object(3)\n",
      "memory usage: 8.4+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>110526.000000</td>\n",
       "      <td>110526.000000</td>\n",
       "      <td>110526.000000</td>\n",
       "      <td>110526.000000</td>\n",
       "      <td>110526.000000</td>\n",
       "      <td>110526.000000</td>\n",
       "      <td>110526.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>37.089219</td>\n",
       "      <td>0.098266</td>\n",
       "      <td>0.197248</td>\n",
       "      <td>0.071865</td>\n",
       "      <td>0.030400</td>\n",
       "      <td>0.020276</td>\n",
       "      <td>0.321029</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>23.110026</td>\n",
       "      <td>0.297676</td>\n",
       "      <td>0.397923</td>\n",
       "      <td>0.258266</td>\n",
       "      <td>0.171686</td>\n",
       "      <td>0.140943</td>\n",
       "      <td>0.466874</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>37.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>55.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>115.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 age    scholarship   hypertension       diabetes  \\\n",
       "count  110526.000000  110526.000000  110526.000000  110526.000000   \n",
       "mean       37.089219       0.098266       0.197248       0.071865   \n",
       "std        23.110026       0.297676       0.397923       0.258266   \n",
       "min         0.000000       0.000000       0.000000       0.000000   \n",
       "25%        18.000000       0.000000       0.000000       0.000000   \n",
       "50%        37.000000       0.000000       0.000000       0.000000   \n",
       "75%        55.000000       0.000000       0.000000       0.000000   \n",
       "max       115.000000       1.000000       1.000000       1.000000   \n",
       "\n",
       "          alcoholism       handicap   sms_received  \n",
       "count  110526.000000  110526.000000  110526.000000  \n",
       "mean        0.030400       0.020276       0.321029  \n",
       "std         0.171686       0.140943       0.466874  \n",
       "min         0.000000       0.000000       0.000000  \n",
       "25%         0.000000       0.000000       0.000000  \n",
       "50%         0.000000       0.000000       0.000000  \n",
       "75%         0.000000       0.000000       1.000000  \n",
       "max         1.000000       1.000000       1.000000  "
      ]
     },
     "execution_count": 233,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "These statistical results from numerical columns is good"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Appointment Attending Percent is 79.81% with number of 88207\n",
      "The Missing Appointment Percent is 20.19% with sum of 22319\n"
     ]
    }
   ],
   "source": [
    "def No_show_percent():\n",
    "    \"\"\"\n",
    "    This function simply detect the number of patients attending and missing the medical appointment \n",
    "    and print the results as message\n",
    "    \n",
    "    Parameters:\n",
    "    \n",
    "    \"\"\"\n",
    "    \n",
    "    sum_of_appointments = df['no_show'].count()\n",
    "    \n",
    "    sum_of_attend = df['no_show'][df['no_show'] == 'No'].count()\n",
    "    attend_percent = sum_of_attend * 100 / sum_of_appointments\n",
    "    \n",
    "    sum_of_miss = df['no_show'][df['no_show'] == 'Yes'].count()\n",
    "    miss_percent = sum_of_miss * 100 / sum_of_appointments\n",
    "    \n",
    "    No_show_percent_message = 'The Appointment Attending Percent is {}% with number of {}\\nThe Missing Appointment Percent is {}% with sum of {}'.format(round(attend_percent, 2), sum_of_attend, round(miss_percent, 2), sum_of_miss)\n",
    "    print(No_show_percent_message)\n",
    "No_show_percent()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "metadata": {},
   "outputs": [],
   "source": [
    "def percentage(any_column):\n",
    "    \"\"\"\n",
    "    This function simply detect the number of patients having and not having one of these six columns \n",
    "    [scholarship, hypertension, diabetes, alcoholism, handicap, sms_received]\n",
    "    and print the results as message\n",
    "    \n",
    "    Parameters:\n",
    "    any column of the above 6 columns\n",
    "    \"\"\"\n",
    "    any_column = str(any_column)\n",
    "    sum_of_appointments = df[any_column].count()\n",
    "    \n",
    "    sum_of_have = df[any_column][df[any_column] == 1].count()\n",
    "    have_percent = sum_of_have * 100 / sum_of_appointments\n",
    "    \n",
    "    sum_of_not_have = df[any_column][df[any_column] == 0].count()\n",
    "    not_have_percent = sum_of_not_have * 100 / sum_of_appointments\n",
    "    \n",
    "    any_column_percent_message = 'The Patients Percent having {} is {}% with number of {}\\nThe Patients Percent not having {} is {}% with sum of {}'.format(any_column,round(have_percent, 2), sum_of_have, any_column, round(not_have_percent, 2), sum_of_not_have)\n",
    "    print(any_column_percent_message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Patients Percent having scholarship is 9.83% with number of 10861\n",
      "The Patients Percent not having scholarship is 90.17% with sum of 99665\n"
     ]
    }
   ],
   "source": [
    "percentage('scholarship')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Patients Percent having hypertension is 19.72% with number of 21801\n",
      "The Patients Percent not having hypertension is 80.28% with sum of 88725\n"
     ]
    }
   ],
   "source": [
    "percentage('hypertension')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Patients Percent having diabetes is 7.19% with number of 7943\n",
      "The Patients Percent not having diabetes is 92.81% with sum of 102583\n"
     ]
    }
   ],
   "source": [
    "percentage('diabetes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Patients Percent having alcoholism is 3.04% with number of 3360\n",
      "The Patients Percent not having alcoholism is 96.96% with sum of 107166\n"
     ]
    }
   ],
   "source": [
    "percentage('alcoholism')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 240,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Patients Percent having handicap is 2.03% with number of 2241\n",
      "The Patients Percent not having handicap is 97.97% with sum of 108285\n"
     ]
    }
   ],
   "source": [
    "percentage('handicap')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Patients Percent having sms_received is 32.1% with number of 35482\n",
      "The Patients Percent not having sms_received is 67.9% with sum of 75044\n"
     ]
    }
   ],
   "source": [
    "percentage('sms_received')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='eda'></a>\n",
    "## Exploratory Data Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='q1'></a>\n",
    "### 1- What are the general statistical results for whole columns?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>neighbourhood</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "      <th>no_show</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>F</td>\n",
       "      <td>62</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  age    neighbourhood  scholarship  hypertension  diabetes  \\\n",
       "0      F   62  JARDIM DA PENHA            0             1         0   \n",
       "\n",
       "   alcoholism  handicap  sms_received no_show  \n",
       "0           0         0             0      No  "
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x1080 with 9 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Histogram of whole numerical columns\n",
    "df.hist(figsize=(15,15));"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['gender'].hist();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['no_show'].hist();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "JARDIM CAMBURI                 7717\n",
       "MARIA ORTIZ                    5805\n",
       "RESISTÊNCIA                    4431\n",
       "JARDIM DA PENHA                3877\n",
       "ITARARÉ                        3514\n",
       "                               ... \n",
       "ILHA DO BOI                      35\n",
       "ILHA DO FRADE                    10\n",
       "AEROPORTO                         8\n",
       "ILHAS OCEÂNICAS DE TRINDADE       2\n",
       "PARQUE INDUSTRIAL                 1\n",
       "Name: neighbourhood, Length: 81, dtype: int64"
      ]
     },
     "execution_count": 246,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['neighbourhood'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "110526"
      ]
     },
     "execution_count": 247,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['neighbourhood'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "JARDIM CAMBURI                 6.982068\n",
       "MARIA ORTIZ                    5.252158\n",
       "RESISTÊNCIA                    4.009011\n",
       "JARDIM DA PENHA                3.507772\n",
       "ITARARÉ                        3.179342\n",
       "                                 ...   \n",
       "ILHA DO BOI                    0.031667\n",
       "ILHA DO FRADE                  0.009048\n",
       "AEROPORTO                      0.007238\n",
       "ILHAS OCEÂNICAS DE TRINDADE    0.001810\n",
       "PARQUE INDUSTRIAL              0.000905\n",
       "Name: neighbourhood, Length: 81, dtype: float64"
      ]
     },
     "execution_count": 248,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "neighbourhood_percent_df = df['neighbourhood'].value_counts() * 100 / df['neighbourhood'].count()\n",
    "neighbourhood_percent_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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/b3JcV2f60GSuiR1LV44v6fqERERERERLSWQHpp2A8YDs8ulYNux9JbpGbY3A7YH/lPSa7rpa2uqILmdGcA3ab+tG+BeqrRY/Zkrtn9Otar9KtsPthvE9hNUK+iNG8MXNZ2XXht4sva+Nzmu6/2fabvDdseoseO7qxoREREREdFWAumhqRP4RC0v8+uBXSWNrVeyPZMqNdRnWnUiaS+q1eHuguTLgROB67qpcyHwDkl/vUpP0m6StujtXKlSX32pmzEobbYGHi5F/wt8tDwbA3wEuLG5Xbsc1xEREREREStC8kgPIZJWpkot9R7g4Ea57Wcl3Up1jrnZ14A7JP17eX+4pI9Spb+6B3hXWeltyfYzpQ+acjDX6yySNA04RdIpZY53A1/o7Vxt/7D9J+cCSY30V+fabpzH/gzVbdyfptqifr7tm9v00SrHdVvJIx0REREREf2VPNJDiKStgLNsv3Ww5/K3rqOjw11dXYM9jYiIiIiIGMKSR3qIk3QI1RbsYwZ7LhEREREREdFetnYPEbZPB04f7HlERERERERE97IiHREREREREdEHCaQjIiIiIiIi+iCBdEREREREREQfJJCOiIiIiIiI6IME0hERERERERF9kEA6IiIiIiIiog8SSEdERERERET0QQLpiIiIiIiIiD5IIB0RERERERHRBwmkIyIiIiIiIvoggXREREREREREHySQjoiIiIiIiOiDBNIRERERERERfZBAOiIiIiIiIqIPEkhHRERERERE9EEC6YiIiIiIiIg+SCAdERERERER0QcJpCMiIiIiIiL6IIF0RERERERERB8kkI6IiIiIiIjogwTSEREREREREX2QQDoiIiIiIiKiDxJIR0RERERERPRBAumIiIiIiIiIPkggHREREREREdEHCaQjIiIiIiIi+iCBdEREREREREQfJJCOiIiIiIiI6IME0hERERERERF9kEA6IiIiIiIiog8SSEdERERERET0gWwP9hwiXnaSngEeGOx5RK+8CnhysCcRvZKf1fCQn9PwkZ/V8JCf0/CRn9XwMNR+ThvYfnVz4cqDMZOIIeAB2x2DPYnomaSu/KyGh/yshof8nIaP/KyGh/ycho/8rIaH4fJzytbuiIiIiIiIiD5IIB0RERERERHRBwmkY6Q6c7AnEL2Wn9XwkZ/V8JCf0/CRn9XwkJ/T8JGf1fAwLH5OuWwsIiIiIiIiog+yIh0RERERERHRBwmkY8SRtJukByQ9JOmowZ5PtCbpbEl/kHTPYM8l2pO0nqQbJd0v6V5JnxnsOUVrklaT9HNJd5Wf1b8N9pyiPUmjJN0p6ZrBnku0J2mupNmSZknqGuz5RGuS1pR0iaRflv+/2maw5xTLkrRx+d9S4+tpSf882PNqJ1u7Y0SRNAp4EHg38BjwC6DT9n2DOrFYhqQdgAXA+bY3H+z5RGuSJgATbN8h6RXA7cAe+d/U0CNJwOq2F0haBbgV+Iztnw3y1KIFSZ8FOoA1bE8b7PlEa5LmAh22h1LO22gi6TzgFtvfkbQqMNb2nwd5WtGN8m/2ecDbbD8y2PNpJSvSMdK8FXjI9q9t/wW4GPjAIM8pWrB9M/DHwZ5HdM/247bvKK+fAe4HJg7urKIVVxaUt6uUr/w1fQiS9Drg74DvDPZcIoY7SWsAOwDfBbD9lwTRw8LOwMNDNYiGBNIx8kwEHq29f4z8oz9iQEiaBGwN3DbIU4k2ynbhWcAfgB/bzs9qaDoF+Dzw0iDPI3pm4HpJt0s6aLAnEy29AXgCOKccl/iOpNUHe1LRo32AiwZ7Et1JIB0jjVqUZUUmYjlJGgdcCvyz7acHez7Rmu3FtqcArwPeKinHJoYYSdOAP9i+fbDnEr2yre2pwO7AoeVYUgwtKwNTgW/b3hp4FsgdOUNY2X7/fuD/DfZcupNAOkaax4D1au9fB/x2kOYS8TehnLe9FLjA9mWDPZ/oWdnWeBOw2+DOJFrYFnh/OXt7MfAuSf89uFOKdmz/tvz3D8DlVEfIYmh5DHistgPnEqrAOoau3YE7bP9+sCfSnQTSMdL8Apgs6fXlr137AFcN8pwihq1ygdV3gfttf32w5xPtSXq1pDXL6zHALsAvB3VSsQzbX7T9OtuTqP4/6gbbHx3kaUULklYvlyxStgrvCiTTxBBj+3fAo5I2LkU7A7kQc2jrZIhv64Zqq0PEiGH7RUmHAdcBo4Czbd87yNOKFiRdBOwIvErSY8CXbX93cGcVLWwL7A/MLmdvAb5k+weDN6VoYwJwXrkJdSXg+7aTWimi/9YFLq/+nsjKwIW2fzS4U4o2PgVcUBZRfg38/SDPJ9qQNJYqu87Bgz2XniT9VUREREREREQfZGt3RERERERERB8kkI6IiIiIiIjogwTSEREREREREX2QQDoiIiIiIiKiDxJIR0RERERERPRBAumIiIiIiIiIPkggHREREUOapMWSZkm6R9L/K3lGX+457CjpHU1l/yzpY+X11yTdLen82vP9JX2m9n4LSee+bJOOiIgVJoF0REREDHWLbE+xvTnwF+CQ3jSStPIAzmFH4K+BdOn7H4ALJY0H3mF7S2BUCZjHAAcC32q0sT0beJ2k9QdwXhERMQgSSEdERMRwcguwkaTVJZ0t6ReS7pT0AQBJB5ZV66uB6yWNk3SOpNllxXivUm9XSTMl3VHqjyvlcyX9WymfLWkTSZOogvfDy8r49sC7gDtsvwi8BKwqScAY4AXgSOAbtl9omv/VwD4r/LsUERErVALpiIiIGBbKKvDuwGzgaOAG228BdgJOkrR6qboNcIDtdwH/Asy3vUVZMb5B0quAY4BdbE8FuoDP1oZ6spR/GzjC9lzgdGB6WRm/BdgWuB3A9jPApcCdwBxgPvAW21e2+BhdwPYD8x2JiIjBMpBbniIiIiJWhDGSZpXXtwDfBf4PeL+kI0r5akBjy/SPbf+xvN6F2gqw7T9JmgZsCvy0WkRmVWBmbbzLyn9vBz7YZk4TgPtr/Z4InAgg6TvAv0r6BLArcLftr5SqfwBe27uPHRERQ1UC6YiIiBjqFtmeUi8o26j3sv1AU/nbgGfrRYCb+hNVsN3ZZrzny38X0/7fSouogvelO5a2Li8fBE61vYOkiyVNtv2r0mZRmz4jImKYyNbuiIiIGI6uAz5VAup6ANvseuCwxhtJawE/A7aVtFEpGyvpjT2M9wzwitr7+4GNWtQ7HvhXYBVgVCl7CWjcNP5G4J4exoqIiCEugXREREQMR8dTBat3S7qnvG/lK8BaJXXWXcBOtp+gulH7Ikl3UwXWm/Qw3tXAnrXLxn4I7FCvIGkP4Be2f2v7z8BMSbMB276rVNsJuLZvHzUiIoYa2c27nSIiIiKiJ5IuBz5ftmz3pv5o4H+B7cpt3xERMUwlkI6IiIjoB0kbA+vavrmX9ScDE23ftEInFhERK1wC6YiIiIiIiIg+yBnpiIiIiIiIiD5IIB0RERERERHRBwmkIyIiIiIiIvoggXREREREREREHySQjoiIiIiIiOiD/w/rVt8yQNnlSgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1008x1008 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplots(figsize=(14,14));\n",
    "plt.barh(neighbourhood_percent_df.index, neighbourhood_percent_df.values);\n",
    "plt.title('Percent of Hospital Places having more appointments (show or no-show)');\n",
    "plt.xlabel('Percent(%)');\n",
    "plt.ylabel('Hospital Places');"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can sum up these histograms to say:\n",
    ">-The majority of patients are below 60 years and number of patients decreases after 60\n",
    ">\n",
    ">-The majority of patients are not included in Brasilian welfare program (Bolsa Família)\n",
    ">\n",
    ">-The majority of patients are not suffering from hypertension, diabetes, alcoholism nor handicap\n",
    ">\n",
    ">-The higher percent of patients did not recieve a SMS to inform them about the appointment\n",
    ">\n",
    ">-The higher percent of patients is females \n",
    ">\n",
    ">-The higher percent of patients had appointments in 'JARDIM CAMBURI' with (\\~7% of whole appointments) then 'MARIA ORTIZ' with (\\~5.25% of whole appointments)\n",
    ">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='q2'></a>\n",
    "### 2- How far does the gender affect the attending of the appointment?\n",
    "Here, I will discuss the no_show column as the dependent variable against gender as an independent variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender  no_show\n",
       "F       No         57245\n",
       "        Yes        14594\n",
       "M       No         30962\n",
       "        Yes         7725\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 250,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gender_no_show_df = df.groupby('gender')['no_show'].value_counts()\n",
    "gender_no_show_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no_show\n",
       "No     57245\n",
       "Yes    14594\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 251,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "female_no_show_df = df.groupby('gender')['no_show'].value_counts().loc['F']\n",
    "female_no_show_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no_show\n",
       "No     30962\n",
       "Yes     7725\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 252,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "male_no_show_df = df.groupby('gender')['no_show'].value_counts().loc['M']\n",
    "male_no_show_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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s98jgdPLs8t+C7yHJjieHRGHAnfSPIqFzLwhIs6mCXqLgSPK88qgef7hbJpbjPy4vKB5LMhpETGfpgVuZo+XR5IkPU/PPPMMCxYs4Kmnlnni4SpvwoQJTJ06ldVWW63rcVa5x2719fWlFzZIkjTybrvtNtZZZx0mTZpEc3BNAJnJokWLeOyxx9hiiy2W6hcRczOzb6DxfGKDJEkaEU899ZQBbgARwaRJk5a7hdIQJ0mSRowBbmDPZ70Y4iRJkipkiJMkSaMjYsW+ujBu3Di23XbbZ1+33357zxZv2rRpPPDAA8MP+Dz1+upUSZKkMWPixIlce+21o12NFcKWOEmStEqbO3cub3jDG9h+++3ZY489uOeeewDYZZddOProo3n961/PVlttxdVXX82+++7L9OnT+djHPvbs+Pvssw/bb789M2bM4OSTTx5wHt///vfZcccd2XbbbXnf+97HkiVLBhxueRjiJEnSKuPJJ5989lDq29/+dp555hmOPPJIzjnnHObOncshhxzCRz/60WeHX3311bnssss4/PDD2Xvvvfn617/OvHnzmD17NosWLQLge9/7HnPnzmXOnDmcdNJJz5b3u+mmmzjrrLP45S9/ybXXXsu4ceM4/fTTX/CyeDhVkiStMjoPp86bN4958+ax2267AbBkyRI22WSTZ/vvtddeALzyla9kxowZz/Z76Utfyl133cWkSZM46aSTOPfccwG46667uPXWW5k0adKz07jooouYO3cuO+ywA9AEyY033vgFL4shTpIkrbIykxkzZnDFFVcM2H+NNdYA4EUvetGz7/u7Fy9ezCWXXMLPfvYzrrjiCtZcc0122WWXZe73lpnMmjWLT3/60yu07h5OlSRJq6yXv/zlLFy48NkQ98wzz3DDDTd0Pf4jjzzCBhtswJprrsnNN9/Mr371q2WG2XXXXTnnnHO4//77AXjwwQe54447XnDdDXGSJGl0ZK7Y1/Ow+uqrc8455/CRj3yEV73qVWy77bZcfvnlXY+/5557snjxYrbZZhtOOOEEdtppp2WG2XrrrfnkJz/J7rvvzjbbbMNuu+327MUTL4TPTpUkSSPipptuYqutthrtaoxZA60fn50qSZK0kjHESZIkVcgQJ0mSVCFDnCRJUoUMcZIkSRUyxEmSJFXIECdJkkZFxIp9dTfP4N3vfvez3YsXL2by5Mm8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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = ['No(Attend)', 'Yes(Not Attend)']\n",
    "x = np.arange(len(labels))\n",
    "width = 0.35\n",
    "\n",
    "bar_value_1 = female_no_show_df \n",
    "bar_value_2 = male_no_show_df\n",
    "\n",
    "plt.subplots(figsize=(10,10));\n",
    "plt.bar(x-width/2, bar_value_1, width, color='red', label='Female');\n",
    "plt.bar(x+width/2, bar_value_2, width, color='blue', label='Male');\n",
    "\n",
    "plt.title('Percent of Patients Gender Attending and Not Attending the Appointment(No=Attend)');\n",
    "plt.xlabel('No-Show');\n",
    "plt.ylabel('Gender Count');\n",
    "plt.xticks(x, labels);\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 254,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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ArBs2TI222yz5cMPOOAAALbffnumT5++fNjzn/987r77bjbZZBPOPPNMLrroIgDuvvtubrvtNjbZZJPl87jiiiuYO3cuu+yyC1AFwec85zlrvC6GMEmSNGplJtOnT+eaa65pO3zdddcF4BnPeMby533dS5cuZfbs2Vx++eVcc801rLfeesyYMWOl+31lJkceeSQf//jHh7R2T0dKkqRR68UvfjGLFi1aHsKWLFnCjTfe2PH0Dz30EBtvvDHrrbcet9xyC9dee+1K47zuda/jggsu4P777wfgj3/8I3feeeca124IkyRJqydzaB+rYcKECVxwwQW8//3vZ8cdd2SnnXbi6quv7nj6ffbZh6VLl7LDDjtw2mmn8bKXvWylcbbbbjs+8pGPsNdee7HDDjuw5557Lr/4f01EruZKl9LT05O9vb2ly5Akaa1z8803s+2225YuY8Rqt30iYm5m9rQb3yNhkiRJBRjCJEmSCjCESZIkFWAIkyRJKsAQJkmSVIAhTJIkqQBDmCRJWi0RQ/vobJnB4Ycfvrx76dKlTJ48mf3333/A6WbPnj3oOMPNny2SpNGq0/9aKmOU3YdztFh//fWZP38+jz/+OJMmTeJHP/oRm2++eemyVotHwiRJ0qiy7777cskllwBw3nnnceihhy4fdt1117H77rvz0pe+lN13351bb711pekfffRRjj76aHbZZRde+tKX8t3vfnfYam8yhEmSpFHlkEMO4fzzz+eJJ57ghhtuYLfddls+bJtttuGqq67i+uuv58Mf/jCnnnrqStN/9KMf5bWvfS1z5szhJz/5CSeffDKPPvrocK4C4OlISZI0yuywww7ccccdnHfeeey3334rDHvooYc48sgjue2224gIlixZstL0P/zhD5k1axaf+tSnAHjiiSe46667hv0nmQxh/fFai5HNay0kaa12wAEHcNJJJzF79mwWL168vP9pp53Ga17zGi666CLuuOMOZsyYsdK0mcm3v/1tXvziFw9jxSvzdKQkSRp1jj76aD70oQ+x/fbbr9D/oYceWn6h/syZM9tOu/fee/P5z3+erD/QX3/99V2ttT+GMEmStFoyh/axKqZMmcJ73/velfq/733v45//+Z95xStewbJly9pOe9ppp7FkyRJ22GEHXvKSl3DaaaetzuqvschRdlqnp6cne3t7u78gT0eObKPs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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = ['No(Attend)', 'Yes(Not Attend)']\n",
    "x = np.arange(len(labels))\n",
    "width = 0.35\n",
    "\n",
    "bar_value_1 = [female_no_show_df[0] / df['no_show'].value_counts()['No'],\n",
    "               female_no_show_df[1] / df['no_show'].value_counts()['Yes']]\n",
    "bar_value_2 = [male_no_show_df[0] / df['no_show'].value_counts()['No'],\n",
    "               male_no_show_df[1] / df['no_show'].value_counts()['Yes']]\n",
    "\n",
    "plt.subplots(figsize=(10,10));\n",
    "plt.bar(x-width/2, bar_value_1, width, color='red', label='Female');\n",
    "plt.bar(x+width/2, bar_value_2, width, color='blue', label='Male');\n",
    "\n",
    "plt.title('Percent of Patients Gender Attending and Not Attending the Appointment(No=Attend)');\n",
    "plt.xlabel('No-Show');\n",
    "plt.ylabel('Gender Count');\n",
    "plt.xticks(x, labels);\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can sum up this bar plot to say:\n",
    ">-The higher percent of patients are Females \n",
    ">\n",
    ">-Females are the more like to attend the appointment\n",
    ">\n",
    ">-Females are the more like to miss the appointment also \n",
    ">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='q3'></a>\n",
    "### 3- Is there any relationship between age and the attending the appointment?\n",
    "Here, I will discuss the no_show column as the dependent variable against age as an independent variable but I will divide the age into 5 sections (1st quarter, 2nd quarter, 3rd quarter, 4th quarter, 5th quarter) each quarter is 25 years"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "metadata": {},
   "outputs": [],
   "source": [
    "bins = [0, 25, 50, 75, 100, 125]\n",
    "age_labels = ['1st quarter', '2nd quarter', '3rd quarter', '4th quarter', '5th quarter']\n",
    "df['age_quarter_names'] = pd.cut(df['age'], bins, labels = age_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>neighbourhood</th>\n",
       "      <th>scholarship</th>\n",
       "      <th>hypertension</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>alcoholism</th>\n",
       "      <th>handicap</th>\n",
       "      <th>sms_received</th>\n",
       "      <th>no_show</th>\n",
       "      <th>age_quarter_names</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>F</td>\n",
       "      <td>62</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>3rd quarter</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>3rd quarter</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>62</td>\n",
       "      <td>MATA DA PRAIA</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>3rd quarter</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>F</td>\n",
       "      <td>8</td>\n",
       "      <td>PONTAL DE CAMBURI</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>1st quarter</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>F</td>\n",
       "      <td>56</td>\n",
       "      <td>JARDIM DA PENHA</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>3rd quarter</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  age      neighbourhood  scholarship  hypertension  diabetes  \\\n",
       "0      F   62    JARDIM DA PENHA            0             1         0   \n",
       "1      M   56    JARDIM DA PENHA            0             0         0   \n",
       "2      F   62      MATA DA PRAIA            0             0         0   \n",
       "3      F    8  PONTAL DE CAMBURI            0             0         0   \n",
       "4      F   56    JARDIM DA PENHA            0             1         1   \n",
       "\n",
       "   alcoholism  handicap  sms_received no_show age_quarter_names  \n",
       "0           0         0             0      No       3rd quarter  \n",
       "1           0         0             0      No       3rd quarter  \n",
       "2           0         0             0      No       3rd quarter  \n",
       "3           0         0             0      No       1st quarter  \n",
       "4           0         0             0      No       3rd quarter  "
      ]
     },
     "execution_count": 256,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age_quarter_names  no_show\n",
       "1st quarter        No         26881\n",
       "                   Yes         8179\n",
       "2nd quarter        No         28730\n",
       "                   Yes         7774\n",
       "3rd quarter        No         25174\n",
       "                   Yes         4857\n",
       "4th quarter        No          4518\n",
       "                   Yes          867\n",
       "5th quarter        No             4\n",
       "                   Yes            3\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 257,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('age_quarter_names')['no_show'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 258,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no_show\n",
       "No     26881\n",
       "Yes     8179\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 258,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "first_quart_no_show_df = df.groupby('age_quarter_names')['no_show'].value_counts()['1st quarter']\n",
    "first_quart_no_show_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "metadata": {},
   "outputs": [],
   "source": [
    "second_quart_no_show_df = df.groupby('age_quarter_names')['no_show'].value_counts()['2nd quarter']\n",
    "third_quart_no_show_df = df.groupby('age_quarter_names')['no_show'].value_counts()['3rd quarter']\n",
    "fourth_quart_no_show_df = df.groupby('age_quarter_names')['no_show'].value_counts()['4th quarter']\n",
    "fifth_quart_no_show_df = df.groupby('age_quarter_names')['no_show'].value_counts()['5th quarter']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Lw+obp58cUTcR9UDd2gH10eSpEHpmWeeMcDVWESwySabsKLH7XcsxGXm7cBOTcofB/bpY57PAp9tUj4dWO54unL/snesdGUlSao5A1y9PZ/2844NkiRJNTQgJzZIkqQBtKp75TzcfFCyJ06SJK20iODkk09e+vyLX/wiZ5xxRr/zfeUrX+Giiy5a+nzx4sVsuummnHbaactM97nPfW7p8Lx58zjnnHNWvtLFrFmzGDOmOmrrjjvu4Jhjjllly+4kQ5wkSVppa6+9NldffTV//vOf255n8eLFnHfeeRx++OFLy6ZMmcK2227LFVdcQeMFJzoZ4hrtuOOOzJkzh9mzZ3dk+auSIU6SJK20oUOHMnHiRL785S8vN+7BBx9kn332YezYseyzzz5LA9KNN97IzjvvzNChzx3dNXnyZE466SS22WYbfvGLXwBw6qmnsnDhQsaNG8cRRxzBqaeeyh/+8AfGjRvHKaecAsAXvvAFXv3qVzN27Fg+8YlPAFUP23bbbcdxxx3HDjvswL777svChQsBmDFjBq961auYMGECZ5999jL1PfDAA7nssstW/UZaxQxxkiRplTj++OO55JJLePLJJ5cpP+GEEzjqqKO4/fbbOeKIIzjxxBMBuPnmm9lll12WTrdw4UJ+8pOf8OY3v5nDDjuMyZMnAzBp0iSGDx/OzJkzueSSS5g0aRIve9nLmDlzJl/4wheYMmUK9957L7feeiszZ85kxowZ/OxnPwPg3nvv5fjjj+fOO+9ko4024qqrrgLgPe95D2eddRa33HLLcusxfvx4fv7zn3dkG61KhjhJkrRKbLDBBhx11FGcddZZy5TfcsstS3eZHnnkkUybNg2ARx55hMbbYV533XXstddevPCFL+Ttb38711xzDUuWLKE/U6ZMYcqUKey0007svPPO3HPPPdx7770AjBo1inHjxgGwyy67MGvWLJ588knmzZvHHnvssbROjTbffHMefvhhBjvPTpUkSavMhz70IXbeeWfe85739DlNzzXRhg8fvsytwiZPnszNN9/MyJEjAXj88ceZOnUqb3jDG1q+ZmZy2mmn8d73vneZ8lmzZrH22msvfT5kyBAWLlxIZra8LtszzzzD8OHDW77mYGBPnCRJq5vMVftYAS960Yt45zvfybe//e2lZa997WuXHmN2ySWX8LrXvQ6A7bbbjvvuuw+Ap556imnTpjF79mxmzZrFrFmzOPvss5fuUh02bBjPPvssAOuvvz7z589fuvz99tuP8847jwULFgDwxz/+kccee4y+bLTRRmy44YZLewQvueSSZcb//ve/X3q26mBmiJMkSavUySefvMxZqmeddRbnn38+Y8eO5eKLL+arX/0qAG984xuXHrt29dVXs/feey/Tc3bQQQdx7bXXsmjRIiZOnMjYsWM54ogj2GSTTdh9990ZM2YMp5xyCvvuuy+HH344EyZMYMcdd+SQQw5ZJuQ1c/7553P88cczYcKE5Xrdpk6dygEHHLCqNkfHxJp2v/jx48fn9OnTu10NSZJWmbvvvpvtttuu29V4Xg4++GA+//nPM3r06G5XBYBFixaxxx57MG3atGXOmh0IzdoxImZk5vhm09sTJ0mSumbSpEk88sgj3a7GUrNnz2bSpEkDHuCej8FfQ0mStNradttt2XbbbbtdjaVGjx49aHoF+2NPnCRJUg0Z4iRJkmrIECdJklRDHhMnSdJqpsV1bJ+XNexCFrVhT5wUMTgfklQTmcnrXvc6rr/++qVlV1xxBfvvv3/by1i4cCF77LEHS5YsYdasWUQEX/va15aOP+GEE7jgggtaLuOCCy5oebusxYsXs+mmm3LaaactU/65z31u6fC8efM455xz2q53f2bNmrX0wsF33HEHxxxzzCpbtiFOkiStlIjg61//Ov/6r//KM888w9NPP83HPvYxzj777LaXcd555/G2t72NIUOGANX9S7/61a/yt7/9re1l9BfipkyZwrbbbssVV1xB43VyOxniGu24447MmTOH2bNnr5LlGeIkSdJKGzNmDAceeCBnnnkmn/zkJ3n3u9/NZz/7WV796lez00478f3vfx+AO++8k1133ZVx48YxduzYpTeqv+SSSzjooIOWLm+zzTZjn3324cILL1zutWbOnMluu+3G2LFjOfjgg3niiSe48sormT59OkcccQTjxo1j4cKFy803efJkTjrpJLbZZht+8YtfAHDqqaeycOFCxo0bxxFHHMGpp57KH/7wB8aNG8cpp5wCwBe+8AVe/epXM3bsWD7xiU8AVQ/bdtttx3HHHccOO+zAvvvuu/Q1Z8yYwate9SomTJiwXJA98MADl96CbKVl5hr12GWXXVJaxqq/y+CqeUhSm+66665lnnfr62jBggX5ile8IseMGZOnnnpqXnzxxZmZ+cQTT+To0aNzwYIFecIJJ+R3vvOdzMxctGhR/vWvf81FixblFltssXQ5DzzwQO6www55//3357bbbpuLFy/O448/Ps8///zMzNxxxx3zpptuyszM008/PU866aTMzNxjjz3yV7/6VdO6/fWvf80tt9wyn3766fzGN76RH/zgB5eOW3fddZd77R4//vGP87jjjsu///3vuWTJkjzggAPypz/9aT7wwAM5ZMiQvO222zIz8x3veMfS9W2s34c//OFlljdt2rR885vf3LSOvdsxMxOYnn1kGnviJEnSKrHuuuvyrne9iyOPPJIbbriBSZMmMW7cOPbcc0+eeeYZZs+ezYQJE/jc5z7HmWeeyYMPPsjw4cP585//zEYbbbTc8kaNGsWuu+7KpZdeurTsySefZN68eeyxxx4AHH300Uvvv9rKddddx1577cULX/hC3v72t3PNNdewZMmSfuebMmUKU6ZMYaeddmLnnXfmnnvuWdp7OGrUKMaNGwfALrvswqxZs5ar35FHHrnM8jbffPOWu3xXhGenSpKkVWattdZirbXWIjO56qqrlrsbw3bbbcdrXvMafvjDH7LffvvxrW99i5122olnnnmm6fI++tGPcsghh/D6179+peo1efJkbr75ZkaOHAnA448/ztSpU3nDG97Qcr7M5LTTTuO9733vMuWzZs1i7bXXXvp8yJAhLFy4kMwkWpyc9swzzzB8+PDnvyIN7ImTJGk1s6p3qD4f++23H1/72tfIsoDbbrsNgPvvv5+XvvSlnHjiibzlLW/h9ttvZ+ONN2bJkiVNg9wrX/lKtt9+e6677joANtxwQzbeeGN+/vOfA3DxxRcv7fVaf/31mT9//nLLeOqpp5g2bRqzZ89m1qxZzJo1i7PPPpvJkycDMGzYMJ599tmmy9hvv/0477zzWLBgAQB//OMfeeyxx/pc74022ogNN9yQadOmAdWxfo1+//vfLz1bdWUZ4iRJ0ip3+umn8+yzzzJ27FjGjBnD6aefDsDll1/OmDFjGDduHPfccw9HHXUUAPvuu+/S4NPbxz72MebMmbP0+YUXXsgpp5zC2LFjmTlzJh//+McBOOaYY3jf+9633IkNV199NXvvvfcyPWcHHXQQ1157LYsWLWLixImMHTuWI444gk022YTdd9+dMWPGcMopp7Dvvvty+OGH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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = ['1st quarter', '2nd quarter', '3rd quarter', '4th quarter', '5th quarter']\n",
    "x = np.arange(len(labels))\n",
    "width = 0.35\n",
    "\n",
    "bar_value_1 = [first_quart_no_show_df['No'], second_quart_no_show_df['No'], third_quart_no_show_df['No'], fourth_quart_no_show_df['No'], fifth_quart_no_show_df['No']]\n",
    "bar_value_2 = [first_quart_no_show_df['Yes'], second_quart_no_show_df['Yes'], third_quart_no_show_df['Yes'], fourth_quart_no_show_df['Yes'], fifth_quart_no_show_df['Yes']]\n",
    "\n",
    "\n",
    "plt.subplots(figsize=(10,10));\n",
    "plt.bar(x-width/2, bar_value_1, width, color='red', label='No(Attend)');\n",
    "plt.bar(x+width/2, bar_value_2, width, color='blue', label='Yes(Not Attend)');\n",
    "\n",
    "plt.title('Percent of Patients\\' ages Attending and Not Attending the Appointment(No=Attend)');\n",
    "plt.xlabel('Ages');\n",
    "plt.ylabel('Attending / Missing Count');\n",
    "plt.xticks(x, labels);\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.groupby('age_quarter_names')['no_show'].value_counts().plot(kind='bar');"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can sum up these 2 bars plot to say:\n",
    ">-The number of Patients who attended the appointment is high in the first 75 years then became low for the following 50 years\n",
    ">\n",
    ">-The number of Patients who missed the appointment is high in the first 75 years then became low for the following 50 years\n",
    ">\n",
    ">-The number of patients above 75 years old is so little compared to whom below 75\n",
    ">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='q4'></a>\n",
    "### 4- Is the enrollment in Brasilian welfare program have an effect on attending the appointment?\n",
    "Here, I will discuss the no_show column as the dependent variable against scholarship as an independent variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "scholarship  no_show\n",
       "0            No         79924\n",
       "             Yes        19741\n",
       "1            No          8283\n",
       "             Yes         2578\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 262,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scholarship_no_show_df = df.groupby('scholarship')['no_show'].value_counts()\n",
    "scholarship_no_show_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "scholarship_no_show_df.plot(kind='bar');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "metadata": {},
   "outputs": [],
   "source": [
    "scholarship_no_show_df.rename(index={0:'Not Enrolled', 1:'Enrolled'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "scholarship   no_show\n",
       "Not Enrolled  No         79924\n",
       "              Yes        19741\n",
       "Enrolled      No          8283\n",
       "              Yes         2578\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 265,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scholarship_no_show_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no_show\n",
       "No     79924\n",
       "Yes    19741\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 266,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not_enrolled_no_show_df = scholarship_no_show_df['Not Enrolled']\n",
    "not_enrolled_no_show_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no_show\n",
       "No     8283\n",
       "Yes    2578\n",
       "Name: no_show, dtype: int64"
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "enrolled_no_show_df = scholarship_no_show_df['Enrolled']\n",
    "enrolled_no_show_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAxsAAAJcCAYAAACR9LmpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAABJF0lEQVR4nO3deZhcZZn38e9tAklkXwIvJEBQIgqIEVpARVCiAi6AiBpEwjoogoiDIOq8io6+4qCiOILCMGwDApMBQUcUB0RkCGCiyM4QWTMghNWIgCTe7x/n6XC6Ut3pTvqkujvfz3XVVVXP2Z6z1vmdrSIzkSRJkqTB9rJOV0CSJEnSyGTYkCRJktQIw4YkSZKkRhg2JEmSJDXCsCFJkiSpEYYNSZIkSY1Y4cNGRIyLiB9HxDMR8e8ND+v7EfF/mxzGUBIRkyIiI2J0+X5NRBy6lP3qtduI+FxE/Muy1HV5qNezzbS5IiIO6GwN22tT1/Uj4tqImB8R3+x0/VZUrfNlOImIjSLivojYtL5uR8R+EXFlp+s3WCLi/oh4e/k8XLZTZ0fEVzpdj6GkU/MxIt4aEXOXx7CaNNz3fSJifETcHRFjO12XTmtZF46KiBP7090Sw0bp8XMR8eeIeDQizoqIVZe1woMlIk6IiH9bhl7sA6wPrJOZH+il/y+W8X86Iq6PiDf2o14HRsR19bLM/Fhm/uMy1LW730u9ASrd/q2MT/21xHEaqjLz/2Xm0oaYsyPir2UazI+I2RGx82DXEfquZ2bunpnnNDHcBhwGPA6snpnHdLoyw9nyXP4GUKeMiGdr24anGxjMGcAnMvO+emFmnp+Z71yWHpdtdkbEdi3li+1E1384m7Ys26mhovyuZUQc21I+NyLe2o/u+/3btSLOxzK+mzXR79ow3lqGc1yTw6kbyL5PJ8NuHwdwjgfOysznS3vXRMTzEbFRrdu3R8T9DdVrSK4LwOnARyJivSW12N8zG+/NzFWBbYA3AP8wkNpEZaieRdkE+J/MXNBHOxeV8R8PXAdcEhGxXGrXjIczc9WW18yB9mQ4HlHtxT+V+bsGcBrV/B3VrsURNM7LYhPgjlyKfwRtevoNZv+X43ar38vfcvS62rZhzcHscURsDJybmT8ZzP6WfgewP/AkMCTPFI4ATwKfiYjVmxqA87FRB+B07beIGEM1rVoPaj8LNH62ZiivCyV8XQFM70/Lfb6A+4G3176fBPykfN4BuB54Gvg98NZae9cAXwX+G3gO2AzYEvgF1UR7FPhcafdlVMnxD8ATwMXA2qXZJCCpJvKDVEdUP1+a7Qb8FXgR+DPw+17G4TWlPk8DtwN7lPIvtXR/SJtuTwD+rfZ9y1KfdWt1ng/cAbyvNrzngYWlv0+X8rOBr9T69R7g5lKv64GtW6b7p4FbgGeAi4CxwCplev6t9PvPwIbAdsAs4E9l2n6rl2nxVmBuH/P7GuAfy3ybD1wJrNsyLw4p8+LaMu/+AXgAeAw4F1ijpf3RtX4fWhvWwcCdwFPAz4FNas3eAdxVxv2fgV/Vu+1tHtHH8tJLt63z5OWl+w3L9wPLtDiZarn9CvBK4GqqZfVx4HxgzVo/PgP8b5l+dwNT+6jnYtOmH/1vu2z0Mn4PANuWzx8pw9yifD8U+NEA1sHRZXq9SLXe/Bl4O9WyN5NqOX6kzK+Va3VI4AjgHuC+JS37bcYhgaOAe8v0OAl4WR/zZw2q5XBeGf9/qLU/Cvhm6c99wJFt5kPrdusgquV0fqnDR1vXJ+A4quX/EWAv4F3A/5Q6fW4Zlr+BrF8HlvrNL+O2X3+Wp16m92YtZf1ZJo+lWiafBc6kOmN8RanPfwFr9WPZPxC4rtbf7wAPUW3XZgNv6a3epf2dynz7SKnryqX8MHoutz8GzqPajj5Xyo7r5+9a2+1jab5/mVdPAJ+n9vvJALZTwDjgHKpt451Uy1df2+1ep1MZ7sVUy858qt/Arlrz1wO/Lc0uAi6ktky2DOdAqgNuPwa+WCuf2z2dgDHAt4GHy+vbpaztb5fzcVG715Z+PVvG40O8tH05hpe2LwfVuhkDfKMM+1Hg+8C4PpaTl5fxnVamYX056B6Xw8p8ewQ4pmU5mlGWkfllmXldrXnb/azW7Vxf49Ru/g50+7Is875Mx+Sl5fONVMvinJbpeA3wxdL9ZqXs7cD9/ZkeA3kxhNeF0nw/4JdLHI9+jOiiHgMblYn2j8CEMvB3Uf0gvqN8H18bgQepds5HA6uVheoYqp3m1YDtS7tHAzcAE6lWnh8AP2xZAc6gWnFfB7wAvKZ1xe+l/isBc4DPASsDu5QJunk/u1/UvNTtJOCh8v0DVDv6L6PaMDwLbFDfKLf062xeWuG2oVrRtqfaATqgTOsxtel+U+n/2lQbqo/VV9aWfs8E9i+fVwV26GV8Fuu2zUr0B+BVZXpfA5zYMi/OpfrhGEcVGOYAryjDvQQ4r6X9djsVe5XuXkO1fPwDcH1pti7Vj+Y+Zf59CljAwMJG2+WlTbf1eTIK+BjVDtuo2nxcAHyi1HMc1Q7oO8ryMJ7qR+Lbpf3NqX70N6zV55V91LPdtOm1/0taNtqM37mUHwyqU55/AA6vNfvUANbB0a3TrHzflmpjNrq0eydwdK15Uh1kWLtMvz6X/TbjkMAvS/cbU+3EH9rH/DkXuIxqGzOptH9Iaf9jVAcGJgJrUf1Itc6H+nZrJeDdVDvbAewM/AXYprY+LQC+UNr9O6qQc0EZ/pZUBx5esZTLX7/WL6r18U+8tF3bANiyP8tTL9O7NWz0Z5m8gWoHYEKZv7+l2pEdQxVUvtiPZf9AeoaNjwDrlHE8BvgjvQTr0v6ZVDvWK1H9Hu3dblq31Lv+w9mf37Xeto9bUP3A71TG+Vtl2ehrJ7W337UTqQ6wrEW1rN5C39vtXqdTGe7zZZxGAV8DbijNVqbakfhUmWb7UO3ALClsTKHacek+IFEPG18uy8J6VMvK9cA/9uf3x/nYc93jpe3Ll8u0eBfV9qc7uH8buJxq27ga1Q7n1/ro//5U+2GjSrun1Jp1j8sPqbYnr6XaltXH+0Ve+l3+NNVBjZVY8n7WonnWj3Hqbf72d/uyLPO+exqMrg37COA/W+pzDdXBum/VloVFYaMf0+N4qvWn7Wu4rAulnW2AJ5e4Tvdjpb+/DOxpqo3SqaVCn6H86NXa/TlwQG0Evlxrti/wu16GcSfl6G/5vgHVQt2985LAxFrzm4BprSt+L/1+C9WG92W1sh8CJ/Sz+xOokuPTVAv41ZQjxW3avRnYM2sb5ZbmixYMqssl/rGl+d3AzrXp/pFas38Cvl9bWVvDxrVUZ2rW7W1cat3+jcUX8FVq8+0fau1/HPhZy4r4ilrzq4CP175v3mbetdupuILamSSqleAvVJfoTKf8GJZmQfVjNpCw0XZ5adPt2VQ/xE+X9+cpR4Rr8/HBJUzTvSjLNtVO2WNUG56V+lHPtmd9euv/kpaNNt0eAlxeW88OBS4s3x/gpZ3m/qyDbcNGm2EeDVxa+57ALrXvfS77bfqXwG4ty+RV7eYP1Y/oC5SzN6Xso8A15fPV9Dwz8fY28+HLvY1baedHwCdr69NzvBQOViv9277W/mxgr6Vc/vq1flHtHDwNvJ8+jmy2W556md5/4qVtwylL6gfVMlmv938Ap9W+f4KXzqK1Lk/X0EvYaDPcp6gdTW1p9vJS773K9x8Al7VM6yX9MPfnd6237eMXKOtW+b4K1W9HXzupvf2u3QvsWmt2KP3YSW83ncpw/6vWbAvgufJ5J6qj2FFrfn3rdKo1WzR/qHaAvl4+18PGH4B31brZlZd2wt66pPFYkecj7cPGc/Tc+X2M6uBOUB3gfGWt2RspZ4976f9/8dKBsX2pwsRKLePy6lr7/wScWRvv+u/yy6iCy1tY8n7WonnW1zgtYf72d/uyLPO+exrU6/b5+vJQ68ehVGH6GaqDSvWw0ef0GMB6PKTXhVI2GVi4pHHp7/XIe2Xmmpm5SWZ+PDOfo9op/EC5afrpchPhjlQ7Kd0eqn3eiGoj1M4mwKW1/txJdQnS+rV2/lj7/Beqo3z9sSHVmYi/1coeoEp7/XVxGf/1MnOXzJwNEBHTI+LmWr23ojoq3x+bAMe0TL+NSn27DWScD6FKpndFxG8i4j19tPtwGZ/669kBDLc+Xzekmp7dHqDa+Vmfvm0CfKc27k9SbTwnlH4uGkZWS/RD7XrSh4FMu29kdV36OKALOCkidq817zHsiFgvIi6MiP+NiD9RXcu5bqnrHKqd7ROAx0p79Xm6RH31fynG71fAWyLi/1DtiF8EvDkiJlFdbnRzaa8/62Bv9X1VRPwkIv5Y6vv/2tS3Pg37s+y3qnf/QEu79Wbr8tLR2nr73ev7hi3tt1uuWuf37hFxQ0Q8Wer6LnqO3xOZubB8fq68P1pr/hxLv/z1a/0q6++HqM6MPBIR/xkRry7178/y1Gqb2rbhqH72o3WcBzIN2oqIYyLizqieFvg01TLbW93fR3XU7afl+/nA7hExfgCD7M/vWm/rXut261mqI4h96Ve/WML2rx/TqXU4Y8v9TRsC/1u2sd3qy1tfvgAcXrYtde2W2YFsA1fY+diLJ7LnPaXd/R9PtTM6uzaOPyvliyk3M7+NanpCdfZ3LNWZ27p+bWvLPtXc0nyg+1m9jVNf+rt9WZZ5385TVAeRFpOZ86guG/5yS6PB2O+E4bEurEYVuPq0LDc/PkSVluo7rKtkZv0xWNnS/iv76NfuLf0am5n/24965BKaPwxs1HKj58ZU19QvtYjYhOrU6ZFUT7JaE7iNaoe5P/V6CPhqyzi/PDN/2I/BL9bvzLwnM/elOnX9dWBGRKzSz9EZqPrwH6ZamLttTLVyPErfHqI6wlwf/3GZeT3V0ZL6Ux6i/r0pWbmN6trF+ga4dXp/rZRtnZmrU13CsOiBAZl5QWbuSDVdkmp+DESf/R+IEn7+QnXPw7WZOZ9qw3IY1RHK7o3hsqyDp1HdXzO51Pdzberbui0Y6LJfn/8bUy137fr9ONWR/9Zlsns8HqG6nKFdfxfrX7k58D+orotev6znP2Up50dfeln++r1+ZebPM/MdVD8id1Ftn2BwlqdBWyb7KyLeQnVU7oNUl1isSfWj1ttwD6D6kXwwIv4I/DvVpQf7lubttsmtZf35XetN63br5VSXNi2N/iyn3cMZ6HRqHc6ElgeebNyfCmbmXVSX9X2upVG7ZbZ7fV3S7yKsoPNxKTxOtZO9ZW0c18jqYRPt7E+1z/fjMl3vpQobrTf39rWtrU+Xl1GNW/e9OYO1n9WfZaQvyzLv2w37FqoDub05iSrEbVsr63N6RPX45NYngi561boZDuvCa6juA+nTsoSNfwPeGxG7RsSoiBgb1SPVJvbS/k+A/xMRR0fEmIhYLSK2L82+D3y17MB3P9N4z37W41FgUvT+1JgbqU41HhcRK0X1eL73Ut0EtyxWoZqp8wAi4iCqMxv1ek2MiJV76f4M4GMRsX1UVomId0dE2wTd4lFgnYhYo7sgIj4SEePLzuPTpXhhu44H2Q+BT0X1vPxVqY5qX5R9P90Lqnn+2YjYEiAi1oiI7kcP/yewZUTsXY6+HQW0Hj1rRDkavCPVvUm9WY1yaWFETKC6ca27+80jYpeyk/o81Y/BQOdDr/1fSr+iCsW/Kt+vafkOy7YOrkZ1qvfPZfodvoT2l2bZPzYi1ipH5z5JdYZmMeUMw8VlXFYr4/P3vPQkkYuBT0bEhIhYk2onrS8rU12rOg9YENUZh2V6NGtf2ix//Vq/ovrvkz3KAYYXqJaf7uVuMJanwV4m+zvMBVTTfnREfAFo+wSkUqepVA8emFJer6MK+geU1h6luvelrrVsoL9rdTOA90TEjmW7/2WW/jf2Yqrt41pl3I7so91+T6c2ZpZuj4qI0RGxN9UDH/rrS1QPUFizVvZD4B/KNmRdqjMg3evfYr9ddSv4fIT249ZW+a0/Azg5yqNHy3Zt1146mU41v6bUXu8H3h0R9R3I/xsRLy+/zQfRc1u7be13+Wiqbc0NDO5+Vr+nQS+WZd7Po7rMvD78m4A1y/xbTGY+TfXQkfqjhPucHlk9Prn1iaCLXjCs1oWdqS6L79NSh43MfAjYk+qoxjyq9HRsb/0sR1TfQTXB/0j1ZJq3lcbfobrJ6cqImE+18G7frj9tdP8R3xMR8ds2w/0rsAewO9WRgFOB6eWozFLLzDuoFrCZVDP3tVRHJLtdTbXD8MeIeLxN97Oobib9Z6rTdHOoroftz7Dvotqg3xvVabENqZ7MdXtUqfg7VNeMPt9LLzaMxdP0+/sz7Db+leoJCNdS3Sz2PNX1k0sah0upVpoLo7os4zaqeURmPk518/2JVKfsJtNz2g6248o0eJbqSQxnUV0b2ZsvUd0U9QxVMLqk1mwMVb0fp1rO12PxI39L0lf/l8avqHZIru3lOyzbOvhp4MNUN8CdQS9BoNtSLvuXUd37cDPVNDmzj3Y/QbWhv5fqZtYLqJZTSv2upDpa9TuqsxQL6CUQlu3WUVQ7DU9RjeflS6jrQPW1/PV3/XoZ1Y3BD1Ndkrgz1bW3MDjL02Avk/3xc6ofsf+hugTheXq/DGV/4ObMvDIz/9j9Ak4Bto6IraiWmS3KNvNHpbuvUe0YPx0Rnx7o71pdZt5OdTPpBVRHBJ+iusxkaXy5dHsf1XX2M6h27NoZyHRqrfNfgb2p1r+nqC7F6/e8zep/Us6jOvjW7StUT0a8BbiV6kber5T22/121a3I8xGqy2/PKePxwX70/zNU288byu/of1Hd19VDROxAdT/C9+rTNTMvL93vW2v9V6XsKqpLPK+sNbuMahl5impe7Z2ZLw7yfla7+dtvyzjv/0J5GmEZ/g5l3M6mOpvbm+9Q+w0ZpOkx5NeFqP7k8F1UT1zrU2SPSzUlaWiJiKS6RGtOA/3enerm+k2W2LLUIRFxONUBpJ07XRctvaE8H6O6j+8+qhvGF7syISJOoLp5va+d7hEpqnskfg28Pqt7lgVExCeAjTJziX8QuSyXUUnSsBIR4yLiXeWSkQlUz0q/tNP1kuoiYoOIeHNEvCwiNqc6a+VyOsw4H0eGzJyXma82aPSUmd/tT9AAw4akFUtQXRL0FNVlVHdSXVMuDSUrU11KN5/qktzLqC7F0PDifJTwMipJkiRJDfHMhiRJkqRGjO50BdScddddNydNmtTpakiSJC3R7NmzH8/MgfxpnYYBw8YINmnSJGbNmtXpakiSJC1RRPT3H+w1jHgZlSRJkqRGGDYkSZIkNcKwIUmSJKkR3rMhSZJWGC+++CJz587l+eef73RVVlhjx45l4sSJrLTSSp2uipYDw4YkSVphzJ07l9VWW41JkyYREZ2uzgonM3niiSeYO3cum266aaero+XAy6gkSdIK4/nnn2edddYxaHRIRLDOOut4ZmkFYtiQJEkrFINGZzn9VyyGDUmSJEmNMGxIkqQVV8Tgvvo1yOCYY45Z9P0b3/gGJ5xwQp/d/OhHP+KOO+5o2+yEE05gwoQJTJkyZdHr6aef7u8U6NOqq64KwP33389WW201oG4PPPBAZsyYMSj10PBl2JAkSVqOxowZwyWXXMLjjz/e7276ChsAn/rUp7j55psXvdZcc81+93vhwoX9blcaKMOGJEnScjR69GgOO+wwTj755MWaPfDAA0ydOpWtt96aqVOn8uCDD3L99ddz+eWXc+yxxzJlyhT+8Ic/9Gs4Z599NnvvvTe77bYbkydP5rjjjlvUbNVVV+ULX/gC22+/PTNnzuRb3/oWW221FVtttRXf/va3++zvwoULOfbYY3nDG97A1ltvzQ9+8AOgetLUkUceyRZbbMG73/1uHnvssf5PFI1Yhg1JkqTl7IgjjuD888/nmWee6VF+5JFHMn36dG655Rb2228/jjrqKN70pjexxx57cNJJJ3HzzTfzyle+crH+nXzyyYsuoXrb2962qPzmm2/moosu4tZbb+Wiiy7ioYceAuDZZ59lq6224sYbb2TcuHGcddZZ3Hjjjdxwww2cccYZ/O53v+u17meeeSZrrLEGv/nNb/jNb37DGWecwX333cell17K3Xffza233soZZ5zB9ddfP0hTS8OZYUOSJGk5W3311Zk+fTqnnHJKj/KZM2fy4Q9/GID999+f6667rl/9q19G9ctf/nJR+dSpU1ljjTUYO3YsW2yxBQ888AAAo0aN4v3vfz8A1113He973/tYZZVVWHXVVdl777359a9/3euwrrzySs4991ymTJnC9ttvzxNPPME999zDtddey7777suoUaPYcMMN2WWXXQY0TTQy+ad+kiRJHXD00UezzTbbcNBBB/XazrI+JnbMmDGLPo8aNYoFCxYA1b94jxo1CqgufxqI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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = ['No(Attend)', 'Yes(Not Attend)']\n",
    "x = np.arange(len(labels))\n",
    "width = 0.35\n",
    "\n",
    "bar_value_1 = not_enrolled_no_show_df \n",
    "bar_value_2 = enrolled_no_show_df\n",
    "\n",
    "plt.subplots(figsize=(10,10));\n",
    "plt.bar(x-width/2, bar_value_1, width, color='red', label='Not Enrolled');\n",
    "plt.bar(x+width/2, bar_value_2, width, color='blue', label='Enrolled');\n",
    "\n",
    "plt.title('Percent of Patients Enrolled in Brasilian welfare program Bolsa Família Attending and Not Attending the Appointment(No=Attend)');\n",
    "plt.xlabel('No-Show');\n",
    "plt.ylabel('Attending / Missing Count');\n",
    "plt.xticks(x, labels);\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can sum up these 2 bars plot to say:\n",
    ">-The number of patients who did not enroll in Brasilian welfare program and attended the appointment is larger than whom did not enroll and attended \n",
    ">\n",
    ">-The number of patients who enroll in Brasilian welfare program and attended the appointment is larger than whom enrolled and attended \n",
    ">\n",
    ">-The scholarship has not a impressive effect to push the patients to attend the appointment\n",
    ">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Limitations\n",
    "1- There are some unlogic values such like \n",
    "    <ul>\n",
    "        <li>age < 0 as I considered age = zero is a new baby</li>\n",
    "        <li>handicap of value > 1 so I returned these values to be 1 </li>\n",
    "    </ul>\n",
    "\n",
    "2- Missing features that may be useful to assure what is the most feature that impacts showing to the appointment such like\n",
    "    <ul>\n",
    "        <li>whether the patient is employeed or not</li>\n",
    "        <li>the distance from the patient location to the hospital location</li>\n",
    "    </ul>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='conclusions'></a>\n",
    "## Conclusions\n",
    ">-The majority of patients are below 60 years and number of patients decreases after 60\n",
    ">\n",
    ">-The majority of patients are not included in Brasilian welfare program (Bolsa Família)\n",
    ">\n",
    ">-The majority of patients are not suffering from hypertension, diabetes, alcoholism nor handicap\n",
    ">\n",
    ">-The higher percent of patients did not recieve a SMS to inform them about the appointment\n",
    ">\n",
    ">-The higher percent of patients is females \n",
    ">\n",
    ">-The higher percent of patients had appointments in 'JARDIM CAMBURI' with (\\~7% of whole appointments) then 'MARIA ORTIZ' with (\\~5.25% of whole appointments)\n",
    ">\n",
    ">-The higher percent of patients are Females \n",
    ">\n",
    ">-Females are the more like to attend the appointment\n",
    ">\n",
    ">-Females are the more like to miss the appointment also \n",
    ">\n",
    ">-The number of Patients who attended the appointment is high in the first 75 years then became low for the following 50 years\n",
    ">\n",
    ">-The number of Patients who missed the appointment is high in the first 75 years then became low for the following 50 years\n",
    ">\n",
    ">-The number of patients above 75 years old is so little compared to whom below 75\n",
    ">\n",
    ">-The number of patients who did not enroll in Brasilian welfare program and attended the appointment is larger than whom did not enroll and attended \n",
    ">\n",
    ">-The number of patients who enroll in Brasilian welfare program and attended the appointment is larger than whom enrolled and attended \n",
    ">\n",
    ">-The scholarship has not a impressive effect to push the patients to attend the appointment\n",
    ">"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
