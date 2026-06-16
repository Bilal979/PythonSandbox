

def cheese_and_buns(org_fun):
    def wrap():
        print('I am upper bun')
        org_fun()
        print('I am lower bun')
    return wrap()

@cheese_and_buns
def chicken():
    print('I\'m roasted chicken')


# cheese_and_buns(chicken)