
itm = input('Item (enter "done" when finished): ')
gros=[]
while itm != "done":
  a={'name':'' ,'price':0.0 ,'quantity':0 }
  a['name']=itm
  price = float(input('Price: '))
  a['price']=price
  quantity = int(input('Quantity: '))
  a['quantity']=quantity
  gros.append(a)
  itm = input('Item (enter "done" when finished): ')
print()
print('-------------------')  
print('receipt')
print('-------------------')

total=0.0
for items in gros:
  print ('{} {} {} KD'.format(items['quantity'],items['name'],items['price']))
  total = total + (items['quantity'] * items['price'])
  
print('-------------------')
print('Total Price: {} KD'.format(total))

