import video

class Tvshow(video.Video):
    def __init__(self,title,duration,season,episode,tv_station):
        video.Video.__init__(self,title,duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
