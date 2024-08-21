class Solution:
    def interpret(self, command: str) -> str:
        mapping = {'G':'G', '()':'o', '(al)':'al'}       
        result=[]
        i=0
        
        while i < len(command):

            if command[i:i+4]=='(al)':
                result.append(mapping['(al)'])
                i+=4
            elif command[i:i+2]=='()':
                result.append(mapping['()'])
                i+=2
            elif command[i]=='G':
                result.append(mapping['G'])
                i+=1
        
        return ''.join(result)

