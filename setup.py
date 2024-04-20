def set_xbox_dvr_dir() -> str:
    """
    Sets the Xbox DVR directory.
    """
    while True:
        xbox_dvr_dir: str = input('> Enter the Xbox DVR directory (for help, tpye \"help\"): ')
        if xbox_dvr_dir.lower() == 'help':
            print('> To find your Xbox DVR directory, do the following:\n\t1. Open your OneDrive folder.\n\t2. Navigate to and click on the Videos folder.\n\t3. Right-click on Game DVR.\n\t4. Press \"Copy as path\".\n\t5. Paste the path here and remove any quotation marks.\n')
            xbox_dvr_dir = input('> Enter the Xbox DVR directory: ').replace('\'', '').replace('\"', '')
        else:
            confirm: str = input(f'> Confirm the Xbox DVR directory is \"{xbox_dvr_dir}\" (yes/no): ')
            if confirm.lower() == 'yes':
                break
            else:
                continue

    return xbox_dvr_dir

def set_game_clips_dir() -> str:
    """
    Sets the Game Clips directory.
    """
    while True:
        game_clips_dir: str = input('> Enter the Game Clips directory: ')
        if game_clips_dir.lower() == 'help':
            print('> To find your Game Clips directory, do the following:\n\t1. Open your OneDrive folder.\n\t2. Navigate to and click on the Videos folder.\n\t3. Right-click on Game-Clips.\n\t4. Press \"Copy as path\".\n\t5. Paste the path here and remove any quotation marks.\n')
            print('> If you already have a seperate directory for your game clips, you can enter that directory instead.\n')
            game_clips_dir = input('> Enter the Game Clips directory: ').replace('\'', '').replace('\"', '')
        else:
            confirm: str = input(f'> Confirm the Game Clips directory is \"{game_clips_dir}\" (yes/no): ')
            if confirm.lower() == 'yes':
                break
            else:
                continue

    return game_clips_dir

if __name__ == '__main__':
    print('> Welcome to the Xbox Game DVR Organizer!\n> Here you can configure where you\'d like to store your game clips.\n')

    xbox_dvr_dir: str = set_xbox_dvr_dir()
    game_clips_dir: str = set_game_clips_dir()

    with open('config.py', 'w') as config_file:
        config_file.write(f'from typing import Final\n\n\n# INFO: Replace the paths with your own paths. These are my paths as an example.\nXBOX_DVR_DIR: Final[str] = r\'{xbox_dvr_dir}\'\nGAME_CLIPS_DIR: Final[str] = r\'{game_clips_dir}\'\n')
    
    print('> Configuration complete!')