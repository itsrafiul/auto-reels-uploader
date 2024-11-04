import os
import time
import random
import pickle
from instagrapi import Client

# Instagram credentials
username = 'your instagram username'
password = 'your instagram password@'

# Initialize Instagram client
cl = Client()

# Load or create session
session_file = 'instagram_session2.pkl'

# Load session if exists
if os.path.exists(session_file):
    with open(session_file, 'rb') as f:
        cl = pickle.load(f)
else:
    # Login if session does not exist
    cl.login(username, password)
    with open(session_file, 'wb') as f:
        pickle.dump(cl, f)

# Path to the reels folder
reels_folder = r"D:\N\reels"

# Function to upload a reel with a random hashtag as caption
def upload_reel(video_path):
    try:
        # Create a list of hashtags
        hashtags = [
            "jdm", "nissan", "r", "s", "z", "cars", "honda", 
            "jdmcars", "jdmgram", "toyota", "stance", "jdmlifestyle", 
            "turbo", "jdmculture", "gtr", "carsofinstagram", "car", 
            "jdmnation", "carporn", "stancenation", "drift", "japan", 
            "subaru", "g", "mazda", "evo", "supra", "skyline", 
            "jdmlife", "carphotography", "civic", "nismo", "vtec", 
            "b", "rx", "sx", "k", "mitsubishi", "photography", 
            "racing", "wrx", "static", "drifting", "slammed", 
            "jdmsociety", "carlifestyle", "hondacivic", "a", "mx", 
            "subie", "gt", "nation", "jz", "jdmdaily", "rb", 
            "sti", "bmw", "typer", "mk", "v", "jdm", 
            "jdmsociety", "jdmstyle", "jdmcar", "jdmlove", "jdmasfuck", 
            "jdmbrand", "jdmlegends", "jdmindonesia", "jdmclassic", 
            "jdmfamily", "jdmporn", "jdmstance", "jdmwheels", 
            "jdmaf", "jdmcarculture", "jdmparts", "jdmhonda", 
            "jdmstickers", "jdmgirl", "jdmlegend"
        ]
        
        # Randomly select hashtags for the caption
        selected_hashtags = random.sample(hashtags, k=min(len(hashtags), 5))  # Select up to 5 random hashtags
        caption = f"JDM Clips {' '.join(['#' + tag for tag in selected_hashtags])}"

        # Upload video as a reel with a caption
        cl.video_upload(video_path, caption=caption)
        print(f"Uploaded {video_path} with hashtags: {caption}")
        return True  # Upload successful
    except Exception as e:
        print(f"Failed to upload {video_path}: {e}", flush=True)
        return False  # Upload failed

# Function to delete the reel after uploading
def delete_reel(video_path):
    try:
        os.remove(video_path)
        print(f"Deleted {video_path}")
    except Exception as e:
        print(f"Failed to delete {video_path}: {e}", flush=True)

# List all video files in the reels folder and sort them
reels_files = sorted([f for f in os.listdir(reels_folder) if f.endswith(".mp4")])

# Loop through each file and upload with a random delay
for index, reel in enumerate(reels_files, start=1):
    reel_path = os.path.join(reels_folder, reel)
    
    # Upload the reel and delete if successful
    if upload_reel(reel_path):
        delete_reel(reel_path)
    
    # Random delay between 2 to 6 minutes
    if index < len(reels_files):  # Avoid waiting after the last upload
        wait_time = random.uniform(30, 80)  # 2 to 6 minutes in seconds
        print(f"Waiting {wait_time / 60:.2f} minutes before next upload...", flush=True)
        time.sleep(wait_time)  # Use the randomly generated wait time
