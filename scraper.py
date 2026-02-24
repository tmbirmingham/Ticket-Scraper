from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import csv
import time

chromedriver_path = os.path.abspath("chromedriver-mac-x64/chromedriver")
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Open your local HTML file
file_path = os.path.abspath("index.html")
driver.get(f"file:///{file_path}")

time.sleep(2)

data = []

try:
    # Loop over ticket rows in table
    rows = driver.find_elements(By.CSS_SELECTOR, "#tickets tbody tr")
    print(f"Found {len(rows)} tickets.")

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) == 6:
            ticket_info = {
                "Ticket ID": cols[0].text.strip(),
                "User": cols[1].text.strip(),
                "Technician": cols[2].text.strip(),
                "Date Submitted": cols[3].text.strip(),
                "Summary": cols[4].text.strip(),
                "Urgency": cols[5].text.strip(),
            }
            data.append(ticket_info)

except Exception as e:
    print(f"Error scraping tickets: {e}")

# Save to CSV
if data:
    keys = data[0].keys()
    with open("tickets_output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Scraping complete. Saved {len(data)} tickets to tickets_output.csv")

driver.quit()