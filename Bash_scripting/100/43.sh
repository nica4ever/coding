#!/bin/bash
# 43. awk '$3 == "ERROR" {print $4}' logs.txt  — print 4th field (service) ONLY for error lines.

awk '$3 == "ERROR" {print $4}' logs.txt
