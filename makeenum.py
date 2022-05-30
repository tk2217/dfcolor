from main import loadProps

named = loadProps("named.txt")
data = loadProps("data.txt")

print("class DFColor {")
for k, v in data.items():
    color = 0
    if v.startswith("NamedTextColor."):
        color = int(named[v.replace("NamedTextColor.", "")], 16)
    else:
        pts = v.split(", ")
        r = int(pts[0]) << 16
        g = int(pts[1]) << 8
        b = int(pts[2])
        color = r + g + b
    
    print(f"    public static final int {k} = 0x{hex(color)[2:].rjust(6, '0')};")

print("}")
