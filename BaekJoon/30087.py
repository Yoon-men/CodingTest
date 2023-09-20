# 백준30087 : 진흥원 세미나
for _ in range(int(input())) : 
    semina = input()
    print("204" if semina == "Algorithm" else "207" if semina == "DataAnalysis" else "302" if semina == "ArtificialIntelligence" else "B101" if semina == "CyberSecurity" else "303" if semina == "Network" else "501" if semina == "Startup" else "105")