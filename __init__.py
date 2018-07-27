"""Top-level package for Git log to timesheet."""

__author__ = """Bimochan Shrestha"""
__email__ = 'bmochan@gmail.com'
__version__ = '0.1.0'

from sys import argv

standup_msg = (argv[1])
lines = standup_msg.split("\n")
separated_lines = []

for line in reversed(lines):
    line_without_hyphen = line.split("-")
    separated_lines.append(line_without_hyphen[1])
for counter, separated_line in enumerate(separated_lines):
    line_without_parenthesis = separated_line.split("(")
    result = str(counter+1) + ")" + line_without_parenthesis[0]
    print(result)
