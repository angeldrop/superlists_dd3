from selenium import webdriver

browser=webdriver.Firefox()
browser.get("http://localhost:8001")

assert 'Django' in browser.title



# from .base import FunctionalTest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from unittest import skip
# import time

            
# class ItemValidationTest(FunctionalTest):

    # def get_error_element(self):
        # return self.browser.find_element_by_css_selector('.has-error')

    # def test_cannot_add_empty_list_items(self):
        # #伊迪丝访问首页，不小心提交了一个空待办事项
        # #输入框中没输入内容，她就按下了回车键
        # self.browser.get(self.live_server_url)
        # self.get_item_input_box().send_keys(Keys.ENTER)

        # #浏览器截获了请求
        # #清单页面不会加载
        # self.wait_for(lambda:self.browser.find_element_by_css_selector(
            # '#id_text:invalid'
        # ))


        # #提示待办事项不能为空#她输入一些文字，然后再次提交，这次没问题了
        # self.get_item_input_box().send_keys('买牛奶')
        # self.wait_for(lambda:self.browser.find_element_by_css_selector(
            # '#id_text:valid'
        # ))
        # #现在可以提交了
        # self.get_item_input_box().send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table('1:买牛奶')

        # #她有点儿调皮，又提交了一个空待办事项
        # self.get_item_input_box().send_keys(Keys.ENTER)

        # #浏览器这次也不会放行
        # self.wait_for_row_in_list_table('1:买牛奶')
        # self.wait_for(lambda:self.browser.find_element_by_css_selector(
            # '#id_text:invalid'
        # ))


        # #输入文字之后就没问题了
        # self.get_item_input_box().send_keys('弄杯茶')
        # self.wait_for(lambda:self.browser.find_element_by_css_selector(
            # '#id_text:valid'
        # ))
        # self.get_item_input_box().send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table('1:买牛奶')
        # self.wait_for_row_in_list_table('2:弄杯茶')


    # def test_cannot_add_duplicate_items(self):
        # #伊迪丝访问首页，新建一个清单
        # self.browser.get(self.live_server_url)
        # self.get_item_input_box().send_keys('买牛奶')
        # self.get_item_input_box().send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table('1:买牛奶')
        
        # #他不小心输入了一个重复的代办事项
        # self.get_item_input_box().send_keys('买牛奶')
        # self.get_item_input_box().send_keys(Keys.ENTER)
        
        # #他看到了一条用帮助的错误消息
        # self.wait_for(lambda:self.assertEqual(
            # self.get_error_element().text,
            # "此清单中已经有此项目了，不得重复！！"
        # ))


    # def test_error_messages_are_cleared_on_input(self):
        # #伊迪丝访问首页，新建一个清单
        # self.browser.get(self.live_server_url)
        # self.get_item_input_box().send_keys('买花花')
        # self.get_item_input_box().send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table('1:买花花')

        # self.get_item_input_box().send_keys('买花花')
        # self.get_item_input_box().send_keys(Keys.ENTER)

        # self.wait_for(lambda:self.assertTrue(
            # self.get_error_element().is_displayed()
        # ))


        # #为了消除错误，他开始输入内容
        # self.get_item_input_box().send_keys('买扥的')


        # #看到错误消失，他满意了
        # self.wait_for(lambda:self.assertFalse(
            # self.get_error_element().is_displayed()
        # ))