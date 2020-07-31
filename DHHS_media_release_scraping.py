from bs4 import BeautifulSoup
import requests
import csv
#datetime to calc dates
from datetime import timedelta,date

#url="https://www.dhhs.vic.gov.au/coronavirus-update-victoria-26-july-2020"

#url stub
urlstub="https://www.dhhs.vic.gov.au/coronavirus-update-victoria-"

#create date deltas
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

#first date active cases listed
#start_dt = date(2020,6,28)
#end_dt = date(2020,6,30)
#date script run
start_dt = date(2020,5,7)
end_dt = date(2020,7,30)

csvfile = open('I:\output.csv', 'w',newline='')
csvfile.truncate(0)

for dt in daterange(start_dt, end_dt):
    urldate = dt.strftime("%d-%B-%Y")
    if urldate == "16-May-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-16-may"
    elif urldate == "30-May-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-saturday-30-may-2020"
    elif urldate == "01-June-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-1-june-2020"
    elif urldate == "08-June-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-8-june-2020"
    elif urldate == "09-June-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-9-june-2020"
    elif urldate == "10-June-2020":
        url = "https://www.dhhs.vic.gov.au/media-release-coronavirus-update-victoria-wednesday-10-june"
    elif urldate == "21-June-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-21-june"
    elif urldate == "01-July-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-1-july-2020"
    elif urldate == "02-July-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-2-july-2020"
    elif urldate == "04-July-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-4-july-2020"
    elif urldate == "09-July-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-9-july-2020"
    elif urldate == "12-July-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-sunday-12-july"
    elif urldate == "15-July-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-wednesday-15-july"
    elif urldate == "16-July-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-thursday-16-july-2020"
    elif urldate == "19-July-2020":
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-19-july"
    else:    
        url = "https://www.dhhs.vic.gov.au/coronavirus-update-victoria-"+urldate
    html_content = requests.get(url).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    lga_table = []
    lga_table = soup.findAll("table")[0]

    output_rows = []
    for table_row in lga_table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = [dt.strftime("%Y-%m-%d")]
        for column in columns:
            output_row.append(column.text.replace('\n', '').replace(u'\xa0', '').replace('\u202f', ''))
        output_rows.append(output_row)

    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

csvfile.close()
