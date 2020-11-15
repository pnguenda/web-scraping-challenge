# Dependencies
import time
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "/Users/paulenguendang/Downloads/chromedriver 2"}
    driver = Browser("chrome", **executable_path, headless=False)


def scrape():
    driver = init_browser()


    # A dict for all of the scraped data
    mars_data = {}

    # Visit the Mars news page. 
    url = "https://mars.nasa.gov/news/"
    driver.visit(url)
 

    # Search for news
    # Scrape page into soup
    html = driver.html
    soup = bs(html, 'html.parser')

    # Find the latest Mars news.
    article = soup.find("div", class_="list_text")
    news_paragraph = soup.find('div', class_ = 'rollover_description_inner').text.strip()
    news_title = soup.find('div', class_ = 'content_title').text.strip()
    news_date = article.find("div", class_="list_date").text.strip()
  
    # Add the news date, title and summary to the dictionary
    mars_data["news_date"] = news_date
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_paragraph