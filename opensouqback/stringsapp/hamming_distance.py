class hamming_distance:
    def __init__(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string
        self.initlize_disance()

    def initlize_disance(self):
        self.distance = 0
        for i in range(len(self.first_string)):
            if self.first_string[i] != self.second_string[i]:
                self.distance +=1        
    
    def __str__(self):
        return 'strings: {} {}\nhamming distance: {}'.format(self.first_string, self.second_string, self.distance)