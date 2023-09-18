import json
# function

noitems = 0


def gen(dict):
    # data[i]['items'][j]['items'][k]['items'][l]
    global noitems
    noitems += 1
    str1 = "["
    str1 += "\"" + dict["Brand"] + "\"" + ","
    str1 += "\"" + dict["Name"].replace("'", "").replace("\"", "") + "\"" + ","
    str1 += str(dict["Price"][1:]).replace(",", "") + ","
    str1 += str(dict["Rating"]) + ","
    str1 += str(dict["No of Reviews"]).replace(",", "") + "]"
    return str1


d = open('sort_data.json', 'r').read()

data = json.loads(d)
f = open("db.pl", "a")

cat = "items(categories,["
ele_cat = "items(electronics_categories,["
fur_cat = "items(furniture_categories,["
hou_cat = "items(household_categories,["
for i in range(len(data)):
    if (i != len(data)):
        cat += data[i]['type'] + ", "
        for j in range(len(data[i]['items'])):
            subcat = ""
            if i == 0:
                if (j != len(data[i]['items']) - 1):
                    ele_cat += data[i]['items'][j]["category"].lower().replace(" ",
                                                                               "_").replace("&", "and") + ", "
                    subcat = "items(" + data[i]['items'][j]["category"].lower().replace(
                        " ", "_").replace("&", "and") + ",["
                    for k in range(len(data[i]['items'][j]['items'])):
                        if (k != len(data[i]['items'][j]['items'])):
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ", "
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])

                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)
                            f.write("\n" + "\n" + prod)
                        else:
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + "])."
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)
                            f.write("\n" + "\n" + prod)
                else:
                    ele_cat += data[i]['items'][j]["category"].lower().replace(" ",
                                                                               "_").replace("&", "and") + "])."
                    subcat = "items(" + data[i]['items'][j]["category"].lower().replace(
                        " ", "_").replace("&", "and") + ",["
                    for k in range(len(data[i]['items'][j]['items'])):
                        if (k != len(data[i]['items'][j]['items']) - 1):
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ", "
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)

                            f.write("\n" + "\n" + prod)
                        else:
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + "])."
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)

                            f.write("\n" + "\n" + prod)
                print(subcat)
                print("")
                f.write("\n" + "\n" + subcat)
            elif i == 1:
                if (j != len(data[i]['items']) - 1):
                    fur_cat += data[i]['items'][j]["category"].lower().replace(" ",
                                                                               "_").replace("&", "and") + ", "
                    subcat = "items(" + data[i]['items'][j]["category"].lower().replace(
                        " ", "_").replace("&", "and") + ",["
                    for k in range(len(data[i]['items'][j]['items'])):
                        if (k != len(data[i]['items'][j]['items'])):
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ", "
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])

                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)
                            f.write("\n" + "\n" + prod)
                        else:
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + "])."
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)
                            f.write("\n" + "\n" + prod)
                else:
                    fur_cat += data[i]['items'][j]["category"].lower().replace(" ",
                                                                               "_").replace("&", "and") + "])."
                    subcat = "items(" + data[i]['items'][j]["category"].lower().replace(
                        " ", "_").replace("&", "and") + ",["
                    for k in range(len(data[i]['items'][j]['items'])):
                        if (k != len(data[i]['items'][j]['items']) - 1):
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ", "
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)

                            f.write("\n" + "\n" + prod)
                        else:
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + "])."
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)

                            f.write("\n" + "\n" + prod)
                print(subcat)
                print("")
                f.write("\n" + "\n" + subcat)
            elif i == 2:
                if (j != len(data[i]['items']) - 1):
                    hou_cat += data[i]['items'][j]["category"].lower().replace(" ",
                                                                               "_").replace("&", "and") + ", "
                    subcat = "items(" + data[i]['items'][j]["category"].lower().replace(
                        " ", "_").replace("&", "and") + ",["
                    for k in range(len(data[i]['items'][j]['items'])):
                        if (k != len(data[i]['items'][j]['items']) - 1):
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ", "
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])

                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)
                            f.write("\n" + "\n" + prod)
                        else:
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + "])."
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)
                            f.write("\n" + "\n" + prod)
                else:
                    hou_cat += data[i]['items'][j]["category"].lower().replace(" ",
                                                                               "_").replace("&", "and") + "])."
                    subcat = "items(" + data[i]['items'][j]["category"].lower().replace(
                        " ", "_").replace("&", "and") + ",["
                    for k in range(len(data[i]['items'][j]['items'])):
                        if (k != len(data[i]['items'][j]['items']) - 1):
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ", "
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)

                            f.write("\n" + "\n" + prod)
                        else:
                            subcat += data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + "])."
                            prod = "items(" + data[i]['items'][j]['items'][k]['subCategory'].lower().replace(
                                " ", "_").replace("&", "and") + ",["
                            for l in range(len(data[i]['items'][j]['items'][k]['items'])):
                                if (l == 0):
                                    prod += gen(data[i]['items'][j]
                                                ['items'][k]['items'][l])
                                elif (l != len(data[i]['items'][j]['items'][k]['items']) - 1):
                                    prod += ", " + \
                                        gen(data[i]['items'][j]
                                            ['items'][k]['items'][l])
                                else:
                                    prod += ", " + \
                                        gen(data[i]['items'][j]['items']
                                            [k]['items'][l]) + "])."
                            print("")
                            print(prod)

                            f.write("\n" + "\n" + prod)
                print(subcat)
                print("")
                f.write("\n" + "\n" + subcat)
    else:
        cat += data[i]['type'] + "])."


print(ele_cat)
print(fur_cat)
print(hou_cat)
f.write("\n" + "\n" + ele_cat)
f.write("\n" + "\n" + fur_cat)
f.write("\n" + "\n" + hou_cat)
# print(fur_subcat)
# print(hou_subcat)
print(cat)
f.write("\n" + "\n" + cat)
# d.close()
f.close()

print(noitems)
