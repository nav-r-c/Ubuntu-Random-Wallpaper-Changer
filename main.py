import os
import numpy as np

class WallpaperChanger:
    def __init__(self) -> None:
        print(__file__)
        self.getRandomWallpaper()
        self.changeWallpaper(self.wallpaper)
    
    def getRandomWallpaper(self) -> None:
        files = os.listdir("/home/nav-r/Pictures/Wallpapers")
        self.wallpaper = np.random.choice(files)
        
    def changeWallpaper(self, wallpaper) -> None: 
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark \"file:///home/nav-r/Pictures/Wallpapers/{wallpaper}\"")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri \"file:///home/nav-r/Pictures/Wallpapers/{wallpaper}\"")
        print(f"Changed Wallpaper to: {wallpaper}")

if __name__ == "__main__":
    w = WallpaperChanger()