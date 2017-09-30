class Event(list):
    def __call__(self, *args, **kwargs):
        for f in self:
            f(*args, **kwargs)
