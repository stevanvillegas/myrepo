import selenium
from selenium import webdriver
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import random



baseurl = 'https://www.apartmentlist.com/'



# for x in range(1,7):
#     r = requests.get(f'https://www.apartmentlist.com/il/evanston/page-{x}')
#     soup = BeautifulSoup(r.content)
#     productlist = soup.find_all('div', class_="e1yk8kly1")
#     for item in productlist:
#         for link in item.find_all('a', href=True):
#             productlinks.append(baseurl + link['href'])

aptlist = []

driver = webdriver.Chrome(ChromeDriverManager().install())
productlinks = []
for page_number in range(1,7):
    link = 'https://www.apartmentlist.com/il/evanston/page-{}'.format(page_number)
    time.sleep(random.randint(1, 3))
    driver.get(link)
    card = driver.find_elements_by_class_name('e19g3lpj2')
    for element in card:
        print(element.get_attribute("href"))
        productlinks.append(element.get_attribute("href"))


# productlinks = ['https://www.apartmentlist.com//il/evanston/the-presidential', 'https://www.apartmentlist.com//il/evanston/central-station-apartments', 'https://www.apartmentlist.com//il/evanston/centrum-evanston', 'https://www.apartmentlist.com//il/evanston/415-premier-evanston']

for link in productlinks:
    print("Going to: ", link)
    driver.get(link)
    time.sleep(random.randint(1, 3))
    #Scroll down to load elements
    driver.execute_script("window.scrollTo(0, 1000);")
    name = driver.find_element_by_class_name('css-q6nuyz').text

    address = driver.find_element_by_xpath("//span[@class='css-5f7kvo']").text
    town = driver.find_element_by_xpath("//span[@class='css-1iuu4fg']").text
    full_address = driver.find_element_by_class_name('evn5xuc2').text
    print(full_address)

    #See if more than 9 units exist
    try:
        button = driver.find_element_by_class_name('exjblwa0')
        button.click()
    except:
        print('No button found')

    units = driver.find_elements_by_class_name('e14690vg5')
    for unit in units:
        print("Unit Text" , unit.text)
        unit_number = " ".join(unit.text.split(' ')[:2])
        unit_price = driver.find_element_by_class_name('e14690vg4').text
        unit_subtitle = driver.find_element_by_class_name('e14690vg6').text.split('·')
        unit_beds = unit_subtitle[0]
        unit_baths = unit_subtitle[1]

        #https://www.apartmentlist.com/il/evanston/1576-oak missing SQFT
        try:
            unit_sqft = unit_subtitle[2]
        except:
            print(link, "Missing Square Feet")
        #Grab Amenities Column
        amenities_column = driver.find_elements_by_class_name('e1b8cokc9')
        print('Amenities')

        #Split by amentieis and remove the column header
        unit_amenities_column = amenities_column[0].text.split('\n')[1:]
        #Create string of amenities
        unit_amenities =','.join(unit_amenities_column)

        property_amenities_column = amenities_column[1].text.split('\n')[1:]
        property_amenities =','.join(property_amenities_column)

        apt = {
            'name' : name,
            'address' : address,
            'full address' : full_address,
            'town' : town,
            'unit_number' : unit_number,
            'unit_price' : unit_price,
            'unit_bed' : unit_beds,
            'unit_baths' : unit_baths,
            'unit_sqft' : unit_sqft,
            'unit_amenities' : unit_amenities,
            'property_amenities' : property_amenities
        }
        print(apt)
        aptlist.append(apt)

driver.quit()

df = pd.DataFrame(aptlist)
print(df)
df.to_csv('evanston apartments.csv')
