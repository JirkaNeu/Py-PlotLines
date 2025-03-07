def prinje(**kwargs):
  print("+-----------------------------------------")
  for key, value in kwargs.items():
    print(f"| Var: {key} | Val: {value}")
  print("+-----------------------------------------")

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
