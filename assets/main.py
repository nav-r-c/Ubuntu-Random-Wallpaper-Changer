import os
import numpy as np

class WallpaperChanger:
    def __init__(self) -> None:
        print(__file__)
        self.getWallpaperPath()
        self.getRandomWallpaper()
        self.changeWallpaper(self.wallpaper)

    def getWallpaperPath(self) -> None:
        self.wallpaperPath = input("Enter Path to Wallpapers: ")
    
    def getRandomWallpaper(self) -> None:
        files = os.listdir(f"{self.wallpaperPath}")
        self.wallpaper = np.random.choice(files)
        
    def changeWallpaper(self, wallpaper) -> None: 
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark \"file://{self.wallpaperPath}/{wallpaper}\"")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri \"file://{self.wallpaperPath}/{wallpaper}\"")
        print(f"Changed Wallpaper to: {wallpaper}")

if __name__ == "__main__":
    w = WallpaperChanger()