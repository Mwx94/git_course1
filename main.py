lendth=input("pleas type length:\n")
width=input("pleas type width:\n")
price=input("how much for 1 meter:\n")
#convert type
length=float(lendth)
width=float(width)
price=float(price)
#احسب مساحة الغرفة عن طريق �
total_area=length*width
total_price=total_area*price
str_total_area=str(total_area)
str_total_price=str(total_price)
print("the total area is:"+str_total_area)
print("give the guy:$"+str_total_price)
