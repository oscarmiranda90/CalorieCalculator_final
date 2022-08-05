def male_bmr(weight, height, age):
    # calculate male bmr
    return 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)


def female_bmr(weight, height, age):
    # calculate female bmr
    return 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)


def weight_conversion(weight, r):
    if r == 0:
        return float(weight)
    else:
        return float(weight / 2.204)


def height_conversion(height, r2):
    if r2 == 0:
        return float(height)
    else:
        return float(height * 30.48)
