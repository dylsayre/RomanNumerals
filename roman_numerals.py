class Solution:


    def intToRoman(number):

        romans = {
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1
        }
        answer = ''

        if number >= romans['I'] and number <= 3999:


            while number != 0:
                for k,v in romans.items():
                    if v <= number:
                        answer = answer + k
                        break
                number -= v
                print(number)
            return answer
        
        else:

            return Exception('Must be a valid number')



number = Solution.intToRoman(3999)

print(number)
