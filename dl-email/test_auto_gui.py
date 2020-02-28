import pyautogui, time, datetime

images = {
  'calendar_icon.PNG': 'click',
  'file.PNG': 'click',
  'open_and_export.PNG': 'click',
  'import_and_export.PNG': 'click',
  'export_to_file.PNG': 'doubleclick',
  'comma_seperated_values.png': 'doubleclick',
  'calendar_option.png': 'doubleclick',
}

def center(box):
  return (box.left + (.5 * box.width), box.top + .5 * box.height)

for image, action in images.items():
  if(image == 'calendar_option.png'):
    pyautogui.scroll(1000)
  button = pyautogui.locateOnScreen(image)
  pyautogui.moveTo(center(button))
  if(action == 'click'):
    pyautogui.click()
  elif(action == 'doubleclick'):
    pyautogui.doubleClick()
  time.sleep(1)

pyautogui.press('enter') # next
pyautogui.press('enter') # yes
time.sleep(1)
pyautogui.press('enter') # finish


day_of_week = datetime.date.today().weekday()
days_to_monday = datetime.timedelta(7-day_of_week)
monday = datetime.date.today() + days_to_monday
print(monday.strftime("%m/%d/%Y"))
friday = monday + datetime.timedelta(4)
print(friday.strftime("%m/%d/%Y"))
pyautogui.write(monday.strftime("%m/%d/%Y")+"\t"+friday.strftime("%m/%d/%Y"))
time.sleep(5)
pyautogui.press('enter')