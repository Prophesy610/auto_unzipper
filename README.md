# Auto-Unzipper: Unzip and Delete Zip Files Automatically

## Description

`Auto-Unzipper` is a simple Python script that automates the process of unzipping all `.zip` files in a specified folder. Once the zip file is extracted, the script will automatically delete the zip file to keep your directory clean and organized.

This script is ideal for situations where you need to quickly extract and remove zip files without manual intervention. It works on **macOS**, **Linux**, and **Windows**.

## Features

- Unzips all `.zip` files within a specified folder.
- Deletes the zip file after extraction to save space.
- Supports file paths with spaces or special characters.
- Easy to use and configure.
- Fully compatible with **macOS**, as well as **Linux** and **Windows** systems.

## Requirements

- Python 3.x
- `zipfile` module (usually comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/auto-unzipper.git
    cd auto-unzipper
    ```

2. Make sure you have Python 3.x installed. You can verify this by running:

    ```bash
    python --version
    ```

3. There are no external dependencies, as this script uses built-in Python libraries.

## Usage

**Important:** The script **needs to be located in the same folder** as the `.zip` files you wish to unzip. Alternatively, you can specify the path to the folder containing the zip files as an argument.

1. **Option 1:** Place the script in the folder where the `.zip` files are stored, then run it:

    ```bash
    python auto_unzipper.py
    ```

2. **Option 2:** If the script is located elsewhere, specify the folder path where your zip files are stored:

    ```bash
    python auto_unzipper.py /path/to/your/folder
    ```

The script will go through all the `.zip` files in the provided directory, unzip them into the same location, and delete the original zip files once extraction is complete.

### Example:

```bash
python auto_unzipper.py /home/user/downloads
