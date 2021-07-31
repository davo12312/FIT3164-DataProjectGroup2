

from base64 import b64encode
from json import dumps
from sys import argv

# specify encoding
ENCODING = 'utf-8'
SCRIPT_NAME, IMAGE_NAME, JSON_NAME = argv


# read in images, convert orginal encoding to bsae64 byte encoding,
# then further convert into strings in utf-8
with open(IMAGE_NAME,'rb') as png_file:
    byte_content = png_file.read()
    base64_bytes = b64encode(byte_content)
    base64_string = base64_bytes.decode(ENCODING)


# save data in dictionary
raw = {}
raw['name'] = IMAGE_NAME
raw['img_str'] = base64_string

json_data = dumps(raw, indent=2)


# save in json file
with open(JSON_NAME,'w') as json_file:
    json_file.write(json_data)




