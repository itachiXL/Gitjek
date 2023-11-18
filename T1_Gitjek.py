from seleniumbase import BaseCase

class Loginpage(BaseCase):
    def test_login_page(self):

        self.open("https://gogagner.com/merowishApp/homepage/")

        self.click("//body/footer[1]/div[1]/div[5]/a[1]/div[1]/*[1]")


