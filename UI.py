import IODataFromFile, Var
from PyQt5 import QtCore, QtWidgets,QtGui
import time

class Ui_MainWindow(object):
    var = None  # type: Var.Var
    font_size = 9
    font = "Arial"
    def setupUi(self, MainWindow, var:Var):

        self.var = var

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 620)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFixedSize(800, 650)
        self.centralwidget.setUpdatesEnabled(True)

        self.WebsiteList = QtWidgets.QTableWidget(self.centralwidget)
        self.WebsiteList.setGeometry(QtCore.QRect(10, 50, 400, 500))
        self.WebsiteList.setObjectName("WebsiteList")
        self.WebsiteList.setColumnCount(4)
        self.WebsiteList.setFont(QtGui.QFont(self.font, self.font_size))
        self.WebsiteList.setHorizontalHeaderLabels(['url', 'status code', 'block','pass'])
        self.WebsiteList.horizontalHeader().setSectionsClickable(False)
        self.WebsiteList.setColumnWidth(0, 150)
        self.WebsiteList.setColumnWidth(1, 100)
        self.WebsiteList.setColumnWidth(2, 60)
        self.WebsiteList.horizontalHeader().setSectionResizeMode(3,QtWidgets.QHeaderView.Stretch)
        self.WebsiteList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.WebsiteList.setUpdatesEnabled(True)



        self.Readfile = QtWidgets.QPushButton(self.centralwidget)
        self.Readfile.setGeometry(QtCore.QRect(10, 10, 120, 32))
        self.Readfile.setFont(QtGui.QFont(self.font, self.font_size))

        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(150, 10, 120, 32))
        self.Run.setFont(QtGui.QFont(self.font, self.font_size))

        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(290, 10, 120, 32))
        self.Save.setFont(QtGui.QFont(self.font, self.font_size))

        # Result Statistics
        self.Result_Type = QtWidgets.QLabel(self.centralwidget)
        self.Result_Type.setGeometry(QtCore.QRect(420, 10, 200, 40))
        self.Result_Type.setFont(QtGui.QFont(self.font, self.font_size))
        self.Result_Type.setText("[ This Round ]")

        self.Result_allType = QtWidgets.QLabel(self.centralwidget)
        self.Result_allType.setGeometry(QtCore.QRect(420, 210, 200, 40))
        self.Result_allType.setFont(QtGui.QFont(self.font, self.font_size))
        self.Result_allType.setText("[ All Rounds ]")

        self.Result_meanType = QtWidgets.QLabel(self.centralwidget)
        self.Result_meanType.setGeometry(QtCore.QRect(420, 410, 200, 40))
        self.Result_meanType.setFont(QtGui.QFont(self.font, self.font_size))
        self.Result_meanType.setText("[ Mean ]")

        self.Result_Title = QtWidgets.QLabel(self.centralwidget)
        self.Result_Title.setGeometry(QtCore.QRect(350, 50, 200, 80))
        self.Result_Title.setFont(QtGui.QFont(self.font, self.font_size))
        self.Result_Title.setText("Normal: ALL-\nPass / Fail /N.A. :\n\nBlock: ALL-\nPass / Fail /N.A. :")
        self.Result_Title.setAlignment(QtCore.Qt.AlignRight)

        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(560, 50, 200, 80))
        self.Result.setFont(QtGui.QFont(self.font, self.font_size))
        self.Result.setAlignment(QtCore.Qt.AlignLeft)
        self.Result.setObjectName("Result")
        self.Result.setText(" \n-- / -- / -- \n\n\n-- / -- / --")

        self.all_Result_Title = QtWidgets.QLabel(self.centralwidget)
        self.all_Result_Title.setGeometry(QtCore.QRect(350, 250, 200, 80))
        self.all_Result_Title.setFont(QtGui.QFont(self.font, self.font_size))
        self.all_Result_Title.setText("Normal: ALL-\nPass / Fail /N.A. :\n\nBlock: ALL-\nPass / Fail /N.A. :")
        self.all_Result_Title.setAlignment(QtCore.Qt.AlignRight)

        self.all_Result = QtWidgets.QLabel(self.centralwidget)
        self.all_Result.setGeometry(QtCore.QRect(560, 250, 200, 80))
        self.all_Result.setFont(QtGui.QFont(self.font, self.font_size))
        self.all_Result.setAlignment(QtCore.Qt.AlignLeft)
        self.all_Result.setText(" \n-- / -- / -- \n\n\n-- / -- / --")

        self.mean_Result_Title = QtWidgets.QLabel(self.centralwidget)
        self.mean_Result_Title.setGeometry(QtCore.QRect(350, 450, 200, 80))
        self.mean_Result_Title.setFont(QtGui.QFont(self.font, self.font_size))
        self.mean_Result_Title.setText("Normal: ALL-\nPass / Fail /N.A. :\n\nBlock: ALL-\nPass / Fail /N.A. :")
        self.mean_Result_Title.setAlignment(QtCore.Qt.AlignRight)

        self.mean_Result = QtWidgets.QLabel(self.centralwidget)
        self.mean_Result.setGeometry(QtCore.QRect(560, 450, 200, 80))
        self.mean_Result.setFont(QtGui.QFont(self.font, self.font_size))
        self.mean_Result.setAlignment(QtCore.Qt.AlignLeft)
        self.mean_Result.setText(" \n-- / -- / -- \n\n\n-- / -- / --")

        # Result of Confusion Matrix(CM)
        #                Expected
        #               True False
        #               -----------
        #         True  | TP | FP |
        # Actual        -----------
        #         False | FN | TN |
        #
        self.CM_title = QtWidgets.QLabel(self.centralwidget)
        self.CM_title.setGeometry(QtCore.QRect(350, 150, 200, 100))
        self.CM_title.setFont(QtGui.QFont(self.font, self.font_size))
        self.CM_title.setAlignment(QtCore.Qt.AlignRight)
        self.CM_title.setText("Confusion Matrix\n" +
                              "TP:\n" +
                              "FP:\n" +
                              "TN:\n" +
                              "FN:")
        self.CM_number = QtWidgets.QLabel(self.centralwidget)
        self.CM_number.setGeometry(QtCore.QRect(560, 150, 200, 100))
        self.CM_number.setFont(QtGui.QFont(self.font, self.font_size))
        self.CM_number.setAlignment(QtCore.Qt.AlignLeft)
        self.CM_number.setText("\n --\n --\n --\n --")

        self.all_CM_title = QtWidgets.QLabel(self.centralwidget)
        self.all_CM_title.setGeometry(QtCore.QRect(350, 350, 200, 100))
        self.all_CM_title.setFont(QtGui.QFont(self.font, self.font_size))
        self.all_CM_title.setAlignment(QtCore.Qt.AlignRight)
        self.all_CM_title.setText("Confusion Matrix\n" +
                              "TP:\n" +
                              "FP:\n" +
                              "TN:\n" +
                              "FN:")
        self.all_CM_number = QtWidgets.QLabel(self.centralwidget)
        self.all_CM_number.setGeometry(QtCore.QRect(560, 350, 200, 100))
        self.all_CM_number.setFont(QtGui.QFont(self.font, self.font_size))
        self.all_CM_number.setAlignment(QtCore.Qt.AlignLeft)
        self.all_CM_number.setText("\n --\n --\n --\n --")

        self.mean_CM_number = QtWidgets.QLabel(self.centralwidget)
        self.mean_CM_number.setGeometry(QtCore.QRect(350, 550, 200, 100))
        self.mean_CM_number.setFont(QtGui.QFont(self.font, self.font_size))
        self.mean_CM_number.setAlignment(QtCore.Qt.AlignRight)
        self.mean_CM_number.setText("Confusion Matrix\n" +
                                  "TP:\n" +
                                  "FP:\n" +
                                  "TN:\n" +
                                  "FN:")
        self.mean_CM_number = QtWidgets.QLabel(self.centralwidget)
        self.mean_CM_number.setGeometry(QtCore.QRect(560, 550, 200, 100))
        self.mean_CM_number.setFont(QtGui.QFont(self.font, self.font_size))
        self.mean_CM_number.setAlignment(QtCore.Qt.AlignLeft)
        self.mean_CM_number.setText("\n --\n --\n --\n --")

        # Statistics
        self.Statistics = QtWidgets.QLabel(self.centralwidget)
        self.Statistics.setGeometry(QtCore.QRect(200, 540, 200, 80))
        self.Statistics.setFont(QtGui.QFont(self.font, self.font_size))
        self.Statistics.setText("Number of data: --\nNumber of rounds: --")

        # Setting
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(15, 550, 150, 40))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setFont(QtGui.QFont(self.font, self.font_size))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Readfile.clicked.connect(self.openFile)
        self.Run.clicked.connect(self.setExecuteFlagTrue)
        self.checkBox.stateChanged.connect(self.RepeatEXE)
        self.Save.clicked.connect(self.saveFile)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Website Fillter Tester"))
        self.Readfile.setText(_translate("MainWindow", "Open..."))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Save.setText(_translate("MainWindow", "Save..."))
        self.checkBox.setText(_translate("MainWindow", "Repeat Execution"))

    def RepeatEXE(self):
        self.var.isRepeatEXE = self.checkBox.isChecked()

    def result(self,isInit:bool):
        self.Statistics.setText(
            "Number of data: " + str(self.var.all_number) + "\nNumber of rounds: " + str(self.var.rounds))
        if isInit is True:
            self.Result.setText(" \n-- / -- / -- \n\n\n-- / -- / --")
            self.all_Result.setText(" \n-- / -- / -- \n\n\n-- / -- / --")
            self.mean_Result.setText(" \n-- / -- / -- \n\n\n-- / -- / --")

            self.CM_number.setText("\n --\n --\n --\n --")
            self.all_CM_number.setText("\n --\n --\n --\n --")
            self.mean_CM_number.setText("\n --\n --\n --\n --")
        else:
            if self.var.rounds is 0:
                return
            # 1 Reasult
            # 1.1 result of this round
            pass_number = self.var.NotToBlock_pass_number + self.var.ToBlock_pass_number
            self.Result.setText(str(self.var.NotToBlock_number) + "\n" +
                                str(self.var.NotToBlock_pass_number) + " / " +
                                str(self.var.NotToBlock_number - self.var.NotToBlock_pass_number) + " / " +
                                str(self.var.NotToBlock_na_number) + "\n\n" +
                                str(self.var.ToBlock_number) + "\n" +
                                str(self.var.ToBlock_pass_number) + " / " +
                                str(self.var.ToBlock_number - self.var.ToBlock_pass_number) + " / " +
                                str(self.var.ToBlock_na_number))

            # 1.2 result of all the rounds
            all_pass_number = self.var.sum_list(self.var.all_NotToBlock_pass_number) + \
                              self.var.sum_list(self.var.all_ToBlock_pass_number)
            all_NotToBlock_na_number = self.var.sum_list(self.var.all_NotToBlock_na_number)
            all_ToBlock_na_number = self.var.sum_list(self.var.all_ToBlock_na_number)
            all_all_number = self.var.sum_list(self.var.all_all_number)

            self.all_Result.setText(str(self.var.sum_list(self.var.all_NotToBlock_number)) + "\n" +
                                str(self.var.sum_list(self.var.all_NotToBlock_pass_number)) + " / " +
                                str(self.var.sum_list(self.var.all_NotToBlock_number) -
                                    self.var.sum_list(self.var.all_NotToBlock_pass_number)) + " / " +
                                str(all_NotToBlock_na_number) + "\n\n" +
                                str(self.var.sum_list(self.var.all_ToBlock_number)) + "\n" +
                                str(self.var.sum_list(self.var.all_ToBlock_pass_number)) + " / " +
                                str(self.var.sum_list(self.var.all_ToBlock_number) -
                                    self.var.sum_list(self.var.all_ToBlock_pass_number)) + " / " +
                                str(all_ToBlock_na_number))

            # 1.3 mean
            self.mean_Result.setText(str("%.4f" % (self.var.sum_list(self.var.all_NotToBlock_number)/self.var.rounds))
                                     + "\n" +
                                str("%.4f" % (self.var.sum_list(self.var.all_NotToBlock_pass_number)/self.var.rounds))
                                     + " / " +
                                str("%.4f" % ((self.var.sum_list(self.var.all_NotToBlock_number) -
                                    self.var.sum_list(self.var.all_NotToBlock_pass_number))/self.var.rounds))
                                     + " / " +
                                str("%.4f" % (all_NotToBlock_na_number/self.var.rounds))
                                     + "\n\n" +
                                str("%.4f" % (self.var.sum_list(self.var.all_ToBlock_number)/self.var.rounds))
                                     + "\n" +
                                str("%.4f" % (self.var.sum_list(self.var.all_ToBlock_pass_number) / self.var.rounds))
                                     + " / " +
                                str("%.4f" % ((self.var.sum_list(self.var.all_ToBlock_number) -
                                               self.var.sum_list(self.var.all_ToBlock_pass_number))/self.var.rounds))
                                     + " / " +
                                str("%.4f" % (all_ToBlock_na_number/self.var.rounds)))

            # 2 CM [TP, FP, TN, FN]
            # 2.1
            self.CM_number.setText("\n " + str(self.var.ToBlock_pass_number) +
                                   "\n " + str(self.var.ToBlock_number-self.var.ToBlock_pass_number) +
                                   "\n " + str(self.var.NotToBlock_pass_number) +
                                   "\n " + str(self.var.NotToBlock_number-self.var.NotToBlock_pass_number))
            # 2.2
            all_TP = self.var.sum_list(self.var.all_ToBlock_pass_number)
            all_FP = self.var.sum_list(self.var.all_ToBlock_number) - \
                     self.var.sum_list(self.var.all_ToBlock_pass_number)
            all_TN = self.var.sum_list(self.var.all_NotToBlock_pass_number)
            all_FN = self.var.sum_list(self.var.all_NotToBlock_number) - \
                     self.var.sum_list(self.var.all_NotToBlock_pass_number)
            self.all_CM_number.setText("\n " + str(all_TP) +
                                       "\n " + str(all_FP) +
                                       "\n " + str(all_TN) +
                                       "\n " + str(all_FN))
            # 2.3
            self.mean_CM_number.setText("\n " + str("%.4f" % (all_TP/self.var.rounds)) +
                                        "\n " + str("%.4f" % (all_FP/self.var.rounds)) +
                                        "\n " + str("%.4f" % (all_TN/self.var.rounds)) +
                                        "\n " + str("%.4f" % (all_FN/self.var.rounds)))

        return

    def clearVar(self):
        self.var.execute_flag = False
        self.var.file_path = ""
        self.result(True)

    def clearWLVar(self):
        self.var.website_list.clear()
        self.delAllColum()
        self.result(True)

    def openFile(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(caption="Choose List File")
        if(filepath[0]==''):
            return
        self.clearVar()
        self.clearWLVar()
        self.var.init_number()
        self.var.init_All_number()
        self.var.file_path = filepath[0]
        self.var.isUpdateWebsiteList = True



    def setExecuteFlagTrue(self):
        if self.var.execute_flag is False:
            self.var.execute_flag = True
            self.var.isInit = False
            self.Run.setText("Stop")
            self.checkBox.setEnabled(False)
        elif self.var.isRepeatEXE is True:
            self.Run.setText("Stopping...")
            self.var.execute_flag = False
        else:
            self.var.execute_flag = False


    def saveFile(self):
        if self.var.execute_flag is True:
            return
        timestr = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filepath = QtWidgets.QFileDialog.getExistingDirectory(caption="Choose Save File Path")

        if filepath is not '':
            file_result = IODataFromFile.OpenFile(str(filepath)+"/WF_"+timestr+"_record.csv",'w')
            file_statistics = IODataFromFile.OpenFile(str(filepath) + "/WF_" + timestr + "_statistics.csv", 'w')

            pass_number = self.var.NotToBlock_pass_number + self.var.ToBlock_pass_number
            all_pass_number = self.var.sum_list(self.var.all_NotToBlock_pass_number) + \
                              self.var.sum_list(self.var.all_ToBlock_pass_number)
            all_NotToBlock_na_number = self.var.sum_list(self.var.all_NotToBlock_na_number)
            all_ToBlock_na_number = self.var.sum_list(self.var.all_ToBlock_na_number)
            all_all_number = self.var.sum_list(self.var.all_all_number)
            all_TP = self.var.sum_list(self.var.all_ToBlock_pass_number)
            all_FP = self.var.sum_list(self.var.all_ToBlock_number) - self.var.sum_list(
                self.var.all_ToBlock_pass_number)
            all_TN = self.var.sum_list(self.var.all_NotToBlock_pass_number)
            all_FN = self.var.sum_list(self.var.all_NotToBlock_number) - self.var.sum_list(
                self.var.all_NotToBlock_pass_number)

            IODataFromFile.WriteFile(file_result, str("ROUND")
                                     + "," + str("WEBSITE_URL")
                                     + "," + str("STATUS_CODE")
                                     + "," + str("TO_BLOCK")
                                     + "," + str("PASS"))
            count = 0
            print(len(self.var.website_list_RepeatEXE))
            if self.var.isRepeatEXE is True and len(self.var.website_list_RepeatEXE) > 1:
                count = len(self.var.website_list_RepeatEXE)

                for i in self.var.website_list_RepeatEXE:
                    for j in i:
                        IODataFromFile.WriteFile(file_result, str(count)
                                                 + "," + str(j.website_url)
                                                 + "," + str(j.status_code)
                                                 + "," + str(j.to_block)
                                                 + "," + str(j.is_pass))
            else:
                count = 1
                for i in self.var.website_list:
                    IODataFromFile.WriteFile(file_result, str(count)
                                             + "," + str(i.website_url)
                                             + "," + str(i.status_code)
                                             + "," + str(i.to_block)
                                             + "," + str(i.is_pass))



            IODataFromFile.WriteFile(file_statistics, str("ROUND")
                                     + "," + str("PASS")
                                     + "," + str("ALL")
                                     + "," + str("NA")
                                     + "," + str("FAIL"))
            for i in range(count):
                IODataFromFile.WriteFile(file_statistics, str(i)
                                         + "," + str(self.var.all_NotToBlock_pass_number[i] +
                                                     self.var.all_ToBlock_pass_number[i])
                                         + "," + str(self.var.all_all_number[i])
                                         + "," + str(self.var.all_NotToBlock_na_number[i] +
                                                     self.var.all_ToBlock_na_number[i])
                                         + "," + str(self.var.all_all_number[i] -
                                                     (self.var.all_NotToBlock_na_number[i] +
                                                      self.var.all_ToBlock_na_number[i]) -
                                                     self.var.all_ToBlock_pass_number[i] -
                                                     self.var.all_NotToBlock_pass_number[i]))
            IODataFromFile.WriteFile(file_statistics, str("all")
                                     + "," + str(all_pass_number)
                                     + "," + str(all_all_number)
                                     + "," + str(all_NotToBlock_na_number+all_ToBlock_na_number)
                                     + "," + str(all_all_number - (all_NotToBlock_na_number+all_ToBlock_na_number) -
                                                 all_pass_number))
            IODataFromFile.WriteFile(file_statistics,str("mean")
                                     + "," + str(all_pass_number/self.var.rounds)
                                     + "," + str(all_all_number/self.var.rounds)
                                     + "," + str((all_NotToBlock_na_number+all_ToBlock_na_number)/self.var.rounds)
                                     + "," + str((all_all_number - (all_NotToBlock_na_number+all_ToBlock_na_number) -
                                                  all_pass_number)/self.var.rounds))

            # Confusion Matrix
            IODataFromFile.WriteFile(file_statistics, str("ROUND")
                                     + "," + str("TP")
                                     + "," + str("FP")
                                     + "," + str("TN")
                                     + "," + str("FN"))
            for i in range(count):
                IODataFromFile.WriteFile(file_statistics, str(i)
                                         + "," + str(self.var.all_ToBlock_pass_number[i])
                                         + "," + str(self.var.all_ToBlock_number[i] -
                                                     self.var.all_ToBlock_pass_number[i])
                                         + "," + str(self.var.all_NotToBlock_pass_number[i])
                                         + "," + str(self.var.all_NotToBlock_number[i] -
                                                     self.var.all_NotToBlock_pass_number[i]))
            IODataFromFile.WriteFile(file_statistics, str("all")
                                     + "," + str(all_TP)
                                     + "," + str(all_FP)
                                     + "," + str(all_TN)
                                     + "," + str(all_FN))
            IODataFromFile.WriteFile(file_statistics, str("mean")
                                     + "," + str(all_TP/self.var.rounds)
                                     + "," + str(all_FP/self.var.rounds)
                                     + "," + str(all_TN/self.var.rounds)
                                     + "," + str(all_FN/self.var.rounds))
        print("Finish")
        return

    def addColum(self, website):
        row = self.WebsiteList.rowCount()
        self.WebsiteList.setRowCount(row + 1)
        self.WebsiteList.setItem(row, 0, QtWidgets.QTableWidgetItem(website.website_url))
        self.WebsiteList.setItem(row, 1, QtWidgets.QTableWidgetItem(website.status_code))
        self.WebsiteList.setItem(row, 2, QtWidgets.QTableWidgetItem(website.to_block))
        self.WebsiteList.setItem(row, 3, QtWidgets.QTableWidgetItem(website.is_pass))


    def updateColum(self, row: int, website):
        print(website.website_url, website.status_code, website.is_pass)
        self.WebsiteList.setItem(row, 0, QtWidgets.QTableWidgetItem(website.website_url))
        self.WebsiteList.setItem(row, 1, QtWidgets.QTableWidgetItem(website.status_code))
        self.WebsiteList.setItem(row, 2, QtWidgets.QTableWidgetItem(website.to_block))
        self.WebsiteList.setItem(row, 3, QtWidgets.QTableWidgetItem(website.is_pass))
        self.WebsiteList.updateGeometry()

    def delAllColum(self):
        count = self.WebsiteList.rowCount()
        while count > 0:
            self.WebsiteList.removeRow(0)
            count -= 1

