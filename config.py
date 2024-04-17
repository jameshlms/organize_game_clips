from typing import Final


# Replace the paths with your own paths. These are my paths as an example.
XBOX_DVR_DIR: Final[str] = r'C:\Users\jrhol\OneDrive\Videos\Xbox Game DVR'
GAME_CLIPS_DIR: Final[str] = r'C:\Users\jrhol\OneDrive\Videos\Game-Clips'

# The follwoing dictionary is used to specify where a game's clips should be stored.
# The format of the key should be the name of the game with Pascal Case with underscores for spaces.
# The value should be the path to the directory where the clips should be stored.
SPECIFIC_GAME_CLIPS_DIR: Final[dict[str, str]] = {}
