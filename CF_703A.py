n = int(input())
m_count = 0
c_count = 0
for i in range(n):
    M, C = map(int, input().split())
    if M > C:
        m_count += 1
    elif M < C:
        c_count += 1
if m_count == c_count:
    print("Friendship is magic!^^")
elif m_count > c_count:
    print("Mishka")
elif m_count < c_count:
    print("Chris")
