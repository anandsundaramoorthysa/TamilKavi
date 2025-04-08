from glob import glob
import os
import json


for indexes, file_path in enumerate(glob('**/*.json')):    
    with open(file_path,"r+",encoding="utf-8") as file:
        data = json.load(file)
        print(data
              )


