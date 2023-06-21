<h1>Flight Deals Scraper</h1>

<p>This project is a Python script that retrieves the best flight deals between two airports using the Skyscanner API. It fetches the prices for direct and indirect flights for a given set of months and saves the results in a CSV file.</p>

<h2>Features</h2>

<ul>
  <li>Retrieves the best flight deals between specified origin and destination airports.</li>
  <li>Supports multiple months to search for flight deals.</li>
  <li>Fetches prices for both direct and indirect flights.</li>
  <li>Saves the results in a CSV file for further analysis.</li>
</ul>

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>Requests library (<code>pip install requests</code>)</li>
</ul>

<h2>Usage</h2>

<ol>
  <li>Clone the repository or download the script.</li>
  <li>Install the required dependencies using pip: <code>pip install requests</code></li>
  <li>Modify the script variables to set the origin and destination airports, currency, user country, and desired months.</li>
  <li>Run the script: <code>python flight_deals.py</code></li>
  <li>The script will retrieve the flight deals and save the results in a CSV file named <code>best_flight_deals.csv</code>.</li>
</ol>

<h2>Configuration</h2>

<ul>
  <li><code>origin</code>: The code for the airport of origin.</li>
  <li><code>destination</code>: The code for the airport of destination.</li>
  <li><code>currency</code>: The currency in which the flight prices are displayed (e.g., USD, EUR).</li>
  <li><code>user_country</code>: The country code for the user's country (used for local deals and information).</li>
  <li><code>months</code>: A list of months (in YYYY-MM format) for which to search for flight deals.</li>
</ul>

<h2>Output</h2>

<p>The script outputs the best flight deals for the specified origin, destination, and months in a CSV file named <code>best_flight_deals.csv</code>. The file contains the following columns:</p>

<ul>
  <li><code>month</code>: The month for which the flight deals are retrieved.</li>
  <li><code>day</code>: The day of the month.</li>
  <li><code>best_direct_price</code>: The best price for a direct flight on that day (or "N/A" if not available).</li>
  <li><code>best_indirect_price</code>: The best price for an indirect flight on that day (or "N/A" if not available).</li>
</ul>
