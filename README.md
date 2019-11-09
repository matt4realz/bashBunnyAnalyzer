# bashBunnyAnalyzer By TeamNoSleep

## As the product is still in its prototyping phase, we have to assume the following
- The Target PC is powered on
- The Target PC is successfully logged in
- The Target PC is running Windows 7 and Later
- The Target PC does not have other anti-virus software aside from Windows Defender as the Payloads are invasive

## Information that can be gathered
- Hardware
  - BIOS, CPU, COM & Serial Devices, RAM and other Hardware related data
- Network
  - Browser History, Target MAC + IP Address and other Network related data
- Software
  - Installed Drivers, Software, Running Processes and Services, OS and other related data
- Accounts
  - Local-User Passwords, Wifi Passwords


## You will need the following external libraries & programms installed
- Payloads from our GitHub inside "Switch2.zip" when BashBunny is in "Storage" mode
- Python3 and above
- tkinter (pip install tkinter)
- pandas (pip install pandas)
- fpdf (pip install fpdf)
- wordcloud (pip install wordcloud)
- matplotlib (pip install matplotlib)

## You will need the following tools
- 'Target' PC for collecting evidence
- 'Investigator' PC for triage analysis of evidence
- 'BashBunny' by Hak5

## Bashbunny LED Legend
- Purple > Initialising
- Blue > Bypassing Windows Defender
- Cyan > Attacking In Progress
- Green > Attack Completed

## Program Flow Guide
### We will be referring to :
- the suspect as 'Target'
- the investigator as 'User'
- the BashBunny as 'device'

1. User starts by ensuring that the Device mode is in 'AttackMode2' which is the most center switch and plug it into the PC.
2. At this point, just allow the Device to run its course as the Windows PowerShell payloads are pre-configured inside.
3. The color will cycle through according to the "BashBunny LED Legend" stated above.
4. Once the device's LED has turned green, the User may remove the device from the Target PC.
5. User will simultaneously load the downloaded program from this GitHub to the PyCharm projects and set the configuration run path to start running from 'UI'.
6. User now switches the Device to 'Storage' mode which is the switch location closest to the USB Header.
7. User may now plug the device into their own Investigation PC.
8. User will navigate to '/loot/info/*pathToTarget*' Folder on the Device.
9. Copy out all the files within the folder into the "filesforTesting" folder in the analysis program
10. User can now click "Analyze Files" on the program, once complete, all relevant data will be displayed.
11. User may also click the "Export PDF" button on the program in order to generate the PDF with the relevant data.
