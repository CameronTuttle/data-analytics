{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup \n",
    "import time\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    # @NOTE: Replace the path with your actual path to the chromedriver\n",
    "    executable_path = {\"executable_path\": \"C:\\\\Users\\\\CAMTUT\\\\Downloads\\\\chromedriver\"}\n",
    "    return Browser(\"chrome\", **executable_path, headless=False)\n",
    "\n",
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    \n",
    "    url = \"https://mars.nasa.gov/news/\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    content = {}\n",
    "   \n",
    "    level = soup.find(\"div\",class_=\"list_text\")\n",
    "\n",
    "    content[\"title\"]= level.find(\"div\",class_=\"content_title\").get_text()\n",
    "    content[\"teaser\"]= level.find(\"div\",class_=\"article_teaser_body\").get_text()\n",
    "\n",
    "    print(content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'title': 'After a Reset, Curiosity Is Operating Normally', 'teaser': 'Curiosity has returned to science operations and is once again exploring the clay unit. '}\n"
     ]
    }
   ],
   "source": [
    "scrape()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    \n",
    "    url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "\n",
    "    browser.find_by_id(\"full_image\").click()\n",
    "    time.sleep(3)\n",
    "    browser.find_link_by_partial_text(\"more info\").click()\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    carousel_items = soup.find(\"img\",class_=\"main_image\").get(\"src\")\n",
    "    featured_image_url = \"https://www.jpl.nasa.gov/\"+str(carousel_items)\n",
    "    \n",
    "    print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov//spaceimages/images/largesize/PIA01384_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "scrape()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    \n",
    "    url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    mars_weather = soup.find(\"div\",class_=\"js-tweet-text-container\").find(\"p\",\"tweet-text\").get_text()\n",
    "    \n",
    "    print(mars_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 92 (2019-03-01) low -94.4ºC (-137.9ºF) high -12.9ºC (8.8ºF)\n",
      "winds from the SW at 4.6 m/s (10.2 mph) gusting to 10.4 m/s (23.2 mph)\n",
      "pressure at 7.20 hPapic.twitter.com/zxXhRFOwTo\n"
     ]
    }
   ],
   "source": [
    "scrape()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\n",
      "Equatorial Diameter:6,792 km\n",
      "\n",
      "\n",
      "\n",
      "Polar Diameter:6,752 km\n",
      "\n",
      "\n",
      "\n",
      "Mass:6.42 x 10^23 kg (10.7% Earth)\n",
      "\n",
      "\n",
      "Moons:2 (Phobos & Deimos)\n",
      "\n",
      "\n",
      "Orbit Distance:227,943,824 km (1.52 AU)\n",
      "\n",
      "\n",
      "Orbit Period:687 days (1.9 years)\n",
      "\n",
      "\n",
      "\n",
      "Surface Temperature: -153 to 20 °C\n",
      "\n",
      "\n",
      "First Record:2nd millennium BC\n",
      "\n",
      "\n",
      "Recorded By:Egyptian astronomers\n",
      "\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    \n",
    "    url = \"https://space-facts.com/mars/\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    mars_facts = soup.find(\"table\",class_=\"tablepress tablepress-id-mars\").get_text()\n",
    "    \n",
    "    print(mars_facts)\n",
    "    \n",
    "scrape()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]\n"
     ]
    }
   ],
   "source": [
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    \n",
    "    url = \"https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    hemisphere_image_urls = []\n",
    "    \n",
    "    title = soup.find(\"h2\",class_=\"title\").get_text()\n",
    "    \n",
    "    url = \"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    image = soup.find(\"img\").get(\"src\")\n",
    "    dictionary= {\"title\":title,\"img_url\":image}\n",
    "    hemisphere_image_urls.append(dictionary)\n",
    "    #print(hemisphere_image_urls)\n",
    "    \n",
    "    #----------------------------------------------------------------------------------------\n",
    "    \n",
    "    url = \"https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    title = soup.find(\"h2\",class_=\"title\").get_text()\n",
    "    #hemisphere_image_urls[\"title\"]=title\n",
    "    \n",
    "    url = \"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    image = soup.find(\"img\").get(\"src\")\n",
    "    dictionary= {\"title\":title,\"img_url\":image}\n",
    "    hemisphere_image_urls.append(dictionary)\n",
    "    #print(hemisphere_image_urls)\n",
    "    \n",
    "  #----------------------------------------------------------------------------------------\n",
    "    \n",
    "    url = \"https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    title = soup.find(\"h2\",class_=\"title\").get_text()\n",
    "    #hemisphere_image_urls[\"title\"]=title\n",
    "    \n",
    "    url = \"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    image = soup.find(\"img\").get(\"src\")\n",
    "    dictionary= {\"title\":title,\"img_url\":image}\n",
    "    hemisphere_image_urls.append(dictionary)\n",
    "    #print(hemisphere_image_urls)\n",
    "    \n",
    "  #----------------------------------------------------------------------------------------\n",
    "    \n",
    "    url = \"https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    title = soup.find(\"h2\",class_=\"title\").get_text()\n",
    "    #hemisphere_image_urls[\"title\"]=title\n",
    "    \n",
    "    url = \"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html,\"html.parser\")\n",
    "    \n",
    "    image = soup.find(\"img\").get(\"src\")\n",
    "    dictionary= {\"title\":title,\"img_url\":image}\n",
    "    hemisphere_image_urls.append(dictionary)\n",
    "    print(hemisphere_image_urls)\n",
    "scrape()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
