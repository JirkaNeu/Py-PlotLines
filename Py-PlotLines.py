from jne import prinje

def loogress(first, last):
  print("\r", f"working: {first+1} of {last} --> {round((first+1)/(last/100), 1)}%", end="")
  if first+1 == last: print("\n done! =)\n")
  return None

try:
  with open("jne.txt", "r", encoding="utf-8") as notes:
    getnotes = []
    for lines in notes:
      getnotes.append(lines.strip("\r\n"))
    notes.close()
    path = getnotes[0]
    path = '/'.join(path.split('\\'))
except:
  path = ""
  try: import ctypes; ctypes.windll.user32.MessageBoxW(0, "check path...", "Python", 1)
  except: print("check path...")


jne_data = path + "sample.txt"

#---------------------------- get data ----------------------------#
try:
  with open(jne_data, "r", encoding="utf-8") as data:
    getdata = []
    for lines in data:
      getdata.append(lines.strip("\r\n"))
    data.close()
except:
  print("no data found - using example instead")
  getdata = ["(0.44); In Australia seatbelts are mandatory for all vehicle occupants.",
             "(0.43); A warm cup of coffee on a chilly morning is just what I need to start the day.",
             "(0.56); The sun was shining brightly in the clear blue sky.",
             "(0.59); The sound of the ocean waves crashing against the shore is so soothing to me.",
             "(0.52); In Australia seatbelts are mandatory for all vehicle occupants.",
             "(0.56); The sun was shining brightly in the clear blue sky.",
             "(0.54); Birds chirping outside my window is calming me every morning.",
             "(0.48)",
             "(0.43); The smell of freshly baked cookies filled the warm and cozy kitchen.",
             "(0.50); I'm looking forward to my summer vacation on the beautiful island beach.",
             "(0.58); A warm cup of coffee on a chilly morning is just what I need to start the day.",
             "(0.56); The sun was shining brightly in the clear blue sky.",
             "(0.44); Birds chirping outside my window is calming me every morning.",
             "(0.56); In Australia seatbelts are mandatory for all vehicle occupants.",
             "(0.59); The sun was shining brightly in the clear blue sky."]

print(getdata)

import pandas as pd
import re
#pattern_t = r"^Titel:" #--> titel
#pattern_e = r"\((\d+(?:.\d+)?)\)$" #--> empty line
pattern_v = r"\((\d+(?:.\d+)?)\); " #--> valid
line_check = ""
iterations = len(getdata)
results = []

for i in range(iterations):
  this_line = getdata[i]
  if re.match(pattern_v, this_line):
    this_line = re.sub(pattern_v, "", this_line)
    if (this_line != line_check):
      results.append(this_line)
    line_check = this_line
  exec('try:loogress(i, iterations)\nexcept:print("working...")')

jne_results = pd.DataFrame()
jne_results = jne_results.assign(ESCO_Skills=results)
count_escos = jne_results['ESCO_Skills'].value_counts()
jne_output = pd.DataFrame({'ESCO': count_escos.index, 'counts': count_escos.values})
result_file = path + "results.xlsx"
jne_output.to_excel(result_file, index=False)


#https://pythonspot.com/matplotlib-bar-chart/

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

categories = count_escos.index
values = count_escos.values

ax.bar(categories, values)
ax.set_title('Frequencies of Strings')
ax.set_xlabel('Sentences')
ax.set_ylabel('Frequency')

plt.show()