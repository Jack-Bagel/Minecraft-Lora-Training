# Scales images and replaces transparent regions by a solid color

from os import walk, path, mkdir
from PIL import Image


def scale_up_and_remove_bg(source_path, factor, color, output_dir):
    with Image.open(source_path) as source_img:
        source_img = source_img.convert("RGBA")
        pixel_map = source_img.load()

        x_size = source_img.size[0]
        y_size = source_img.size[1]

        for i in range(x_size):
            for j in range(y_size):

                if pixel_map[i,j][3] == 0:
                    pixel_map[i,j] = color
        
        output_path = f"{output_dir}{source_path.split('/')[-1].split('.')[-2]}.png"
        source_img.resize((x_size*factor,y_size*factor),Image.Resampling.BOX).save(output_path)

def scale_down_and_remove_bg(source_path, factor, color, output_dir):
    with Image.open(source_path) as source_img:
        source_img = source_img.convert("RGBA")
        pixel_map = source_img.load()

        x_size = source_img.size[0]
        y_size = source_img.size[1]

        for i in range(x_size):
            for j in range(y_size):

                if pixel_map[i,j][3] == 0:
                    pixel_map[i,j] = color
        
        output_path = f"{output_dir}{source_path.split('/')[-1].split('.')[-2]}.png"
        source_img.thumbnail((x_size*factor,y_size*factor),Image.Resampling.BOX).save(output_path)
    

if __name__ == "__main__":
    SCALING_FACTOR = 2
    SOURCE_DIR = r"C:/Users/ilysa/Documents/GitHub/Minecraft-Lora-Training/image_2/7_minecraft/"
    BG_COLOR = (0, 255, 0, 255) # (R, G, B, A) for color that replaces transparent pixels
    OUTPUT_DIR = r"C:/Users/ilysa/Documents/GitHub/Minecraft-Lora-Training/image_2/7_minecraft/"

    if not path.isdir(OUTPUT_DIR):
        mkdir(OUTPUT_DIR);

    for (_,_,filenames) in walk(SOURCE_DIR):
        for filename in filenames:
            scale_up_and_remove_bg(SOURCE_DIR+filename, SCALING_FACTOR, BG_COLOR, OUTPUT_DIR)