from selenium.webdriver.common.by import By


class HomePageLocators:
    Select_room = (By.CSS_SELECTOR, "select#room")
    Start_time = (By.CSS_SELECTOR, "input#start-time")
    End_time = (By.CSS_SELECTOR, "input#end-time")
    Book_room_button = (By.CSS_SELECTOR, "#booking-form button")