from WorldBankScraper import WorldBankScraper

if __name__ == '__main__':
    base_url = 'https://ieg.worldbankgroup.org/data'
    scraper = WorldBankScraper(base_url)
    data = scraper.scrape_data()
    scraper.save_to_csv(data, 'world_bank_data.csv')
