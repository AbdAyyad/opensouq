class levention_distance:
    def __init__(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string
        self.initlize_mem()
        self.distance = self.calc_distance(0,0)
       
    def initlize_mem(self):
        self.mem = []
        for i in range(len(self.first_string) + 1):
            self.mem.append([ -1 for j in range(len(self.second_string) + 1) ])
    
    def calc_distance(self, idx_one, idx_two):
        if idx_one == len(self.first_string) and idx_two == len(self.second_string):
            self.mem[idx_one][idx_two] = 0
            return self.mem[idx_one][idx_two]

        if(idx_one >= len(self.first_string) or idx_two >= len(self.second_string)):
            return 1000000000000000000


        if(self.mem[idx_one][idx_two] != -1):
            return self.mem[idx_one][idx_two]
    
    
        subCost = 0

        if self.first_string[idx_one] == self.second_string[idx_two]:
            subCost = 0
        else : 
            subCost = 1
    
        subPath = subCost + self.calc_distance(idx_one+1,idx_two+1)
        deletePath = 1 + self.calc_distance(idx_one,idx_two+1)
        insertPath = 1 + self.calc_distance(idx_one+1,idx_two)

        self.mem[idx_one][idx_two] = min(subPath,min(deletePath, insertPath))
        return self.mem[idx_one][idx_two]

    def __str__(self):
        return 'strings: {} {}\nlevention distance: {}'.format(self.first_string, self.second_string, self.distance)


