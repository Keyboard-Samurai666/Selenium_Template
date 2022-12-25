# Import the necessary libraries
from selenium import webdriver

# Create a webdriver object and specify the path to the chromedriver executable
driver = webdriver.Chrome('/home/austin/scripts_python/resources/chromedriver_linux64(1)/chromedriver')

# Choose a website and store it in the web_site variable
web_site = input("What is the site name?:\n")
# Use the webdriver to navigate to a website
driver.get(web_site)


# Find an element on the page using one of the find_element_* methods
element = driver.find_element_by_id('some-element-id')

# Interact with the element using one of the element's methods
element.click()

# Close the browser window
driver.quit()
