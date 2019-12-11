import requests, csv, time
from bs4 import BeautifulSoup

timestr = time.strftime("%Y%m%d")
URL1 = "https://sfbay.craigslist.org/search/sby/apa?"
resp1 = requests.get(URL1)
resp1.encoding = 'utf-8'
webpage1 = resp1.content
soup1 = BeautifulSoup(webpage1, "html.parser")

with open('Craistlist_SFBayArea%s.csv'%timestr, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    writer.writerow(["Website"] + ["Title"] + ["Price"] + ["BedroomSqFt"] + ["Bed"] + ["SquareFoot"] +["City"])

    TotalRentCount = 0

    for onerent in soup1.select('body > section > form > div > ul > li > p'):
        TotalRentCount += 1

        Website = onerent.select('a')[0]['href']
        Title = onerent.select('a')[0].text
        Price = onerent.select('span > span')[1].text
        BedroomFt = onerent.select('span > span')[2].text.replace(" ","").replace('-','/').replace('\n','').replace('ft2/','ft2').strip(' (').strip(')')
        Bed = BedroomFt.rstrip('/0123456789ft2')
        SquareFoot = BedroomFt.lstrip('0123456789').strip('br/')
        City = onerent.select('span > span')[3].text.strip(' (').strip(')')

        print(Website)
        print(Title)
        print(Price)
        print(BedroomFt)
        print(Bed)
        print(SquareFoot)
        print(City)
        writer.writerow([Website] + [Title] + [Price] + [BedroomFt] + [Bed] + [SquareFoot] + [City])
    print("TotalRentCount:", TotalRentCount)
######################################################################################

    # for onerent in soup1.select('body > section > form > div > ul > li'):
    #     TotalRentCount += 1
    #     for spantag in onerent.findAll("span", attrs={"class": "result-meta"}):
    #             #.select('p > span'):
    #         # .findAll("span", attrs={"class": "result-meta"}):
    #         # print(spantag)
    #
    #         Price = spantag.findAll("span", attrs={"class": "result-price"})
    #         BedroomFt = spantag.findAll("span", attrs={"class": "housing"})
    #         City = spantag.findAll("span", attrs={"class": "result-hood"})
    #
    #         print(Price)
    #         print(BedroomFt)
    #         print(City)

            # Price1 = str(Price)
            # Price2 = Price1.strip('[<span class="result-price">').strip('</span>]')
            # BedroomFt1 = str(BedroomFt)
            # BedroomFt2 = BedroomFt1.strip('[<spanclass="housing">').strip('<sup>2</sup> -').strip('                </span>]').replace(" ","")
            # City1 = str(City)
            # City2 = City1.strip('[<span class="result-hood"> ').strip('</span>]')
            #
            # print(Price2)
            # print(BedroomFt2)
            # print(City2)

    #     writer.writerow([Price] + [BedroomFt] + [City])
    # print("TotalRentCount:", TotalRentCount)
