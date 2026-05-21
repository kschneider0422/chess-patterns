from PIL import Image


fp_out = "animation_5_13.gif"

frames = [
    'frame_5_13_005.png',
    'frame_5_13_015.png',
    'frame_5_13_045.png',
    'frame_5_13_135.png',
    'frame_5_13_405.png',
    'frame_5_13_405.png',
    'frame_5_13_405.png',
    'frame_5_13_405.png',
    ]

# Load images
img, *imgs = [Image.open(f) for f in frames]

# Save as GIF
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=750, loop=0)