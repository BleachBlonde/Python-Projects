shareNumber= float(input('Enter number of shares:'))
purchasePrice= float(input('Enter purchase price:'))
sellPrice= float(input('Enter sale price:'))

#Math to get determine the amount lost or gained
initialPurchase= shareNumber*purchasePrice
initialSell= shareNumber*sellPrice

#Stock Brokers Payments
stockBroker= initialPurchase*0.03
final_stock_broker= initialSell*0.03

#Absolute Value tells the computer not to throw a negative in the display of how much is lost or gained
finalSell= initialSell-(final_stock_broker+stockBroker+initialPurchase)
show= abs(finalSell)
totalCost= initialPurchase+stockBroker+final_stock_broker


if initialSell >= totalCost:
	print ('After the transaction, you gained', show,'dollars.')
else:
	print ('After the transaction, you lost', show,'dollars.')
input('\nPress ENTER to exit')
