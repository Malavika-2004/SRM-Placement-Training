a=int(input())
if a<=200:
    print(f"Rs.{int(a*0.5)}")
elif 201<=a<=400:
    print(f"Rs.{int(a*0.65+100)}")
elif 401<=a<=600:
    print(f"Rs.{int(a*0.80+200)}")
else:
    print(f"Rs.{int(a*1.25+425)}")
