from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\Compressed\chromedriver_win32\chromedriver.exe")
driver.maximize_window()   #For maximizing window
driver.get('https://web.whatsapp.com/')

if __name__ == "__main__":        #loop for true value of sucess 
    while True:
        input('Enter anything after scanning QR code..  Hit ENTER to start')
        name = input('Enter the name of User or Number or Group : ')
        capname=name.title()                        #captilize the first letter of name and surname
        
        if name.isdigit():                          #check input is number or not
            val=(f'+91 {name[:5]} {name[5:]}')      #f sring to make in number form
        else:
            val = str(capname)

        filepath = input('Enter your filepath (images/video): ')
        user = driver.find_element_by_xpath(f'//span[@title = "{val}"]').click()
        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]').click()

        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)

        sleep(2)
        send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]').click()
