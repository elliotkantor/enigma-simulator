# Enigma Encoder
A collection of accessible interfaces to interact with the [Enigma Machine Simulator](www.101computing.net/enigma-encoder/).

## Local Installation
1. Install python3
2. Download and unzip this file
3. Change directories to this file by typing `cd path/to/enigma-simulator`
4. If you will be running the app, install packages with `python3 -m pip install -r requirements.txt`

## Running the code
### Hosted web app
Go to [the app](https://share.streamlit.io/elliotkantor/enigma-simulator/main/app.py) and follow instructions to use.
### Basic Command Line
1. Run `python3 main.py`
2. Enter the text you want to encode/decode (it goes both ways). Enter nothing to stop the program. Type a leading space to save to `output.txt`. 
### Web app (local)
1. Run `streamlit run app.py`
2. Your web browser should open to `localhost:8501` and you can use the site. Settings are not saved after refresh.

## Changing settings
The simplest way to change settings is to open `settings.py` in a text editor like Notepad (NOT MS Word), change values to something that makes sense, and saving it. If you need to reset settings, you can copy `settings_backup.py` and overwrite `settings.py`. If you really mess things up you can re-download this repository.

### Crucial settings
The following are the most important settings that you'll want to mess with:
- `rotors`: can be I - V (1 to 5), with exactly 3 rotors selected. Extras at the end will be ignored
- `reflector`: either UKW-B or any other string (goes to reflector B or C)
- `ringSettings`: any three unique capital letters
- `ringPositions`: any three unique capital letters
- `plugboard`: an arbitrary number of 2 letter combos, where no letter EVER repeats in the entire space-separated list. You can make it empty to not use the plugboard.