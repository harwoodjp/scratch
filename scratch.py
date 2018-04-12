import os
import sys
import datetime
from subprocess import call

now = datetime.datetime.now()

EDITOR_PATH="subl"
SCRATCH_PATH="/Users/jharwood/.scratch"
TODAYS_PATH="{}/{}-{}-{}".format(SCRATCH_PATH, now.year, now.month, now.day)
CURRENT_TIME="{}h{}m{}s".format(now.hour, now.minute, now.second)

if not os.path.exists(SCRATCH_PATH):
    os.makedirs(SCRATCH_PATH)

if not os.path.exists(TODAYS_PATH):
    os.makedirs(TODAYS_PATH)

if (len(sys.argv) > 1):
  NEW_FILE="{}/{}.{}".format(TODAYS_PATH, CURRENT_TIME, sys.argv[1])
  print(NEW_FILE)
  os.system("{} {}".format(EDITOR_PATH, NEW_FILE))
else: 
  os.system("{} {}".format(EDITOR_PATH, TODAYS_PATH))

