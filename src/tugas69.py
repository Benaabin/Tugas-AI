from operator import truediv


def checkFloat(bil):
    try:
        float(bil)
        return True
    except ValueError:
        return False

print(checkFloat("abc123"))
print(checkFloat("123.321"))