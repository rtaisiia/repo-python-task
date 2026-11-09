def analyze_log_file(log_file_path):
    result_dictionari = {}
    try:
        with open (log_file_path, "r") as my_file:
            for line in my_file:
                # print("Перевірка:\n", line)
                my_list = line.split(" ")
                # print(my_list[8])
                if my_list[8] in result_dictionari:
                    result_dictionari[my_list[8]] += 1
                else:
                    result_dictionari[my_list[8]] = 1

    except FileNotFoundError:
        print("apache_logs.txt file not found")
    except IOError:
        print("apache_logs.txt Error reading file")
    return result_dictionari

result = analyze_log_file("apache_logs.txt")
print("РЕЗУЛЬТАТ:\n", result)