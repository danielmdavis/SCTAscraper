# SCTAscraper
_Chromedriver, Selenium &amp; Flask for Python. Logs you in with your Oracle SSO, scrapes the SCTA UI and passes a json through a pseudo-API. Milage may vary with the whims of SCTA._

To run this app you must first run chromedriver. Run chromedriver by double-clicking and it will handle browser execution from there.

SCTAscraper is built in Python 3. `brew install` python and `pip install` selenium and flask.

The scraping in handled from `sctaScraper.py` and the server is handled from `endpoint.py`. 

Put a valid SSO into the place marked in `sctaScraper.py` and a valid PW into the file called `secret.txt`.

From the application folder, `python endpoint.py` to launch flask. By default it serves to `localhost:5000`.

The terminal will alert you when the session has been spun up and credentialled fully. At that point you should be able to navigate to the endpoint in your browser, triggering a scrape and returning the json data.

