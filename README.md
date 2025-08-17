# LLSorter
A Love Live Character true round robin Sorter written in Python 3.13.

## Features
- Every character from μ's to Ikizurai-Bu!
- Has additional data like group preference, blood type preference, and height preference!
- True round robin, providing the most accurate answers possible.
- "Quick" mode which uses transitive relationships to dramatically reduce time required to complete (common with other Love Live character sorters online)

## Caveats
- True round robin takes an immense amount of comparisons (1953 comparisons!)
- Some characters do not have data for blood type (they are ignored on data displays)
- Rival group characters are not included.
- Slow initial run (could be fixed by precaching the images I guess? Doesn't seem worth it, once a user has seen all of the characters once the performance is just fine)

## TODO
- Maybe add the rival groups (would take only a few minutes but I'm lazy)
- Maybe add supporting characters
- Find a way to repurpose code to host online

## Credits
- All images are pulled from the [Love Live Wiki](https://love-live.fandom.com/wiki/Main_Page) in order to have a consistent appearance.
