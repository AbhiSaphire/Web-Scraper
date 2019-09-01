import os, requests
from bs4 import BeautifulSoup


def download(n):
	print ("Function running")
	links = clist[n].find("div", {"class": "d-links"})
	downpagelink = links.find("a", {"class": "downnow"})["href"]
	downres = requests.get(str(downpagelink))
	downsoup = BeautifulSoup(downres.text, "html.parser")
	c2 = downsoup.find("div", {"class": "col-sm-9 col-md-7 col-xs-12"})
	downlink = c2.find("a")["href"]
	songname = downsoup.find("h1", {"class": "title"}).text.replace("Download", "").replace("Mp3", "").strip()
	response = requests.get(str(downlink))
	print("Downloading song...please wait for some time (depending on your internet speed)")
	try:
	    with open(songname + ".mp3", 'wb') as f:
	        f.write(response.content)
	        print("Done downloading!")
	except:
	    print("ERROR! maybe there is a problem with your internet connection or the site is down.")

def listener(n):
	print("Working")


if __name__ == "__main__":
	os.chdir("/home/abhishek/Downloads")
	r = requests.get("https://mp3download.center/")
	baseurl = str(r.url)
	name = str(input("Enter the song name: "))
	name = name.replace(" ", "%20").lower()
	searchpage = requests.get(baseurl + "mp3/" + name)
	clist = []
	searchsoup = BeautifulSoup(searchpage.text, "html.parser")
	c = searchsoup.find("div", {"class": "media-body"})
	if c is None:
		print("query not found!")
	else:
		for i in range(5):
			print(str(i + 1) + ") " + str(c.text.strip().replace("play", "").replace("download", "")))
			clist.append(c)
			c = c.findNext("div", {"class": "media-body"})
			if c is None:
			    break
		n = int(input("Enter song number from the list: "))
		n = n - 1
		option = int(input("Press 1 to download the song, press 2 to listen the song :"))
		if option == 1:
			download(n)
		elif option == 2:
			listener(n)
