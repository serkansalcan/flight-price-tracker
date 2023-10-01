<h1>Flight Price Tracker</h1>

<p>Flight Price Tracker is a Python script that helps you monitor and receive alerts for the lowest prices of direct and indirect flights between specified destinations.</p>

<h2>Features</h2>

<ul>
  <li>Track and compare the lowest prices of direct and indirect flights.</li>
  <li>Receive email alerts for price drops.</li>
  <li>Supports multiple months to search for flight deals.</li>
</ul>

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>Required Python packages: requests, csv, os, smtplib</li>
</ul>

<h2>Usage</h2>

<ol>
  <li>Clone the repository or download the script.</li>
  <li>Install the required dependencies</code></li>
  <li>Modify the script variables to set the origin and destination airports, currency, user country, and desired months.</li>
  <li>Run the script: <code>python price-tracker.py</code></li>
  <li>The script will check for the lowest flight prices and send email alerts for any price drops.</li>
</ol>

<h2>Configuration</h2>

<ul>
  <li><code>origin</code>: The code for the airport of origin.</li>
  <li><code>destination</code>: The code for the airport of destination.</li>
  <li><code>currency</code>: The currency in which the flight prices are displayed (e.g., USD, EUR).</li>
  <li><code>user_country</code>: The country code for the user's country (for local deals).</li>
  <li><code>months</code>: A list of months (in YYYY-MM format) for which to search for flight deals.</li>
  <li>Additionally, you should configure the email settings in the send_email function with your sender's email address and password, as well as the recipient's email address.</li>
</ul>
