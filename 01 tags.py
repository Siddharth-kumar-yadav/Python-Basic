import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())    
#print(soup.title.string, type(soup.title.string))
#print(soup.find_all('div')[1])

#for link in soup.find_all("a"):
#    print(link)

# for link in soup.find_all("a"):
#     print(link.get("herf"))
#     print(link.get_text())

# s = soup.find(id="link3")
# print(s.get("herf")) 
# print(s.get_text()) 

# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
#print(soup.span.get("class"))

# print(soup.find(class_="italic"))
# for child in soup.find(class_="container").children:
#     print(child)
# i =0
# for parent in soup.find(class_="box").parents:
#     i +=1
#     print(parent)
#     if(i==2):
#         break

# cont = soup.find(class_="container")
# cont.name="span"
# cont["class"]="myclass class2"
# cont.string="I am a String"
# print(cont)

ulTag = soup.new_string("ul")

liTag = soup.new_string("li")
liTag.string="Home"
ulTag.append(liTag)

liTag = soup.new_string("li")
liTag.string="About"
ulTag.append(liTag)

soup.html.body.insert(0, ulTag)
with open("modified.html","w") as f:
    f.write(str(soup))