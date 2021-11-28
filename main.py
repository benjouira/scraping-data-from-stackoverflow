# read the read me file first
from bs4 import BeautifulSoup
import requests

url = "https://stackoverflow.com/questions"
page_Limit = 1

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

def answers (question_url):
    full_url =  "https://stackoverflow.com"+question_url

if __name__ == "__main__":
    print(scrape())
    # scrape()
