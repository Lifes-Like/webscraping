import re
pattern = re.compile('ca.e') 
# . : 하나의 문자를 의미 (ca.e) > care, cafe, case (O) | caffe (X)
# ^ : 문자열의 시작 (^de) > desk, destination (O) | fade (X)
# $ : 문자열의 끝 (se$) > case, base (O) | face (X)
def print_match(match):
    if match:
        print(f'match.group() : {match.group()}') # 일치하는 문자열 반환
        print(f'match.string : {match.string}') # 입력받은 문자열
        print(f'match.start() : {match.start()}') # 일치하는 문자열의 시작 index
        print(f'match.end() : {match.end()}') # 일치하는 문자열의 끝 index
        print(f'match.span() : {match.span()}') # 일치하는 문자열의 시작/끝 index
    else:
        print('매칭되지 않음')

match = pattern.match('careless') # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(match) # 정규식과 매칭 O, 매칭되지 않으면 에러 발생
 
match = pattern.search('good care') # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(match)

matchlst = pattern.findall('good care cafe') # findall : 일치하는 모든 것을 리스트 형태로 반환
print(matchlst)

# 1. p = re.compile('원하는 형태')
# 2. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
#    m = p.search('비교할 문자열') : 주어진 문자열중에 일치하는게 있는지 확인
#  lst = p.finall('비교할 문자열') : 일치하는 모든 것을 '리스트'형태로 반환

# 원하는 형태 : 정규식
# . : 하나의 문자를 의미
# ^ : 문자열의 시작
# $ : 문자열의 끝