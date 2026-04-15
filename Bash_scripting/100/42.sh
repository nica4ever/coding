#!/bin/bash
# 42. awk '$3 == "ERROR" {print $0}' logs.txt  — print whole line where 3rd field is ERROR.

awk '$3 == "ERROR" {print $0}' logs.txt
