import requests
import csv


def get_best_flight_deals(origin, destination, currency, user_country, months):
    best_deals = []

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
        response_json = response.json()

        days_prices = response_json["PriceGrids"]["Grid"][0]
        for index, day_price in enumerate(days_prices):
            direct_price = day_price.get("Direct", {}).get("Price", "N/A")
            indirect_price = day_price.get("Indirect", {}).get("Price", "N/A")
            data = {
                "month": month,
                "day": index + 1,
                "best_direct_price": direct_price,
                "best_indirect_price": indirect_price
            }
            best_deals.append(data)

    return best_deals


def save_best_deals_to_csv(best_deals, filename):
    field_names = ["month", "day", "best_direct_price", "best_indirect_price"]
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(best_deals)


if __name__ == "__main__":
    origin = "ISTA"
    destination = "KULM"
    currency = "USD"
    user_country = "TR"
    months = ["2023-07", "2023-08", "2023-09", "2023-10", "2023-11", "2023-12"]

    best_deals = get_best_flight_deals(origin, destination, currency, user_country, months)
    save_best_deals_to_csv(best_deals, "best_flight_deals.csv")
