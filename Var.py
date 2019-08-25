import ConnectWebsite, IODataFromFile, UI, Var

class Var:
    def __init__(self, browser_type: str):
        # Debug
        self.debug = True
        self.error_text = str
        # File
        self.file_path = str  # Input File Path

        # List to Save Input Data
        self.website_list = []
        self.website_isBlock = []             # True: the website is to be block /False: the website isn't to be block
        self.website_list_RepeatEXE = []      # save website_list for  repeat execution

        # List to Save Result
        self.rounds = 0
        self.all_number = 0                   # Sum of this round number of input website
        self.NotToBlock_pass_number = 0       # Sum of this round number of pass website that not be blocked
        self.ToBlock_pass_number = 0          # Sum of this round number of pass website that be blocked
        self.NotToBlock_na_number = 0         # Sum of this round number of no reply website that not be blocked
        self.ToBlock_na_number = 0            # Sum of this round number of no reply that be blocked
        self.ToBlock_number = 0               # Sum of this round number of to block and not including na
        self.NotToBlock_number = 0            # Sum of this round number of not to block and not including na

        self.all_all_number = []              # Sum of all round number of website
        self.all_NotToBlock_pass_number = []  # Sum of all round number of pass website that not be blocked
        self.all_ToBlock_pass_number = []     # Sum of all round number of pass website that be blocked
        self.all_NotToBlock_na_number = []    # Sum of all round number of no reply website that not be blocked
        self.all_ToBlock_na_number = []       # Sum of all round number of no reply website that be blocked
        self.all_ToBlock_number = []          # Sum of all round number of to block and not including na
        self.all_NotToBlock_number = []       # Sum of all round number of not to block and not including na

        # UI
        self.ui = None                     # Main Windows. type:  UI
        self.isUpdateWebsiteList = False   # Flag that if read input data success, then set "True"

        # Execution Config
        self.isfinished = True
        self.isRepeatEXE = False
        self.browser_type = str    # browser type. ex:Chrome, Firefox, etc.
        self.execute_flag = False  # the test is executing

    def input_website_list(self):
        self.ui.clearWLVar()
        ListURL = IODataFromFile.getWebsiteList(self.file_path)
        if (ListURL == False):
            return False
        else:
            # i[0]:url, i[1]:is_block
            for i in ListURL:
                self.website_list.append(Website(url=i[0], to_block=i[1]))
                self.ui.addColum(self.website_list[len(self.website_list) - 1])
        return ListURL

    # initial the var(this round):
    def init_number(self):
        self.all_number = 0
        self.NotToBlock_pass_number = 0
        self.ToBlock_pass_number = 0
        self.ToBlock_na_number = 0
        self.NotToBlock_na_number = 0
        self.ToBlock_number = 0
        self.NotToBlock_number = 0

    # initial the var(all rounds):
    def init_All_number(self):
        self.rounds = 0
        self.all_all_number.clear()
        self.all_NotToBlock_pass_number.clear()
        self.all_ToBlock_pass_number.clear()
        self.all_ToBlock_na_number.clear()
        self.all_NotToBlock_na_number.clear()
        self.all_ToBlock_number.clear()
        self.all_NotToBlock_number.clear()

    def sum_list(self, lst):
        sum = 0
        for i in lst:
            sum += i
        return int(sum)


    # Class to Save Input
class Website:
    website_url = ''
    status_code = ''
    to_block = ''      # the website is illegal and to be block, then set "T", otherwise set 'F'
    is_pass = ''       # pass the the website blocking function, then set "T", otherwise set 'F'

    def __init__(self,url: str,to_block: bool):
        self.website_url = url
        self.to_block = to_block
