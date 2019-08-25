from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import chrome, firefox
from selenium.webdriver.chrome.options import Options

def getHttpStatus(browser):
    for responseReceived in browser.get_log('performance'):
        try:
            response = json.loads(responseReceived[u'message'])[u'message'][u'params'][u'response']
            if response[u'url'] == browser.current_url:
                # Success
                return (response[u'status'],browser.current_url)
        except Exception as e:
            print("[getHttpStatus(response_http]" + str(e))

            pass
        try:
            response = json.loads(responseReceived[u'message'])[u'message'][u'params']

            # Blocked in 'HTTPS', and there exist "ERR_SSL_PROTOCOL_ERROR"
            if (response[u'errorText'].find("ERR_SSL_PROTOCOL_ERROR") >= 0):
                return (-1, browser.current_url)
        except Exception as e:
            print("[getHttpStatus(response_https)]" + str(e))
            pass
    # Fail
    return False

def isRedirection(currentURL:str,redirecttionURL:str):
    if(currentURL.find(redirecttionURL)>=0):
        return True
    else:
        return False

def CreateBrowser(browser:str):
    '''

    :param browser: {"Firefox","Chrome"}
    :return: webdriver

    '''
    if(browser == "Firefox"):
        return webdriver.Firefox(executable_path=firefox.GeckoDriverManager().install(),
                                service_args=["--verbose", "--log-path=./firefoxdriverxx.log"],
                                desired_capabilities=getDesiredCapabilities("firefox"))

    option = webdriver.ChromeOptions()
    option.add_argument('--ignore-certificate-errors')
    return webdriver.Chrome(executable_path=chrome.ChromeDriverManager().install(),
                            service_args=["--verbose", "--log-path=./chromedriverxx.log"],
                            desired_capabilities=getDesiredCapabilities("chrome"),
                            chrome_options=option)
def InitBrowser(browser):
    browser.set_page_load_timeout(60)
    # browser.minimize_window()

def ConnectWebsite(browser,URL):
    try:
        print(URL)
        browser.get(URL)
    except Exception as e:
        print("[ConnectWebsite]"+str(e))
        return False

    result = getHttpStatus(browser)

    if(result == False):
        return False
    elif(result[0]==-1):
        return (result, True)
    else:
        return (result,isRedirection(result[1],"twb.moe.edu.tw"))


def CloseBrowser(browser):
    try:
        browser.close()
        browser.quit()
    except Exception as e:
        print("[ClearBrowser]"+str(e))
        pass

def getDesiredCapabilities(browser):
    d = None
    if(browser == "chrome"):

        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = {'performance': 'ALL'}
    elif(browser == "firefox"):
        d = DesiredCapabilities.FIREFOX
        d['loggingPrefs'] = {'performance': 'ALL'}
    return d


