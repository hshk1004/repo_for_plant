# def AaddB(A,B):
#     A=int(A)
#     B=int(B)
#     print(A+B)
# def AsubB(A,B):
#     A=int(A)
#     B=int(B)
#     print(A-B)
# def AmulB(A,B):
#     A=int(A)
#     B=int(B)
#     print(A*B)
# def AdevideB(A,B):
#     A=int(A)
#     B=int(B)
#     print('%0.0f' % (A/B))
# def AextB(A,B):
#     A=int(A)
#     B=int(B)
#     print('%0.0f' % (A%B))
# def check_range(A,B):
#     A=int(A)
#     B=int(B)
#     if A<=10000:
#         if A>=1:
#             if B<=10000:
#                 if B>=1:
#                     mathfuncall(A,B)
#     else:
#         return 0

    

# def allfunc():
#     A,B = input().split()
#     check_range(A,B)

# def mathfuncall(A,B):
#     AaddB(A,B)
#     AsubB(A,B)
#     AmulB(A,B)
#     AdevideB(A,B)
#     AextB(A,B)

# allfunc()

def allfunc():
    A,B = input().split()
    A=int(A)
    B=int(B)
    if A<=10000:
        if A>=1:
            if B<=10000:
                if B>=1:
                    print(A+B)
                    print(A-B)
                    print(A*B)
                    print('%0.0f' % (A/B))
                    print('%0.0f' % (A%B))
    else:
        return 0

allfunc()

# 결과 값이 같은데 왜 안되는지 이해가 안됨...