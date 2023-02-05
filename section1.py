#1. 나라별 수도를 순차적으로 반복시켜서 nation 리스트에 저장해 두엇씁니다.
#   nation 리스트위 내용을 이용하여 다음과 같은 nation.txt 파일을 생성하세요.

#nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
# nation.txt
# 그리스-아테네
# 독일-베를린
# 러시아-모스크바
# 미국-워싱턴

def section13_01():
    nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
    with open ('nation.txt', 'w', encoding='UTF-8') as f:
        for n in range(0,len(nation),2):
            f.write(nation[n] + '-' + nation[n+1] + '\n')

#2. 웹 하드에 업로드 되어있는 연락처.txt 파일이 있습니다.
# 파일안에 저장된 연락처중 011로 시작하는 연락처를 모두 010으로 수정하세요.

#총 n건의 011데이터를 찾았습니다.
#(과정)
#모든 데이터를 수정했습니다.
li = []

def section13_02():
    with open('연락처.txt', 'r') as f:
        for i in f.readlines():
            li.append(i)
    with open('연락처.txt','w') as f:
        #i.find('011') -> 011 로 시작하면 0 -> 010으로 수정

        for i in li:
            if i.find('011'):
                f.write(i)
            else:
                i = i.lstrip('011')
                f.write('010' + i)

