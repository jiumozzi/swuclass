## 모르겠음 ##

seminar_dict = {
    "Algorithm": "204",
    "DataAnlaysis": "207",
    "ArtificialInterlligence": "302",
    "CyberSecurity": "B101",
    "Network": "303",
    "Startup": "501",
    "TestStrategy": "105",
}
N = int(input())

seminars = [input() for _ in range(N)]

for seminar in seminars:
    print(seminar_dict[seminar])
