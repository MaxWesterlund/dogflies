#!/usr/bin/env python3
import json
from datetime import datetime

FONT = {
    "0": [
    "  __", 
    " / /", 
    "/_/ "],
    
    "1": [
    "  _", 
    "  /", 
    "_/_"],
    
    "2": [
    "  __", 
    " '_/", 
    "/__ "],
    
    "3": [
    "  __", 
    "  _/", 
    "._/ "],
    
    "4": [
    "    ",
    " /_/",
    "  / ",],
    
    "5": [
    "  __",
    " /_ ",
    "._/ "],
    
    "6": [
    "  _ ",
    " /_'",
    "/_/ "],
    
    "7": [
    " __",
    " _/",
    " / "],
    
    "8": [
    "  __",
    " /_/",
    "/_/ "],
    
    "9": [
    "  __",
    " /_/",
    "._/ "],
    
    ":": [
    "  ",
    " _",
    "- "]
}

def render(s):
    rows = ["", "", ""]
    for ch in s:
        for i in range(3):
            rows[i] += FONT[ch][i]
    art = "\n".join(r.rstrip() for r in rows)
    return "<span line_height='0.9rem'>" + art + "</span>"

now = datetime.now()
print(json.dumps({
    "text": render(now.strftime("%H:%M")),
    "tooltop": "false",
    "class": "asciiclock",
}))
