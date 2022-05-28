class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int (age)
        self.tracks = list(tracks)
        self.score = float (score)
        
    @classmethod
    def change_name(self, new_name):
        self.name = new_name
        print("The student's new name is %s " %new_name)
        
    @classmethod
    def change_age(self, new_age):
        self.age = new_age
        print("The student's new age is %d " %new_age)

    def add_track(self, new_track):
        self.tracks.append(new_tracks)
        print("The student's new track is %s " %self.track)
        
    @staticmethod
    def get_score():s
        return (Bob.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(70.24)
