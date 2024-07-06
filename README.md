# The 47 Kenyan Counties

![Screenshot from 2024-07-04 06-51-19](https://github.com/OluochIan/kenya-counties-borders/assets/100572229/7425b06a-3cfc-4d4f-8ff6-f68c501bb1d2)


## Setup
    1. git clone 'https://github.com/OluochIan/kenyan-health-facilities.git'
    2. CReate a python virtual environment
    3. pip install -r requirements.txt
    
### Run Application
    - make build
    - make makemigrations
    - make migrate
    - make superuser
    - make shell
      to load the boundaries data run these commands in the shell
        >>> from app import load_layer
        >>> load_layer.run()
        >>> quit()


