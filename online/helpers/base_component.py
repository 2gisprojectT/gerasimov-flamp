__author__ = 'vi.gerasimov'


class BaseComponent(object):
    def __init__(self, driver, element=None):
        """
        :type driver: WebDriver
        :type element: WebElement
        """
        self.driver = driver
        self.element = element