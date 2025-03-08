def loogress(first, last):
  print("\r", f"working: {first+1} of {last} --> {round((first+1)/(last/100), 1)}%", end="")
  if first+1 == last: print("\n done! =)\n")

try:
  with open("notes.txt", "r") as notes:
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

print(path)
print("")
print(getnotes)

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


print(getdata)

iterations = len(getdata)

for i in range(iterations):
  print(getdata[i])
  #exec('try:loogress(i, iterations)\nexcept:print("working...")')

import re
#pattern = r"^Titel:"
pattern = "Titel:"

for i in range(iterations):
  print(getdata[i])
  if getdata[i].startswith(pattern):
    print("Hell yeah..!!")
  #if re.match(pattern, getdata[i]):
  #  print("Titel found...")
  #exec('try:loogress(i, iterations)\nexcept:print("working...")')


#https://pythonspot.com/matplotlib-bar-chart/
