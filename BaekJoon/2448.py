# 백준2448 : 별 찍기 - 11
from typing import List

def joyGo(N: int) -> List[str]: 
    star_list = [
        "  *  ", 
        " * * ", 
        "*****"
    ]
    
    def makeRecursiveStar(n: int) -> List[str]: 
        if n == 3: 
            return star_list
        
        basic_star = makeRecursiveStar(n // 2)
        final_star = []

        ## Let's make first star!
        for row in basic_star: 
            final_star.append(' '*(n//2) + row + ' '*(n//2))
        
        ## Let's make second and third stars!
        for row in basic_star: 
            final_star.append(row + ' ' + row)

        return final_star


    return makeRecursiveStar(N)



if __name__ == "__main__": 
    stars = joyGo(int(input()))
    for row in stars: 
        print(row)



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, ans"), 
    [
        (
            1, 
            24, 
            '''                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** *****'''.split('\n')
        )
    ]
)

def test_joyGo(case_num: int, N: int, ans: List[str]) -> None: 
    res = joyGo(N)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {res})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ