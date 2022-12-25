import os
import numpy as np
import pickle

class WallpaperChanger:
    def __init__(self) -> None:
        self.getWallpaperPath()
        self.getRandomWallpaper()
        self.changeWallpaper(self.wallpaper)
        self.storeWallpaperPath()

    def getWallpaperPath(self) -> None:
        if ("path.bin" not in os.listdir(__file__.rstrip("main.py"))):
            self.wallpaperPath = input("Enter Path to Wallpapers: ")
        else:
            file = open("path.bin", "rb")
            self.wallpaperPath = pickle.load(file)
    
    def getRandomWallpaper(self) -> None:
        files = os.listdir(f"{self.wallpaperPath}")
        self.wallpaper = np.random.choice(files)
        
    def changeWallpaper(self, wallpaper) -> None: 
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark \"file://{self.wallpaperPath}/{wallpaper}\"")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri \"file://{self.wallpaperPath}/{wallpaper}\"")
        print(f"Changed Wallpaper to: {wallpaper}")
    
    def storeWallpaperPath(self) -> None:
        with open("path.bin", "wb") as file:
            pickle.dump(self.wallpaperPath, file)
        

if __name__ == "__main__":
    w = WallpaperChanger()