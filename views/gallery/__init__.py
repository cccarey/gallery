import web, config, os

from app.gallery import Gallery

render = config.render

class root:
    def GET(self, gallery_name):
        gallery_split = gallery_name.split('/')
        if 'collection' in gallery_split:
            if 'simple' in gallery_split:
                collection_name = gallery_split[3]
            else:
                collection_name = gallery_split[2]
            gallery_name = gallery_split[0]
        
        gallery = Gallery(gallery_name)
        
        if 'simple' in gallery_split:
            if len(gallery_split[4]) == 0:
                current_image = gallery.get_next_image(collection_name)
            else:
                current_image = gallery_split[4]
            return render.simple(
                collection_name,
                gallery.get_disk_path(collection_name, current_image, for_disk=False), 
                gallery.get_previous_image(collection_name, current_image), 
                gallery.get_next_image(collection_name, current_image)
                )
        elif 'collection' in gallery_split:
            return render.collection(gallery.get_images(collection_name))
        else:
            return render.gallery(gallery)
