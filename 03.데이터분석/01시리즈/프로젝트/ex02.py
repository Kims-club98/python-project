import os
import pandas as pd
file_name='data/학생정보.csv'
score=pd.read_csv(file_name)

while True:
    os.system('cls')
    print('-'*50)
    print('+'*20+ ' 성적관리 ' +'+'*20)
    print('1.등록 | 2. 목록 | 3. 검색 | 4. 수정 | 5. 삭제 | 0.종료')
    print('-'*50)
    menu=input('메뉴선택>')
    if menu =='0':
        input('프로그램을 종료합니다!')
        break
    elif menu=='1':
        input('아무키나 누르세요!')
    elif menu=='2':
        for i in range(0, len(score)):
            row=score.loc(i)
            print(f"{row['지원번호']}, {row['국어']}")
    elif menu=='3':
        input('아무키나 누르세요!')
    elif menu=='4':
        input('아무키나 누르세요!')
    elif menu=='5':
        input('아무키나 누르세요!')
    else:
        input('잘못 누르셨습니다.' 
        '0에서 5사이를 입력하세요!')