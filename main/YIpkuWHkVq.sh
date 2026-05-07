#!/bin/bash
if [ $# -ne 2 ]; then
  echo "Usage: $0 <input_file> <output_file>"
  exit 1
fi
input_file="$1"
output_file="$2"
if [ ! -f "$input_file" ]; then
  echo "Input file does not exist."
  exit 1
fi
if [ -f "$output_file" ]; then
  echo "Output file already exists. Overwriting."
fi
line_count=$(wc -l < "$input_file")
word_count=$(wc -w < "$input_file")
char_count=$(wc -c < "$input_file")
echo "Processing file: $input_file"
echo "Lines: $line_count" > "$output_file"
echo "Words: $word_count" >> "$output_file"
echo "Characters: $char_count" >> "$output_file"
echo "Content:" >> "$output_file"
cat "$input_file" >> "$output_file"
echo "File processed successfully."
exit 0
