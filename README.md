# Bookmark Merger

A simple Python script to merge Netscape-format bookmark files (commonly exported from browsers like Firefox or Chrome).

## Features

- Merges two bookmark files into one
- Automatically deduplicates bookmarks, keeping the most recent version based on the ADD_DATE attribute
- Organizes bookmarks by folders
- Outputs the merged bookmarks to `merged_bookmarks.html` in Netscape format

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository.
2. Ensure Python 3 is installed on your system.

## Usage

1. Navigate to the directory containing `bookmark_merger.py`.
2. Run the script:

   ```bash
   python3 bookmark_merger.py
   ```

3. When prompted, enter the names of the two bookmark files you want to merge (including extensions, e.g., `bookmarks1.html`).
4. The merged bookmarks will be saved as `merged_bookmarks.html` in the same directory.

## Example

Suppose you have two bookmark files: `bookmarks_firefox.html` and `bookmarks_chrome.html`.

- Run the script and enter:
  - First file: `bookmarks_firefox.html`
  - Second file: `bookmarks_chrome.html`
- The result will be `merged_bookmarks.html` containing all unique bookmarks from both files, organized by folders.

## How It Works

- The script reads the bookmark files and parses them into bookmarks and folders.
- It deduplicates bookmarks by URL, preferring the one with the most recent date.
- Bookmarks are sorted by date and grouped by folders.
- The output is a valid Netscape bookmark file that can be imported back into browsers.

## Contributing

Feel free to submit issues or pull requests if you find bugs or want to add features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Originally created by [nmogadas](https://github.com/nmogadas). Maintained by [Ygryan360](https://github.com/Ygryan360).
