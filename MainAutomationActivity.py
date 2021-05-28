from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import function
import config
from function import newviewItemfunction


config.driver.get("https://qado.medisource.com/login")
config.driver.maximize_window()

function.loginfunction('superagent@geeksnest', 'Tester2021@')
#For Healthcare Tab Function
function.clicktabsfunction()
function.inputDatafunction('Generika Healthcare Inc.', 'Marc John The Pogi',
                                 '1335  Cottrill Lane', 'Saint Louis', '63130', '314-515-7176', '314-323-6831',
                               'generika@gmail.com')
function.SaveFunction()
function.returnFunction()
function.viewItemfunction()
function.EditItemfunction('This is a Business Agreement 101', 'www.baalink.com')
function.viewItemfunction()
function.DeleteItemfunction()

#for Emergency Tab Function
function.newclicktabsfunction()
function.newInputdatafunction('EMR Urdaneta District', '300 600 9000', '100 200 3000')
function.newSaveFunction()
function.newreturnFunction()
function.newviewItemfunction()
function.newEditItemfunction('911 117 8888', '588 358 7000')

function.newviewItemfunction()
function.newDeleteItemfunction()



