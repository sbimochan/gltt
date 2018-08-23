# Git log to timesheet

First you need to install git standup
## Install

You can install `git-standup` using one of the options listed below

| Source | Command |
| --- | --- |
| curl | `curl -L https://raw.githubusercontent.com/kamranahmedse/git-standup/master/installer.sh \| sudo sh` |
| npm | `npm install -g git-standup` |
| brew | `brew update && brew install git-standup` |
| aur | `pacaur -S git-standup-git` |
| manual | Clone and run `make install` |

## Usage

Simply run it in your project directory and it will give you the output from the last working day

```shell
git standup
```
for previous x days
```shell
git standup -d x
```
Install git-log-to-timesheet

## Install
```shell
cd
git clone https://github.com/sbimochan/gltt.git
alias gltt="python3 ~/gltt/__init__.py"
```

## Usage
Simply copy the result produced by git standup and dump using git-log-to-timesheet
```shell
gltt  "cbb99f8e - Change Logic for datetime (14 minutes ago) <sbimochan>
     10237353 - Implement logic (47 minutes ago) <sbimochan>"
```
The result produced can then be pasted to your timesheet.

<script type='text/javascript' src='https://ko-fi.com/widgets/widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#46b798', 'D1D8IIBU');kofiwidget2.draw();</script>