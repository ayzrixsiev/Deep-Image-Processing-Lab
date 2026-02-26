import os
from skimage import data, io

output_dir = "data/benchmarks"
os.makedirs(output_dir, exist_ok=True)

images_to_save = {
    "astronaut.png": data.astronaut(),
    "camera.png": data.camera(),
    "coins.png": data.coins(),
    "coffee.png": data.coffee(),
    "cat.png": data.chelsea(),
    "grass.png": data.grass(),
}

print(f"📥 Saving benchmark images to {output_dir}...")

for filename, img_data in images_to_save.items():
    path = os.path.join(output_dir, filename)
    io.imsave(path, img_data)
    print(f"✅ Saved: {filename}")

print("\n🚀 Done! You now have a local dataset to play with.")
