#!/bin/bash

for rarfile in *.rar; do
    # Prompt for password for each file
    # Does not ask for [a] for files with multiple contents
    # Comment off the read line does not work

    read -sp "Enter password for $rarfile: " password
    echo
    unrar x -p"$password" "$rarfile"
done

