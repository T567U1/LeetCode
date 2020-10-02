class RecentCounter:

    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        self.calls += t,
        while self.calls[0] + 3000 < self.calls[-1]:
            self.calls = self.calls[1:]

        return len(self.calls)
