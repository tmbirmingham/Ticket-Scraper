# Ticket Scraper Demo

This is a **demo Selenium scraper** that extracts ticket information from a local HTML file (`index.html`) and saves it to a CSV file (`tickets_output.csv`).  

**Note:** This is a slightly altered version of a scraper originally used for an internal ticketing system. All sensitive information has been removed, and it uses **dummy ticket data** only.

---

## How It Works

1. The scraper loops through ticket IDs and treats each row in `index.html` as a new ticket.
2. For each ticket, it extracts the following fields:
   - Ticket ID
   - User
   - Technician
   - Date Submitted
   - Summary
   - Urgency
3. All tickets are saved into a CSV file (`tickets_output.csv`) for easy viewing and analysis.

The main logic flow is:

- Open the `index.html` file in a browser via Selenium.
- Loop through all ticket rows.
- For each row, create a ticket object (dictionary) and collect the relevant fields.
- Append each ticket to a list.
- Save the list of tickets to `tickets_output.csv`.

## Files in this Repo

- `index.html` — Dummy ticket data in table format  
- `scraper.py` — Selenium scraper script  
- `requirements.txt` — Python dependencies
- `tickets_output.csv` — Sample output from script


---

## Notes

- This project is safe to run locally.  
- You can expand `index.html` with more dummy tickets for testing.  
- This demo preserves the original logic flow but uses only non-sensitive, sample data.
- The version of your Chrome browser and the ChromeDriver will need to be the same version number in order for the script to work.
