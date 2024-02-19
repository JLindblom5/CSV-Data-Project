with open ("CoromonDataset.csv", "r") as file:
    header = file.readline().split(",")
    stats = file.readlines()
    coromon_names = []
    coromon_types = []
    coromon_health_points = []
    coromon_attack = []
    coromon_special_attack = []
    coromon_defense = []
    coromon_special_defense = []
    coromon_speed = []
    coromon_stamina_points = []
    type_totals = {}
    type_counts = {}

    for items in stats:
        stats_split = items.split(",")
        coromon_names.append(stats_split[0])
        coromon_types.append(stats_split[1])
        coromon_health_points.append(stats_split[2])
        coromon_attack.append(stats_split[3])
        coromon_special_attack.append(stats_split[4])
        coromon_defense.append(stats_split[5])
        coromon_special_defense.append(stats_split[6])
        coromon_speed.append(stats_split[7])
        coromon_stamina_points.append(stats_split[8])   
    stamina_points_without_newline = [point.strip() for point in header]

    for nums in range(len(coromon_types)):
        current_type = coromon_types[nums]
        health_points_val = int(coromon_health_points[nums])
        attack_val = int(coromon_attack[nums])
        special_attack_val = int(coromon_special_attack[nums])
        defense_val = int(coromon_defense[nums])
        special_defense_val = int(coromon_special_defense[nums])
        speed_val = int(coromon_speed[nums])
        stamina_points_val = int(coromon_stamina_points[nums])

        if current_type in type_totals:
            type_totals[current_type][0] += health_points_val
            type_totals[current_type][1] += attack_val
            type_totals[current_type][2] += special_attack_val
            type_totals[current_type][3] += defense_val
            type_totals[current_type][4] += special_defense_val
            type_totals[current_type][5] += speed_val
            type_totals[current_type][6] += stamina_points_val
            type_counts[current_type] += 1
        else:
            type_totals[current_type] = [health_points_val, attack_val, special_attack_val, defense_val, special_defense_val, speed_val, stamina_points_val]
            type_counts[current_type] = 1

    def num_of_coromon():
        print(len(coromon_types),"coromon exist")

    def random_coromon(random):
        coromon_index= coromon_names.index(random)
        print(header[0],":",coromon_names[coromon_index])
        print(header[1],":",coromon_types[coromon_index])
        print(header[2],":",coromon_health_points[coromon_index])
        print(header[3],":",coromon_attack[coromon_index])
        print(header[4],":",coromon_special_attack[coromon_index])
        print(header[5],":",coromon_defense[coromon_index])
        print(header[6],":",coromon_special_defense[coromon_index])
        print(header[7],":",coromon_speed[coromon_index])
        print(stamina_points_without_newline[8],":",coromon_stamina_points[coromon_index])
        
    def types_coromon():
        a=[]
        for items in coromon_types:
            if items not in a:
                a.append(items)      
        b= ", ".join(a)
        print(f"The different types of Coromon's are {b}")
    

    def average_value():
        print("Average stats for each Coromon type:")
        for coromon_type, total in type_totals.items():
            count = type_counts[coromon_type]
            average = [t / count for t in total]
            print(f"\nType: {coromon_type}")
            print("Health Points:", average[0])
            print("Attack:", average[1])
            print("Special Attack:", average[2])
            print("Defense:", average[3])
            print("Special Defense:", average[4])
            print("Speed:", average[5])
            print("Stamina Points:", average[6])

    def health_points():
        health_list= []
        type_list = []
        for coromon_type, total in type_totals.items():
            count = type_counts[coromon_type]
            average = [t / count for t in total]
            health_list.append(average[0])
            type_list.append(coromon_type)
        a = (health_list.index(max(health_list))) 
        b = (health_list.index(min(health_list)))
        if letter_chosen == "E":
            print(f"Coromon type {type_list[a]} has an average of {max(health_list)} health points, which is the highest average of all types.")
        elif letter_chosen == "F":
            print(f"Coromon type {type_list[b]} has an average of {min(health_list)} health points, which is the lowest average of all types.")

    def attack_points():
        attack_points_list = []
        type_list = []
        for coromon_type, total in type_totals.items():
            count = type_counts[coromon_type]
            average = [t / count for t in total]
            attack_points_list.append(average[1])
            type_list.append(coromon_type)
        a= (attack_points_list.index(max(attack_points_list))) 
        b= (attack_points_list.index(min(attack_points_list))) 
        if letter_chosen == "G":
            print(f"Coromon type {type_list[a]} has an average of {max(attack_points_list)} attack points, which is the highest average of all types.")
        elif letter_chosen == "H":
            print(f"Coromon type {type_list[b]} has an average of {min(attack_points_list)} attack points, which is the lowest average of all types.")

    def special_attack_points():
        special_attack_points_list = []
        type_list = []
        for coromon_type, total in type_totals.items():
            count = type_counts[coromon_type]
            average = [t / count for t in total]
            special_attack_points_list.append(average[2])
            type_list.append(coromon_type)
        a= (special_attack_points_list.index(max(special_attack_points_list))) 
        b= (special_attack_points_list.index(min(special_attack_points_list))) 
        if letter_chosen == "I":
            print(f"Coromon type {type_list[a]} has an average of {max(special_attack_points_list)} special attack points, which is the highest average of all types.")
        elif letter_chosen == "J":
            print(f"Coromon type {type_list[b]} has an average of {min(special_attack_points_list)} special attack points, which is the lowest average of all types.")

    def defense_points():
        defense_points_list = []
        type_list = []
        for coromon_type, total in type_totals.items():
            count = type_counts[coromon_type]
            average = [t / count for t in total]
            defense_points_list.append(average[3])
            type_list.append(coromon_type)
        a= (defense_points_list.index(max(defense_points_list))) 
        b= (defense_points_list.index(min(defense_points_list))) 
        if letter_chosen == "K":
            print(f"Coromon type {type_list[a]} has an average of {max(defense_points_list)} defense points, which is the highest average of all types.")
        elif letter_chosen == "L":
            print(f"Coromon type {type_list[b]} has an average of {min(defense_points_list)} defense points, which is the lowest average of all types.")

    def special_defense_points():
        special_defense_points_list = []
        type_list = []
        for coromon_type, total in type_totals.items():
            count = type_counts[coromon_type]
            average = [t / count for t in total]
            special_defense_points_list.append(average[4])
            type_list.append(coromon_type)
        a= (special_defense_points_list.index(max(special_defense_points_list))) 
        b= (special_defense_points_list.index(min(special_defense_points_list))) 
        if letter_chosen == "M":
            print(f"Coromon type {type_list[a]} has an average of {max(special_defense_points_list)} special defense points which is the highest average of all types.")
        elif letter_chosen == "N":
            print(f"Coromon type {type_list[b]} has an average of {min(special_defense_points_list)} special defense points, which is the lowest average of all types.")

    def speed_points():
        speed_points_list = []
        type_list = []
        for coromon_type, total in type_totals.items():
            count = type_counts[coromon_type]
            average = [t / count for t in total]
            speed_points_list.append(average[5])
            type_list.append(coromon_type)
        a= (speed_points_list.index(max(speed_points_list))) 
        b= (speed_points_list.index(min(speed_points_list))) 
        if letter_chosen == "O":
            print(f"Coromon type {type_list[a]} has an average of {max(speed_points_list)} speed points, which is the highest average of all types.")
        elif letter_chosen == "P":
            print(f"Coromon type {type_list[b]} has an average of {min(speed_points_list)} speed points, which is the lowest average of all types.")
  
    print("Enter the letter corresponded with the information to see the information:")
    print("A. Number of Coromons that exist")
    print("B. Displays a Coromons information of your choice ")
    print("C. Different types of Coromons")
    print("D. Average value for each property of every Coromon type")
    print("E. Coromon type with the highest average health points")
    print("F. Coromon type with the lowest average health points")
    print("G. Coromon type with the highest average attack points")
    print("H. Coromon type with lowest average attack points")
    print("I. Coromon type with the highest average special attack points")
    print("J. Coromon type with the lowest average special attack points")
    print("K. Coromon type with the highest average defense points")
    print("L. Coromon type with the lowest average defense points")
    print("M. Coromon type with the highest average special defense points")
    print("N. Coromon type with the lowest special defense points")
    print("O. Coromon type with the highest average speed points")
    print("P. Coromon type with the lowest average speed points")
    letter_chosen= input("- Choose a letter: ").upper()
    print("--------------------------------------------------------------------")
    
    if letter_chosen== "A":
        num_of_coromon()

    if letter_chosen == "B":
        random_coromon_enter = input("Select any Coromon, and it's information will be displayed: ").capitalize()
        random_coromon(random_coromon_enter)

    if letter_chosen == "C":
        types_coromon()

    if letter_chosen == "D":
        average_value()

    if letter_chosen == "E":
        health_points()

    if letter_chosen == "F":
        health_points()

    if letter_chosen == "G":
        attack_points()

    if letter_chosen == "H":
        attack_points()

    if letter_chosen == "I":
        special_attack_points()

    if letter_chosen == "J":
        special_attack_points()

    if letter_chosen == "K":
        defense_points()

    if letter_chosen == "L":
        defense_points()

    if letter_chosen == "M":
        special_defense_points()

    if letter_chosen == "N":
        special_defense_points()

    if letter_chosen == "O":
        speed_points()

    if letter_chosen == "P":
        speed_points()
