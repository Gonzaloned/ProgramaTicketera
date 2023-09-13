import winsound

class SoundPlayer:
    
    def play(self, path:str):
        winsound.PlaySound(path, 0)

