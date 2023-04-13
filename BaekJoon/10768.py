# 백준10768 : 특별한 날
def joyGo(M: str, D: str) -> None : 
    date = f"{M.zfill(2)}-{D.zfill(2)}"
    print("After" if date > "02-18" else "Special" if date == "02-18" else "Before")

if __name__ == "__main__" : 
    M = input()
    D = input()

    joyGo(M, D)