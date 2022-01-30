from abc import ABC,abstractmethod
from dataclasses import dataclass


@dataclass
class Media:
    name : str
    location : str
    rate : float
    
    @abstractmethod
    def media_player(self):
        pass
   
class MediaPlayer(ABC):
    file_location=None
    
    def __init__(self):
        self.media_list=list()
        self.play_list = []

        for item in self.media_list :
            if item.location.startswith(self.file_location) :
                self.play_list.append(item)
                
    
    # @abstractmethod
    def set_playlist(self,media_list):
        pass

    def get_playlist(self):
        return self.media_list
    

    def play(self):
        for media in self.media_list:
            media.media_player()


    def playe_by_name(self):
        self.media_list = sorted(self.media_list, key=lambda x: x.name)
        self.play()

    
    def play_by_rating(self):
        self.media_list = sorted(self.media_list, key=lambda x: x.rating)
        self.play()

    

class WebMediaPlayer(MediaPlayer):
    file_location="https://"
    
    def play(self):
        
        for item in self.play_list:
            print (f"{item.name} playing on {item.location}")
            
            

class LocalMediaPlayer(MediaPlayer):
    file_location=("C:\\" , "/")
    
    def play(self):
        
        for item in self.play_list:
            print(f"{item.name} playing {item.location}")
            
            
            
   
   

'''checking'''
if __name__ == '__main__':
         
   
    media1 = Media('/loc1', 'music1', 1)
    media2 = Media('/loc2', 'music2', 2)


    my_list = [media1,media2]
    wmediaplayer = WebMediaPlayer(my_list)
    print(wmediaplayer.play())
    print(wmediaplayer.playe_by_name())
    print(wmediaplayer.play_by_rating())
    lmp = LocalMediaPlayer()

    print(lmp.play())
    print(lmp.playe_by_name())
    print(lmp.play_by_rating())