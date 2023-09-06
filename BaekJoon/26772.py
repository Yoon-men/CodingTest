# 백준26772 : Poziome serca
def joyGo(n: int) -> None : 
    text = """ @@@   @@@  
@   @ @   @ 
@    @    @ 
@         @ 
 @       @  
  @     @   
   @   @    
    @ @     
     @      """.split('\n')

    ans_list = [text[i] * n for i in range(len(text))]
    print('\n'.join(ans_list))


if __name__ == "__main__" : 
    joyGo(int(input()))