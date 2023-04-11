# Calcute the wholesale price for 60 bookcovers

cp = 24.95
sp1 = 3
sp2 = 0.75

wholesale_price = (cp * 0.6) * 60

shipping_cost = (3 + (59 * sp2))

discounted_price = wholesale_price + shipping_cost
print(discounted_price)

# Ans from source
print(60 *(0.6 * cp + sp2) + (sp1 - sp2))
