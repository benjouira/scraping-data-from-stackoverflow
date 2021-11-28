# scraping-data-from-stackoverflow
scraping questions and answers from stackoverflow

first you need to install BeautifulSoup library , run this command on cmd :
pip install Beautifulsoup4 requests

************
base url 
https://stackoverflow.com/questions

we notice that the url of second page is this
https://stackoverflow.com/questions?tab=newest&page=2
=> we have two parametre tab and page,
=> every page has almost 15 questions

we notice also that the base url can be like this
https://stackoverflow.com/questions?tab=newest&page=1

