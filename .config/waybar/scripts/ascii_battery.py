#!/usr/bin/env python3
import json
import psutil # sudo pacman -Sy python-psutil

S = "<span color='#ff0000'>"
E = "</span>"

FONT = {
    "0": [
        " _ ",
        "|.|",
        "|_|"
    ],
    "1": [
        " . ",
        "'.|",
        "'.|"
    ],
    "2": [
        " _ ",
        "'_|",
        "|_'"
    ],
    "3": [
        " _ ",
        "'_|",
        "'_|"
    ],
    "4": [
        " . ",
        "|_|",
        "'.|"
    ],
    "5": [
        " _ ",
        "|_'",
        "'_|"
    ],
    "6": [
        " _ ",
        "|_'",
        "|_|"
    ],
    "7": [
        " _ ",
        "'.|",
        "'.|"
    ],
    "8": [
        " _ ",
        "|_|",
        "|_|"
    ],
    "9": [
        " _ ",
        "|_|",
        "'_|"
    ],
    "%": [
        "  ",
        "o/",
        "/o"
    ]
}

LENGTH = 7

def add_empty(i, n):
    if (i == 0):
        return " _ " * n
    elif (i == 1):
        return "¦_¦" * n
    elif (i == 2):
        return "¦_¦" * n

    return ""

def render(s):
    art = ""
    len_empty = LENGTH - len(s)
    d = {
        " ":" ",
        ".":"_",
        "'":"¦",
        "_":f"{S}_{E}",
        "|":f"{S}|{E}"
    }
    for i in range(3): # row
        art += add_empty(i, len_empty)
        
        for ch in s: # character
            for j in range(len(FONT[ch][i])): # char
                x = d[FONT[ch][i][j]]
                art += x
        if i != 2:
            art += "\n"
    return art
                

battery = psutil.sensors_battery()
print(json.dumps({
    "text": render(str(round(battery.percent))) + str(round(battery.percent)),
    "class": "ascii_battery",
}))
