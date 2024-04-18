n, m = map(int, input().split())
#2d dp
dp = [10000000000 for i in range(n)]
for i in range(m):
    nr_books, ship_cost = map(int, input().split())
    for j in range(nr_books):
        book_nr, book_cost = map(int, input().split())
        if dp[book_nr-1] > book_cost+ship_cost:
            dp[book_nr - 1] = book_cost + ship_cost

print(sum(dp))