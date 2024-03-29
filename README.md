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

One liner install
```shell
sudo curl https://raw.githubusercontent.com/sbimochan/gltt/master/gltt -o /usr/local/bin/gltt && sudo chmod +x /usr/local/bin/gltt
```

## Usage

```shell
gltt "{result from git standup command}"
```


The result produced can then be pasted to your timesheet.

<a href='https://ko-fi.com/D1D8IIBU' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi2.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
