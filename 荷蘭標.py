
import os
bid_process_end=False
dic=[]
while not bid_process_end:
  name=input("What is your name?")
  buy_bid=float(input("What's your bid?"))
  decition=input("Are there any other bidders? Types yes or no.").lower()
  add_dic={}
  add_dic[0]=name
  add_dic[1]=buy_bid
  add_dic[2]=decition
  dic.append(add_dic)    
  if decition=="yes":
    bid_process_end=False
    os.system('clear')
  elif decition=="no":
    bid_process_end=True


for i in range(0,len(dic)):
  max_bid=0
  if dic[i][1]> max_bid:
    max_bid=dic[i][1]
    get_bidder=max_bid=dic[i][0]
print(f"the winner is {get_bidder}, and the price is {max_bid}")
