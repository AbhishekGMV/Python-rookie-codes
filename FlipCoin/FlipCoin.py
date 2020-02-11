from random import randint
def flipCoin():
    '''Uses the randint function of random module to provide flip effect of a coin.
       Also counts the number of occurrence of each outcome(heads and tails).
    '''
    heads = tails = count = 0
    while True:
        n = input("Press any key to flip the coin or 'q' to quit: ")
        if n == 'q':
            break
        flip = randint(0,1)
        if flip == 0:
            heads+=1
            print('Heads')
        if flip == 1:
            tails+=1    
            print('Tails')
        count+=1    
    print(f'\nCoin was flipped {count} times ({tails} tails, {heads} heads)')  
    
if __name__ == '__main__':
    flipCoin() 
