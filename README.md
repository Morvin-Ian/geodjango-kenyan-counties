# The 47 Kenyan Counties

![Screenshot from 2024-07-11 11-30-12](https://github.com/Morvin-Ian/kenyan-counties-borders/assets/78966128/7791be43-233d-4c5b-a018-8ce5aa4388d2)


## Setup
    1. git clone 'git@github.com:Morvin-Ian/kenya-counties.git'
    
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


