# Python Image Manipulation Tutorial

Create raw images folder
```bash
mkdir raw_images
cd raw_images
```

Use [Azure Copy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) to download sample image dataset from [LILA BC](https://lila.science/image-access)
```bash
azcopy cp "https://lilablobssc.blob.core.windows.net/missouricameratraps/images/Set1/1.02-Agouti/SEQ75520?st=2020-01-01T00%3A00%3A00Z&se=2034-01-01T00%3A00%3A00Z&sp=rl&sv=2019-07-07&sr=c&sig=zf5Vb3BmlGgBKBM1ZtAZsEd1vZvD6EbN%2BNDzWddJsUI%3D" . --recursive
azcopy cp "https://lilablobssc.blob.core.windows.net/missouricameratraps/images/Set1/1.02-Agouti/SEQ75583?st=2020-01-01T00%3A00%3A00Z&se=2034-01-01T00%3A00%3A00Z&sp=rl&sv=2019-07-07&sr=c&sig=zf5Vb3BmlGgBKBM1ZtAZsEd1vZvD6EbN%2BNDzWddJsUI%3D" . --recursive
```

Create python venv
```bash
python3 -m venv env #only done once
```
Activate python virtual enviroment
```bash
source env/bin/activate
```

Install dependancies
```bash
pip install pillow #only need to do once 
```

