



class StockSpanner:
    def __init__(self):
        
        self.stk = []   

    def next(self, price: int) -> int:
        cur_span = 1
        while self.stk and self.stk[-1][0] <= price:
            _, span = self.stk.pop()
            cur_span += span
        self.stk.append((price, cur_span))
        return cur_span






