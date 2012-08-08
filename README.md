# gallery #

A simple web.py based picture gallery operating solely on the file structure of your gallery

## Quick Setup ##

*   Checkout the repo
*   Get the web.py, pythonmagick, and pyexiv2 (min version 0.3.2) packages. E.g., on ubuntu:

        sudo apt-get install python-webpy python-pythonmagick python-pyexiv2

*   Link your images to static/galleries

        ln -s {your directory} static/galleries
    
*   Create or link a thumbnail directory

        mkdir static/thumbs
    
*   Run

        python code.py

    OR (on Linux)

        ./code.py

## Special Notes and Known Issues ##

### Image Directory Structure and Filenames ###

App runs off a simple, but specific directory structure underneath static/galleries. 
Images are expected in in the collection subdirectories.
    
    |-  gallery-1-name
        |-  collection-1-name
        |-  collection-2-name
        |-  collection-3-name
        |-  ...
    |-  gallery-2-name
        |-  collection-1-name
        |-  ...
    |-  ...
        
Directory and filenames cannot have spaces or other special characters in them.
There is no urlencoding or the like at this time.

### IMAGE_PATHS ###

You can set IMAGE_PATHS to serve your images through a web server, such as Apache. For example,
consider setting up your images at http://localhost/gallery-pics/galleries and thumbnails at
http://localhost/gallery-pics/thumbs. On a default Ubuntu apache2 install, you would set 
IMAGE_PATHS to these values:

    'disk_root': '/var/www/gallery-pics',
    'http_root': 'http://localhost/gallery-pics',
    'galleries': 'galleries',
    'thumbs': 'thumbs'
    
With these settings, put your source images in `/var/www/gallery-pics/galleries` and create
a thumbnail directory at `/var/www/gallery-pics/thumbs`.

