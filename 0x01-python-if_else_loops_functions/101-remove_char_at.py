#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for ch in str:
       if n >= 0 and n < len(str):
           if (ch == str[n]):
               continue
           s += ch
       else:
           s += ch
    return s
