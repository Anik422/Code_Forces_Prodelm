from posixpath import split


n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print((b-a%b)%b)
# exec(int (input())*"a,b = map(int, input().split());print((b-a%b)%b);")


# exec(int(input())*"a,b=map(int,input().split());print((b-a%b)%b);")