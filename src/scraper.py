import cloudscraper


def scrape(url):
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    return response.text
