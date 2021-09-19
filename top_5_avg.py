class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items = sorted(items, key = lambda x:(x[0], -x[1]))
        records = {}
        for x in items:
            if x[0] in records:
                records[x[0]].append(x[1])
            else:
                records[x[0]] = [x[1]]
        res = []
        for k,v in records.items():
            res.append([k, sum(v[:5])//5])
        return res