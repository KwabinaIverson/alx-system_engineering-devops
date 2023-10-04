#!/usr/bin/env ruby

# Check if the script has received an argument
if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb <text>"
  exit 1
end

# Define the regular expression pattern
pattern = /School/

# Get the input text from the command line argument
text = ARGV[0]

# Use the regular expression to check for a match
if text =~ pattern
  puts "Matched: #{$&}" # Output the matched text
else
  puts "No match found"
end
