class SingletonClass:
    __instance = None

    @staticmethod
    def get_instance():
        if SingletonClass.__instance == None:
            SingletonClass.__instance = SingletonClass()
        return SingletonClass.__instance

    def __init__(self):
        if SingletonClass.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            SingletonClass.__instance = self


if __name__ == "__main__":

    my_instance = SingletonClass()
    # my_instance = SingletonClass().get_instance()
    print(my_instance)

    my_instance = SingletonClass.get_instance()
    print(my_instance)

    my_instance = SingletonClass.get_instance()
    print(my_instance)

    my_instance2 = SingletonClass()
    print(my_instance2)
