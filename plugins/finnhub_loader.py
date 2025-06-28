import finnhub


def scrape_news():
    finnhub_client = finnhub.Client(api_key="cpt14cpr01qpk40rpj7gcpt14cpr01qpk40rpj80")

    news = finnhub_client.general_news('general', min_id=0)

    return news
