REGISTRY = {}

def registered(cls):
    key = f"{cls.__module__}.{cls.__name__}"
    REGISTRY[key] = cls
    return cls


if __name__ == "__main__":

    @registered
    class A:
        some_attribute = "a"

    print(REGISTRY)