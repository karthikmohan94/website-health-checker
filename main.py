import requests
import time
from datetime import datetime
import csv


def check_website(url):
    
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\nChecking {url}...")

    try:
        start_time = time.perf_counter()

        response = requests.get(url, timeout=5)

        end_time = time.perf_counter()

        response_time = round(end_time - start_time, 2)
        status_code = response.status_code

        if 200 <= status_code < 400:
            status = "ONLINE"
        else:
            status = "PROBLEM"

        print("\n----- RESULT -----")
        print("Website:", url)
        print("Status:", status)
        print("HTTP Status Code:", status_code)
        print("Response Time:", response_time, "seconds")

        save_result(
            url,
            status,
            status_code,
            response_time
        )

    except requests.RequestException as error:
        print("\n----- RESULT -----")
        print("Website:", url)
        print("Status: OFFLINE")
        print("Error:", error)

        save_result(
            url,
            "OFFLINE",
            "N/A",
            "N/A"
        )


def save_result(url, status, status_code, response_time):
    checked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("results.csv", "a+", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        file.seek(0)

        if file.read() == "":
            writer.writerow([
                "Checked At",
                "Website",
                "Status",
                "HTTP Status Code",
                "Response Time"
            ])

        writer.writerow([
            checked_at,
            url,
            status,
            status_code,
            response_time
        ])

def main():
    print("==============================")
    print("     WEBSITE HEALTH CHECKER")
    print("==============================")

    websites = input(
        "\nEnter website URLs separated by commas: "
    )

    if not websites.strip():
        print("No website URL entered.")
        return

    website_list = websites.split(",")

    for url in website_list:
        url = url.strip()

        if url:
            check_website(url)

    print("\nResults saved to results.csv")

if __name__ == "__main__":
    main()