from start import WebDriverWait,By,EC,Keys,webdriver,sleep,starting
from selenium.webdriver.common.action_chains import ActionChains
class choosen_Following:
    def __init__(self,driver,hashtag):
        self.driver = driver
        #Get hashtag for specify the community we want to get attention from
        self.hashtag = hashtag
        #Same usage as recommendedFollow

    # Setting everything to be ready for following people
    def set(self):
        # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Go to mainpage in case of any error occure ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
        if self.driver.current_url != 'https://www.instagram.com/':
            self.driver.get('https://www.instagram.com/')
            WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]'))).click()
        # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Setting everything well-done ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))).send_keys(self.hashtag)
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/a[1]/div/div[2]/span'))).click()
        user_follower = WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'))).get_attribute("title")
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()
        print(user_follower)
        if "," in user_follower:
            user_follower = user_follower.replace(",","")
        elif "." in user_follower:
            user_follower = user_follower.replace(".","")
        print(user_follower)
        return user_follower

    # Following dailyFollow times people we want from choosen instagram page
    def followAllFollowers(self,user_follower):
        for i in range(1,user_follower):
            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Scrolling down while doing the task well-done ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
            element = WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]')))
            ActionChains(self.driver).move_to_element(element).perform()

            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Getting the button text well-done ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
            element_button = element.find_element_by_tag_name('button')

            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Finally following algorithm WELL-DONE ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓
            if element_button.text == "Takip Et":
                element_button.click()
            else:
                pass

    def followAlways(self,user_follower,number=1,counter = 1):
        count = counter
        new_userFollower = user_follower
        for i in range(number, user_follower):
            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Scrolling down while doing the task well-done ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
            element1 = WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]')))
            

            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Getting the button text well-done ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
            element_button1 = element1.find_element_by_tag_name('button')
            if i > 10:
                pre_element_button1 = self.driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i - 10}]')
                if element_button1.text == "Takip Et":
                    if pre_element_button1.find_element_by_tag_name("button").text == "Takip Et":
                        sleep(900)
                        break
                    else:
                        element_button1.click()
                        count += 1
                        print(count)
                else:
                    pass
            else:
                if element_button1.text == "Takip Et":
                    element_button1.click()
                    count += 1
                    print(count)
            ActionChains(self.driver).move_to_element(element1).perform()
        self.followAlways(user_follower=new_userFollower,number = i - 10,counter=count)
            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Finally following algorithm WELL-DONE ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓
