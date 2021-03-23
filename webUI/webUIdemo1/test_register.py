# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 12:18
# @Author  : Daniel
from webUI.webUIdemo1.index_page import IndexPage


class TestRegister:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        self.index.goto_login().goto_register().register()

