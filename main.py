"""
    Note:
        1. The Version only support the "Chrome" browser
        2. these files is the main code file, other code files are belong the "selenium"
           package, and the reason is there has a code file "config.py" must edit when
           the program is be package into a execution.
            (1) WF/Main.py
            (2) WF/ConnectWebsite.py
            (3) WF/UI.py
            (4) WF/Var.py

        3. If you want to package this project into a execution by using "Pyinstaller",
        you must edit the "config.py",
        you should change the code A to code B,
        because the path of setting file "default.ini" will be change in the execution.

        Code A : "_default_config_path = os.path.join(os.path.dirname(__file__), 'default.ini')"
        Code B : "_default_config_path = os.path.join(os.path.dirname(__file__), 'default.ini/default.ini')"


"""
import ConnectWebsite, IODataFromFile, UI, Var
import sys
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication

global var
__browser_type__ = "Chrome"

class WTThread(QtCore.QThread):
    def __init__(self,parent=None,):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        while True:
            global var
            # update GUI website url list
            if var.isUpdateWebsiteList is True:
                var.input_website_list()
                var.isUpdateWebsiteList = False
                var.all_number = len(var.website_list)
                var.ui.result(False)

            while var.execute_flag is True and var.isfinished is True:
                    WebsiteTestMain(var.input_website_list())
            time.sleep(1)



def WebsiteTestMain(ListURL):

    if ListURL is False:
        var.ui.Run.setText("Run")
        return False
    var.isfinished =False
    # create
    browser = ConnectWebsite.CreateBrowser(var.browser_type)  # create webdriver

    # initial
    ConnectWebsite.InitBrowser(browser)    # init webdriver
    var.website_list_RepeatEXE.clear()
    var.init_All_number()                  # initial the number of the result for all round

    # start
    while True:
        # initial this round variable
        count = 0
        var.init_number()                  # initial the number of the result for this round

        # start
        for i in ListURL:                  # check the url whether is including "HTTP"
            print(i)
            if i[0].find("http") is -1:
                i[0] = "http://" + i[0]

            # get the url
            result = ConnectWebsite.ConnectWebsite(browser,i[0])
            print(result)
            # "result" is False ==> the website is no request,
            #                       and webdriver must to restart(
            #                       there are some problem with the webdriver
            #                       when the website is no request)
            if result is False:
                var.website_list[count].status_code = "N.A."
                var.website_list[count].ispass = 'F'
                if var.website_list[count].to_block is 'T':
                    var.ToBlock_na_number += 1
                else:
                    var.NotToBlock_na_number += 1

                # restart the browser
                try:
                    browser.close()
                except Exception as e:
                    print("[Browser Close]"+str(e))

                try:
                    browser.quit()
                except:
                    print("[Browser Quit]" + str(e))

                # create new browser
                browser = ConnectWebsite.CreateBrowser(var.browser_type)
                ConnectWebsite.InitBrowser(browser)
            else:
                # status_code is -1 ， Blocked in 'Https' (ERR_SSL_PROTOCOL_ERROR)
                if result[0][0] is -1:
                    var.website_list[count].website_url = str(i[0])
                    var.website_list[count].status_code = "ERR_SSL_PROTOCOL_ERROR"
                else:
                    var.website_list[count].status_code = str(result[0][0])
                    var.website_list[count].website_url = str(i[0])

                if result[1] is True:
                    if var.website_list[count].to_block is 'T':
                        var.website_list[count].is_pass = 'T'
                        var.ToBlock_pass_number += 1
                        var.ToBlock_number += 1
                    else:
                        var.website_list[count].is_pass = 'F'
                        var.NotToBlock_number += 1
                else:
                    if var.website_list[count].to_block is 'F':
                        var.website_list[count].is_pass = 'T'
                        var.NotToBlock_pass_number += 1
                        var.NotToBlock_number += 1
                    else:
                        var.website_list[count].is_pass = 'F'
                        var.ToBlock_number += 1

            var.ui.updateColum(count, var.website_list[count])
            count += 1
            var.all_number += 1
            if var.execute_flag is False and var.isRepeatEXE is False:

                break
        # every round result add to the list
        var.rounds += 1
        var.all_ToBlock_pass_number.append(var.ToBlock_pass_number)
        var.all_NotToBlock_pass_number.append(var.NotToBlock_pass_number)
        var.all_ToBlock_number.append(var.ToBlock_number)
        var.all_NotToBlock_number.append(var.NotToBlock_number)
        var.all_NotToBlock_na_number.append(var.NotToBlock_na_number)
        var.all_ToBlock_na_number.append(var.ToBlock_na_number)
        var.all_all_number.append(var.all_number)

        var.ui.result(False)
        if var.isRepeatEXE is False:
            var.execute_flag = False
            break
        # Stop in Repeat Execute Mode
        elif var.execute_flag is False and var.isRepeatEXE is True:
            break
        # Repeat Execute
        else:
            time.sleep(4)
            var.website_list_RepeatEXE.append(var.website_list.copy())

    var.ui.Run.setText("Run")
    var.ui.checkBox.setEnabled(True)
    var.ui.result(False)
    ConnectWebsite.CloseBrowser(browser)
    var.isfinished = True

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = QMainWindow()

    var = Var.Var(__browser_type__)

    var.ui = UI.Ui_MainWindow()
    var.ui.setupUi(window,var)
    window.show()

    thread = WTThread()
    thread.start()

    app.exec_()
    sys.exit(app.exit(0))


