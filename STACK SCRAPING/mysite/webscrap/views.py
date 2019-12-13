from django.shortcuts import render
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#For Scraping
import requests;
import bs4;
from datetime import date



# Create your views here.

#The Homepage Accessing View
def index(request) :
    return render(request, 'webscrap/home.html')

#Unifinished New Feature view
def latest(request) :
    return render(request, 'webscrap/latest.html')

#View for Newest
def newest(request) :
    import requests;
    from datetime import date
    import bs4;
    import datetime
    import time

    month_to_date = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9,
                     "Oct": 10, "Nov": 11, "Dec": 12}
    date_to_month = {value: key for key, value in month_to_date.items()}

    # print(date_to_month[3])
    class Date:
        def __init__(self, d, m, y):
            self.d = d
            self.m = m
            self.y = y

            # To store number of days in

    # all months from January to Dec.
    monthDays = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

    # This function counts number of
    # leap years before the given date
    def countLeapYears(d):

        years = d.y

        # Check if the current year needs
        # to be considered for the count
        # of leap years or not
        if (d.m <= 2):
            years -= 1

        # An year is a leap year if it is a
        # multiple of 4, multiple of 400 and
        # not a multiple of 100.
        return int(years / 4 - years / 100 +
                   years / 400)

    # This function returns number of
    # days between two given dates
    def getDifference(dt1, dt2):

        # COUNT TOTAL NUMBER OF DAYS
        # BEFORE FIRST DATE 'dt1'

        # initialize count using years and day
        n1 = dt1.y * 365 + dt1.d

        # Add days for months in given date
        for i in range(0, dt1.m - 1):
            n1 += monthDays[i]

            # Since every leap year is of 366 days,
        # Add a day for every leap year
        n1 += countLeapYears(dt1)

        # SIMILARLY, COUNT TOTAL NUMBER
        # OF DAYS BEFORE 'dt2'
        n2 = dt2.y * 365 + dt2.d
        for i in range(0, dt2.m - 1):
            n2 += monthDays[i]
        n2 += countLeapYears(dt2)

        # return difference between
        # two counts
        return (n2 - n1)

    date_time = (datetime.datetime.now() - datetime.timedelta(days=7)).date()
    mon = str(date_time)
    month = mon[5:7]
    day_org = mon[8:10]
    mn = int(month)
    month_org = date_to_month[mn]

    def checkNeg(s):
        for i in range(len(s)):
            if s[i] == '-':
                return -1

    pagenum = 0
    ques = []
    link = []
    votes = []

    over = 0

    while pagenum < 1000:
        pagenum += 1
        pageurl = "https://stackoverflow.com/search?page=" + str(pagenum) + "&tab=Newest&q=android%20features"
        res = requests.get(pageurl)  # Data from Stack Overflow

        soup = bs4.BeautifulSoup(res.text, 'html.parser')  # Building a lxml file from res.text

        # print(soup)
        # building the question and hyperlink arrays
        Count = 0
        question_ref = soup.select('.question-hyperlink')
        vote_ref = soup.select('.vote')
        time_ref = soup.select('.relativetime')

        for i in range(0, 15):
            qu = (question_ref[i].text)
            ques.append(qu.lstrip())
            link.append("https://www.stackoverflow.com" + question_ref[i].get('href'))
            strin = (vote_ref[i].text)
            if checkNeg(strin):
                votes.append(-1)
            else:
                vote = [int(s) for s in strin.split() if s.isdigit()]
                votes.append(vote[0])
            times = time_ref[i].text
            if not ("hour" in times or "yesterday" in times or "days" in times):
                mon_tar = times[:3]
                mon_tar = month_to_date[mon_tar]
                # print(mon)
                day_tar = times[4:]

                dt1 = Date(int(day_org), int(month_to_date[month_org]), 2019)
                dt2 = Date(int(day_tar), int(mon_tar), 2019)
                diff = getDifference(dt1, dt2)
                # print(diff)
                if diff < 0:
                    over = 1
                    break
        if over == 1:
            break
        time.sleep(3)

    most_recent_ques = ques[:10]
    most_recent_link = link[:10]

    return render(request, 'webscrap/newest.html', {'res' : zip(most_recent_link, most_recent_ques)})

#View for most voted
def voted(request):
    import requests;
    from datetime import date
    import bs4;
    import datetime
    import time

    month_to_date = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9,
                     "Oct": 10, "Nov": 11, "Dec": 12}
    date_to_month = {value: key for key, value in month_to_date.items()}

    # print(date_to_month[3])
    class Date:
        def __init__(self, d, m, y):
            self.d = d
            self.m = m
            self.y = y

            # To store number of days in

    # all months from January to Dec.
    monthDays = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

    # This function counts number of
    # leap years before the given date
    def countLeapYears(d):

        years = d.y

        # Check if the current year needs
        # to be considered for the count
        # of leap years or not
        if (d.m <= 2):
            years -= 1

        # An year is a leap year if it is a
        # multiple of 4, multiple of 400 and
        # not a multiple of 100.
        return int(years / 4 - years / 100 +
                   years / 400)

    # This function returns number of
    # days between two given dates
    def getDifference(dt1, dt2):

        # COUNT TOTAL NUMBER OF DAYS
        # BEFORE FIRST DATE 'dt1'

        # initialize count using years and day
        n1 = dt1.y * 365 + dt1.d

        # Add days for months in given date
        for i in range(0, dt1.m - 1):
            n1 += monthDays[i]

            # Since every leap year is of 366 days,
        # Add a day for every leap year
        n1 += countLeapYears(dt1)

        # SIMILARLY, COUNT TOTAL NUMBER
        # OF DAYS BEFORE 'dt2'
        n2 = dt2.y * 365 + dt2.d
        for i in range(0, dt2.m - 1):
            n2 += monthDays[i]
        n2 += countLeapYears(dt2)

        # return difference between
        # two counts
        return (n2 - n1)

    date_time = (datetime.datetime.now() - datetime.timedelta(days=7)).date()
    mon = str(date_time)
    month = mon[5:7]
    day_org = mon[8:10]
    mn = int(month)
    month_org = date_to_month[mn]

    def checkNeg(s):
        for i in range(len(s)):
            if s[i] == '-':
                return -1

    pagenum = 0
    ques = []
    link = []
    votes = []

    over = 0

    while pagenum < 1000:
        pagenum += 1
        pageurl = "https://stackoverflow.com/search?page=" + str(pagenum) + "&tab=Newest&q=android%20features"
        res = requests.get(pageurl)  # Data from Stack Overflow

        soup = bs4.BeautifulSoup(res.text, 'html.parser')  # Building a lxml file from res.text

        # print(soup)
        # building the question and hyperlink arrays
        Count = 0
        question_ref = soup.select('.question-hyperlink')
        vote_ref = soup.select('.vote')
        time_ref = soup.select('.relativetime')

        for i in range(0, 15):
            qu = (question_ref[i].text)
            ques.append(qu.lstrip())
            link.append("https://www.stackoverflow.com" + question_ref[i].get('href'))
            strin = (vote_ref[i].text)
            if checkNeg(strin):
                votes.append(-1)
            else:
                vote = [int(s) for s in strin.split() if s.isdigit()]
                votes.append(vote[0])
            times = time_ref[i].text
            if not ("hour" in times or "yesterday" in times or "days" in times):
                mon_tar = times[:3]
                mon_tar = month_to_date[mon_tar]
                # print(mon)
                day_tar = times[4:]

                dt1 = Date(int(day_org), int(month_to_date[month_org]), 2019)
                dt2 = Date(int(day_tar), int(mon_tar), 2019)
                diff = getDifference(dt1, dt2)
                # print(diff)
                if diff < 0:
                    over = 1
                    break
        if over == 1:
            break
        time.sleep(3)

    most_recent_ques = ques[:10]
    most_recent_link = link[:10]

    for i in range(len(votes)):
        for j in range(len(votes) - 1):
            if votes[j] < votes[j + 1]:
                votes[j], votes[j + 1] = votes[j + 1], votes[j]
                ques[j], ques[j + 1] = ques[j + 1], ques[j]
                link[j], link[j + 1] = link[j + 1], link[j]

    top_voted_ques = ques[:10]
    top_voted_link = link[:10]

    return render(request, 'webscrap/voted.html', {'res': zip(top_voted_link, top_voted_ques)})