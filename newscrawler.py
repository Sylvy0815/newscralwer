import requests
from bs4 import BeautifulSoup
import csv

def scrape_news():
    # URL of the website to be scraped
    url = 'https://media.naver.com/press/023/ranking?type=popular'

    # Send a request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 뉴스 목록을 찾아서 추출
    news_list = soup.select('.press_ranking_list li')

    # 추출된 데이터를 저장할 CSV 파일 생성
    with open('news.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Title'])

        # 각 뉴스 항목에 대해 순위와 제목 추출
        for news in news_list:
            rank = news.select_one('.list_ranking_num').text.strip()
            title = news.select_one('.list_title').text.strip().replace(',', ' ')
            writer.writerow([rank, title])

    print("뉴스 데이터가 news.csv 파일에 저장되었습니다.")

    # # Find the news list in the HTML
    # news_list = soup.select('.press_ranking_list li')

    # # Create or open a CSV file to store the news
    # with open('news.csv', 'w', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Rank", "Title"])

    #     # Extract and write rank and title for each news item
    #     for news in news_list:
    #         rank = news.select_one('.num_rank').text.strip()
    #         title = news.select_one('.list_title').text.strip().replace(',', ' ')
    #         writer.writerow([rank, title])

    # print("Scraping completed and data saved to news.csv")

# Run the function
scrape_news()


