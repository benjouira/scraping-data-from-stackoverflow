# read the read me file first
from bs4 import BeautifulSoup
import requests

# base url
url = "https://stackoverflow.com/questions"
page_Limit = 1000 #number of page you want to scrapy from 1 to 1000

def build_url(base_url = url , tab="newest", page = 1):
    # page 2 url exemple 
    # https://stackoverflow.com/questions?tab=newest&page=2
    return f"{base_url}?tab={tab}&page={page}"

def scrape_page(page=1):
    # Function to scrape a single page in stacoverflow
    response = requests.get(build_url(page=page))
    page_questions = []
    soup = BeautifulSoup(response.text,"html.parser")
    question_summary = soup.find_all("div", class_="question-summary")

    for summary in question_summary:
        question = summary.find(class_="question-hyperlink").text
        a = summary.find(class_="question-hyperlink", href = True)
        # print (a["href"])
        question_url = a["href"]
        vote_count = summary.find(class_="vote-count-post").find("strong").text 
        answers_count = summary.find(class_="status").find("strong").text 
        views_count = summary.find(class_="views").text.split()[0] 
        page_questions.append(
            {
                "question" : question,
                "question_url" : question_url,
                "answers" : answers_count,
                "views" : views_count,
                "votes" : vote_count

            }
        )
    return page_questions

def scrape():
    # Functio to scrape to page_limit
    questions = []
    for i in range(1,page_Limit+1):
        page_questions = scrape_page (i)
        questions.extend(page_questions)
    return questions

def export_data():
    data = scrape()
    print (type(data))
    with open("questions.csv", "w") as data_file:
        fieldnames = ["question","question_url","answers","views","votes"]
        data_writer = csv.DictWriter(data_file, fieldnames=fieldnames)
        data_writer.writeheader()
        for d in data:
            data_writer.writerow(d)
        print("Done")

if __name__ == "__main__":
    export_data()

    
