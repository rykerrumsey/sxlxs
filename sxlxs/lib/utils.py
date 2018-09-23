from pyfiglet import Figlet

def printTitleScreen():
    """Print title screen to the console"""
    # tested 'isometric3' 'o8' 'jazmine'
    print()
    f = Figlet(font='cosmic')
    print(f.renderText('sxlxs'))

# verify to make sure the file exists return True if it does False if it does not
# todo: move to lib dir
def verify_file(file_path):
    # expand file path
    file_path = fs.abspath(file_path)

    # convert file_path to Path object
    file_path = Path(file_path)

    # check to see if the file exist
    if file_path.is_file():
        return True
    else:
        return False
