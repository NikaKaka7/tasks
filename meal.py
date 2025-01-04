#Suppose that you’re in a country where it’s customary to eat
# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00
# , and dinner between 18:00 and 19:00. Wouldn’t it be nice if
# you had a program that could tell you what to eat when?
def main():
    time = input("What time is it? ")
    if 7<= convert(time) <= 8:
        print("breakfast time")
    if 12<= convert(time) <= 13:
        print("lunch time")
    if 18<= convert(time) <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    minutes = round(int(minutes)/60,2)
    result = int(hours) + minutes
    return result



if __name__ == "__main__":
    main()
