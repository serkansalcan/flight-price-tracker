import requests
import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def get_lowest_prices(origin, destination, currency, user_country, months):
    lowest_prices = {'direct_price': float('inf'), 'indirect_price': float('inf')}
    lowest_dates = {'direct_date': '', 'indirect_date': ''}

    base_url = "https://www.skyscanner.net/g/monthviewservice/{}/{}/en-US/calendar/{}/{}/{}"
    query_params = {"profile": "minimalmonthviewgridv2"}
    headers = {
        "authority": "www.skyscanner.net",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,tr;q=0.8",
        "sec-fetch-site": "same-origin"
    }

    for month in months:
        url = base_url.format(user_country, currency, origin, destination, month)
        response = requests.get(url, headers=headers, params=query_params)
        response.raise_for_status()
        response_json = response.json()

        days_prices = response_json.get("PriceGrids", {}).get("Grid", [])[0]

        for index, day_price in enumerate(days_prices):
            direct_price = day_price.get("Direct", {}).get("Price", float('inf'))
            indirect_price = day_price.get("Indirect", {}).get("Price", float('inf'))

            if direct_price < lowest_prices['direct_price']:
                lowest_prices['direct_price'] = direct_price
                lowest_dates['direct_date'] = f"{month}-{index + 1}"

            if indirect_price < lowest_prices['indirect_price']:
                lowest_prices['indirect_price'] = indirect_price
                lowest_dates['indirect_date'] = f"{month}-{index + 1}"

    return lowest_prices, lowest_dates


def load_lowest_prices_from_csv():
    lowest_prices = {'direct_price': float('inf'), 'indirect_price': float('inf')}
    if os.path.isfile('lowest_prices.csv'):
        with open('lowest_prices.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                direct_price_str = row['direct_price']
                indirect_price_str = row['indirect_price']

                if direct_price_str and indirect_price_str:
                    lowest_prices['direct_price'] = float(direct_price_str)
                    lowest_prices['indirect_price'] = float(indirect_price_str)
    return lowest_prices


def save_lowest_prices_to_csv(lowest_prices):
    fieldnames = ['direct_price', 'indirect_price']
    with open('lowest_prices.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            'direct_price': lowest_prices['direct_price'],
            'indirect_price': lowest_prices['indirect_price']
        })


def send_email(subject, message):
    sender_email = "email1@gmail.com"
    sender_password = ""

    recipient_email = "email2@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
        smtp_server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", str(e))


if __name__ == "__main__":
    origin = "ISTA"
    destination = "KULM"
    currency = "USD"
    user_country = "TR"
    months = ["2023-10", "2023-11", "2023-12", "2024-01", "2024-02", "2024-03"]

    stored_lowest_prices = load_lowest_prices_from_csv()
    lowest_prices, lowest_dates = get_lowest_prices(origin, destination, currency, user_country, months)

    for flight_type in ['direct', 'indirect']:
        price_key = f'{flight_type}_price'
        date_key = f'{flight_type}_date'

        if lowest_prices[price_key] < stored_lowest_prices[price_key]:
            price_drop = stored_lowest_prices[price_key] - lowest_prices[price_key]
            if stored_lowest_prices[price_key] == float('inf'):
                subject = f"{flight_type.capitalize()} Flight Alert"
                message = f"{flight_type.capitalize()} Flight: {lowest_dates[date_key]}, price: ${lowest_prices[price_key]}"
            else:
                subject = f"{flight_type.capitalize()} Flight Price Drop Alert"
                message = f"{flight_type.capitalize()} Flight: ${price_drop} drop, {lowest_dates[date_key]}, price: ${lowest_prices[price_key]}"

            send_email(subject, message)
            stored_lowest_prices[price_key] = lowest_prices[price_key]

    save_lowest_prices_to_csv(stored_lowest_prices)


