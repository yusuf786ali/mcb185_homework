gunzip -c ../MCB185/data/dictionary.gz | grep -v "[^aicrnzo]" | grep "r" | grep -c  -E "^.{4,}"
