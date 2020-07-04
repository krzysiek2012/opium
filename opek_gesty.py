import os
import unittest
from appium import webdriver
from time import sleep
#ten plik jest skopiowany z poprzedniej wersji czyli opek

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



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
