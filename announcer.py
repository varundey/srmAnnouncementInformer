#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import requests
from gi.repository import Notify as nt

no_of_notifs = 2

icon  = "/home/varun/Desktop/git/srmAnnouncementInformer/assets/srmuniv_icon.png"
url = "http://www.srmuniv.ac.in/Announcements"

def get_soup(url):
	main_class = "col-lg-12 col-xs-12 col-md-12 col-sm-12 margin-top-20px responsive-top news-border padding-0px"
	soup = bs(requests.get(url, headers={'User-Agent':'Mozilla/5.0'} ).content, "lxml")
	soup = soup.findAll("div",{"class":main_class})
	return soup

def take_n(n, soup):
	for i in range(n):
		get_date(soup[i])

def get_date(soup):
	date = soup.find("div",{"class":"latest-month"}).text.strip()
	get_head(soup, date)

def get_head(soup, date):
	heading = soup.find("h4").text
	notify(date, heading)

def notify(date, heading):
	nt.init("App Name")
	nt.Notification.new(date, heading, icon).show()

if __name__ == "__main__":
	soup = get_soup(url)
	take_n(no_of_notifs, soup)