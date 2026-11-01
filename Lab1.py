def analyze_log_file(log_file_path):
    try:
        my_file = open (log_file_path, "r")
    except FileNotFoundError:
        print("apache_logs.txt file not found")
    except IOError:
        print("apache_logs.txt Error reading file")
    result_dictionari = {}
    for line in my_file:
        print(line)
        my_list = line.split(" ")
        print(my_list)
        print(my_list[8])
        if my_list[8] in result_dictionari:
            result_dictionari[my_list[8]] += 1
        else:
            result_dictionari[my_list[8]] = 1
    return result_dictionari
result = analyze_log_file("apache_logs.txt")
print(result)
#analyze_log_file("apache_logs.txt")