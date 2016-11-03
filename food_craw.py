import bs4
import requests
from food import Food

#get hmtl from the website
link = "http://list25.com/25-worlds-spiciest-foods"
response = requests.get(link)

# parse html
soup = bs4.BeautifulSoup(response.content,"html.parser")

# craw img & desc
container_tag = soup.find("div", attrs= {"class":"list-entry"})
print(container_tag)

# food_tags = container_tag.find_all("div", attrs = {"class":"buzz_superlist_item"})
#
# for food in food_tags:
#     img = food.div.div.img["src"]
#     name = food.div.h2.string
#     desc = food.div.div.p.get_text()
#     print(img, name, desc)
#     #Food(name = name, img = img, desc = desc).save()



