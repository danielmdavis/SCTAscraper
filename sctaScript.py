import time
import folium
import pandas
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

absPath, filename = os.path.split(os.path.abspath(__file__))
browser = webdriver.Chrome(executable_path=absPath + '/chromedriver')
url = 'https://apex-fusioncrm.oraclecorp.com/apex/f?p=112:1:17249489586307::NO:::&tz=-5:00'
browser.get(url)
# browser.minimize_window()

name = browser.find_element_by_name("ssousername")


name.send_keys("my.email@oracle.com") #valid oracle email here


password = browser.find_element_by_name("password")
password.send_keys(open("secret.txt").read())
login = browser.find_element_by_class_name("submit_btn").click()



def switch_to_popup(row_number):
    handles = browser.window_handles
    browser.switch_to.window(handles[0])
    row_num = str(row_number)
    browser.find_element_by_xpath("//*[@id='report_my_tme_rpt']/tbody[2]/tr/td/table/tbody/tr["+row_num+"]/td[4]/span/a/img").click()
    browser.switch_to.window(handles[1])
    print(handles)

def get_opportunities() :
    browser.find_element_by_xpath("//*[@id='report_my_tme_rpt']/tbody[2]/tr/td/table/tbody/tr[1]/td[4]/span/a/img").click()

    handles = browser.window_handles

    browser.switch_to.window(handles[1])
    opportunity_list = browser.find_elements_by_xpath("//*[@id='wwvFlowForm']/div[2]/*")
    opportunity_list_parsed = []
    
    for x in range(2,len(opportunity_list),2):
        opportunity_list_parsed.append( opportunity_list[x].get_attribute("innerHTML") )

    task_list = []
    opp_count = 1
    for x in opportunity_list_parsed:
        # opp_str = str(opp_count)
        # handles = browser.window_handles
        # browser.switch_to.window(handles[0])
        # browser.find_element_by_xpath("//*[@id='report_my_tme_rpt']/tbody[2]/tr/td/table/tbody/tr[1]/td[4]/span/a/img").click()
        # handles = browser.window_handles
        # browser.switch_to.window(handles[1])
        # browser.find_element_by_xpath("//*[@id='wwvFlowForm']/div[2]/a["+opp_str+"]").click()
        # opp_count += 1

        tasks = []
        browser.switch_to.window(handles[0])    
        tasks_raw = browser.find_element_by_xpath("//*[@id='f07_0001']")
        options = [x for x in tasks_raw.find_elements_by_tag_name("option")]
        for task in options:
            tasks.append(task.get_attribute("innerHTML")) #inner task going stale when full interation above uncommented.
        task_list.append(tasks)

    print(task_list)

    task_list = ["Travel", "Training/Personal Development"]
    eng_dict = dict.fromkeys(opportunity_list_parsed, task_list)
    # eng_dict = dict(zip(opportunity_list_parsed, task_list))
    browser.switch_to.window(handles[0])
    return eng_dict

def opportunity_payload() :
    return json.dumps(get_opportunities())

def add_row(engagement_number,row_number,duration) :
    eng_num = str(engagement_number)
    row_num = str(row_number)
    duration = str(duration)

    browser.switch_to.window(browser.window_handles[0])
    browser.find_element_by_id("B11874850291795532552").click() #add row
    switch_to_popup(row_num)
    browser.find_element_by_xpath("//*[@id='wwvFlowForm']/div[2]/a["+eng_num+"]").click()

    browser.switch_to.window(browser.window_handles[0])
    task = browser.find_element_by_id("f07_000"+row_num)
    task.click()
    browser.find_element_by_xpath("//*[@id='f07_000"+row_num+"']/option[2]").click()
    # note = browser.find_element_by_id("f10_0002")
    # note.send_keys("test")
    time = browser.find_element_by_id("f08_000"+row_num)
    time.send_keys(duration)

