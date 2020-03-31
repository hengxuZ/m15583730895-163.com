# -*- coding: utf-8 -*-
# @Author  : hengxu
import os,datetime,time
from testCase.case import testinterface
from Public.py_Html import createHtml
from Public.get_excel import datacel
from  Public.Dingtalk import send_ding
'''执行测试的主要文件'''
def start_interface_html_http():
    #运行时间
    starttime=datetime.datetime.now()
    # 设置测试报告标题日期
    day= time.strftime("%Y年%m月%d日%H:%M", time.localtime(time.time()))
    # 获取当前项目路径
    basdir=os.path.abspath(os.path.dirname(__file__))
    
    path = os.getcwd() + '\\test_case_data\\case.xlsx'

    listid, listkey, listConent, listurl, listfangshi, listqiwang, listname = datacel(path)

    listrelust, list_fail, list_pass, list_json,list_exption,list_weizhi = testinterface()

    filepath =os.path.join(basdir+'\\test_Report\\%s-result.html'%day)
    
    # 如果文件路径创建失败，直接调用系统底层创建路径
    if os.path.exists(filepath) is False:

        os.system(r'touch %s' % filepath)

    endtime=datetime.datetime.now()

    createHtml(titles=u'http接口自动化测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listConent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust,weizhi=list_weizhi,exceptions=list_exption)

    # 钉钉内容模板           
    contec = u'http接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
    list_pass, list_fail, list_exption, list_weizhi, filepath)
    # 连接钉钉
    # send_ding(content=contec)
if __name__ == '__main__':
    start_interface_html_http()