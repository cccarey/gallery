# -*- coding: UTF-8 -*-

import web, config, pyexiv2, unicodedata
from config import *
from api import *
from app.gallery import Gallery

class metadata:
    def GET(self, uri_base):
        set_headers()
        ids = self.get_ids(uri_base)
        metadata = self.get_metadata(ids)
        return json.dumps({
                'dimensions': metadata.dimensions, 
                'comment': metadata.comment,
                'mime_type': metadata.mime_type,
                'iptc_charset': metadata.iptc_charset,
                'exif': self.create_tag_dict(metadata, 'exif'), 
                'xmp': self.create_tag_dict(metadata, 'xmp')
            })

    def POST(self, uri_base):
        set_headers()
        ids = self.get_ids(uri_base)
        metadata = self.get_metadata(ids)
        if ids['tag_key'] == 'comment':
            metadata.comment = unicodedata.normalize('NFKD', web.input().value).encode('ascii', 'ignore')
        else:
            metadata[ids['tag_key']] = web.input().value
        metadata.write(preserve_timestamps=True)
        return ''
        
    def get_metadata(self, ids):
        gallery = Gallery(ids["gallery"])
        metadata = pyexiv2.ImageMetadata(gallery.get_disk_path(
                dir=ids["collection"], file=ids["image"]
            ))
        metadata.read()
        return metadata        
        
    def get_ids(self, uri_base):
        parts = uri_base.split('/', 4)
        return {
            "gallery": parts[0],
            "collection": parts[1],
            "image": parts[2],
            "tag_key": None if len(parts) < 4 else unicodedata.normalize('NFKD', parts[3]).encode('ascii', 'ignore')
            }

    def create_tag_dict(self, metadata, tag_type="exif"):
        result = dict()
        
        keys = metadata.exif_keys
        if tag_type == "xmp": keys = metadata.xmp_keys
        if tag_type == "iptc": keys = metadata.iptc_keys
        
        for key in keys:
            result[key] = {
                    'label': metadata[key].label if tag_type == 'exif' else metadata[key].title,
                    'human_value': metadata[key].human_value if tag_type == 'exif' else None,
                    'raw_value': metadata[key].raw_value
                }
        return result
        

