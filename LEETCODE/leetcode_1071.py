"""
2つの文字列sとtについて、次の条件を満たすとき「tはsを割る(divide)」と言います。
s=t+t+...+t+t (つまり、tを1回以上連結してsができる場合)

2つの文字列str1とstr2が与えられたとき、両方の文字列を割ることができる最も大きな文字列xを返してください。
もし存在しない場合は、空文字列""を返してください。

"""
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 両方を連結して同じなら公約数が存在する

        print("str1+str2:" + str1 + str2)
        print("str2+str1:" + str2 + str1)

        if str1 + str2 != str2 + str1:
            return ""
     
        # 長さの最大公約数を求めて、その長さの部分文字列を返す
        gcd_length = math.gcd(len(str1), len(str2))
        return str1[:gcd_length]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))
    print(sol.gcdOfStrings("ABABAB", "ABAB"))
    print(sol.gcdOfStrings("LEET", "CODE"))

