import datetime as dt
import pandas
import random
import smtplib

EMAIL = 'deepam@gmail.com'   #use your own email
PASSWORD = 'deepam'

data = pandas.read_csv("birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row.day): data_row for (index, data_row) in data.iterrows()

}

current_date = dt.datetime.now()
month = current_date.month
day = current_date.day
today = (month, day)

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    print(birthday_person)
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person['email'],
            msg=f"Happy Birthday!\n\n {contents}"
        )
