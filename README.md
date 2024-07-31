👾The future of rol games is here
🖐️Dont miss our Kickstarter


##Content

-[Project description](#project_description)
-[Architecture System](#architecture)
-[Requeriments](#requeriments)
-[Instalation](#instalation)
-[Uses](#uses)
-[Project estrcture](proyect_estructure)
-[License](#license)

## Project Description
The rol interactive table has few modules:
1. **Image recognition**: A camera detects the position of the miniatures on the table
2. **Electromagnet control**: moves the miniatures thanks to the info send by the image recognition system
3. **Info visualization**: Shows the dinamic information like videos or images based of game events
4. **System cordination**: Manage the comunication between the diferent modules


## Architecture System
![Architecture_System](docs/arquitectura.png)

## Requeriments
- Python 3.8+
- OpenCV
- TensorFlow
- Paho-MQTT
- Pygame
- Kivy
