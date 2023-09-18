import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import random

with open('/content/drive/MyDrive/[07] Colab Notebooks/Artificial Intelligence/categories.json') as f:
    data = json.load(f)


baseurl = "https://www.flipkart.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

total_dump = []
for h in range(0, 3):
    cats = data[h]["categories"]

    print(data[h]["type"])
    productdict = {}
    productdict["type"] = data[h]["type"]
    ite = []
    for i in range(0, len(cats)):
        subsubdict = {}
        print(cats[i]["category"])
        subsubdict["category"] = cats[i]["category"]
        print(cats[i]["subCategories"])
        productCats = cats[i]["subCategories"]
        item = []
        for j in range(1, len(productCats)):
            subdict = {}
            k = requests.get(
                'https://www.flipkart.com/search?q='+productCats[j-1]).text
            soup = BeautifulSoup(k, 'html.parser')
            productlist = soup.find_all("div", {"class": "_4ddWXP"})
            print(productCats[j-1])
            subdict["subCategory"] = productCats[j-1]
            items = []
            if (len(productlist) == 0):
                productlist = soup.find_all("div", {"class": "_2kHMtA"})
                for k in range(1, min(len(productlist), 30)):
                    dict = {}
                    if ((productlist[k-1].find("div", {"class": "_4rR01T"}) != None) & (productlist[k-1].find("div", {"class": "_30jeq3 _1_WHN1"}) != None)):
                        all_words = productlist[k].find(
                            "div", {"class": "_4rR01T"}).string.split()
                        dict['Brand'] = all_words[0]
                        dict['Name'] = productlist[k].find(
                            "div", {"class": "_4rR01T"}).string
                        print(
                            'Name: ' + productlist[k].find("div", {"class": "_4rR01T"}).string)
                        dict['Price'] = productlist[k].find(
                            "div", {"class": "_30jeq3 _1_WHN1"}).string
                        print(
                            'Price: ' + productlist[k].find("div", {"class": "_30jeq3 _1_WHN1"}).string)
                        dict['No of Reviews'] = random.randint(100, 2000)
                        dict['Rating'] = float(f'{random.uniform(3,4.9):.2f}')
                        items.append(dict)
            elif (len(productlist) == 0):
                productlist = soup.find_all("div", {"class": "_13oc-S"})
                for k in range(1, min(len(productlist), 30)):
                    dict = {}
                    if ((productlist[k-1].find("div", {"class": "_4rR01T"}) != None) & (productlist[k-1].find("div", {"class": "_30jeq3 _1_WHN1"}) != None)):
                        all_words = productlist[k].find(
                            "div", {"class": "_4rR01T"}).string.split()
                        dict['Brand'] = all_words[0]
                        dict['Name'] = productlist[k].find(
                            "div", {"class": "_4rR01T"}).string
                        print(
                            'Name: ' + productlist[k].find("div", {"class": "_4rR01T"}).string)
                        dict['Price'] = productlist[k].find(
                            "div", {"class": "_30jeq3 _1_WHN1"}).string
                        print(
                            'Price: ' + productlist[k].find("div", {"class": "_30jeq3 _1_WHN1"}).string)
                        dict['No of Reviews'] = random.randint(100, 2000)
                        dict['Rating'] = float(f'{random.uniform(3,4.9):.2f}')
                        items.append(dict)
            else:
                for k in range(1, min(len(productlist), 30)):
                    dict = {}
                    if ((productlist[k-1].find("a", {"class": "s1Q9rs"}) != None) & (productlist[k-1].find("div", {"class": "_30jeq3"}) != None)):
                        all_words = productlist[k-1].find(
                            "a", {"class": "s1Q9rs"}).string.split()
                        dict['Brand'] = all_words[0]
                        dict["Name"] = productlist[k -
                                                   1].find("a", {"class": "s1Q9rs"}).string
                        print(
                            'Name: ' + productlist[k-1].find("a", {"class": "s1Q9rs"}).string)
                        print(
                            'Price: ' + productlist[k-1].find("div", {"class": "_30jeq3"}).string)
                        dict["Price"] = productlist[k -
                                                    1].find("div", {"class": "_30jeq3"}).string
                        dict['No of Reviews'] = random.randint(100, 2000)
                        dict['Rating'] = float(f'{random.uniform(3,4.9):.2f}')
                        items.append(dict)
            subdict["items"] = items
            item.append(subdict)
        subsubdict["items"] = item
        ite.append(subsubdict)
    productdict["items"] = ite
    total_dump.append(productdict)

print(total_dump)
