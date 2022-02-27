def rgbint(r, g, b):
    return  (r * (256^2)) + (g * 256) + b

def loadProps(name):
    f = open(name, "r")
    content = f.readlines()
    f.close()

    out = dict()

    for line in content:
        line = line.strip()
        if line == "": continue

        spl = line.split("=", 1)
        out[spl[0].strip()] = spl[1].strip()

    return out


named = loadProps("named.txt")
data = loadProps("data.txt")

for k, v in data.items():
    color = ""
    if v.startswith("NamedTextColor."):
        color = '%06x' % int(named[v.replace("NamedTextColor.", "")], 16)
    else:
        pts = v.split(", ")
        color = "%02x%02x%02x" % (int(pts[0]), int(pts[1]), int(pts[2]))
    # print(f"<#{color}>{k}: #{color}")
    print(f"<span class=\"mc-font cls\" style=\"color: #{color};\">{k}: #{color}</span><br/>")