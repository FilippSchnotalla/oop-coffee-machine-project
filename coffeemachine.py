class CoffeeMachine():
    def __init__(self, water, coffee, milk, money):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.money = money
        self.MENU = {
            'espresso': {
                'ingredients': {
                    'water': 50,
                    'coffee': 18,
                },
                'cost': 1.5,
            },
            'latte': {
                'ingredients': {
                    'water': 200,
                    'milk': 150,
                    'coffee': 24,
                },
                'cost': 2.5,
            },
            'cappuccino': {
                'ingredients': {
                    'water': 250,
                    'milk': 100,
                    'coffee': 24,
                },
                'cost': 3.0,
            }
        }
        
    def check_resources(self, drink):
        if self.water < self.MENU[drink]['ingredients']['water']:
            print('Not enough water to make ', drink)
            return False
        elif self.coffee < self.MENU[drink]['ingredients']['coffee']:
            print('Not enough coffee to make ', drink)
            return False
        if drink == 'latte' or drink == 'cappuccino':
            if self.milk < self.MENU[drink]['ingredients']['milk']:
                print('Not enough milk to make ', drink)
                return False
        return True
    
    def substract_resources(self, drink):
        self.water -= self.MENU[drink]['ingredients']['water']
        self.coffee -= self.MENU[drink]['ingredients']['coffee']
        if drink == 'latte' or drink == 'cappuccino':
            self.milk -= self.MENU[drink]['ingredients']['milk']
            
    def payment(self):
        print('Please insert coins.')
        quarters = input('How many quarters?: ')
        dimes = input('How many dimes?: ')
        nickles = input('How many nickles?: ')
        pennies = input('How many pennies?: ')
        total = (float(quarters) * 0.25) + (float(dimes) * 0.10) + (float(nickles) * 0.05) + (float(pennies) * 0.01)
        print('Total: {0}$'.format(total))
        return total

    def check_payment(self, payment, drink):
        if payment >= self.MENU[drink]['cost']:
            if payment > self.MENU[drink]['cost']:
                print('Here is your change of {0}$.'.format(payment - self.MENU[drink]['cost']))
            self.substract_resources(drink)
            print('Here is your {0}, enjoy!.'.format(drink))
        else:
            print('Not enough coins here is your refund of {0}$.'.format(payment))
            
    def run(self):
        while(True):
            user_input = input('What would you like? Espresso | Latte | Capuccino: ')
            if user_input == 'off': exit()
            
            elif user_input.lower() == 'espresso':
                if self.check_resources('espresso'):
                    paying = self.payment()
                    self.check_payment(paying, 'espresso')
                    self.money += self.MENU['espresso']['cost']
                
            elif user_input.lower() == 'latte':
                if self.check_resources('latte'):
                    paying = self.payment()
                    self.check_payment(paying, 'latte')
                    self.money += self.MENU['latte']['cost']
                
            elif user_input.lower() == 'cappuccino':
                if self.check_resources('cappuccino'):
                    paying = self.payment()
                    self.check_payment(paying, 'cappuccino')
                    self.money += self.MENU['cappuccino']['cost']
                
            elif user_input.lower() == 'report':
                print('Water:', self.water)
                print('Milk:', self.milk)
                print('Coffee:', self.coffee)
                print('Profit:', self.money)
                
            else:
                print('Please choose between Espresso | Latte | Capuccino.')
                print()