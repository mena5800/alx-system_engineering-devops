#!/bin/bash

# Get the word to append
word="#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join"

# Get a list of all files
files=$(find . -type f)

# Loop through the files and append the word
for file in $files; do
  echo "$word" >> $file
done
