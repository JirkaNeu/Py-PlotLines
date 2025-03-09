def loogress(first, last):
  print("\r", f"working: {first+1} of {last} --> {round((first+1)/(last/100), 1)}%", end="")
  if first+1 == last: print("\n done! =)\n")
  return None

try:
  with open("notes.txt", "r", encoding="utf-8") as notes:
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


#------------------------------------------------------------------#
#---------------------------- get data ----------------------------#
try:
  with open("sample.txt", "r", encoding="utf-8") as data:
    getdata = []
    for lines in data:
      getdata.append(lines.strip("\r\n"))
    data.close()
except:
  print("no data")


import pandas as pd
import re
#pattern_t = r"^Titel:" #--> titel
#pattern_e = r"\((\d+(?:.\d+)?)\)$" #--> empty line
pattern_v = r"\((\d+(?:.\d+)?)\); " #--> valid
line_check = ""
iterations = len(getdata)
#iterations = 35
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

