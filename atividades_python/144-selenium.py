from selenium import webdriver
from time import sleep
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'arquivos/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=arquivos/Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            #tgl_menu = self.chrome.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/button')
            #tgl_menu.click()
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro fazer logout:', e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('usuario')
            input_password.send_keys('senha')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('Erro ao fazer login:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()

    chrome.faz_logout()

    sleep(5)
    chrome.sair()
