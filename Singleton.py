class Singleton(type):
    instanse={}
    def __call__(cls):
        if cls not in cls.instanse :
            cls.instances[cls] = super().__call__()
        return cls.instances[cls]