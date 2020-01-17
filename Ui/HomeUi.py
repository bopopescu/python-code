#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-14 8:36
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : HomeUi.py

import wx


class Mywin(wx.Frame):

    def __init__(self, parent, title):

        super(Mywin, self).__init__(parent, title=title, size=(600, 400))
        global t3
        global t2
        global rbox
        global cb1
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(panel)

        txt1 = "表单提交"

        txt = txt1 + "\n"

        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        lbl.SetFont(font)
        lbl.SetLabel(txt)

        box.Add(lbl,0,wx.ALIGN_CENTER)
        l2 = wx.StaticText(panel, 1, "title：")
        hbox2.Add(l2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        t2 = wx.TextCtrl(panel, style = wx.TE_LEFT)
        t2.SetMaxLength(10)
        hbox2.Add(t2, 5,  wx.ALIGN_LEFT, 5)
        box.Add(hbox2)

        l3 = wx.StaticText(panel, 1, "内容：")
        hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        t3 = wx.TextCtrl(panel, size=(200, 100), style=wx.TE_MULTILINE)
        # t2.SetMaxLength(5)

        hbox3.Add(t3, 5, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        box.Add(hbox3)
        lblList = ['笔记', '日记', '数据']

        rbox = wx.RadioBox(panel, label='RadioBox', pos=(80, 10), choices=lblList,
                                majorDimension=1,
                                style=wx.RA_SPECIFY_ROWS)
        hbox4.Add(rbox, 5, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        box.Add(hbox4)
        # self.Bind(wx.EVT_TEXT, self.onRadioBox,self.rbox)
        cb1 = wx.CheckBox(panel, label = 'Value A',pos = (10,10))
        hbox5.Add(cb1, 5, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        box.Add(hbox5)

        btn1 = wx.Button(panel, label="提 交")

        hbox6.Add(btn1, 5, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        box.Add(hbox6)
        # 提交按钮
        btn1.Bind(wx.EVT_BUTTON, self.OnStart)
        panel.SetSizer(box)

        self.Centre()
        self.Show()


    def OnStart(self, e):
        print('标题：'+t2.GetValue())
        print('内容：' + t3.GetValue())
        print('单选：' + rbox.GetStringSelection())
        # print('选项：' + cb1.GetValue())

app = wx.App()
Mywin(None, '测试')
app.MainLoop()
