import web, config, os

from app.gallery import Gallery

render = config.render

class root:
    def GET(self, gallery_name):
        gallery_split = gallery_name.split('/')

        if 'collection' in gallery_split:
            if 'simple' in gallery_split:
                return self.simple_nav(gallery_split[0], gallery_split)
            if 'collage' in gallery_split:
                return self.collage(gallery_split[0], gallery_split)
            return self.collection(gallery_split[0], gallery_split)
        
        gallery = Gallery(gallery_name)
        return render.gallery(gallery)

    def collection(self, gallery_name, gallery_split):
        collection_name = gallery_split[2]
        gallery = Gallery(gallery_name)
        return render.collection(gallery.get_images(collection_name))

    def simple_nav(self, gallery_name, gallery_split):
        collection_name = gallery_split[3]

        gallery = Gallery(gallery_name)
        
        if len(gallery_split) == 4: # len(gallery_split[4]) == 0:
            current_image = gallery.get_next_image(collection_name)
        else:
            current_image = gallery_split[4]

        return render.simple(
            gallery_name,
            collection_name,
            gallery.get_disk_path(collection_name, current_image, for_disk=False), 
            gallery.get_previous_image(collection_name, current_image), 
            gallery.get_next_image(collection_name, current_image)
            )

    def collage(self, gallery_name, gallery_split):
        collection_name = gallery_split[3]
        gallery = Gallery(gallery_name)
        return render.collage(gallery_name, gallery.get_images(collection_name))

