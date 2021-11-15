from pathlib import Path
from PIL import Image

exts = [".jpg", ".JPG"]
raw_path='raw_images'
output_path = "output"

percent = 75./100
thumbnail_size=(128,128)

# Generate Path objects
raw_path = Path.cwd().joinpath(raw_path)
output_path = Path.cwd().joinpath(output_path)
thumbnail_path = output_path.joinpath('thumbnails')

# Dictionary to save filenames, paths and thumbnail paths to
image_data={}

# Get File list
imfiles = raw_path.rglob("*.JPG") #simple
# To handle multiple extentions use the wcmatch library version of Path
# from wcmatch.pathlib import Path
# imfiles = raw_path.rglob(["*.JPG","*.jpg","*.png"])

# Resize to percentage
for img in imfiles:
    print(img)
    try:
        im = Image.open(img)
        width, height = im.size
        newsize = (  int(width * percent), int(height * percent)  )
        im_smaller = im.resize(newsize)

        # Convert im to thumbnail (in place)
        im.thumbnail(thumbnail_size)

        # Save outputs paths
        # Get relative img path
        relative_output_path = img.relative_to(  Path.cwd().joinpath(raw_path )  )
        im_output_path = output_path.joinpath( relative_output_path )

        # thumbnail_path
        im_thumbnail_path = thumbnail_path.joinpath(relative_output_path)

        # Add to image dictionary
        image_data[img.name] = ( str(im_output_path), 
                                 str(im_thumbnail_path),
                                 str(img.parent.name) )

        # Create Paths
        im_output_path.parent.mkdir(parents=True, exist_ok=True)
        im_thumbnail_path.parent.mkdir(parents=True, exist_ok=True)

        # Save
        im_smaller.save(im_output_path)
        im.save(im_thumbnail_path) #im was replaced by it's thumbnail
    except:
        print("cannot open " + img.name)


# create html list
html = """<!DOCTYPE html>
<html lang="en"
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Gallery</title>
    <link rel="stylesheet" href="style.css">
</head>
<style>
img {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 5px;
    width: 150px;
}
img:hover {
    box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
}
</style>
<body>
    
    <h2>Thumbnail Image</h2>
    <p>Click on the image to enlarge it.</p>"""

footer = """</body>
</html>"""

sequence_name_old=""

for i in image_data.items():
    image_name = i[0]
    image_path=i[1][0]
    thumbnail_path=i[1][1]
    sequence_name=i[1][2]
    if sequence_name != sequence_name_old:
        sequence_name_old = sequence_name
        html += f"""<h3>{sequence_name}</h3>
        """


    html += f"""<a target="_blank" href="{image_path}">
        <img src="{thumbnail_path}" alt="Forest">
    </a>"""

html += footer

try:
    from bs4 import BeautifulSoup
    html = BeautifulSoup(html, 'html.parser').prettify()
except:
    print ("BeautifulSoup not installed. resulting HTML might be a little rough...")
    

with open(output_path.joinpath('index.html'), "w") as outfile:
    outfile.write(html)    

