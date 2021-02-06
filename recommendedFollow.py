from start import WebDriverWait,By,EC,Keys,webdriver,sleep,starting

class randomFollow:
    def __init__(self,driver,dailyFollow):
        self.driver = driver
        #daily follow is for specify how many people wanted to follow 
        #If we try to follow infinite people per use than instagram will ban us from being bot
        self.dailyFollow = dailyFollow

    #Going to recommended page
    def goToRecommended(self):
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a/div')))
        self.driver.get('https://www.instagram.com/explore/people/suggested/')
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div[2]/div/div/div[1]')))

    #Following dailyFollow times people in the recommended page
    def followAll(self):
        for i in range(1,50):
            try:
                element = WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,f'//*[@id="react-root"]/section/main/div/div[2]/div/div/div[{i}]/div[3]/button')))
                if element.text == "Takip Et":
                    element.click()
            except TimeoutError:
                break

