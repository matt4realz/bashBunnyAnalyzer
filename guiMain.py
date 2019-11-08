import tkinter as tk
import time
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import Button, Tk, HORIZONTAL
import fpdf
import unicodedata
from os import getcwd
from tkinter import filedialog


"""For Derek's Services"""
import pandas as pd

"""For Farid URL"""
import re
from collections import OrderedDict
import urllib
from urllib.parse import urlparse


class MainGui(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        global profilingList
        profilingList = {}
        global flist
        flist = []
        global wordList
        wordList = []
        global displaySim
        displaySim = float(0.0)
        global barVar
        barVar = 0

        global d_descending
        d_descending = []

        global stopwords
        self.stopwords = []

        global systemDefence
        systemDefence = []

        global drama
        drama = ['kissasian.sh']

        global pornSites
        pornSites = ['Pornhub', 'xvideos']

        global messengers
        messengers = ['web.whatsapp.com', 'web.telegram.com']

        global schoolSites
        schoolSites = ['myportal.nus.edu.sg', 'NTU', 'xsite.singaporetech.edu.sg', 'SUTD']

        global socialMedia
        socialMedia = ['facebook.com', 'Instagram', 'Twitter']

        global terrorism
        terrorism = ["bombs", "guns", "grenade", "fire"]

        global searchSites
        searchSites = ["google", "bing", "yahoo"]

        global healthFitness
        healthFitness = ['www.menshealth.com']

        with open("filesForTesting/stopwords.txt", "r") as filestream:
            for line in filestream:
                currentline = line.split(",")
                for x in currentline:
                    self.stopwords.append(x)

        """title START"""
        title_frame = tk.Frame(self, bd=10, bg="black")
        title_frame.grid(row=0, column=0, columnspan=12, sticky=(tk.W, tk.E))
        heading = tk.Label(title_frame, text="Team NoSleep BashBunny Analyzer", font=("arial", 20, "bold"),
                           fg="white", bg="black")
        heading.grid(row=0, column=1)
        title_frame.grid_columnconfigure(0, weight=1)  # fill up empty spaces to left of heading
        title_frame.grid_columnconfigure(2, weight=1)  # fill up empty spaces to right of heading
        """title END"""

        """Investigation Detail Start Here"""
        investigation_row_frame = tk.Frame(self, bd=10, bg="black")
        investigation_row_frame.grid(row=1, column=0, columnspan=12, sticky=(tk.W, tk.E))

        case_id_lbl = tk.Label(investigation_row_frame, text="Case ID :", bg="black", fg="white", padx=27.5, font="bold")
        case_id_lbl.grid(row=0, column=1)
        case_id_input = tk.Entry(investigation_row_frame, width=20, bg="white", fg="black")
        case_id_input.grid(row=0, column=2)

        lead_invest_lbl = tk.Label(investigation_row_frame, text="Lead Investigator :", bg="black", fg="white", padx=2, font="bold")
        lead_invest_lbl.grid(row=1, column=1)
        lead_invest_input = tk.Entry(investigation_row_frame, width=20, bg="white", fg="black")
        lead_invest_input.grid(row=1, column=2)

        extract_date_lbl = tk.Label(investigation_row_frame, text="Extracted Date :", bg="black", fg="white", padx=9, font="bold")
        extract_date_lbl.grid(row=2, column=1)
        extract_date_input = tk.Entry(investigation_row_frame, width=20, bg="white", fg="black")
        extract_date_input.grid(row=2, column=2)

        """Investigation Detail End Here"""



        """Button Frame"""
        button_row_frame = tk.Frame(self, bd=10, bg="black")
        button_row_frame.grid(row=2, column=0, columnspan=12, sticky=(tk.W, tk.E))


        """Do All Method Button Starts Here"""
        analysis_btn = tk.Button(button_row_frame, text="Analyze Files", bg="white", fg="black", font="bold", padx="30", command=lambda: self.loadBar() &
                                                                                         self.urlHistory(url_text,
                                                                                                         self.stopwords) & self.servicesAnalysis(
            services_text)
                                                                                         & self.hardwareAnalysis(
            hardware_text)
                                                                                         & self.profilingAnalysis(
            profiling_text,pdf_btn))
        analysis_btn.grid(row=0, column=1)
        """Do All Method Button Ends Here"""

        """PDF Button"""
        pdf_btn = tk.Button(button_row_frame, text="Export To PDF", bg="white", fg="black", font="bold", padx="30", command=lambda: self.exportPDF(case_id_input,
                                                                                                   lead_invest_input,
                                                                                                   extract_date_input,
                                                                                                   profiling_text, url_text))
        pdf_btn.grid(row=0, column=2)
        """PDF Button"""



        


        """loadingBar Starts Here"""
        maxVal = 100
        currentVal = 0
        loadingBarFrame = tk.Frame(self, bd=10, bg="black")
        loadingBarFrame.grid(row=5, column=0, columnspan=12, sticky=(tk.W, tk.E))
        self.loadingBar = Progressbar(loadingBarFrame, orient=HORIZONTAL, length=1350, mode='determinate')
        self.loadingBar.grid(row=0, column=1)
        """loadingBar Ends Here"""

        """URL Text Area Starts Here"""
        analysis_frame = tk.Frame(self, bd=10, bg="black")
        analysis_frame.grid(row=6, column=0, sticky=tk.W)

        url_text = tk.Text(analysis_frame, width=56, height=17, state=DISABLED, bg="black", fg="white")
        url_text.grid(row=1, column=1)
        url_file_txt = tk.Label(analysis_frame, text="URL History", bg="black", fg="white", font="bold")
        url_file_txt.grid(row=0, column=1)
        """URL Text Area Ends Here"""

        """Services Text Start Here"""
        services_text = tk.Text(analysis_frame, width=56, height=17, state=DISABLED, bg="black", fg="white")
        services_text.grid(row=1, column=2)
        services_file_txt = tk.Label(analysis_frame, text="Target's Running Services", bg="black", fg="white", font="bold")
        services_file_txt.grid(row=0, column=2)
        """Services Text Ends Here"""

        """Hardware Text Area Start Here"""
        hardware_text = tk.Text(analysis_frame, width=56, height=17, state=DISABLED, bg="black", fg="white")
        hardware_text.grid(row=1, column=3)
        hardware_file_txt = tk.Label(analysis_frame, text="Hardware", bg="black", fg="white", font="bold")
        hardware_file_txt.grid(row=0, column=3)
        """Hardware Text Area Ends Here"""

        """Profiling Text Area Start Here"""
        profiling_frame = tk.Frame(self, bd=10, bg="black")
        profiling_frame.grid(row=7, column=0)

        profiling_text = tk.Text(profiling_frame, width=171, height=13, state=DISABLED, bg="black", fg="white")
        profiling_text.grid(row=1, column=1)
        profiling_file_txt = tk.Label(profiling_frame, text="Profiling", bg="black", fg="white", font="bold")
        profiling_file_txt.grid(row=0, column=1)
        """Profiling Text Area Ends Here"""

    def loadBar(self):
        currentVal = 0
        maxVal = 20
        self.loadingBar['value'] = currentVal
        for i in range(maxVal):
            currentVal = currentVal + 10
            time.sleep(0.05)
            self.loadingBar['value'] = currentVal
            self.loadingBar.update()
        return 0

    def loadBarReset(self):
        self.loadingBar['value'] = 0
        self.loadingBar.update()
        return 0

    # Click listeners START

    @staticmethod
    def urlHistory(url_text, stopwords):
        url_text.config(state="normal")

        '''declare variables'''
        dictionary = {}
        analysis_text_path = 'filesForTesting/Browser History.txt'
        analysis_lines = []
        path = []
        url_main_key = []

        print("\n")

        '''Encapsulated function to get rid of URL encoding characters,
         split URLs into words and append to global array wordList'''

        def getWordsFromURL(url):
            url = re.sub(r'[^\x00-\x7F]+', '', url)
            '''gets rid of URL encoding characters for example %2f, %21, %22'''
            #url = urllib.parse.unquote(url)
            '''split url into words'''
            words = re.compile(r'[\:/?=\-&\#\+]+', re.UNICODE).split(url)
            for word in words:
                if word.lower() not in stopwords and len(word) > 2:
                    wordList.append(word.lower())

        '''Open file and read lines'''
        with open(analysis_text_path) as fp:
            '''add the first line to array'''
            line = fp.readline()
            analysis_lines.append(line)
            cnt = 1
            while line:
                '''print("Index {}: {}".format(cnt, line.strip())) #uncomment this to view index of array'''
                '''add subsequent lines to array'''
                line = fp.readline()
                if not line == '' or not line == '\n':
                    analysis_lines.append(line)
                    cnt += 1

        '''Make use of getWordsFromURL function to append keywords to wordList'''
        for i in analysis_lines:
            getWordsFromURL(i.strip("\n"))

        '''Store words into dictionary'''
        for items in wordList:
            dictionary[items] = (wordList.count(items))

        '''sort by value descending'''
        d_descending = OrderedDict(sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True))
        global urlDictionary
        urlDictionary = d_descending.copy()

        '''print to console'''
        for key, value in d_descending.items():
            url_text.insert(END, key + ' - ' + str(value))
            url_text.insert(END, '\n')

        '''print to GUI'''
        analysis_lines = ("".join(analysis_lines))
        path = ("".join(path))
        url_main_key = ("".join(url_main_key))



        url_text.config(state=DISABLED)
        return 0

    @staticmethod
    def servicesAnalysis(services_text):
        services_text.config(state="normal")
        servicesPath = 'filesForTesting/Services.txt'
        global servicesList
        servicesList = []
        global systemDefence
        systemDefence = ['1Password', 'Bitlocker', 'Dashlane', 'Windows Defender Antivirus Service', 'McAfee AP Service',
                         'McAfee Firewall Core Service',
                         'McAfee Module Core Service', 'McAfee PEF Service',
                         'McAfee Security Scan Component Host Service',
                         'McAfee Service Controller', 'McAfee Validation Trust Protection Service', 'McAfee WebAdvisor',
                         'NordVPN', 'PyCharm IDE']

        services_text.config(state="normal")

        """Begin Method Here"""
        service_file = pd.read_fwf(servicesPath)
        service_file.columns = ["State", "Name", "App", "Path"]
        for line in service_file.Name[1:]:
            servicesList.append(line)

        servicesList.sort()

        global servicesPaths1
        servicesPaths1 = servicesList.copy()

        if all(elem in systemDefence for elem in servicesList):
            systemDefence = systemDefence.copy()

        systemDefence = ('\n'.join(systemDefence))


        services_text.insert(END, ('\n'.join(servicesList)))

        services_text.config(state=DISABLED)
        return 0

    @staticmethod
    def hardwareAnalysis(hardware_text):
        hardware_text.config(state="normal")


        """Begin Method Here"""

        service_file = pd.read_csv("filesForTesting/Hard Disk.txt", sep="\s+", header=None,
                                   names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        count_row = service_file.shape[0]
        i = 2
        global storagedevice
        storagedevice = []

        while (i < count_row):
            if re.search("Rem", service_file.b[i]):
                storagedevice.append(
                    "Storage name: " + service_file.a[i] + ", Storage Size: " + service_file.f[i] + "GB, Free Space: " +
                    service_file.j[i] + '\n')
            elif re.search("Fixed", service_file.b[i]):
                storagedevice.append(
                    "Storage name: " + service_file.a[i] + ", Storage Size: " + service_file.g[i] + "GB, Free Space: " +
                    service_file.j[i] + '\n')
            i += 1;
        storagedevice = ("".join(storagedevice))

        global windows
        windows = []
        cpu_file = pd.read_csv("filesForTesting/CPU.txt", delim_whitespace=True, header=None,
                                   names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        windows.append(
            "Hardware Specs: " + cpu_file.c[1] + cpu_file.d[1] + cpu_file.e[1] + cpu_file.f[1] + cpu_file.g[1] +
            cpu_file.h[1])
        windows = ("\n".join(windows))

        global os_info
        os_info = []
        operatingsys = pd.read_csv("filesForTesting/Operating System.txt", delim_whitespace=True, header=None,
                                       names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        os_info.append("OS: " + operatingsys.c[0] + " " + operatingsys.d[0] + " " + operatingsys.e[0])
        os_info = ("\n".join(os_info))


        user_file = pd.read_csv("filesForTesting/Local-User.txt", delim_whitespace=True, header=None,
                                    names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        count_row = user_file.shape[0]
        i = 2
        global users
        users = []
        while (i < count_row):
            users.append(user_file.c[i])
            i = i + 1;
        users = ("\n".join(users))


        ram = pd.read_csv("filesForTesting/RAM.txt", delim_whitespace=True, header=None,
                              names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        count_row = ram.shape[0]
        i = 3
        global ram_info
        ram_info = []
        while (i < count_row):
            ram_info.append("Ram Chips: " + ram.a[i] + " " + ram.b[i] + " Total Ram: " + ram.a[0])
            i = i + 1;
        ram_info = ("\n".join(ram_info))


        win_user_pass = pd.read_csv("filesForTesting/Windows User Passwords.txt", delim_whitespace=True, header=None,
                                        names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        count_row = win_user_pass.shape[0]
        i = 2
        global passwordlist
        passwordlist = []
        while (i < count_row):
            passwordlist.append(
                    "URL: " + win_user_pass.a[i] + '\n' + "Username: " + win_user_pass.b[i] + '\n' + "Password: " + win_user_pass.c[
                        i] + '\n')
            i = i + 1;
        passwordlist = ("\n".join(passwordlist))

        win_wifi_pass = pd.read_csv("filesForTesting/Wifi Password.txt", delim_whitespace=True, header=None,
                                    names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        count_row = win_wifi_pass.shape[0]
        i = 2
        wifi_pass = []
        while (i < count_row):
            if (win_wifi_pass.b[i] != 'The'):
                wifi_pass.append("WIFI Name " + win_wifi_pass.a[i] + '\n' + "Password: " + win_wifi_pass.b[i] + '\n')
                i = i + 1
            else:
                i = i + 1
        wifi_pass = ("\n".join(wifi_pass))

        computer_ip = pd.read_csv("filesForTesting/Network.txt", delim_whitespace=True, header=None,
                                  names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        user = []
        user.append("COMPUTER MAC ADDRESS: " + computer_ip.d[0] + '\n')
        user.append("COMPUTER IP ADDRESS: " + computer_ip.d[1] + '\n')
        user.append("PUBLIC IP ADDRESS: " + computer_ip.d[2] + '\n')

        user = ("\n".join(user))

        hardware_text.insert(END, '-----USB Storage Devices-----')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, storagedevice + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, '-----Hardware Specs-----')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, windows + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, '-----OS Installed-----')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, os_info + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, '-----User Accounts-----' + '\n')
        hardware_text.insert(END, users + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, '-----Installed Ram-----' + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, ram_info + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, '-----Extracted User Accounts-----' + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, passwordlist + '\n')
        hardware_text.insert(END, '-----Extracted WIFI Accounts-----' + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, wifi_pass + '\n')
        hardware_text.insert(END, '-----IP ADDRESS-----' + '\n')
        hardware_text.insert(END, '\n')
        hardware_text.insert(END, user + '\n')
        hardware_text.config(state=DISABLED)
        return 0


    @staticmethod
    def profilingAnalysis(profiling_text, pdf_btn):
        profiling_text.config(state="normal")


        """Begin URL Analysis Here"""
        for key, value in urlDictionary.items():
            if value >= 40:
                if key in socialMedia:
                    profiling_text.insert(END,
                                          'The user uses a lot of social media, the site that was visited the most was ')
                    profiling_text.insert(END, "'" + key + "' " + str(value) + ' times')
                    profiling_text.insert(END,
                                          ' this suggests that the target uses social media for browsing often.' + '\n')
                    profilingList[key] = key
                    profilingList[value] = value
                if key in schoolSites:
                    profiling_text.insert(END,
                                          'Based on the number of times the user visited ' + "'" + key + "'"
                                          + ' student portal a total of ' + str(
                                              value) + ' times' + ', this suggests that the user is likely to be a student there.' + '\n')

                    profilingList[key] = key
                    profilingList[value] = value
                if key in messengers:
                    profiling_text.insert(END, 'The messenging app that the user uses the most often is ')
                    profiling_text.insert(END, "'" + key + "' " + str(value) + ' times,')
                    profiling_text.insert(END,
                                          ' this suggests that the target might have used this messenging site as a means of communication.' + '\n')
                    profilingList[key] = key
                    profilingList[value] = value

                if key in drama:
                    profiling_text.insert(END,
                                          'The target also happens to be a major fan of Drama, with the most visited site being ')
                    profiling_text.insert(END, "'" + key + "' " + str(value) + ' times \n')
                    profilingList[key] = key
                    profilingList[value] = value


                if key in healthFitness:
                    profiling_text.insert(END, 'The target displays potential narcissistic / self-concious traits '
                                               'as the target has viewed ' + "'" + key + "'" + ' a total of ' + "'" + str(value) + "'" + ' times.')

                    profiling_text.insert(END, '\n')
                    profilingList[key] = key
                    profilingList[value] = value

        """Begin Services Analysis Here"""
        if systemDefence != '':
            profiling_text.insert(END, '\n')
            profiling_text.insert(END, "Target's Potential Defences")
            profiling_text.insert(END, '\n')
            profiling_text.insert(END, '===========================')
            profiling_text.insert(END, '\n')
            profiling_text.insert(END, systemDefence)
            profiling_text.insert(END, '\n')
        if any("VPN" or "Password" in s for s in systemDefence):
            profiling_text.insert(END, '\n')
            profiling_text.insert(END, "It should be noted that the Target has VPN's and/or Password Managers "
                                       "Installed on their computer. This shows that the target is likely one who is "
                                       "tech savvy and might have stored key password information within his "
                                       "computer." + '\n')

        """Begin Hardware Analysis Here"""

        profiling_text.config(state=DISABLED)
        pdf_btn.config(state="normal")
        return 0


    @staticmethod
    def reset_frame(url_input_path, url_text, url_button_btn):
        url_input_path.config(text="")
        url_text.config(text="")
        url_button_btn.config(state="normal")
        return 0



    @staticmethod
    def exportPDF(case_id_input, lead_invest_input, extract_date_input, profiling_text, url_text):

        pdf = fpdf.FPDF(format='letter')
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.write(12, "Team NoSleep's BashBunny Analyzer")
        pdf.ln()
        pdf.write(10, "=================================")
        pdf.ln()
        pdf.write(8, "Case ID : "+str(case_id_input.get()))
        pdf.ln()
        pdf.write(8, "Lead Investigator : "+str(lead_invest_input.get()))
        pdf.ln()
        pdf.write(8, "Data Extracted Date : " + str(extract_date_input.get()))
        pdf.ln()
        pdf.ln()
        pdf.write(10, "URL Keyword and Hit Counts :")
        pdf.ln()
        pdf.write(10, "=================================")
        pdf.ln()
        for k,v in urlDictionary.items():
            if v > 15:
                pdf.write(8, k + ' - ' + str(v)+'hits')
                pdf.ln()

        pdf.ln()
        pdf.write(10, "=================================")
        pdf.ln()
        pdf.write(10, "Target System Services :")
        pdf.ln()
        pdf.write(10, "=================================")
        pdf.ln()

        for line in servicesPaths1:
            pdf.write(8, line)
            pdf.ln()

        pdf.write(8, "Target Hardware Data : ")
        pdf.ln()
        pdf.write(8, "========================")
        pdf.ln()


        pdf.write(8, storagedevice)
        pdf.ln()
        pdf.write(8, windows)
        pdf.ln()
        pdf.write(8, os_info)
        pdf.ln()
        pdf.ln()
        pdf.write(8, users)
        pdf.ln()
        pdf.ln()
        pdf.write(8, ram_info)
        pdf.ln()
        pdf.ln()
        pdf.write(8, passwordlist)
        pdf.ln()
        pdf.ln()

        pdf.write(8, "Target Personality Analysis : ")
        pdf.ln()
        pdf.write(8, "==============================")
        pdf.ln()
        pdf.write(8, profiling_text.get("1.0", END))

        pdf.output("Report.pdf")

        return 0







