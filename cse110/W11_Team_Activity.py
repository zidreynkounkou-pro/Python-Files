# Core requirements
# 1

with open("hr_system.txt") as file:
    for new_file in file:

        # 2
        new_line = new_file.strip()
        clean_line = new_line.split(" ")
        if (clean_line[2]).lower() == "engineer":

            print(f"{clean_line[0]} (ID: {clean_line[1]}), {clean_line[2]} - ${float(clean_line[3]) /24 + 1000:.2f}")
        else:
            print(f"{clean_line[0]} (ID: {clean_line[1]}), {clean_line[2]} - ${float(clean_line[3])/24:.2f}")



