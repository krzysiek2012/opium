import os
import unittest
from appium import webdriver
from time import sleep
#ten plik jest skopiowany z poprzedniej wersji czyli opek

#dodatkowy import dopisuje, importujemu class'e ktora nam na to pozwoli
from appium.webdriver.common.touch_action import TouchAction


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class TestingApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Krzysztof (Galaxy A5)'
        #plik w tym samym folderze, ale w sumie zainstalowaem ja odrecznie na fonie
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['udid'] = 'fb66d463' #do uzupelnienia
        #https://stackoverflow.com/questions/23081263/adb-android-device-unauthorized
        # tutaj znalazlem jak podlaczyc telefon, nie bylo latwo, trzebabylo parerazy zeby bulo po
        # $adb devices -> autorized
        desired_caps['appPackage'] = 'io.appium.android.apis'#tutorial poniej przypadku testowego na code shale
        #http://www.automationtestinghub.com/apppackage-and-appactivity-name/
        #metoda pierwsza
        #aczkolwiek zadzialalo dopiero jak znalazlem na stack overflow

        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #tutaj apium serwer (chyba)

    def tearDown(self):
        self.driver.quit()

    def test_simple_action(self):
        # tutaj selectory do appium
        # http://appium.io/docs/en/commands/element/find-elements/
        # accessbilibity -> content-desc dostepny w android, mozna po tym lokalizowac, dobre,
        # wyjatkowe, moze miec nazwe podobna do TEXT ale to nie znaczy ze cos ten tego, bo inne sa
        # w webowce nie ma content desc
        #
        self.driver.is_app_installed('io.appium.android.apis')
        #podejscie najprostrze
        #to jest poprawene linijka nizej ale zrobimy tapa
        #self.driver.find_element_by_accessibility_id('Views').click()
        #tapniecie to takie pykniecie, w wielu przypadkach to jest to samo co klikniecie
        #gesture touchAction appium -> http://appium.io/docs/en/writing-running-appium/touch-actions/#touchaction
        #
        elo = self.driver.find_element_by_accessibility_id('Views')
        action = TouchAction(self.driver)
        action.tap(elo).perform()
        sleep(3)

        self.driver.find_element_by_accessibility_id('Expandable Lists').click()
        self.driver.find_element_by_accessibility_id('1. Custom Adapter').click()

        elo2 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="People Names"]')
        elo2.click() # nieobowiazkowe w testach
        action.long_press(elo2).perform()
        sleep(3)
        #jak clikniesz to sie rozwija lista ale jak dluzej przytrzymasz to masz w tedy menu
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Sample action"]').click()

        sleep(3)





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
