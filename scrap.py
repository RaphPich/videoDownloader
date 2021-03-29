from sys import argv
import requests
from bs4 import BeautifulSoup
import pytube

if len(argv)==1:
	print("Please enter url")
	exit()

url = argv[1]
print("Starting with :",url)


youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download()