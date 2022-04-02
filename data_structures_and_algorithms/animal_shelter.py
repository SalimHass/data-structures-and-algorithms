from data_structures_and_algorithms.stack_and_queue import Queue


class Cat:
    def __init__(self, name):
        self.name = name


class Dog:
    def __init__(self, name):
        self.name = name

class AnimalShelter:

    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if type(animal) is Cat:
            self.cat_queue.enqueue(animal)
        if type(animal) is Dog:
            self.dog_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref == "cat":
            return self.cat_queue.dequeue()
        if pref == "dog":
            return self.dog_queue.dequeue()
        return None

if __name__=="__main__":
    tom=Cat("tom")
    wof=Dog("wof")
    ani_shel=AnimalShelter()
    ani_shel.enqueue(tom)
    ani_shel.enqueue(wof)
