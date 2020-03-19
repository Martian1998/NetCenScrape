import requests
from bs4 import BeautifulSoup 
import os 
def main():
    print("always use python3 to run the crawler")
    """ creates a list to keep hold of the links
    that are to be followed, and then invokes
    crawler with the first link """
    linkRecord = list()
    linkCheck = []
    linkRecord.append("")
    linkCheck.append("False")
    url = "http://www.syedfaaizhussain.com/"
    name = url[14:-5]
    crawler(linkRecord, 0, url, linkCheck, name)

def crawler(links, index, url, linkCheck, name):
    """ gets the html from the specified link and also 
    modifies the links to achieve the goal of getting
    the complete site """
    if linkCheck[index]==True:
        return
    print (links[index] + "=========>" + str(index))
    if name in links[index]:
        toCallUrl = links[index]
    else: 
        toCallUrl = url+links[index]
    response = requests.get(toCallUrl)
    linkCheck[index] = True
    with open(str(index)+".html",'wb') as fb:
        fb.write(response.content)
    soup = BeautifulSoup(response.text, 'lxml')
    newLinks=[]
    for child in soup.descendants:
        if child.name == "a":
            newLinks.append(child)
    for link in newLinks:
        if not link.has_attr("href"):
            continue
        link = link['href']
        if (not link in links) and (not "http" in link or name in link) and (not "mailto" in link) and (not "www" in link or name in link) and (not "javascript" in link) and (not "pdf" in link) and (not "jpg" in link) and (not "png" in link) and (not "gif" in link):
            links.append(link)
            linkCheck.append(False)
    for i in range(index+1, len(links)):
        index=index+1
        crawler(links,index, url,linkCheck, name)

if __name__ == "__main__":
    main()