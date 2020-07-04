import os
import unittest
from appium import webdriver
from time import sleep


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class TestingApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Krzysztof (Galaxy A5)'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['udid'] = 'fb66d463' #do uzupelnienia
        desired_caps['appPackage'] = 'io.appium.android.apis'#tutorial poniej przypadku testowego na code shale
        #http://www.automationtestinghub.com/apppackage-and-appactivity-name/
        #metoda pierwsza

        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #tutaj apium serwer (chyba)

    def tearDown(self):
        self.driver.quit()

    def test_simple_action(self):
        # tutaj selectory do appium
        # http://appium.io/docs/en/commands/element/find-elements/
        # accessbilibity -> content-desc dostepny w android, mozna po tym lokalizowac, dobre, wyjatkowe, moze miec nazwe podobna do TEXT ale to nie znaczy ze cos ten tego, bo inne sa
        # w webowce nie ma content desc
        #
        self.driver.is_app_installed('io.appium.android.apis')
        self.driver.find_element_by_accessibility_id('Graphics').click()
        self.driver.find_element_by_accessibility_id('Arcs').click()
        #header_element = self.driver.find_element_by_id()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
