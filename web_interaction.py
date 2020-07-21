import string
from time import sleep
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


class web_interaction:

    def __init__(self, dr):
        self.dr = dr
        self.what_keyword = 'what' # ID
        self.sugest = '/html/body/div[2]/form/div[1]/div/nav/a/p/strong' # XPATH
        self.btn_search = '/html/body/div[2]/form/button' # XPATH
        self.btn_order = 'order' # NAME
        self.store_boxes = 'left' #CLASS
        self.store = 'aTitle' # CLASS
        self.name = 'infoContent' # CLASS
        self.address = 'advAddress' # CLASS
        self.phone = 'advPhone' # CLASS
        self.more = 'linkSeeMore' # CLASS
        
    def close(self):
        self.dr.quit()
    
    def navigate(self, url):
        self.dr.get(url)
    
    def current_url(self):
         return self.dr.current_url
        
    def go_back(self):
        self.dr.back()
        sleep(5)   
        
    def search(self, name = None):
        self.dr.find_element_by_id(self.what_keyword).send_keys(name)
        sleep(2)
        try:    
            self.dr.find_element_by_xpath(self.sugest).click()
        except:
            self.dr.find_element_by_xpath(self.btn_search).click()
    
    def get_links(self):
        self.links = []
        htmls = []
        boxes = self.dr.find_elements_by_class_name(self.store_boxes)
        
        for box in boxes:
            htmls.append(box.get_attribute('innerHTML'))
    
        for html in htmls:
            soup = BeautifulSoup(html, 'html.parser')
            a = soup.h2.a
            self.links.append(a.get('href'))
        
        return self.links
    
    def _get_store_name(self):
        try:
            div = self.dr.find_element_by_class_name(self.name).get_attribute('innerHTML')
            soup = BeautifulSoup(div, 'html.parser')
            name = soup.h1.get_text()
            return name
        except:
            return None
        
    def _get_store_address(self):
        try:
            div = self.dr.find_element_by_class_name(self.address).get_attribute('innerHTML')
            soup = BeautifulSoup(div, 'html.parser')
            address = soup.p.get_text(strip = True)
            address = address.replace('\n', '')
            address = address.replace('\t', '')
            return address
        except:
            return None
        
    def _get_store_phone(self):
        try:
            div = self.dr.find_element_by_class_name(self.phone).get_attribute('innerHTML')
            soup = BeautifulSoup(div, 'html.parser')
            phones = soup.find_all('p')
            phone = []
            for num in phones:
                phone.append(num.get_text(strip = True))
            return ','.join(phone)
        except:
            return None
        
    def see_more_stores(self):
        self.dr.find_element_by_class_name(self.more).click()