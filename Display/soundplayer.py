from multiprocessing import Process
import winsound

class SoundPlayer:
    
    def play(self, path:str):
        winsound.PlaySound(path, 0)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()