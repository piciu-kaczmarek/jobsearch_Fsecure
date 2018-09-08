from selenium import webdriver
from selenium.webdriver import ActionChains
import time

searched_job = input("What is the position You are looking for? (i.e.:(Quality Engineer): ")
browser_name = input("What is Your browser?(type: firefox or chrome): ")

if browser_name == "chrome":
    driver = webdriver.Chrome()
elif browser_name != "chrome":
    driver = webdriver.Firefox()

# go to desired web page

print("Step 1 \n Going to F-secure page and finding career section")

address = "https://www.f-secure.com/en/web/about_global/careers"
driver.get(address)

career = driver.find_element_by_xpath("//a[@href='https://www.f-secure.com/en/web/about_global/careers']")
job_opp = driver.find_element_by_xpath("//a[@href='https://www.f-secure.com/en/web/about_global/careers/job-openings']")
point = ActionChains(driver).move_to_element(career)
point.perform()
job_opp.click()

# look for a job offer


city_list = driver.find_element_by_xpath("//select[@id='job-city']/option[text()='Poznań']").click()

page_link = driver.find_element_by_xpath("//a[@class='page-link']")
page_link_number = page_link.get_attribute("text")
page_link_number = int(page_link_number)

time.sleep(1)


def job_search(searched_job):
    xpath_job = "//h2[text()='" + searched_job + "']"
    job = driver.find_element_by_xpath(xpath_job)
    display_value = job.is_displayed()
    page_url = driver.current_url
    if display_value:
        print("There is a open position for a {} in F-Secure. Go to {}".format(searched_job, page_url))
    else:
        print("I'm sorry, there are no open positions for a {} at this moment on this page".format(searched_job))


# click on ok button for cookies

cookie_button = driver.find_element_by_xpath("//a[@class='btn btn-primary']").is_displayed()
if cookie_button:
    driver.find_element_by_xpath("//a[@class='btn btn-primary']").click()


# Change the page
def turn_the_page():
    next_page = driver.find_element_by_xpath("//a[@class='page-link next']")
    next_page.click()
    print("I have just turn the page")


# asses the finding

def get_page_number():
    page_url = list(driver.current_url)
    last_url_sign = (page_url[-1])
    # print(type(last_url_sign))
    if last_url_sign == "s":
        return 1
    elif last_url_sign != "s":
        last_url_sign = int(last_url_sign)
        return last_url_sign


print("Step 2 \n Looking for a position of {}".format(searched_job))

job_search(searched_job)

for i in range(1, page_link_number):
    turn_the_page()
    job_search(searched_job)


print("Thanks for checking, goodbye!")
driver.close()
