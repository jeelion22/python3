# parent class
class MP3:
  def __init__(self, artist, title, album, length, genre):
    self.artist = artist
    self.title = title
    self.album = album
    self.length = length
    self.genre = genre
    
  def get_artist(self):
    return f"The artist is {self.artist}"
    
  def get_title(self):
    return f"The title is {self.title}"
    
  def get_album(self):
    return f"The album is {self.album}"
    
  def get_length(self):
    return f"The length is {self.length}"
    
  def get_genre(self):
    return f"The genre is {self.genre}"
    
# child class

class Podcast(MP3):
    def __init__(self, name, title, length, genre, date):
      super().__init__(title, length, genre)
      self.name = name
      self.date = date

p = Podcast("Planet Money", "Hollywood's Black List", 1460, "economics", "10 July 2020")
print(p.get_name())