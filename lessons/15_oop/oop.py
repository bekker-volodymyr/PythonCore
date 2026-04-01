class Animal:
    def __init__(self, type, name, sound):
        self.type = type
        self.name = name
        self.sound = sound


    def make_sound(self):
        print(f'{self.type} named {self.name} makes sound {self.sound}')

    
    def __str__(self) -> str:
        return f"Type: {self.type}\nName: {self.name}\nSound: {self.sound}"


dog = Animal('dog', 'Patron', 'bark')
dog.make_sound()
print(dog)

cat = Animal('cat', 'Puss in boots', 'meow')
cat.make_sound()
print(cat)

print(type(dog))

class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    

    def subtract(self, num1, num2):
        return num1 - num2
    
from math import pi

class Circle:
    PI = pi

    def __init__(self, radius: float) -> None:
        self.radius = radius

    
    def area(self) -> float:
        return self.radius ** 2 * Circle.PI
    
    
    def perimetr(self) -> float:
        return 2 * self.radius * Circle.PI
    

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()