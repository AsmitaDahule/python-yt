from datetime import datetime

current_hour = datetime.now().hour

if current_hour >= 5 and current_hour < 12:
    print("Good Morning")
elif current_hour >= 12 and current_hour < 17:
    print("Good Afternoon")
elif current_hour >= 17 and current_hour < 21:
    print("Good Evening")
else:
    print("Good Night")
