#!/usr/bin/env python3

import shutil

def convert_bytes(bytes_number):
# https://tutorialspoint4all.com/python-program-to-convert-bytes-to-kilobytes-megabytes-gigabytes-and-terabytes/
    tags = ["Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"]
    i = 0
    double_bytes = bytes_number

    while (i < len(tags) and bytes_number >= 1024):
        double_bytes = bytes_number / 1024.0
        i = i + 1
        bytes_number = bytes_number / 1024

    return str(round(double_bytes, 2)) + " " + tags[i]


du = shutil.disk_usage("/")
result = f"Total space {convert_bytes(du.total)} \nUse Space:  {convert_bytes(du.used)} \nFree Space:  {convert_bytes(du.free)}"
print(result)
