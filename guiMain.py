import tkinter as tk
import time
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import Button, Tk, HORIZONTAL
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
            profiling_text))
        analysis_btn.grid(row=0, column=1)
        """Do All Method Button Ends Here"""



        


        """loadingBar Starts Here"""
        maxVal = 100
        currentVal = 0
        loadingBarFrame = tk.Frame(self, bd=10, bg="black")
        loadingBarFrame.grid(row=5, column=0, columnspan=12, sticky=(tk.W, tk.E))
        self.loadingBar = Progressbar(loadingBarFrame, orient=HORIZONTAL, length=1500, mode='determinate')
        self.loadingBar.grid(row=0, column=1)
        """loadingBar Ends Here"""

        """URL Text Area Starts Here"""
        analysis_frame = tk.Frame(self, bd=10, bg="black")
        analysis_frame.grid(row=6, column=0, sticky=tk.W)

        url_text = tk.Text(analysis_frame, width=62, height=25, state=DISABLED, bg="black", fg="white")
        url_text.grid(row=1, column=1)
        url_file_txt = tk.Label(analysis_frame, text="URL History", bg="black", fg="white", font="bold")
        url_file_txt.grid(row=0, column=1)
        """URL Text Area Ends Here"""

        """Services Text Start Here"""
        services_text = tk.Text(analysis_frame, width=62, height=25, state=DISABLED, bg="black", fg="white")
        services_text.grid(row=1, column=2)
        services_file_txt = tk.Label(analysis_frame, text="Target's Running Services", bg="black", fg="white", font="bold")
        services_file_txt.grid(row=0, column=2)
        """Services Text Ends Here"""

        """Hardware Text Area Start Here"""
        hardware_text = tk.Text(analysis_frame, width=62, height=25, state=DISABLED, bg="black", fg="white")
        hardware_text.grid(row=1, column=3)
        hardware_file_txt = tk.Label(analysis_frame, text="Hardware", bg="black", fg="white", font="bold")
        hardware_file_txt.grid(row=0, column=3)
        """Hardware Text Area Ends Here"""

        """Profiling Text Area Start Here"""
        profiling_frame = tk.Frame(self, bd=10, bg="black")
        profiling_frame.grid(row=7, column=0)

        profiling_text = tk.Text(profiling_frame, width=187, height=17, state=DISABLED, bg="black", fg="white")
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
    def prompt_sheet_location(self):
        """
        Ask the user to select which sheet to use
        :return: String, path of py file
        """
        current_working_directory = getcwd()  # where the code is ran from
        filename = filedialog.askopenfilename(initialdir=current_working_directory, title="Select py file",
                                              filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

        flist.append(filename)

        print(flist)

    @staticmethod
    def urlHistory(url_text, stopwords):
        url_text.config(state="normal")

        '''declare variables'''
        dictionary = {}
        analysis_text_path = 'filesForTesting/browser2.txt'
        analysis_lines = []
        path = []
        url_main_key = []

        print("\n")

        '''Encapsulated function to get rid of URL encoding characters,
         split URLs into words and append to global array wordList'''

        def getWordsFromURL(url):
            '''gets rid of URL encoding characters for example %2f, %21, %22'''
            url = urllib.parse.unquote(url)
            '''split url into words'''
            words = re.compile(r'[\:/?=\-&\#\+]+', re.UNICODE).split(url)
            for word in words:
                if word.lower() not in stopwords and len(word) > 2:
                    wordList.append(word.lower())

        '''Open file and read lines'''
        with open(analysis_text_path, encoding='utf-16') as fp:
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
        service_file = pd.read_fwf(servicesPath, encoding='utf-16')
        service_file.columns = ["State", "Name", "App", "Path"]
        for line in service_file.Name[1:]:
            servicesList.append(line)

        servicesList.sort()

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

        service_file = pd.read_csv("filesForTesting/Hard Disk.txt", delim_whitespace=True, header=None,
                                       names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], encoding='utf-16')
        count_row = service_file.shape[0]
        i = 2
        storagedevice = []
        while (i < count_row):
            storagedevice.append(
                "Storage name: " + str(service_file.a[i]) + ", Storage Size: " + str(service_file.f[i]) + "GB, Free Space: " +
                str(service_file.j[i]) + '\n')
            i += 1;
        storagedevice = ("".join(storagedevice))


        windows = []
        cpu_file = pd.read_csv("filesForTesting/CPU.txt", delim_whitespace=True, header=None,
                                   names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], encoding='utf-16')
        windows.append(
            "Hardware Specs: " + cpu_file.c[1] + cpu_file.d[1] + cpu_file.e[1] + cpu_file.f[1] + cpu_file.g[1] +
            cpu_file.h[1])
        windows = ("\n".join(windows))


        os_info = []
        operatingsys = pd.read_csv("filesForTesting/Operating System.txt", delim_whitespace=True, header=None,
                                       names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], encoding='utf-16')
        os_info.append("OS: " + operatingsys.c[0] + " " + operatingsys.d[0] + " " + operatingsys.e[0])
        os_info = ("\n".join(os_info))


        user_file = pd.read_csv("filesForTesting/Local-User.txt", delim_whitespace=True, header=None,
                                    names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], encoding='utf-16')
        count_row = user_file.shape[0]
        i = 2
        users = []
        while (i < count_row):
            users.append(user_file.c[i])
            i = i + 1;
        users = ("\n".join(users))


        ram = pd.read_csv("filesForTesting/RAM.txt", delim_whitespace=True, header=None,
                              names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], encoding='utf-16')
        count_row = ram.shape[0]
        i = 3
        ram_info = []
        while (i < count_row):
            ram_info.append("Ram Chips: " + ram.a[i] + " " + ram.b[i] + " Total Ram: " + ram.a[0])
            i = i + 1;
        ram_info = ("\n".join(ram_info))


        win_user_pass = pd.read_csv("filesForTesting/Windows User Passwords.txt", delim_whitespace=True, header=None,
                                        names=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], encoding='utf-16')
        count_row = win_user_pass.shape[0]
        i = 2
        passwordlist = []
        while (i < count_row):
            passwordlist.append(
                    "URL: " + win_user_pass.a[i] + '\n' + "Username: " + win_user_pass.b[i] + '\n' + "Password: " + win_user_pass.c[
                        i] + '\n')
            i = i + 1;
        passwordlist = ("\n".join(passwordlist))


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
        hardware_text.config(state=DISABLED)
        return 0

    @staticmethod
    def profilingAnalysis(profiling_text):
        profiling_text.config(state="normal")


        """Begin URL Analysis Here"""
        for key, value in urlDictionary.items():
            if value >= 40:
                if key in socialMedia:
                    profiling_text.insert(END,
                                          'The user uses a lot of social media, the site that was visited the most was ')
                    profiling_text.insert(END, "'" + key + "' " + str(value) + ' times')
                    profiling_text.insert(END,
                                          ' this suggests that the target uses social media for browsing often' + '\n')
                if key in schoolSites:
                    profiling_text.insert(END,
                                          'Based on the number of times the user visited ' + "'" + key + "'"
                                          + ' student portal a total of ' + str(value) + ' times' + ', this suggests that the user is likely to be a student there.' + '\n')

                if key in messengers:
                    profiling_text.insert(END, 'The messenging app that the user uses the most often is ')
                    profiling_text.insert(END, "'" + key + "' " + str(value) + ' times,')
                    profiling_text.insert(END, ' this suggests that the target might have used this messenging site as a means of communication.' + '\n')

                if key in drama:
                    profiling_text.insert(END, 'The target also happens to be a major fan of Drama, with the most visited site being ')
                    profiling_text.insert(END, "'" + key + "' " + str(value) + ' times \n')

        """Begin Services Analysis Here"""
        if systemDefence != '':
                profiling_text.insert(END, '\n')
                profiling_text.insert(END, "Target's Potential Defences")
                profiling_text.insert(END, '\n')
                profiling_text.insert(END, '===========================')
                profiling_text.insert(END, '\n')
                profiling_text.insert(END, systemDefence)
        if any("VPN" or "Password" in s for s in systemDefence):
            profiling_text.insert(END, '\n')
            profiling_text.insert(END, "It should be noted that the Target has VPN's and/or Password Managers "
                                       "Installed on their computer. This shows that the target is likely one who is "
                                       "technically savvy and might have stored key password information within his "
                                       "computer." + '\n')

        """Begin Hardware Analysis Here"""

        profiling_text.config(state=DISABLED)
        return 0

    @staticmethod
    def reset_frame(url_input_path, url_text, url_button_btn):
        url_input_path.config(text="")
        url_text.config(text="")
        url_button_btn.config(state="normal")
        return 0







