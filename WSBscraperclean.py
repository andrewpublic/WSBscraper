import praw
import xlsxwriter

reddit = praw.Reddit(client_id='biRuOMuCJCyNiw',
    client_secret = 'E6uL2FScBRdyGCtFpprT-2We1qg',
    user_agent='windows:com.nodomain.wsbscraperCE:v0.1 (by u/StudentOfAwesomeness)')

book = xlsxwriter.Workbook('test.xlsx')
worksheet = book.add_worksheet()

worksheet.set_column('A:A', 20)

n = 0

submission = reddit.submission(id='g6k3gr')
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    worksheet.write(n, 0, comment.body)
    n = n + 1

book.close()