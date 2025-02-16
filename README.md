# Subtitle Time Shift Script

This is a Python script designed to help you adjust the timing of subtitles in `.srt` files. Whether you need to fix sync issues or simply shift the timing, this script will allow you to add or subtract time to all subtitle timestamps in the file.

---

## Features

- Adjust subtitle times by any given amount of seconds.
- Supports `HH:MM:SS,SSS` format commonly used in `.srt` subtitle files.
- Creates a new adjusted subtitle file with the same content but with updated timings.

---

## Installation

No installation is required, just make sure you have Python installed (version 3.x recommended).

1. Clone the repository or download the script.
2. Ensure your subtitle file is in `.srt` format and accessible.

---

## Usage

1. Download the `subtitle_time_shift.py` script and place it in the same folder as your `.srt` subtitle file, or specify the full path to the subtitle file.
2. Open your terminal/command prompt and run the script:

```bash
python subtitle_time_shift.py
```

3. When prompted, enter the number of seconds you want to shift the subtitle times by:
   - Positive number to **increase** the timestamp (delay subtitles).
   - Negative number to **decrease** the timestamp (advance subtitles).

Example input:
```
Enter the number of seconds to increase the timestamps: 2.5
```

4. The script will read your subtitle file, adjust the timestamps, and create a new file with `_adj` appended to the original filename. For example, if your file was `movie.srt`, the adjusted file will be named `movie.srt_adj`.

---

## Example

Given a subtitle line like:

```
00:01:23,500 --> 00:01:25,000
Hello, how are you?
```

If you input `2` seconds to shift, the adjusted subtitle will be:

```
00:01:25,500 --> 00:01:27,000
Hello, how are you?
```

---

## Code Walkthrough

- **`convert_to_seconds(time_str)`**: Converts a subtitle timestamp from `HH:MM:SS,SSS` format to total seconds (including milliseconds).
  
- **`convert_to_timestamp(seconds)`**: Converts seconds back into the `HH:MM:SS,SSS` format.

- **`adjust_subtitles(file_path, time_shift_seconds)`**: Reads the `.srt` file, identifies all timestamps using regex, and applies the time shift. Then, it writes the adjusted subtitles to a new file.

---

## Requirements

- Python 3.x
- No external dependencies (uses built-in Python libraries like `re`).



