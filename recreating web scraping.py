import requests
from bs4 import BeautifulSoup
oyo_url="https://www.oyorooms.com/hotels-in-banglore/"
req=requests.get(oyo_url)
content=req.content
soup=BeautifulSoup(content,"html.parser")
all_hotels=soup.find_all("div",{"class": "hotelcard_listing"})
for hotel in all_hotels:
        hotel_name=hotel.find("h3",{"class":"listinghoteldescription_hotelname"}).text
        hotel_address=hotel.find("span",{"itemprop":"streetaddress"}).text
        hotel_price=hotel.find("span",{"class":"listingprice_finalprice"}).text
        hotel_rating=hotel.find("span",{"class":"hotelrating_ratingsummary"}).text
print(hotel_name,hotel_address,hotel_price,hotel_rating)
         
