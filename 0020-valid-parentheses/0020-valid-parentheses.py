class Solution:
    def isValid(self, s: str) -> bool:
        emp =[]
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs.values():
                emp.append(ch)
            else:
                if not emp or emp[-1] != pairs[ch]:
                    return False
                emp.pop()

        return len(emp) == 0