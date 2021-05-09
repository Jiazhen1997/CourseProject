from celery import Celery

redis_url = 'redis://localhost:6379/0'
app = Celery('overridden by celery command', broker=redis_url)

@app.task
def consume(a, b):
    print "c"o"n"s"u"m"e" "a"+"b" "=" "%"d"" ""%"" ""(""a"" ""+"" ""b"")""
"" "" "" "" ""r""e""t""u""r""n"" ""a"" ""+"" ""b""
