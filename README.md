# Instagram Reel Auto-Uploader

This project automates the uploading of Reels to Instagram using a Python script powered by the `instagrapi` library. Follow these steps to install the required dependencies and run the script.

## Prerequisites

- Python 3.6 or higher
- Instagram account credentials

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/itsrafiul/auto-reels-uploader.git
   cd auto-reels-uploader
   
Install Required Libraries

Install the instagrapi library and any additional dependencies listed in requirements.txt:


pip install -r requirements.txt
Alternatively, you can install instagrapi directly:


pip install instagrapi
Usage

Configure Your Script

Add the hashtags, it will randomly select 15 hastags each time while uploading to bypass the spam detection.

Place your all reels to /reels folder and replace it in i2.py line 28 as shown.

Update the script with your Instagram credentials.

Once configured, you can run the script with:

Run the Script

python i2.py

Troubleshooting

If you encounter login or upload issues:


Ensure you have enabled two-factor authentication on your Instagram account, and follow any prompts if needed.
Instagram may temporarily block automated actions. If this happens, wait and try again later.
Additional Information
Documentation for instagrapi: instagrapi GitHub
License: MIT License
