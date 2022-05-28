class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int (age)
        self.tracks = list(tracks)
        self.score = float (score)
        
    @classmethod
    def change_name(self, my_name):
        self.name = my_name
        print("The student's new name is %s " %my_name)
        
    @classmethod
    def change_age(self, my_age):
        self.age = my_age
        print("The student's new age is %d " %my_age)

    def add_track(self, my_track):
        self.track = my_track
        print("The student's new track is %s " %my_track)
        
    @staticmethod
    def get_score():
        return (Bob.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(70.24)
