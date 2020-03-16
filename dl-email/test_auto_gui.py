import pyautogui, time, datetime, webbrowser

images = {
  #'calendar_icon.PNG': 'click',
  'file.PNG': 'click',
  'open_and_export.PNG': 'click',
  'import_and_export.PNG': 'click',
  'export_to_file.PNG': 'doubleclick',
  'comma_seperated_values.png': 'doubleclick',
  'calendar_option2.png': 'doubleclick',
}

def center(box):
  return (box.left + (.5 * box.width), box.top + .5 * box.height)

time.sleep(3) # time to tab into outlook

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


# next weekday
# monday = 0
# tuesday = 1
# wed = 2
# thur = 3
# fri = 4
day_of_week = datetime.date.today().weekday()
if(day_of_week == 4): # if friday
  days_to_monday = datetime.timedelta(7-day_of_week)
  next_weekday = datetime.date.today() + days_to_monday
else:
  next_weekday = datetime.date.today() + datetime.timedelta(1)
print(next_weekday.strftime("%m/%d/%Y"))
pyautogui.write(next_weekday.strftime("%m/%d/%Y")+"\t"+next_weekday.strftime("%m/%d/%Y"))
time.sleep(5)
pyautogui.press('enter')

webbrowser.open("https://calendar.google.com/calendar/r/settings/export")