import os
import shlex
import subprocess

workingDB = None
UserQuery = None
TableList = [None]

def inputCleaner(wordToRemove): # Removes ; and command
  query = UserQuery.replace(";", "")
  return query.replace(wordToRemove, "")

def databaseExistenceCheck(db): # Checks if database exists
  if db in subprocess.run(['ls', '|', 'grep', db], capture_output=True, text=True).stdout:
    return 1
  else:
    return 0
