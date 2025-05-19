# New Contributor Overview

This project provides small scripts to automatically open a Zoom meeting URL a few minutes before a scheduled time. The codebase includes experiments with `tkinter` GUIs and CSV handling. Below is a brief guide for new contributors.

## Repository Structure

- `zoom-enter-kun.py` – main script offering scheduling features.
- `sample.py` and `codes_from_ChatGPT.py` – prototype versions that show development progress.
- `GUIwindow_byChatGPT.py` – GUI example for choosing a meeting and time.
- `sample_url.csv` – example CSV file containing meeting names and URLs.
- `comment_from_ChatGPT.txt` – conversation log describing earlier debugging steps.
- `README.md` – project introduction and usage notes (mostly in Japanese).

## Important Points

1. Meeting links are stored in a CSV file with the format:
   
   ```csv
   name,url
   定例の会議,https://example.com/meeting
   ```
   Edit or replace `sample_url.csv` to match your environment.
2. The scripts rely on the `pandas` library for CSV reading.
3. Time scheduling uses `tkinter` widgets. The `zoom-enter-kun.py` file contains a `zoom_enter_kun` class implementing the logic.

## Getting Started

1. Install requirements:
   ```bash
   pip install pandas
   ```
2. Prepare your own `url.csv` based on the sample and place it next to the script.
3. Run the main script with Python 3:
   ```bash
   python3 zoom-enter-kun.py
   ```

### Learning Steps for New Contributors

1. Review `zoom-enter-kun.py` to understand the core class and scheduling logic.
2. Explore `GUIwindow_byChatGPT.py` for a simpler GUI-only example if you are new to `tkinter`.
3. Check the conversation log in `comment_from_ChatGPT.txt` for context on early development choices.
4. Experiment with editing `sample_url.csv` and running the script to see how scheduling works.

Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or new features.
