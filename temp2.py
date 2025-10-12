import os
from PIL import Image

# Set the root directory for your portfolio images
portfolio_dir = 'assets/portfolio'
thumbnails_dir = 'thumbnails'
thumbnail_size = (200, 200)

# Create thumbnails directory if it doesn't exist
os.makedirs(thumbnails_dir, exist_ok=True)

# Walk through all files in portfolio directory and subdirectories
for root, dirs, files in os.walk(portfolio_dir):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
            img_path = os.path.join(root, file)
            # Create a similar subfolder structure in thumbnails_dir
            rel_dir = os.path.relpath(root, portfolio_dir)
            thumb_subdir = os.path.join(thumbnails_dir, rel_dir)
            os.makedirs(thumb_subdir, exist_ok=True)
            thumb_path = os.path.join(thumb_subdir, file)
            # Create thumbnail
            try:
                with Image.open(img_path) as img:
                    img.thumbnail(thumbnail_size)
                    img.save(thumb_path)
                    print(f"Thumbnail created: {thumb_path}")
            except Exception as e:
                print(f"Error processing {img_path}: {e}")
