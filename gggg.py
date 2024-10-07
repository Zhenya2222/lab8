user_input=(input("Введіть декілька слів: "))
split_user_input=user_input.split()
print(split_user_input)
longest=max(split_user_input, key=len)
print("Нвйбільше слово: ", longest)
print("Кількість символів у найбільшому слоів: ", len(longest))




   