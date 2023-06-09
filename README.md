# Warsaw Housing Price Distribution Analysis

This script analyzes the distribution of housing prices in Warsaw, Poland by scraping data from the otodom.pl website. It performs a normality test on the collected prices and visualizes the distribution using a histogram.

## Prerequisites
Before running the script, make sure you have the following dependencies installed:
```python
BeautifulSoup
Requests
Pandas
Matplotlib
SciPy
```

You can install the required dependencies using the following command:
```python
pip install beautifulsoup4 requests pandas matplotlib scipy
```
## Usage
- Run the script using Python.
The script will scrape housing price data from the otodom.pl website for the first 10 pages.
It will extract the price and area information for each listing.
A summary of the collected data will be displayed, including count, mean, standard deviation, minimum, quartiles, and maximum values.
The script will generate a histogram showing the distribution of prices in different price ranges.
Finally, a normality test will be performed using the Shapiro-Wilk test, and the test statistic and p-value will be displayed.
## Conclusion
Based on the analysis, the p-value obtained from the normality test is less than 0.05, indicating that the distribution of housing prices on the first 10 pages of the otodom.pl website is not normally distributed. Therefore, we reject the null hypothesis (H0) and conclude that the housing prices in Warsaw do not follow a normal distribution.

Please note that the analysis is limited to the data collected from the specific web pages scraped and may not represent the entire housing market in Warsaw.




