from pathlib import Path
from typing import Final, Generator
from plyer import notification
from os import path

from config import XBOX_DVR_DIR, GAME_CLIPS_DIR


def get_game_dir(file_name: str) -> str:
    """
    Extracts the game directory from the file name.
    """
    game_dir = file_name[:file_name.find('-')]
    game_dir = ''.join(c for c in game_dir if c.isalnum() or c.isspace())
    game_dir = game_dir.replace(' ', '_')
    return game_dir

def determine_source_path(file_name: str) -> Path:
    """
    Determines the source path of the file.
    """
    return Path(f'{XBOX_DVR_DIR}\\{file_name}')

def determine_dest_path(file_name: str) -> Path:
    """
    Determines the destination path of the file.
    """
    file_path: str = f'{GAME_CLIPS_DIR}\\{get_game_dir(file_name)}\\{file_name}'
    return Path(file_path)

def migrate_file(file_name: str) -> None:
    """
    Migrates the file from the source path to the destination path.
    """
    source_path: Path = determine_source_path(file_name)
    dest_path: Path = determine_dest_path(file_name)
    if not dest_path.exists():
        dest_path.parent.mkdir(parents=True, exist_ok=True)

    source_path.replace(dest_path)
    
def organize_game_clips() -> None:
    notification.notify(title='Organize Game Clips',
                        message='Organizing...',
                        app_icon=r'C:\Users\jrhol\Automated-Tasks\organize_game_clips\a834d39f-1ab5-4d7d-ac2d-85192e54844d.ico',
                        app_name='Organize Game Clips',
                        timeout=3)
    
    xbox_dvr_path: Path = Path(XBOX_DVR_DIR)
    entries: Generator[Path, None, None] = xbox_dvr_path.iterdir()
    
    for entry in entries:
        name: str = entry.name
        if name[0].isalpha():
            migrate_file(name)
        
if __name__ == '__main__':
    organize_game_clips()
    

