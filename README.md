# sunflower_fm-plugin-7zip
Very simple wrapper for ``7za`` as a plugin for [Sunflower FM](https://github.com/MeanEYE/Sunflower).

## Requirements
You need to have ``7za`` command on PATH.

## Installation

### Manual
- download package from https://github.com/tssk/sunflower_fm-plugin-7zip/releases
- extract to ``~/.config/sunflower/user_plugins/``
- rename created folder to ``7zip``

### GIT
```
cd ~/.config/sunflower/user_plugins
git clone https://github.com/tssk/sunflower_fm-plugin-7zip.git 7zip
```

## TODO / Known issues
- Does not check if the target archive already exist. - CAN OVERWRITE YOUR DATA!
- Does not hide Extract options when non-archive file type is selected.
- Can only add one directory or file to the archive.

## P.S.
Never used Python before. Code heavily copied from https://github.com/ArseniyK/archiver
