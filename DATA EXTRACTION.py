# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 09:27:30 2022

@author: user
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
from requests import get


#url = 'https://www.imdb.com/title/tt2442560/episodes/?ref_=tt_ov_epl'

#movie_data= requests.get(url)

#soup= BeautifulSoup(movie_data.text, 'html.parser')

# Initializing the series that the loop will populate
community_episodes = []

# For every season in the series-- range depends on the show
for sn in range(6):
    # Request from the server the content of the web page by using get(), and store the server’s response in the variable response
    response = get('https://www.imdb.com/title/tt2442560/episodes/?ref_=' + str(sn))

    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(response.text, 'html.parser')

    # Select all the episode containers from the season's page
    episode_containers = page_html.find_all('div', class_ = 'info')

    # For each episode in each season
    for episodes in episode_containers:
            # Get the info of each episode on the page
            season = sn
            episode_number = episodes.meta['content']
            title = episodes.a['title']
            airdate = episodes.find('div', class_='airdate').text.strip()
            rating = episodes.find('span', class_='ipl-rating-star__rating').text
            total_votes = episodes.find('span', class_='ipl-rating-star__total-votes').text
            desc = episodes.find('div', class_='item_description').text.strip()
            # Compiling the episode info
            episode_data = [season, episode_number, title, airdate, rating, total_votes, desc]

            # Append the episode info to the complete dataset
            community_episodes.append(episode_data)
            
#import pandas as pd 
community_episodes = pd.DataFrame(community_episodes, columns = ['season', 'episode_number', 'title', 'airdate', 'rating', 'total_votes', 'desc'])

community_episodes.head(8)

community_episodes.to_excel('Peaky_blinders_ep_reviews_.xlsx')
