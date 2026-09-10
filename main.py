##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# 4. Send the letter generated in step 3 to that person's email address.
def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=f"{birthday['email']}",
                                msg=f"Subject: Happy Birthday\n\n{content_txt}")


# 1. Update the birthdays.csv
birthdays_df = pd.read_csv("birthdays.csv")
birthday_dict= birthdays_df.to_dict("records")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
today = (now.month, now.day)

for birthday in birthday_dict:
    birthday_date = (birthday["month"], birthday["day"])
    if today == birthday_date:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as file:
            content_list = file.readlines()
            content_txt = "".join(content_list)
            content_txt = content_txt.replace("[NAME]", birthday["name"])
        with open(f"letter_templates/letter_to_send.txt", "w") as file:
            file.write(content_txt)
        send_email()





