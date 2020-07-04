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
        desired_caps['udid'] = 'localhost:fb66d463' #do uzupelnienia
        desired_caps['appPackage'] = 'com.example.android.contactmanager'#tutorial poniej przypadku testowego na code shale
        #http://www.automationtestinghub.com/apppackage-and-appactivity-name/
        #metoda pierwsza
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #tutaj apium serwer (chyba)

    def tearDown(self):
        self.driver.quit()

    def test_simple_action(self):
        self.assertTrue(True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
