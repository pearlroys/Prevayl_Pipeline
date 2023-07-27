import requests
from bs4 import BeautifulSoup
import pandas as pd


prevayl_list = []


urls = ["https://shop.prevayl.com/collection/mens-performance-wear", "https://shop.prevayl.com/collection/womens-performance-wear"]
for url in urls:
    web = requests.get(url)
    soup = BeautifulSoup(web.content, "html.parser")
   

    # Check if the page is loading correctly
    if web.status_code == 200:
        print("Page loaded successfully.")
    else:
        print("Failed to load the page.")
        exit()



    # Check if the div elements with the specified class are being selected
    product_cards = soup.find_all("a", class_="ProductCardSimple_root__xCduQ")
    if len(product_cards) > 0:
        print(f"Found {len(product_cards)} sportswear items.")
    else:
        print("No sportswear items found.")
        exit()
    # product_cards = soup.find_all("a", class_="ProductCardSimple_root__xCduQ")

    for product_card in product_cards:
        product_name = product_card.find("h2", class_="Heading_root__RsZIY").text.strip()
        product_description = product_card.find("div", class_="ProductCardSimple_description__FIQ0r").p.text.strip()
        product_price = product_card.find("div", class_="flex flex-row justify-between items-baseline w-full gap-5 md:gap-7").p.text.strip()

        # # Print the extracted data
        # print("Product Name:", product_name)
        # print("Product Description:", product_description)
        # print("Product Price:", product_price)
        # print()

        # Append the data to the list
        prevayl_list.append({
            'Product Name': product_name,
            'Product Description': product_description,
            'Product Price': product_price
        })

# Create a DataFrame from the data
df = pd.DataFrame(prevayl_list)
df.to_csv('prevayl.csv')