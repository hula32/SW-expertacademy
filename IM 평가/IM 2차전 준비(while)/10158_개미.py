# 가로 w 세로 h
# 출발 (p, q)
# 45도 방향으로 움직임
# 1시간 뒤 (p+1, q+1) 한 칸당 1시간
# 경계 부딪치면 반사
# t시간 후의 위치(x,y) 계산



# 경계를 만나면 현재 부호와 반대로 움직임(+ -> - / - -> +)



# r이 w에 도달하기 전
def r_up(r, time_r):
    start_r = r
    time_r = 0

    while start_r < w:
        start_r += 1
        time_r += 1
    
    return start_r, time_r

# r이 w에 도달한 후
def r_down(r, time_r):
    start_r = r
    time_r = 0

    while start_r > 0:
        start_r -= 1
        time_r = 0

    return start_r, time_r

# c이 w에 도달하기 전
def c_up(c, time_c):
    start_c = c
    time_c = 0

    while start_c < w:
        start_c += 1
        time_c += 1
    
    return start_c, time_c

# c이 0에 도달한 후
def c_down(c, time_c):
    start_c = c
    time_c = 0

    while start_c > 0:
        start_c -= 1
        time_c = 0

    return start_c, time_c


w, h = map(int, input().split()) # 배열 
p, q = map(int, input().split()) # 처음 위치
t = int(input(())) # 시간
 
# t 시간 후의 위치
time_r = time_c = 0 # 현재시간
start_r, start_c = p, q # 위치


if 0 <= start_r < w and 0 <= start_c < h:
    if time_r < t and time_c < t: 
        s_r, t_r = r_up(start_r, time_r)
        start_r = s_r
        time_r = t_r
        s_c, t_c = c_up(start_c, time_c)
        start_c = s_c
        time_c += t_c
if start_r == w:
    
    s_r, t_r = r_down(start_r, time_r)
    start_r = s_r
    time_r += t_r
if start_c == h:
    s_c, t_c= c_down(start_c, time_r)
    start_c = s_c
    time_c += t_c
   

    




