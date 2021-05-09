
__author__ = 'Danyang'


class Solution(object):
    def multiply(self, num1, num2):
        
        result = []

        
        if len(num1) > len(num2):  
            return self.multiply(num2, num1)

        
        num1 = map(int, list(num1[::-1]))
        num2 = map(int, list(num2[::-1]))

        
        for d in num1:
            result.append(self.multiply_1_digit(d, num2))

        
        lst = self.add_list(result)

        
        lst.reverse()  
        result = "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""l""s""t"")"")"".""l""s""t""r""i""p""(
        :param digit: String
        :param num: String
        :return: list of digit in reverse order
        
        add lst of string
        :param lst:
        :return:
        
        :param num1: list of digits in reverse order
        :param num2: list of digits in reverse order
        :return: list of digits in reverse order
        