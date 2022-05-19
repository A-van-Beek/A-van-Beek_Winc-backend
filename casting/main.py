# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print(f"Leek is {leek_price} euro per kilo.")

order = "leek 4"
leek_number = order[(order.find(" ")+1):]

sum_total = int(leek_number) * leek_price
print(sum_total)

broccoli_price = 2.34
boccoli_order = "broccoli 1.6"
boccoli_number = boccoli_order[(boccoli_order.find(" ")+1):]
sum_broccoli = round(float(boccoli_number) * broccoli_price, 2)
print(f"{boccoli_number}kg broccoli costs {sum_broccoli}e")