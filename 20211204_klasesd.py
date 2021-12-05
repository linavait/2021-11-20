def greeting(func):
    def wrapper(*args, **kwargs):
        return f" merry christmas , {func(*args, **kwargs)}"
    return wrapper


@greeting
def kiss():
    return ":*"

@greeting
def personalization(name):
    return f" dear {name} "


if __name__ == "__main__":
    # dekoruota_kiss_func = greeting(kiss)
    # print(kiss())
    # print(dekoruota_kiss_func())
    # dekoruota_personalization_fun = greeting(personalization)
    # print(dekoruota_personalization_fun("John"))
    print(kiss())
    print(personalization(name="Smith"))
