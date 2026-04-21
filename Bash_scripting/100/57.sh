#!/bin/bash
# 57. uniq logs.txt  — remove adjacent duplicate lines. (Must sort first!)
sort -k4 logs.txt | uniq -c 
