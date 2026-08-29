class Solution:
    def reverseBits(self, n: int) -> int:
        #n is a dummy binary this time, Now we have to do is i) First Convert this decimal _(reverse of the binary)
        binary = bin(n)[2:].zfill(32)     # binary string conversion & zfill(32) -> strict implies to pad to 32 bits
        res = ""
        rev = binary[::-1]        #Slice of form last 2 pos as it have '0b' notation
      
        return int(rev,2)


        # rev = binary[::-1]      # reversed string
        # print(rev)
        # return int(rev, 2)      #back to decimal
        #here int(string, base) : base specify in which data type is the string is of? of example 2-> string is binary, 16-> string is hexadecimal and convert it to standar int-> base10