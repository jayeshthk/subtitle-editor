import re

def convert_to_seconds(time_str):
    """Convert a timestamp to seconds."""
    hours, minutes, seconds = time_str.split(':')
    seconds, milliseconds = seconds.split(',')
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000
    return total_seconds

def convert_to_timestamp(seconds):
    """Convert seconds to a timestamp string (HH:MM:SS,SSS)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{milliseconds:03}"

def adjust_subtitles(file_path, time_shift_seconds):
    """Adjust the time in an SRT file by the given time shift in seconds."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regular expression to match the timestamps in the SRT file
    pattern = r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})'

    def adjust_time(match):
        start_time = match.group(1)
        end_time = match.group(2)

        start_seconds = convert_to_seconds(start_time) + time_shift_seconds
        end_seconds = convert_to_seconds(end_time) + time_shift_seconds

        new_start_time = convert_to_timestamp(start_seconds)
        new_end_time = convert_to_timestamp(end_seconds)

        return f"{new_start_time} --> {new_end_time}"

    adjusted_content = re.sub(pattern, adjust_time, content)

    with open(f"{file_path}_adj", 'w', encoding='utf-8') as f:
        f.write(adjusted_content)

    print(f"File saved as 'adjusted_{file_path}' with {time_shift_seconds} seconds added.")

file_path = 'Desktop/filename.srt' 
time_shift_seconds = float(input("Enter the number of seconds to increase the timestamps: "))
adjust_subtitles(file_path, time_shift_seconds)
