# Minecraft-Lora-Training
Folder used to train a LoRa model to make Minecraft's style textures using the Kohya trainer.

# How to use
First thing first, you need to have a basic understanding of Stable Diffusion and how to use LoRas models.
Here are some tutorials to help you out:

How to Install & Use Stable Diffusion on Windows: https://youtu.be/onmqbI5XPH8

Once you arrive at the "Download model / checkpoint" section of the video, make sure you download and use stable diffusion V2.1 model: https://huggingface.co/stabilityai/stable-diffusion-2-1

This is what is based my LoRA model on, if you don't use this specific model, the LoRA won't work!


Stable Diffusion LoRA Models: A Complete Guide: https://aituts.com/stable-diffusion-lora/

You can find the Minecraft LoRA model in the Model folder of this repo.


Once you have all the basics and are ready to generate an image, **make absolutely sure that the resolution of the image is 256x256**, otherwise you'll get some weird results.

the reason behind this is that the images I trained the model on are all in 256x256, and trying to generate something with a different resolution will confuse the AI.

That's pretty much all there is to it, you can use any Sampling method that you want it won't really change anything.

# Limitations
despite have a relatively big data set for my training, the descriptions are extremely simple and are for the most part only the name of the texture itself.
That means that the AI doesn't know what a lot of things are supposed to look like. 

For example, it knows what a sword should look like and understands that a Diamond Sword is blue, and a Ruby Sword is red, but it doesn’t know what the handle or the blade of
a sword is, so if your prompt is something too specific, it will probably give you a crappy result.

To counter this problem, I will manually edit the descriptions of the 3000+ textures as well as remove the weird and redundant textures that could confuse the AI.
If you want to contribute and help me on this project, you are more than welcome. There is no need for new textures at the moment, adding good descriptions is what the training data is lacking.

# Contributions
If you wish to contribute to the project, you can directly edit the descriptions of the different items located in the "image/5_minecraft" folder. When modifying the text file, please be as precise as possible in describing the item. 
Here's an example for a diamond sword: "Diamond sword, Diamond blade, Diamond Hilt with a wooden grip." 
Something like that should do the trick. Although I could have explicitly mentioned a blue blade in the description, in Minecraft, diamond items are generally associated with the color blue/turquoise. By omitting that detail, the AI can infer that diamond items should be blue. If you wish to avoid AI inferences, you need to add complexity to the description.

When creating descriptions, the key objective is to ensure that the AI understands the appearance, nature, and specific characteristics of a given item.

# To the Authors of the different assets
If you are the author of certain assets used in training the AI and would like them to be removed, please reach out to me via Discord (Jack Bagel#5043) or open an issue specifying your request to have your assets removed from the dataset. I will promptly delete any models that utilized your assets and create new ones accordingly.
# Credits
Here is a list of all the mods and assets I used for training this model, along with their respective licenses:

Druidcraft (GNU Lesser General Public License)

SpellBladeNext/Fabric (MIT)

Artifacts (MIT)

RLArtifacts (MIT)

Better End (MIT)

Better Nether (MIT)

Farmer's Delight (MIT)

Enderscape (MIT)

Quark (CC BY-NC-SA 3.0)

TwilightForest (CC BY-NC-SA 4.0)

Nether's Delight (MIT)

Ice and Fire: Dragons (GNU Lesser General Public License)

Reliquary Reincarnations (GNU Lesser General Public License)

Alex's Mobs (GNU Lesser General Public License)

Botania (Botania custom license)

Ender IO (Public Domain *based*)

Immersive Armors (GNU Lesser General Public License)

End Remastered (I'm the owner and give permission to anyone to train on my mod assets)

Overite (MIT)

Echoing Depths (MIT)

malcolmriley (Creative Commons Attribution 4.0 International)

If I have made any mistakes regarding the licensing of these mods, please let me know.
