from auto import auto
import time

brave = r"E:/airdrop-tool/brave/#2/browser/brave-portable.exe"
driver_path = r"E:/auto-airdrop/chromedriver_win32_92/chromedriver.exe"
profile = r"E:/airdrop-tool/chrome/#0/GoogleChromePortable.exe"
chrome_profile_path = r"E:/airdrop-tool/chrome/#0/Data/profile"
twitter_profiles = [
    'cconchimnho01',
    'LTrngQuang6'
]

telegram_groups = [
    'https://t.me/AvaxLauncherAnn',

]
with auto.undetected_chrome(chrome_profile_path) as driver:
    driver.get("https://gmail.com")
    time.sleep(2)
