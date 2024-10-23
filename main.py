class Pakistan:
    def capital(self):
        print("The capital of Pakistan is Islamabad")
    def language(self):
        print("The language of Pakistan is Urdu")
class Finland:
    def capital(self):
           print("The capital of Finland is Helsinki")
    def language(self):
        print("The language of Finland is Finnish")
obj1=Pakistan()
obj2=Finland()        
for country in (obj1,obj2):
    country.capital()
    country.language()