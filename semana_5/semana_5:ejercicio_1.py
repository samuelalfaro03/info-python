
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

combined_list = []
for i in range(len(first_list)):
    combined_list.append(first_list[i])
    combined_list.append(second_list[i])

print(combined_list)