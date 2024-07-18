# import time

# print ("я играю")

# time.sleep(10)

# print("я закончил")
# =========================================================
# import random

# random_number = random.randint(0, 100)
# print(random_number)
import random

min_n = 0
max_n = 100
count_us = 7
print(f"Начало игры угадай число от {min_n} Do {max_n}")

import time
print("начола игры")

bot_n = random.randint(0, 100)

while True:
    if count_us == 0:
        print(f"игра законченна")
        break
 
    user_ans = int(input(f"увас ешо {count_us} gjgsnjr угадайте число: "))
  
    if user_ans > bot_n:
        print("Это болше заданного числа: ")
    elif user_ans < bot_n:
        print("Это меньше заданного числа: ")
    elif user_ans == bot_n:
        print("ураааа вы угадали")
        break

    count_us -= 1


x1 = time.sleep(10)
print(bot_n)
print.x1 = ("игра законченна")