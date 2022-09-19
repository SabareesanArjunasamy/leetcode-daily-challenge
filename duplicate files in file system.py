from collections import defaultdict


def findDuplicate(paths):
    m = defaultdict(list)
    for p in paths:
        path = p.split()

        directoryPath, rest = path[0], path[1:]
        for f in rest:
            fileName, fileContent = f.split('(')[0], f.split('(')[1][:-1]
            m[fileContent].append("{}/{}".format(directoryPath, fileName))
    # print(m)
    # print(m[k] for k in m.keys())
    # print(m[v] for v in m.values())
    return [m[k] for k in m.keys() if len(m[k]) > 1]


paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
         "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

print(findDuplicate(paths))

paths2 = ["root/a 1.txt(abcd) 2.txt(efgh)",
          "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]

print(findDuplicate(paths2))
