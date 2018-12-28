# script start
print('\n starting... \n')

# core dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# dictionary for some settings now and later on
TARGET = {}

# case details
TARGET['url'] = 'https://www.google.com/'
TARGET['input string'] = 'Opus Online'
TARGET['expected name'] = 'Opus Online'
TARGET['expected address'] = 'Pärnu maantee 139c, 11317 Tallinn'
TARGET['expected phone'] = '+44 20 7205 2170'
TARGET['expected website'] = 'https://www.opusonline.co/'

# browser object
# TODO: bonus options - headless mode and custom user agent string
class Browser (object):
	driver = None  # driver itself
	name = ''  # for output
	def __init__(self, driver, name):
		self.driver = driver
		self.name = name

# CSS selectors to hunt (possible subject to change as time goes)
TARGET['main container'] = 'div#rcnt'
TARGET['sidebar'] = 'div.knowledge-panel:nth-of-type(1)'
TARGET['name'] = 'div.kp-header > div > div:nth-child(2) span:nth-of-type(1)'
TARGET['address'] = 'div[data-attrid="kc:/location/location:address"] div div span:nth-of-type(2)'
TARGET['phone'] = 'div[data-attrid="kc:/collection/knowledge_panels/has_phone:phone"] div div span:nth-of-type(2)'
TARGET['link'] = 'div.kp-header > div > div:nth-child(2) a.ab_button:nth-of-type(1)'

# the test
# TODO: make less repeatable stuff (especially lookups)
def test(browser):

	browser.driver.set_window_size(1080,800)
	# navigate to uri
	browser.driver.get(TARGET['url'])
	print(browser.name+' got the case')

	try:
		# enter search query
		WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.NAME, 'q')))
		browser.driver.find_element_by_name('q').send_keys(TARGET['input string'])
		print(browser.name+' wrote "'+TARGET['input string']+'" in the form')

		# click the button
		WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.NAME, 'btnK')))
		browser.driver.find_element_by_name('btnK').click()
		print(browser.name+' clicked the button')

		# wait for the HTML to be loaded and check expectations
		print(browser.name+' is attempting to get the panel')
		WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, TARGET['sidebar'])))
		print(browser.name+' found the panel, attempting to find the address')

		# lookup location of the sidebar
		container = browser.driver.find_element(By.CSS_SELECTOR, TARGET['main container']).size
		foundPos = browser.driver.find_element(By.CSS_SELECTOR, TARGET['sidebar']).location
		print(container)
		print(foundPos)

		# lookup name
		try:
			WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, TARGET['name'])))
			foundName = browser.driver.find_element(By.CSS_SELECTOR, TARGET['name']).text
			print(browser.name+' found '+foundName)
		except:
			print(browser.name+' has not found a name')

		# lookup address
		try:
			WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, TARGET['address'])))
			foundAddress = browser.driver.find_element(By.CSS_SELECTOR, TARGET['address']).text
			print(browser.name+' found '+foundAddress)
		except:
			print(browser.name+' has not found an address')

		# lookup phone
		try:
			WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, TARGET['phone'])))
			foundPhone = browser.driver.find_element(By.CSS_SELECTOR, TARGET['phone']).text
			print(browser.name+' found '+foundPhone)
		except:
			print(browser.name+' has not found a phone number')

		# check the website button
		try:
			WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, TARGET['link'])))
			try:
				browser.driver.find_element(By.CSS_SELECTOR, TARGET['link']).click()
				WebDriverWait(browser.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
				foundWebsite = browser.driver.current_url
				print(browser.name+' found '+foundWebsite)
			except:
				print(browser.name+' did something wrong')
		except:
			print(browser.name+' has not found a website button')

		# report
		# TODO: make prettier output
		print('\n')

		if (foundPos['x'] > (container['width']/2)):
			print(browser.name+' sees the company overview block on the right, as expected')
		else:
			print(browser.name+' does not see the company overview block on the right, as expected')
		if (foundName == TARGET['expected name']):
			print(browser.name+' sees the name as expected')
		else:
			print(browser.name+' does not see the name as expected')
		if (foundAddress == TARGET['expected address']):
			print(browser.name+' sees the address as expected')
		else:
			print(browser.name+' does not see the address as expected')
		if (foundPhone == TARGET['expected phone']):
			print(browser.name+' sees the phone number as expected')
		else:
			print(browser.name+' does not see the phone number as expected')
		if (foundWebsite == TARGET['expected website']):
			print(browser.name+' sees the website button as expected')
		else:
			print(browser.name+' does not see the website button as expected')

		print('\n')

	# close the browser
	finally:
		browser.driver.quit()

# call the function on each browser.
# TODO: make parallel processing
cram = Browser(webdriver.Chrome(), 'Chromium')
test(cram)
fox = Browser(webdriver.Firefox(), 'Firefox')
test(fox)

# script end
print('\n done... \n')