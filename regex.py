def match(s, p):
    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], '?'}
    if p[0] == '*':
        return match(s, p[1:]) or match(s[1:], p) if bool(s) else False
    else:
        return first_match and match(s[1:], p[1:])


if __name__ == '__main__':
    p = '*b?'
    s = 'b'
    res = match(s, p)
    print(res)
