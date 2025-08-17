# LLSorter
A Love Live Character true round robin Sorter written in Python 3.13.

## Features
- Every character from μ's to Ikizurai-Bu!
- Has additional data like group preference, blood type preference, and height preference!
- True round robin, providing the most accurate answers possible.
- "Quick" mode which uses transitive relationships to dramatically reduce time required to complete (common with other Love Live character sorters online)
- Uses true randomness to avoid bias (in both modes).

## Caveats
- True round robin takes an immense amount of comparisons (1953 comparisons!)
- Some characters do not have data for blood type (they are ignored on data displays)
- Rival group characters are not included.
- Slow initial run (could be fixed by precaching the images I guess? Doesn't seem worth it, once a user has seen all of the characters once the performance is just fine. Web version works perfectly.)
- True random makes quick mode slower than other LL sorting websites, but I do not intend to change this.
- Local version way less refined.

## TODO
- Maybe add the rival groups (would take only a few minutes but I'm lazy)
- Maybe add supporting characters

## Download
- It's recommended to use the [web version](https://yuberz.github.io/llsort.github.io/) instead of downloading, but if you want to run it locally...
- Download and install Python 3.13 (added to PATH)
- Download the latest [LLSort.py](https://github.com/Yuberz/LLSorter/archive/refs/heads/main.zip) file directly from the repository.
- Run it using ```python ./LLSort.py```

## Credits
- All images are pulled from the [Love Live Wiki](https://love-live.fandom.com/wiki/Main_Page) in order to have a consistent appearance.
