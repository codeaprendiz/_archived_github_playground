import pickle

class MyClass:
    def __init__(self, data):
        self.data = data

    def __reduce__(self):
        import os
        return (os.system, ('echo "Hello, world!"',))

user_input = input("Enter some data: ")
my_object = MyClass(user_input)
serialized_object = pickle.dumps(my_object)

deserialized_object = pickle.loads(serialized_object)