# IM_COOL_BOOY_GIF/main.py
from IM_COOL_BOOY_GIF.im_cool_booy_gif import main
from PIL import Image, ImageDraw, ImageFont
import os
import sys
import imageio
import numpy as np
import socket
from tqdm import tqdm

sdcard_path = '/storage/emulated/0/Download/'
output_folder = '/storage/emulated/0/IM-COOL-BOOY/'

valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.webp', '.tiff',
                    '.ico', '.raw', '.heif', '.heic', '.avif', '.exr', '.svg',
                    '.psd', '.indd')

text = "SL Android Official ™ | IM COOL BOOY"
font_path = "/system/fonts/NotoSerif-Bold.ttf"
font_size = 15
font = ImageFont.truetype(font_path, font_size)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def delete_existing_gifs(output_folder):
    gif_files = [file for file in os.listdir(output_folder) if file.endswith('.gif')]
    for gif_file in gif_files:
        os.remove(os.path.join(output_folder, gif_file))
    print("\033[1;31m🚮🚮🚮️ Existing GIFs in the output folder have been deleted...!\033[0m")

class GoldTqdm(tqdm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bar_format = "\033[1;33m{l_bar}{bar}{r_bar}\033[0m"

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

device_ip = get_ip()

frames = []
video_frames = []

try:
    delete_existing_gifs(output_folder)

    if not os.path.exists(sdcard_path):
        raise FileNotFoundError(f"The directory {sdcard_path} does not exist.")

    image_files = [os.path.join(sdcard_path, file) for file in os.listdir(sdcard_path)
                   if file.lower().endswith(valid_extensions)]

    if not image_files:
        print("\033[1;33m🚫 No images found in the folder! Please check the path. 🛑\033[0m")
        exit()

    output_path_gif = os.path.join(output_folder, "COOLBOOY.gif")
    output_path_video_gif = os.path.join(output_folder, "COOLBOOY_video.gif")

    base_width, base_height = 450, 450

    for img_path in GoldTqdm(image_files, desc="🔄 Processing Images", ncols=80, unit="file"):
        img = Image.open(img_path).convert("RGB")
        img = img.resize((base_width, base_height), Image.LANCZOS)

        draw = ImageDraw.Draw(img)

        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        x = (img.width - text_width) // 2
        y = img.height - text_height - 7

        shadow_offset = 2
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill="black")
        draw.text((x, y), text, font=font, fill="white")

        frames.append(np.array(img))
        video_frames.append(np.array(img))

    print("\n🔄 Saving Photo GIF...")
    with GoldTqdm(total=100, desc="⚙️ Creating Photo GIF", ncols=80, unit="step") as pbar:
        imageio.mimsave(output_path_gif, frames, fps=2, palettesize=1000, duration=0.2)
        for _ in range(100):
            pbar.update(1)

    print("\n🔄 Saving Video-like GIF...")
    with GoldTqdm(total=100, desc="⚙️ Creating Video GIF", ncols=80, unit="step") as pbar:
        imageio.mimsave(output_path_video_gif, video_frames, fps=6, palettesize=1000, duration=0.1)
        for _ in range(100):
            pbar.update(1)

    with imageio.get_writer(output_path_gif, mode='I', duration=0.2) as writer:
        writer.meta = {'IP Address': device_ip}

    with imageio.get_writer(output_path_video_gif, mode='I', duration=0.1) as writer:
        writer.meta = {'IP Address': device_ip}

    photo_gif_size = os.path.getsize(output_path_gif) / (1024 * 1024)
    video_gif_size = os.path.getsize(output_path_video_gif) / (1024 * 1024)

    print("\033[1;32m✅ GIFs were successfully created...! 🥳\033[0m")
    print(f"\033[1;32m📂 Photo GIF Path: {output_path_gif}\033[0m")
    print(f"\033[1;32m📂 Video-like GIF Path: {output_path_video_gif}\033[0m")
    print(f"\033[1;32m📏 Resolution: 450×450 (Square HD)\033[0m")
    print(f"\033[1;32m📦 Photo GIF Approx. Size: ~{photo_gif_size:.2f} MB\033[0m")
    print(f"\033[1;32m📦 Video-like GIF Approx. Size: ~{video_gif_size:.2f} MB\033[0m")
    print(f"\033[1;32m📡 Device IP Address: {device_ip}\033[0m")
    print("\033[1;32m🤝 SL Android Official ™ 💎\033[0m")
    print("\033[1;32m⚙️  Tool Developed By IM COOL BOOY 💻\033[0m")

    print("\033[1;31m🚫 Do not create inappropriate GIFs...! 🚫\033[0m")
    print("\033[1;33m⚠️️️❌💀\033[0m")

except FileNotFoundError as fnf_error:
    print("\033[1;31m🚫 Directory error occurred! Please check the path. 🛑\033[0m")
    print(f"\033[1;34mError Details: {str(fnf_error)}\033[0m")
    print("\033[1;33m🎯 Solution: Verify the path '{sdcard_path}' exists and contains valid image files.\033[0m")

except Exception as e:
    print("\033[1;31m🚫 An error occurred while creating the GIFs! 🛑\033[0m")
    print(f"\033[1;34mError Details: {str(e)}\033[0m")
    print("\033[1;33m🎯 Solution: Check for other issues such as permission errors or invalid image files.\033[0m")

def pink_text(text):
    return "\033[38;5;213m" + text + "\033[0m"

def main():

    print(pink_text("""
    1️⃣ Create a folder named 'Download' in your sdcard.
    2️⃣ Place the photos you want to include in the GIF into that folder.
    3️⃣ Run the command 'IM-COOL-BOOY-GIF'....➡️➡️➡️➡️
    """))

def main_function():
    print("🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️🛅️")

if __name__ == "__main__":
    main()
