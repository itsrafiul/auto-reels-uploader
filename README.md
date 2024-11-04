# Instagram Reel Auto-Uploader

This project automates the uploading of Reels to Instagram using a Python script powered by the `instagrapi` library. Follow these steps to install the required dependencies and run the script.

## Prerequisites

- Python 3.6 or higher
- Instagram account credentials

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/instagram-reel-auto-uploader.git
   cd instagram-reel-auto-uploader
Install Required Libraries

Install the instagrapi library and any additional dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Alternatively, you can install instagrapi directly:

bash
Copy code
pip install instagrapi
Usage
Configure Your Script

Update the script with your Instagram credentials. For security, it’s best to avoid hardcoding credentials directly in the code. Consider using environment variables.

Run the Script

Once configured, you can run the script with:

bash
Copy code
python upload_reel.py
Troubleshooting
If you encounter login or upload issues:

Ensure you have enabled two-factor authentication on your Instagram account, and follow any prompts if needed.
Instagram may temporarily block automated actions. If this happens, wait and try again later.
Additional Information
Documentation for instagrapi: instagrapi GitHub
License: MIT License
