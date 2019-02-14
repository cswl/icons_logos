#!/usr/bin/env python3

# Upload to imgur and generate links.

from imgurpoi import *

import json
import os, sys

from pathlib import Path, PurePath

def get_script_path() :
    return  Path(PurePath(sys.argv[0]).parent).resolve()

def init() :
    pathlist = Path(Path.cwd()).glob('logos/*')
    logos_data = dict()

    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        config = get_config()
        if not config:
            print("Cannot upload - could not find config file")
            return
        image = path
        imgur_resp= imgur_uploader(image, id=config["id"], secret=config["secret"])
        logos_str = PurePath(path).name
        if imgur_resp["success"] == True :
            imgur_data = imgur_resp["data"]
            print(logos_str)
            print (imgur_data.get("link"))
            logos_data[logos_str] = imgur_data.get("link")
            
    logos_file = get_script_path().joinpath('logos.txt')
    with open('logos.txt', 'w') as f:
        json.dump(logos_data, f, ensure_ascii=False)
        
    
init()