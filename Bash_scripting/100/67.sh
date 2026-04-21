#!/bin/bash
# 67. Write a function `biggest_file_in_dir` that takes a directory and
#     echoes the largest file inside. Use du or ls -S.

biggest_file_in_dir(){
    ls -S "${1}" | head -n1
}

biggest_file_in_dir ~/Games
