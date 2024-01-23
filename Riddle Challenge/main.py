from rick_riddle import solution

path = 'files/'
if __name__ == '__main__':
    with open(path + "inputs.txt", "r") as file:        
        lines = file.readlines() 

        for line in lines:            
            solve = solution(line[:-1])
            with open(path + "outputs.txt", "a") as f:
                f.write(f'The solution for {line} is:\n')
                f.write(f'{solve}\n')
                f.write('\n')
            