<h1>Flight Price Tracker</h1>

<p>Flight Price Tracker is a Python script that helps you monitor and receive alerts for the lowest prices of direct and indirect flights between specified destinations.</p>

<h2>Features</h2>

<ul>
  <li>Fetches flight prices from Skyscanner for a given route and set of months.</li>
  <li>Monitors both direct and indirect flight prices.</li>
  <li>Sends email alerts when price drops are detected.</li>
  <li>Logs execution and error messages for easy troubleshooting.</li>
  
</ul>

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>Required Python packages installed. You can install them using `pip install -r requirements.txt`</li>
  <li>A SendGrid API key for sending email alerts. Set it as an environment variable named `SENDGRID_API_KEY`.</li>
  <li>Configuration of sender and recipient email addresses in the script.</li>
</ul>

<h2>Usage</h2>

<ol>
  <li>Clone the repository or download the script.</li>
  <li>Install the required dependencies</li>
  <li>Set your SendGrid API key as an environment variable named `SENDGRID_API_KEY`</li>
  <li>Configure sender and recipient email addresses in the script</li>
  <li>Modify the script variables to set the origin and destination airports, currency, user country, and desired months.</li>
  Obtain the codes for the origin and destination airports from the Skyscanner after performing a search in the website. These codes can be found in the URL.
  <li>Run the script: <code>python price-tracker.py</code></li>
  <li>The script will check for the lowest flight prices and send email alerts for any price drops. It will also log its execution in a file named 'flight_price_tracker.log'.</li>
</ol>

<h2>Scheduled Execution (Optional)</h2>

<p>For continuous tracking, consider running the script on a cloud server using a cron job or similar scheduling mechanism.
