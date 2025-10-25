#!/bin/bash

# Check if exactly 4 arguments are provided
if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <base_name> <start> <end> <extension>"
  exit 1
fi

base_name=$1
start=$2
end=$3
extension=$4

# Generate files from start to end
for ((i=start; i<=end; i++)); do
  padded=$(printf "%02d" "$i")
  filename="${base_name}${padded}.${extension}"
  touch "$filename"
  echo "Created file: $filename"
done
