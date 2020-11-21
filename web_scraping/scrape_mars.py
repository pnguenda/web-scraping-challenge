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
#     article = soup.find("div", class_="list_text")
    news_paragraph = soup.find('div', class_ = 'rollover_description_inner').text.strip()
    news_title = soup.find('div', class_ = 'content_title').text.strip()
#     news_date = article.find("div", class_="list_date").text.strip()
  
    # Add the news date, title and summary to the dictionary
#     mars_data["news_date"] = news_date
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_paragraph
    
    # JPL Mars Space Images - Featured Image

    driver.visit(img_url)
    img_html = driver.html
    img_soup = bs(img_html, "html.parser")
   

    feature_img = img_soup.find('article',attrs={'class':'carousel_item'})
    feature_img_url_string = feature_img['style']
    featured_image_link = re.findall(r"'(.*?)'",feature_img_url_string)
    featured_image_url = 'https://www.jpl.nasa.gov'+ featured_image_link[0]

    mars_data['featured_img_url'] = featured_image_url
    
    # Mars Facts
#     driver.visit(mars_facts_url)
    mars_facts_df = pd.read_html(mars_facts_url)
    mars_facts_table_df = mars_facts_df[0]
    mars_facts_table_df.columns = ['Description','Value']
    mars_facts_table_df.set_index('Description',inplace=True)
    
    mars_facts_html =  mars_facts_table_df.to_html()

    mars_data['facts'] = mars_facts_html
    
    
    # Mars Hemispheres
    driver.visit(mars_hemi_url)
    mars_hemi_html = driver.html
    mars_hemi_soup = bs(mars_hemi_html, "html.parser")
    mars_hemi_url = mars_hemi_soup.find_all('div', class_='item')
    titles=[]
    hemi_img_urls=[]
    
    for img in mars_hemi_url:
        title = img.find('h3').text
        url = img.find('a')['href']
        hemi_img_urls = 'https://astrogeology.usgs.gov' + mars_hemi_url
        img_data = dict({'title':title, 'img_url':hemi_img_urls})
        mars_hemi_img.append(img_data)
        
    mars_data['hemi_img'] = mars_hemi_img
    
    
    browser.quit()
    return mars_data
    