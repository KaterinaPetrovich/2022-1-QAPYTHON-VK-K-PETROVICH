from pages.main_page import MainPage
from locators import SegmentPageLocators
from selenium.webdriver.common.by import By


class SegmentPage(MainPage):
    locators = SegmentPageLocators()

    def create_segment(self, segments_name):
        self.click(self.locators.CREATE_SEGMENT_BUTTON)
        self.click(self.locators.ADD_SEGMENTS_ITEM)
        self.click(self.locators.CHECKBOX)
        self.click(self.locators.SUBMIT_BUTTON)
        self.send_keys(self.locators.SEGMENTS_NAME_INPUT, segments_name)
        self.click(self.locators.FINAL_SUBMIT_BUTTON)

    def delete_segment(self, segments_name):
        segment = self.find((By.XPATH, f'//a[@title = "{segments_name}"]'))
        segm_id = segment.get_attribute('href').split("/")[-1]
        self.click((By.XPATH, f'//div[contains(@data-test,"{segm_id}")]//input[@type="checkbox"]'))
        self.click(self.locators.SELECT_MODULE)
        self.click(self.locators.DELETE_BUTTON)
