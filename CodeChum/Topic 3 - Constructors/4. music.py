class Music:
    def __init__(self, duration: int = 0, genre: str = "Unknown", duration_type: str = "m"):
        self.duration = duration
        self.genre = genre
        
        if duration_type == "h":
            self.duration = self.duration*60
        elif duration_type == "d":
            self.duration = self.duration*1440