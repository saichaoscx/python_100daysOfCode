#from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)
print("Welcome to the secret auction program.")

auction_list = []
otherBid = "yes"

while otherBid == "yes":
  new_auction = {}
  new_auction["name"] = input("What is your name?: ")
  new_auction["bid"] = int(input("What's your bid?: $"))
  auction_list.append(new_auction)
  otherBid = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  if otherBid == "yes":
   # clear()
    print(auction_list)
  else:
    final_name = ""
    final_bid = 0
    for i in range(len(auction_list)):
      if auction_list[i]["bid"] > final_bid:
        #print(i)
        final_bid = auction_list[i]["bid"]
        final_name = auction_list[i]["name"]
    #clear()
    print(f"The winner is {final_name} with a bid of ${final_bid}.")
