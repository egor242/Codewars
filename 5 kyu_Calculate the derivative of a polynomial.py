def derivative(eq):
    if "x" not in eq:
        return "0"
    eq_tmp = eq.replace("-", "+-").lstrip("+")
    eq_tmp = eq_tmp.split("+")
    eq_tmp2 = []
    for element in eq_tmp:
        if "x^" in element:
            element_tmp = element.split("x^")
            if len(element_tmp[0]) == 1 and not element_tmp[0].isdigit():
                element_tmp[0] += "1"
            elif len(element_tmp[0]) == 0:
                element_tmp[0] = "1"
            eq_tmp2.append(element_tmp)
        elif "x" in element:
            eq_tmp2.append([element.split("x")[0] if len(element.split("x")[0]) > 0 else 1, 1])

    result = ""
    for a, b in eq_tmp2:
        result += str(int(a) * int(b)) + "x^" + str(int(b) - 1) + "+"
    if "x^0+" in result:
        result = result[:-4]
    result = result.replace("+-", "-").replace("^1+", "+").rstrip("+")
    return result


s = "33x^13+38x^12+20x^8+52x^6-20x^2"
print(derivative(s))





