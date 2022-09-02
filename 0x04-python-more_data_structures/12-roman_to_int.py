#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        res = 0
        r_num = {
           'I': 1,
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000}

        for i in range(len(roman_string)):
            if r_num.get(roman_string[i], 0) == 0:
                return (0)

            if (i != (len(roman_string) - 1) and
               r_num[roman_string[i]] < r_num[roman_string[i + 1]]):
                res -= r_num[roman_string[i]]

            else:
                res += r_num[roman_string[i]]
        return res
    else:
        return 0
