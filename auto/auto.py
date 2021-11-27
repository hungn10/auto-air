import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions as exs
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class undetected_chrome(uc.Chrome):
    def __init__(self, profile_path) -> None:
        #thuộc tính cơ bản
        #setting để không nhận diện
        options = uc.ChromeOptions()
        #options.binary_location = profile_path
        #options.add_argument("--remote-debugging-port=9222")
        options.user_data_dir = profile_path
        #options.add_argument('--proxy-server=52.185.165.115:8000')
        super(undetected_chrome, self).__init__(
            "E:/auto-airdrop/chromedriver.exe",
            options=options
        )
        self.set_window_size(1000, 1000)
        self.implicitly_wait(10)



    #auto join group telegram
    def auto_join_telegram(self, telegram_groups):
        #mở telegram web
        self.get('https://web.telegram.org/z/')
        #find search box and enter hubofairdrop
        telegram_search = self.find_element_by_css_selector('input[id="telegram-search-input"]')
        telegram_search.send_keys('hubofairdrop')
        time.sleep(1)
        #hit enter button

        telegram_search.send_keys(Keys.ENTER)
        #click vào save message

        time.sleep(1)
        count = 0
        for link in telegram_groups:
            #tim nhom và tham gia
            link_to_group = self.find_elements_by_css_selector(
                f'a[href="{link}"]'
            )
            #xem đã có trong box khonng
            if len(link_to_group) > 0:
                link_to_group[0].click()
            else:
                print("Don't find any group")
                continue
            #tham gia nhóm
            time.sleep(1)
            join_button = self.find_elements_by_css_selector(
                'button[class="Button tiny primary fluid has-ripple"]'
            )
            if len(join_button) > 0:
                join_button[0].click()
                count += 1
                time.sleep(1)
            else:
                print(f"{link} already joined")
            #back to save message
            self.execute_script("window.history.go(-1)")
            time.sleep(1)
        return print(f"Joined {count} group")



    #auto follow twitter
    def follow_twitter(self, handle):
        count = 0
        for username in handle:
            self.get(f'https://twitter.com/{username}')
            time.sleep(3)
            follow = self.find_element_by_css_selector(
                f'div[aria-label*="@{username}"]'
            )
            if follow.text == "Follow":
                self.execute_script(
                    f"""document.querySelector('div[aria-label="Follow @{username}"]').click()"""
                )
                count += 1
            else:
                print(f'Alreadry follow {username}')
        return print(f"Success Following {count}")


    #exit driver
    def exit_driver(self):
        self.quit()