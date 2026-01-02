# Duplicate File Finder

A Python application that scans directories to find duplicate files by comparing their content using MD5 hashing. The tool provides a user-friendly interface with progress tracking and generates a detailed report of all duplicate files found.

## Features

- **Graphical Folder Selection**: Easy-to-use folder selection dialog
- **Real-time Progress Tracking**: Visual progress bar showing scan status
- **Content-based Detection**: Uses MD5 hashing to identify duplicates by file content, not just filename
- **Detailed Reports**: Generates a comprehensive text report with all duplicate groups
- **Space Savings Calculation**: Shows potential disk space that could be freed by removing duplicates
- **Recursive Scanning**: Scans all subdirectories within the selected folder
- **Cross-platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.7 or higher
- tkinter (usually included with Python, but may need to be installed separately on Linux)

## Installation

1. Clone or download this repository
2. Ensure Python 3.7+ is installed on your system
3. Install tkinter if needed:
   - **Windows/macOS**: Usually pre-installed with Python
   - **Linux**: Install with `sudo apt-get install python3-tk` (Debian/Ubuntu) or equivalent

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. A folder selection dialog will appear - choose the directory you want to scan

3. A progress window will show the scanning progress in real-time

4. Once scanning is complete, a completion dialog will display:

   - Number of duplicate groups found
   - Location of the generated report file

5. Open `duplicates_report.txt` to view the detailed report

## Report Format

The generated report (`duplicates_report.txt`) includes:

- **Header**: Report generation timestamp
- **Summary**: Total number of duplicate groups and files
- **Duplicate Groups**: Each group shows:
  - Group number
  - Number of duplicate files in the group
  - File size of each duplicate
  - Full paths of all duplicate files
- **Space Savings**: Total potential disk space that could be recovered

### Example Report Structure

```
================================================================================
DUPLICATE FILES REPORT
================================================================================
Generated: 2024-01-15 14:30:25

Found 3 duplicate group(s) with 7 total files.

--------------------------------------------------------------------------------
Group 1: 3 duplicate files (2.50 MB each)
--------------------------------------------------------------------------------
  [1] C:\Users\Documents\photo1.jpg
  [2] C:\Users\Documents\backup\photo1.jpg
  [3] C:\Users\Downloads\photo1_copy.jpg

...
```

## How It Works

1. **File Hashing**: The application reads each file in chunks and calculates an MD5 hash of its contents
2. **Grouping**: Files with identical hashes are grouped together as duplicates
3. **Filtering**: Only groups with more than one file are considered duplicates
4. **Reporting**: All duplicate groups are written to a text file with detailed information

## Technical Details

- **Hashing Algorithm**: MD5 (Message Digest 5)
- **Chunk Size**: 8KB chunks for efficient memory usage with large files
- **File Encoding**: UTF-8 for report generation
- **GUI Framework**: tkinter for cross-platform compatibility

## File Structure

```
duplicate_file_finder/
├── main.py              # Main application with GUI and report generation
├── helpers.py           # Core functions for hashing and duplicate detection
└── README.md            # This file
```

## Limitations

- **MD5 Collisions**: While extremely rare, MD5 has theoretical collision vulnerabilities. For most use cases, this is not a concern
- **Large Directories**: Scanning very large directories (100,000+ files) may take considerable time
- **File Permissions**: Files that cannot be read due to permissions will be skipped
- **Memory Usage**: Very large files are handled efficiently, but scanning many large files simultaneously may use significant memory

## Troubleshooting

### Progress window doesn't appear

- Ensure tkinter is properly installed
- Try running from a terminal to see any error messages

### "No module named 'tkinter'" error

- Install tkinter: `sudo apt-get install python3-tk` (Linux)
- On Windows/macOS, reinstall Python with tkinter support

### Slow performance

- Large directories with many files will take time to scan
- The application processes files sequentially to ensure accuracy
- Consider scanning smaller subdirectories separately

### Files not detected as duplicates

- Ensure files are truly identical (same content, not just same name)
- Check file permissions - files that can't be read are skipped

## License

This project is provided as-is for personal and educational use.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Future Enhancements

Potential improvements could include:

- Option to automatically delete duplicate files
- Support for different hash algorithms (SHA-256, etc.)
- Export reports in different formats (CSV, JSON)
- Filter options (by file type, size, etc.)
- Batch processing of multiple directories
