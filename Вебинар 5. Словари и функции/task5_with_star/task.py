def to_roman(val):
    """Преобразование арабского числа в римское
    :param val: арабское число
    :return: римское число
    """
    # todo Здесь нужно написать код
    o1 = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
    o2 = {10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC"}
    o3 = {100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM"}
    o4 = {1000: "M", 2000: "MM", 3000: "MMM"}
    roman_str = str()
    if val // 1000 * 1000 != 0:
        roman_str += o4[val // 1000 * 1000]
    if val // 100 % 10 * 100 != 0:
        roman_str += o3[val // 100 % 10 * 100]
    if val // 10 % 10 * 10 != 0:
        roman_str += o2[val // 10 % 10 * 10]
    if val % 10 != 0:
        roman_str += o1[val % 10]
    return roman_str
