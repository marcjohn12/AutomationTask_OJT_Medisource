from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config


def loginfunction(un, up):
    
    time.sleep(5)
    usernametb = config.driver.find_element_by_xpath('//*[@id="loginemail"]').send_keys(un)
    time.sleep(5)
    passwordtb = config.driver.find_element_by_xpath('//*[@id="loginpassword"]')
    passwordtb.send_keys(up)
    time.sleep(3)
    loginbtn = config.driver.find_element_by_xpath('//*[@id="mhLP-ln"]/div[2]/form/div[6]/button')
    loginbtn.click() 
    time.sleep(5)
def clicktabsfunction():
    
    time.sleep(3)
    medicalresourcetb = config.driver.find_element_by_xpath('//*[@id="sidebar"]/side-bar/div/div[1]/ul/li[5]/a/span')
    medicalresourcetb.click()
    time.sleep(5)
    healthcarevendortb = config.driver.find_element_by_xpath('//*[@id="sidebar"]/side-bar/div/div[1]/ul/li[5]/ul/li[5]/a')
    healthcarevendortb.click()
    time.sleep(5)
    NewVendorbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/a')
    NewVendorbtn.click() 
    time.sleep(5)
    
def inputDatafunction(vn, cp, adr, ct, zc, pn, fx, emadr):
    
    time.sleep(3)
    Dropdownbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/div/div')
    Dropdownbtn.click() 
    time.sleep(3)
    selectVendorbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/div/div/div/ul/li[4]')
    selectVendorbtn.click() 
    time.sleep(3)
    Vendornametb = config.driver.find_element_by_name('name').send_keys(vn)
    time.sleep(3)
    ContactPtb = config.driver.find_element_by_name('contactPerson').send_keys(cp)
    time.sleep(3)
    Addresstb = config.driver.find_element_by_name('address').send_keys(adr)
    time.sleep(3)
    Citytb = config.driver.find_element_by_name('city').send_keys(ct)
    time.sleep(3)
    DropdownStatebtn = config.driver.find_element_by_xpath('//*[@id="state_chosen"]')
    DropdownStatebtn.click() 
    time.sleep(3)
    selectStatebtn = config.driver.find_element_by_xpath('//*[@id="state_chosen"]/div/ul/li[30]')
    selectStatebtn.click()
    time.sleep(3)
    zipcodetb = config.driver.find_element_by_id('zipCode').send_keys(zc)
    time.sleep(3)
    PhoneNumtb = config.driver.find_element_by_name('addPhone').send_keys(pn)
    time.sleep(3)
    FaxNumtb = config.driver.find_element_by_name('fax').send_keys(fx)
    time.sleep(3)
    EmailAddtb = config.driver.find_element_by_name('email').send_keys(emadr)
    time.sleep(3)
    DropdownServicesbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[12]/td[2]/div/div/div/a')
    DropdownServicesbtn.click() 
    time.sleep(3)
    selectServicebtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[12]/td[2]/div/div/div/div/ul/li[1]')
    selectServicebtn.click()
    time.sleep(3)

def SaveFunction():
    
    time.sleep(5)
    Savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[2]')
    Savebtn.click() 
    time.sleep(5)

def returnFunction():    
    
    time.sleep(3)
    backbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/ul/li/button')
    backbtn.click() 
    time.sleep(5)

def viewItemfunction():
    
    time.sleep(3)
    viewtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[5]')
    viewtb.click() 
    time.sleep(5)
    time.sleep(3)
    Closetb = config.driver.find_element_by_xpath('/html/body/div[12]/div/div/div/div[3]/button')
    Closetb.click() 
    time.sleep(5)
    
def EditItemfunction(bu, bl):
    
    editbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[5]/td[6]/div/button')
    config.driver.execute_script("arguments[0].click();", editbtn)
    time.sleep(5)
    checkboxbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[13]/td[2]/div/label[1]/input')
    checkboxbtn.click()
    time.sleep(3)
    baaUploadtb = config.driver.find_element_by_name('baaUpload').send_keys(bu)
    time.sleep(3)
    baaLinktb = config.driver.find_element_by_name('baaLink').send_keys(bl)
    time.sleep(3)
    SaveEditbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[2]')
    SaveEditbtn.click() 
    time.sleep(5)
    backbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/ul/li/button')
    backbtn.click() 
    time.sleep(5)

def DeleteItemfunction():
    
    time.sleep(10)
    checkbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[5]/td[1]/div[1]/div[1]/label/input')
    config.driver.execute_script("arguments[0].click();", checkbtn)
    time.sleep(5)
    Dltbtn = config.driver.find_element_by_xpath('//*[@id="Delete"]/li/button')
    Dltbtn.click() 
    time.sleep(5)
    Yesbtn = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]')
    Yesbtn.click() 
    time.sleep(5)

def newclicktabsfunction():
    
    time.sleep(3)
    EmergencyServicestb = config.driver.find_element_by_xpath('//*[@id="sidebar"]/side-bar/div/div[1]/ul/li[5]/ul/li[6]/a')
    EmergencyServicestb.click()
    time.sleep(5)
    NewVendorbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/a')
    NewVendorbtn.click() 
    time.sleep(5)
    
def newInputdatafunction(EN, PN, OPN):
    
    time.sleep(3)
    DropdownCategorybtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/div/div')
    DropdownCategorybtn.click() 
    time.sleep(3)
    selectCategorybtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/div/div/div/ul/li[4]')
    selectCategorybtn.click() 
    time.sleep(3)
    Emergencynametb = config.driver.find_element_by_name('name').send_keys(EN)
    time.sleep(3)
    PhoneNum = config.driver.find_element_by_name('phonenumber').send_keys(PN)
    time.sleep(3)
    OtherPhoneNum = config.driver.find_element_by_name('otherphonenumber').send_keys(OPN)
    time.sleep(5)
def newSaveFunction():
    
    time.sleep(5)
    Savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[2]')
    Savebtn.click() 
    time.sleep(5)

def newreturnFunction():    
    
    time.sleep(3)
    backbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/ul/li/button')
    backbtn.click() 
    time.sleep(5)    

def newviewItemfunction():
    
    time.sleep(3)
    viewtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[4]')
    viewtb.click()
    time.sleep(5)
    Closetb = config.driver.find_element_by_xpath('/html/body/div[12]/div/div/div/div[3]/button')
    Closetb.click() 
    time.sleep(5)
    
def newEditItemfunction(nPN, nOPN):
    
    editbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[4]/td[5]/div/button')
    config.driver.execute_script("arguments[0].click();", editbtn)
    time.sleep(5)
    config.driver.find_element_by_name('phonenumber').clear()
    time.sleep(3)
    PhoneNum = config.driver.find_element_by_name('phonenumber').send_keys(nPN)
    time.sleep(3)
    config.driver.find_element_by_name('otherphonenumber').clear()
    time.sleep(3)
    OtherPhoneNum = config.driver.find_element_by_name('otherphonenumber').send_keys(nOPN)
    time.sleep(5)
    SaveEditbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[2]')
    SaveEditbtn.click() 
    time.sleep(5)
    backbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/ul/li/button')
    backbtn.click() 
    

def newDeleteItemfunction():
    
    time.sleep(10)
    checkbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[4]/td[1]/div/div[1]/label/input')
    config.driver.execute_script("arguments[0].click();", checkbtn)
    time.sleep(5)
    Dltbtn = config.driver.find_element_by_xpath('//*[@id="Delete"]/li/button')
    Dltbtn.click() 
    time.sleep(5)
    Yesbtn = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]')
    Yesbtn.click() 
    time.sleep(5)
    
    
    
    
    



