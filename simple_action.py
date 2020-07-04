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
        self.driver.find_element_by_accessibility_id('Graphics').click()
        self.driver.find_element_by_accessibility_id('Arcs').click()
        header_element = self.driver.find_element_by_id('android:id/action_bar_title')
        HeaderText = header_element.text
        self.assertIsNotNone(header_element)
        #jak by nie dzialo to to na dysku screen 4, jest inna opcja
        print(f"naglowek to: {HeaderText}")
        #self.driver.keyevent(4)

        #keyevent appium android, powinna sie pojawic cala lista tych przyciskow, domyslnie w
        #telefonie (4) to klawisz back i stad ta funkcja..https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_BACK
        #creen shot np mozna w apium napisac albo klawisz (120), trzeba sprawdzi
        #takeing screen shot with Appium -> robi sie w telefonie
        #self.driver.keyevent(120)
        self.driver.back()
        self.driver.keyevent(4)

        app_button = self.driver.find_element_by_accessibility_id('App')
        #moje, nie sprawdzilem
        #if app_button.is_displayed():
            #print(f'guzik app jest wyswietlony')
        sleep(1)
        self.assertIsNotNone(app_button)

        ile_wszys = self.driver.find_elements_by_id('android:id/text1')
        #trzeba policzyc ile zakladek
        #moje, trzeba dopracowac
        #for x in ile_wszys:
            #print(f'wlasnie to znalazlem{x}')
        total = len(ile_wszys)
        print(f'liczba to: {total}')
        #pan cos jeszcze z ifem wrzucil, sprawdz se na screenach  od 5..


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
