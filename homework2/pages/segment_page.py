from pages.main_page import MainPage
from locators import SegmentPageLocators


class SegmentPage(MainPage):
    locators = SegmentPageLocators()

    def create_segment(self, segments_name):

        self.click(self.locators.CREATE_SEGMENT_BUTTON)
        self.click(self.locators.ADD_SEGMENTS_ITEM)
        self.click(self.locators.CHECKBOX)
        self.click(self.locators.SUBMIT_BUTTON)
        self.send_keys(self.locators.SEGMENTS_NAME_INPUT, segments_name)
        self.click(self.locators.FINAL_SUBMIT_BUTTON)
