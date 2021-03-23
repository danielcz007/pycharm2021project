# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 15:44
# @Author  : Daniel
from webUI.seleniumPO_page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainpage = MainPage()

    def test_addmember(self):
        assert self.mainpage.goto_add_member().add_member()