import requests

respond = requests.get('https://github.com/Lifes-Like')
print(f'응답코드 : {respond.status_code}') # 200이면 정상

if respond.status_code == requests.codes.ok:
    print('정상입니다.')
else:
    print(f'문제가 생겼습니다. [에러코드 : {respond.status_code}]') # 200이면 정상

respond = requests.get('https://google.com')
respond.raise_for_status() # 문제 있으면 에러 내뱉고 프로그램 끝냄

print('웹 스크래핑을 진행합니다.')
print(len(respond.text))

with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(respond.text)

