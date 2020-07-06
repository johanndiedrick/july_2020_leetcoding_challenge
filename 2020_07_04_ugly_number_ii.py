ass Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        numbers = [1]
        
        i = 0
        j = 0
        k = 0
        
        while(len(numbers) <= n - 1):
            
            temp1 = numbers[i] * 2;
            temp2 = numbers[j] * 3;
            temp3 = numbers[k] * 5;
            
            min_temp = min(temp1, temp2, temp3)
            
            numbers.append(min_temp)
            
            if min_temp == temp1: i += 1
                
            if min_temp == temp2: j += 1
                
            if min_temp == temp3: k += 1
                
        print(numbers)
        return numbers[-1]
        
        '''
        counter = 1
        for num in range(1, 1690*2*3*5):
            if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0):
                counter += 1
                print(num)
            if counter == n:
                return num
        '''
