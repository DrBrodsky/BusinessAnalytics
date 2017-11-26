from lxml import html
import requests
import csv

# data extraction example from movie title: the a-team
with open('movieLinks.txt', 'r') as f:
    read = csv.reader(f, delimiter = ",")
    for line in read:
        lines = line

def remove_brackets(list):
    return (list or [None])[0]

with open("extract.csv","w") as p:
    keys = ["Domestic Total Gross","Genre","Production Budget","MPAA Rating","Distributor","Release Date","Title","Foreign","OpeningWeekend","WidestRelease","CloseDate","In Release"]
    writer = csv.DictWriter(p, keys)
    writer.writeheader()
    for row in lines:
        try:
            clean = row[2:-1]
            url = "http://www.boxofficemojo.com" + clean
            page = requests.get(url)
            tree = html.fromstring(page.text.replace("&nbsp;", ""))

            data = {}
            print(url)
            # Domestic Total Gross
            data["Domestic Total Gross"] = remove_brackets(tree.xpath('//*[@id="body"]//font[starts-with(normalize-space(.),"Domestic Total Gross:")]/b/text()'))
            # Genre
            data["Genre"] = remove_brackets(tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"Genre:")]/b/text()'))
            # Production Budget
            data["Production Budget"] = remove_brackets(tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"Production Budget:")]/b/text()'))
            # MPAA Rating
            data["MPAA Rating"] = remove_brackets(tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"MPAA Rating:")]/b/text()'))
            # Distributor
            data["Distributor"] = remove_brackets(tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"Distributor:")]/b/a/text()'))
            # Release Date
            data["Release Date"] = remove_brackets(tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"Release Date:")]/b/nobr/a/text()'))
            # Movie Title
            data["Title"] = remove_brackets(tree.xpath('/html/head/title/text()'))

            # Work around &nbsp; issue

            # Foreign Box Office
            data["Foreign"] = remove_brackets(tree.xpath('//*[@class="mp_box_content"]//a[starts-with(normalize-space(.),"Foreign:")]/../following-sibling::*[1][name()="td"]/text()'))
            # Opening Weekend
            data["OpeningWeekend"] = remove_brackets(tree.xpath('//*[@class="mp_box_content"]//a[starts-with(normalize-space(.),"OpeningWeekend:")]/../following-sibling::*/text()'))
            # Widest Release
            data["WidestRelease"] = remove_brackets(tree.xpath('//*[@class="mp_box_content"]//td[starts-with(normalize-space(.),"WidestRelease:")]/following-sibling::*/text()'))
            # Close Date
            data["CloseDate"] = remove_brackets(tree.xpath('//*[@class="mp_box_content"]//td[starts-with(normalize-space(.),"CloseDate:")]/following-sibling::*/text()'))
            # In Release
            data["In Release"] = remove_brackets(tree.xpath('//*[@class="mp_box_content"]//td[starts-with(normalize-space(.),"In Release:")]/following-sibling::*/text()'))

            print(data["Title"])
            #save everything into csv file
            writer.writerow(data)
        except Exception as inst:
            print(inst)
            with open("errorlog.txt", "a") as errorfile:
                errorfile.write(url, inst)
        
