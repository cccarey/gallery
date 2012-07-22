# gallery #

A simple web.py based picture gallery operating solely on the file structure of your gallery

## Quick Setup ##

*   Checkout the repo
*   Get the web.py and pythonmagick packages. E.g., on ubuntu:

        sudo apt-get install python-webpy python-pythonmagick

*   Link your images to static/galleries

        ln -s {your directory} static/galleries
    
*   Create or link a thumbnail directory

        mkdir static/thumbs
    
    OR  

        ln -s {your directory} static/thumbs
    
*   Run

        python code.py

    OR (on Linux)

        ./code.py
    
## Special Notes and Known Issues ##

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


       
