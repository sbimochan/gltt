"""Top-level package for Git log to timesheet."""

__author__ = """Bimochan Shrestha"""
__email__ = 'bmochan@gmail.com'
__version__ = '0.1.0'

from sys import argv
import re
import subprocess

if(len(argv) > 1):
    standup_msg = subprocess.getoutput('git standup -d {}'.format(argv[1]))
else:
    standup_msg = subprocess.getoutput('git standup')
lines = standup_msg.split("\n")
separated_lines = []

for line in reversed(lines):
    lines_without_hyphen = re.sub('^[\w\d]*\s(.)', '', line)
    separated_lines.append(lines_without_hyphen)

for counter, separated_line in enumerate(separated_lines):
    cleaned_line= re.sub('\((.*?)\)(\s<(.*)>)?', '', separated_line)
    cleaned_line = cleaned_line.strip()
    result = str(counter+1) + ")" + cleaned_line
    print(result)
