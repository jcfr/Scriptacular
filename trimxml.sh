#!/bin/bash

`rm -f temp.xml`

while IFS= read -r -u3 -d $'\0' file; do
  echo "Processing ${file:2}"
  `~/Projects/Scriptacular/trimxml.py $file > temp.xml`
  `xmllint --format temp.xml --output $file`
done 3< <(find . -name *.xml -print0)

`rm temp.xml`
