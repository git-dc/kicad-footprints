filename = "C_0603_1608Metric.kicad_mod"


def change_file(filename):
    mark = False
    ref_line = ""
    with open(filename) as fp:
        new_lines = []
        for line in fp:
            if mark:
                print("\nFOOTPRINT:", filename, sep="\t", end="\n\n")
                print(ref_line)
                print("\tBEFORE:", line, sep="\t")
                line = line.split("size ")
                line[0] += "size "
                line[1] = line[1].split(")")
                line[1][0] = "0.508 0.508"
                line[1] = ")".join(line[1])
                line = "".join(line)
                line = line.split("thickness ")
                line[0] += "thickness "
                line[1] = line[1].split(")")
                line[1][0] = "0.127"
                line[1] = ")".join(line[1])
                line = "".join(line)
                print("\tAFTER:", line, sep="\t")
            if "REF**" in line:
                ref_line = line
                mark = True
            else:
                mark = False
                new_lines.append(line)
        with open(filename, "w") as fp:
            fp.writelines(new_lines)


[
    proc_datafile("./" + item)
    for item in sorted(os.listdir("irr_data"))
    if item[:5] == "Daily"
]
change_file(filename)
