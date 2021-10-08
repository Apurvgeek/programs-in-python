import random 
import argparse 
import string

class RandPass:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.arguments()
        self.args = self.parser.parse_args()    
        
    def arguments(self):
        self.parser.add_argument('--nums','-n',type=int)
        self.parser.add_argument('--asciinum','-a',type=int)
        self.parser.add_argument('--letters','-l',type=int)

    def password(self):
        if self.args.nums:
            print(''.join(random.sample(string.digits,self.args.nums)))
        elif self.args.asciinum:
            print(''.join(random.sample(string.ascii_letters+string.digits,self.args.asciinum)))
        elif self.args.letters:
            print(''.join(random.sample(string.ascii_letters,self.args.letters)))
        else:
            print(''.join(random.sample(string.ascii_lowercase,6)))
x=RandPass()
x.password()
