# Create raw images folder
mkdir raw_images
cd raw_images

# Use Azure Copy (azcopy) to download sample image dataset from LILA BC (https://lila.science/image-access)
azcopy cp "https://lilablobssc.blob.core.windows.net/missouricameratraps/images/Set1/1.02-Agouti/SEQ75520?st=2020-01-01T00%3A00%3A00Z&se=2034-01-01T00%3A00%3A00Z&sp=rl&sv=2019-07-07&sr=c&sig=zf5Vb3BmlGgBKBM1ZtAZsEd1vZvD6EbN%2BNDzWddJsUI%3D" . --recursive
azcopy cp "https://lilablobssc.blob.core.windows.net/missouricameratraps/images/Set1/1.02-Agouti/SEQ75583?st=2020-01-01T00%3A00%3A00Z&se=2034-01-01T00%3A00%3A00Z&sp=rl&sv=2019-07-07&sr=c&sig=zf5Vb3BmlGgBKBM1ZtAZsEd1vZvD6EbN%2BNDzWddJsUI%3D" . --recursive

#Create python venv
python3 -m venv env
source env/bin/activate

pip install pillow 


