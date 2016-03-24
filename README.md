# skua
skua is a tool to download data, such as pictures or videos, from websites.

This project is in a very early stage of development.
However, it already provides some functionality:

## Usage
Basic usage:
```
python skua.py [URL] {Destination path}
```
`[URL]` is the only required parameter. Files embedded in this URL are downloaded and stored in the current directory.
Currently, only JPEG images are downloaded. Other file types will be supported in future updates.

`{Destination path}` is an optional parameter that allows the user to specify the target directory.
Note that (JPEG) file name will simply be appended to the provided path. Therefore, the path should end with `/`. Since the file name is merely appended to this path, it is possible to define a prefix, e.g., `~/Pictures/abc` would store all (JPEG) files in the folder `~/Pictures` and prepend the string 'abc' to each file name.

## Future Development
Many options will be added in the future:

* Define the set of file extensions that should be downloaded.
* Exclude files containing a certain string or pattern.
* Define a custom random delay between downloads.

More importantly, `extractors` will be introduced, which enable customizable rules on how to extract the desired content from various websites.
