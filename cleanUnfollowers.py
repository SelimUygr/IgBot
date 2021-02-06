from start import WebDriverWait,By,EC,Keys,webdriver,sleep,starting
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import os

class cleaner:
    def __init__(self,driver,dailyunfollow=40):
        self.driver = driver
        self.dailyunfollow = dailyunfollow
        with open("userinfo.txt","r") as info:
            self.username = info.read()

    def findUnfollowers(self,number=1):
        followers_list = self.setFollowersList()
        with open("followersCount.txt","r") as fc:
            followers_count = fc.read()
        if number == 1:
            print("getting followers list")
            followers_count = self.goToFollowersTab()
            with open("followersCount.txt","w") as fc:
                fc.write(str(followers_count))
            print(followers_count)
            print(len(followers_list))
	    print(type(followers_list))

        # Set the for loop
        if len(followers_list) == 0:
            # Go to profile
            self.driver.get(f'https://www.instagram.com/{self.username}/')
            # Click the followers tab
            WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()
            for i in range(1,int(followers_count)):
                # Move to every single followers for seeing all of them
                element = WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]')))
                element_name = element.find_element_by_tag_name('span a').text

                # Open the text file to write update followers 
                with open("followers.txt",'a') as followerKeeper:
                    if element_name not in followers_list:
                        followers_list.append(element_name)
                        followerKeeper.write(element_name + "\n")
                    else:
                        pass
                ActionChains(self.driver).move_to_element(element).perform()
            # Go to profile
            self.driver.get(f'https://www.instagram.com/{self.username}/')
        
        if self.driver.current_url != f"https://www.instagram.com/{self.username}/following/":
            # Go to profile
            self.driver.get(f'https://www.instagram.com/{self.username}/')

            # Click the followings tab
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))).click()
                
        # Set the for loop
        for x in range(number,number + int(self.dailyunfollow)):
            print("we are in always")
            # Set element2 for get reference in actionchains 
            element2 = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div/div/div[2]/ul/div/li[{x}]')))
            ActionChains(self.driver).move_to_element(element2).perform()
            # Get username
            element2_name = element2.find_element_by_tag_name('span a').text
            # Get button
            element2_button = element2.find_element_by_tag_name('button')
            if element2_name not in followers_list and element2_button.text == "Takiptesin":
                print("unfollower Found")
                # unfollowers_list.append(element2_name)
                element2_button.click()
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[1]'))).click()
            else:
                pass
        
        sleep(900)
        self.findUnfollowers(number=x)
            
            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Cleaning unfollowers WELL-DONE ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓1

    def setFollowersList(self):
        # Check the file of followers if empty
        filesize = os.path.getsize("followers.txt")
        print("filesize:",filesize)

        # If not empty get the followers from file to list
        if filesize != 0:
            with open("followers.txt","r") as followers_file:
                followers_list = followers_file.readlines()
            
            followers_list = [x.strip() for x in followers_list]

        # If empty let the list be empty too
        else:
            followers_list = []

        return followers_list

    def goToFollowersTab(self):
        if self.driver.current_url != "https://www.instagram.com/mmhhmmttat/":
            # Go to profile
            self.driver.get('https://www.instagram.com/mmhhmmttat/')
            # Get number of followers from followers tab for set the for loop 
            elem = WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')))
            followers_count = int(elem.text)
        else:
            # Get number of followers from followers tab for set the for loop 
            elem = WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')))
            followers_count = int(elem.text)

        return followers_count - 1

    