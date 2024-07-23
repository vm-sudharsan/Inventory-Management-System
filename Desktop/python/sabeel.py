#Coffee Machine Project
def check(order):
      for i in order:
            if order[i]>resources[i]:
                  print(f"not enough {i}")
                  return False
      return True
def coins():
      print("insert coin")
      t=0
      a=5*int(input("5Rs:"))
      b=10*int(input("10Rs:"))
      c=20*int(input("20Rs:"))
      t=a+b+c
      return t
def suc(a,b):
      if a>=b:
            global profit
            profit+=b
            c=a-b
            print(f"Here is your Rs{c} in change")
            return True
      else:
            print("Sorry thats not enough money. money refunded")
            return False
def make(a,order):
      for i in order:
           resources[i]-=order[i]
      print(f" enjoy your {a}")   

profit=0
menu={
      "latte":{
            "ingredients":{
                   "water":200,
                   "milk":150,
                   "coffee":24,
            },
            "cost":150
      },
      "cappuccino":{
            "ingredients":{
                   "water":250,
                   "milk":100,
                   "coffee":24,
            },
            "cost":200
      },
      "expresso":{
            "ingredients":{
                   "water":50,
                   "coffee":18,
            },
            "cost":100
      }
}
resources={
      "water":500,
      "milk":200,
      "coffee":100,
}
is_on=True
while is_on:
      choice=input("what would you like to have?(latte/expresso/cappuchino)")
      if choice=="off":
            is_on=False
      if choice=="report":
            print(f"Water={resources['water']}ml")
            print(f"Milk={resources['milk']}ml")
            print(f"coffee={resources['coffee']}ml")
            print(f"money=Rs{profit}")
      else:
            coffe_type=menu[choice]
            print(coffe_type)
            if check(coffe_type["ingredients"]):
                 pay=coins()      
                 if suc(pay,coffe_type['cost']):
                       make(choice,coffe_type['ingredients'])