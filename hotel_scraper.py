import csv
from selenium import webdriver
import time

# default path to file to store data
path_to_file = "./reviews.csv"
input_file_path = "./urls.txt"

inputFile = open(input_file_path, 'r', encoding="utf-8")
csvReader = csv.reader(inputFile)

# Open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Hotel Name", "Date", "Rating (/50)", "Title", "Review"])

# Import the webdriver
driver = webdriver.Firefox()

for url in csvReader:
    url = url[0]
    if url[0] == "#":
        continue
    driver.get(url)
    hotel_name = driver.find_element_by_xpath(".//h1[@class='_1mTlpMC3']").text
    # total_number = int(driver.find_element_by_xpath(".//span[@class='_33O9dg0j']").text[:-8])
    # num_page = math.ceil(total_number/5)
    # change the value inside the range to save more or less reviews
    while 1==1:
        # expand the review
        time.sleep(2)

        container = driver.find_elements_by_xpath(".//div[@class='_2wrUUKlw _3hFEdNs8']")


        for j in range(len(container)):
            title = container[j].find_element_by_xpath(".//div[@class='glasR4aX']").text
            date = container[j].find_element_by_xpath(".//span[@class='_34Xs-BQm']").text[14:]
            rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
            read_more = True
            try:
                container[j].find_element_by_xpath(".//span[@class='_3maEfNCR']").click()
            except:
                pass
            review = container[j].find_element_by_xpath(".//q[@class='IRsGHoPm']").text.replace("\n", " ")
            csvWriter.writerow([hotel_name, date, rating, title, review])

        try:
            # change the page
            driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()
        except:
            break

driver.close()
