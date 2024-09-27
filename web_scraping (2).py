import requests
import csv
from bs4 import BeautifulSoup

date = input("enter hte date for your match .")

page_contant = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#")

def info(page_contant):

    match_Details =[]

    surace = page_contant.content
    soup = BeautifulSoup(surace, "lxml")
    championships = soup.find_all("div", {'class':'matchCard'})
    
    # create a funcyion to get the info of all matches
    def get_match_title(championships):
        campionship_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.find_all("div", {'class':'item future liItem'})
        number_of_matches = len(all_matches)
        for i in range(number_of_matches):
            # get the names of teams
            team_A = all_matches[i].find("div", {'class':'teamA'}).text.strip()
            team_B = all_matches[i].find("div", {'class':'teamB'}).text.strip()

            # get score of the match
            m_Result = all_matches[i].find("div",{'class':'MResult'}).find_all("span", {'class':'score'})
            score = f"{m_Result[0].text.strip()} - {m_Result[1].text.strip()}"
            
            # get time of match
            time_match = all_matches[i].find("div", {'class':'MResult'}).find("span", {'class':'time'}).text.strip()
            
           #get the Date of match
            date_of_match = all_matches[i].find("div", {'class':'date'}).text.strip()

            # get he state of match
            statu_of_match = all_matches[i].find("div", {'class':'matchStatus'}).text.strip()
            match_Details.append({ "campionship_title": campionship_title,
                                "team_A": team_A,
                                "team_B": team_B,
                                "time_match": time_match,
                                "score": score,
                                "Date": date_of_match,
                                "status_of_match": statu_of_match })
    
    for j in range(len(championships)):
        get_match_title(championships[j])
    
    key = match_Details[0].keys()

    with open("E:\python.project\match_info.csv", "w", encoding="UTF-8") as output_file :
        dict_writer = csv.DictWriter(output_file, key)
        dict_writer.writeheader()
        dict_writer.writerows(match_Details)
        print("file created")

info(page_contant)




