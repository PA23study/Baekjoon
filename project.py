import sys

# 출력 포맷

def print_line():
    print('Student\t\t','Name\t\t','Midterm','Final\t','Average','Grade')
    print('---------------------------------------------------------------------')
    
def new_command():
    s = input('# 명령어를 입력하세요 :')
    return s

def show_student(StudentInfo):
    
    # 평균 점수를 기준으로 정렬하기 x[0] = key, x[1] = value , x[1][4] = avg_score
    sorted_StudentInfo= sorted(StudentInfo, key= lambda x : x[1][4], reverse=True)
    # sorted_StudentInfo는 평균 점수를 기준으로 정렬된 튜플로 이루어진 리스트
    # [ (학번1, [이름,성,중간,기말,평균,학점] ) ,( 학번2, [이름,성,중간,기말,평균,학점] ) .... ]

    # 표에 맞게 출력하기
    print_line()
    for v in sorted_StudentInfo:
        print(v[0],'\t',v[1][0],v[1][1],'\t',v[1][2],'\t',v[1][3],'\t',v[1][4],'\t',v[1][5])
        
def search_student(StudentInfo, student_id):
    
    flag = 0 # 찾고자 하는 학생이 목록에 있는지 표시하는 flag
    num = 0 # 몇 번째 학생인지 표시
    for v in StudentInfo:
        if student_id == v[0] :
            flag = 1
            print_line()
            print(v[0],'\t',v[1][0],v[1][1],'\t',v[1][2],'\t',v[1][3],'\t',v[1][4],'\t',v[1][5])
            break
        num += 1
            
    return (flag, num)


        
# 점수 수정 함수

def change_score(StudentInfo, student_id, midORfinal, new_score):
    num = 0
    
    
    for v in StudentInfo:
        if v[0] == student_id:
            break
        else:
            num += 1
    
    #정보를 수정할 학생은 num번째 학생
    
    if midORfinal == 'mid': # 중간고사 점수 수정
        new_avg = (new_score + int(StudentInfo[num][1][3])) / 2 # 평균점수 수정
        # 학점 수정
        if new_avg >= 90:
            new_grade = 'A'
        elif new_avg >= 80:
            new_grade = 'B'
        elif new_avg >= 70:
            new_grade = 'C'
        elif new_avg >= 60:
            new_grade = 'D'
        else:
            new_grade = 'F'
        StudentInfo[num] = (StudentInfo[num][0], [StudentInfo[num][1][0], StudentInfo[num][1][1], new_score, StudentInfo[num][1][3], new_avg, new_grade])
            
    else: # 기말고사 점수 수정
        new_avg = (new_score + int(StudentInfo[num][1][2])) / 2 # 평균점수 수정
        # 학점 수정
        if new_avg >= 90:
            new_grade = 'A'
        elif new_avg >= 80:
            new_grade = 'B'
        elif new_avg >= 70:
            new_grade = 'C'
        elif new_avg >= 60:
            new_grade = 'D'
        else:
            new_grade = 'F'
        StudentInfo[num] = (StudentInfo[num][0], [StudentInfo[num][1][0], StudentInfo[num][1][1], StudentInfo[num][1][2], new_score, new_avg, new_grade])
        
                
    print('Score changed.')
    print(StudentInfo[num][0],'\t',StudentInfo[num][1][0],StudentInfo[num][1][1],'\t',StudentInfo[num][1][2],'\t',StudentInfo[num][1][3],'\t',StudentInfo[num][1][4],'\t',StudentInfo[num][1][5])

    
    
# 학생 추가 함수
def add_student(StudentInfo, student_id, name, mid_score, final_score):
    
    avg_score = (mid_score + final_score) / 2
    if avg_score >= 90:
        grade = 'A'
    elif avg_score >= 80:
        grade = 'B'
    elif avg_score >= 70:
        grade = 'C'
    elif avg_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    new_tuple = (student_id, [ name[0], name[1], str(mid_score), str(final_score), avg_score, grade])
    StudentInfo.append(new_tuple)
# 학점 검색 함수
def search_grade(StudentInfo, grade):
    
    flag = 0 # 해당 학점에 해당하는 학생이 존재하는지 표시하는 flag
    print_line_flag = 0 # 출력 포맷이 이미 출력되었는지 표시하는 flag
    
    for v in StudentInfo:
        if grade == v[1][5] : # 해당 학점에 해당하는 학생을 발견한경우
            flag = 1
            if print_line_flag == 0:
                print_line_flag = 1
                print_line()
                print(v[0],'\t', v[1][0],v[1][1],'\t',v[1][2],'\t',v[1][3],'\t',v[1][4],'\t',v[1][5])
            else : # 학생 정보 출력
                print(v[0],'\t', v[1][0],v[1][1],'\t',v[1][2],'\t',v[1][3],'\t',v[1][4],'\t',v[1][5])
                
            
        else: # 아직 학생을 발견하지 못한 경우
            continue
            
    if flag == 0: # 학생이 존재하지 않는 경우
        print('NO RESULTS.')
# 특정 학생 삭제 함수
def remove_student(StudentInfo, student_id):
    
    flag = 0 # 특정 학생이 존재하는지 확인하는 flag
    
    flag, num = search_student(StudentInfo, student_id)
    
    if flag == 0 : # 특정 학생이 존재하지 않음
        print("NO SUCH PERSON.")
    
    else:
        del StudentInfo[num]
# 종료 함수
def quit_program(StudentInfo):
    
    save = input('Save data?[yes/no]')
    
    if save == 'yes': # 다른 이름으로 저장
        new_name = input('File name:') # 새 파일 이름
        new_file = open(new_name, 'w') # 파일 쓰기모드로 열기
        
        # 정렬하여 저장하기
        StudentInfo= sorted(StudentInfo, key= lambda x : x[1][4], reverse=True)
        for v in StudentInfo:
            
            data = v[0]+'\t'+v[1][0]+' '+v[1][1]+'\t'+v[1][2]+'\t'+v[1][3]+'\t'+str(v[1][4])+'\t'+v[1][5]+'\n'
            new_file.write(data)
            
        new_file.close()
    
    
    
    
# 파일불러오기    
    

if len(sys.argv) == 1:
    file = open('students.txt', 'r')
else:
    file = open(sys.argv[1], 'r')


print(file.name,"파일을 불러옵니다.")


StudentInfo = {} # 학생 정보를 저장할 딕셔너리


for line in file:
    words = line.split()
    avg_score = (int(words[3])+int(words[4])) / 2 # 평균 점수 
    
    # 학점
    if avg_score >= 90:
        grade = 'A'
    elif avg_score >= 80:
        grade = 'B'
    elif avg_score >= 70:
        grade = 'C'
    elif avg_score >= 60:
        grade = 'D'
    else : 
        grade = 'F'
    
    # 딕셔너리 key=학번, value=[이름, 성, 중간점수, 기말점수, 평균점수, 학점]
    StudentInfo[words[0]] = [words[1], words[2], words[3],words[4], avg_score, grade]
    
print_line()
for k,v in StudentInfo.items():
    print(k,'\t',v[0],v[1],'\t',v[2],'\t',v[3],'\t',v[4],'\t',v[5])

# 딕셔너리를 튜플로 이루어진 리스트로 전환하기
StudentInfo = list(tuple(StudentInfo.items()))

# 명령어 받기 show, search, changescore, searchgrade, add, remove, quit
s = new_command()
print()

while True:
    
    s = s.lower()
    
    if s == 'show': # 전체 학생 정보 출력
        print("전체 학생 정보를 출력합니다.\n")
        show_student(StudentInfo)
        s = new_command()
        continue

        
        
    elif s == 'search': # 특정 학생 검색
        student_id = input('검색할 학번을 입력하세요. Student ID:')
        
        flag, num = search_student(StudentInfo, student_id) # 학번 검색 함수
        
        if flag == 0:
            print("NO SUCH PERSON\n\n")
            s = new_command()
            continue
            
        s = new_command()
        continue
    
    
    
    
    elif s == 'changescore': # 점수 수정
        
        student_id = input('검색할 학번을 입력하세요. Student ID:')
        flag, num = search_student(StudentInfo, student_id) # 학번 검색 함수
        
        if flag == 0: # 학번이 존재하지 않으면 명령어 입력으로 되돌아간다.
            print("NO SUCH PERSON\n\n")
            s = new_command()
            continue
        
        # 학번이 존재한다면 mid/final 을 묻는다.
        midORfinal = input('Mid/Final?')
        
        
        #중간 점수 수정하기
        if midORfinal == 'mid':
            new_score = int(input('Input new score:')) # 수정할 점수
            
            if new_score >= 0 and new_score <= 100:
                change_score(StudentInfo, student_id, midORfinal, new_score) # 정보 수정 함수 (학생리스트, n번째학생, 중간또는기말, 수정할점수)
                s = new_command()
                continue
            else: continue
            
        #기말 점수 수정하기
        elif midORfinal == 'final':
            new_score = int(input('Input new score:')) # 수정할 점수
            
            if new_score >= 0 and new_score <= 100:
                change_score(StudentInfo, student_id, midORfinal, new_score)
                s = new_command()
                continue
            else: continue
        
        else: # mid/final 외의 문자가 입력되면 명령어 입력으로 되돌아간다.
            print('Wrong Word')
            s = new_command()
            continue
        
        

    elif s == 'searchgrade': # grade 검색
        grade = input('Grade to search:')
        search_grade(StudentInfo, grade)
        s = new_command()
    
    
    elif s == 'add': # 학생 추가
        student_id = input('Student ID:')
        flag, num = search_student(StudentInfo, student_id)
        
        if flag == 1: # 학번이 이미 존재함
            print('ALREADY EXISTS') 
            s = new_command()
            continue
        else:
            name = input('Name:').split() # [성,이름]
            mid_score = int(input('Midterm Score:')) # 중간고사 점수 입력
            if mid_score >=0 and mid_score <= 100 :
                final_score = int(input('Final Score:')) # 기말고사 점수 입력
                if final_score >=0 and final_score <= 100 :
                    add_student(StudentInfo, student_id, name, mid_score, final_score)
                    print('Student added.')
                    s = new_command()
                    continue
                else: # 기말고사 점수가 0~100을 벗어나면
                    print('Wrong Score')
                    s = new_command()
                    continue
                                  
            else: # 중간고사 점수가 0~100을 벗어나면
                print('Wrong Score')
                s = new_command()
                continue
            
            s = new_command()
            continue
            
    elif s == 'remove':
        if StudentInfo == []: # 목록에 아무도 없을 경우
            print("List is empty.")
            s = new_command()
        else: 
            
            student_id = input('Student ID:')
            remove_student(StudentInfo, student_id)
            s = new_command()

    
    elif s == 'quit':
        quit_program(StudentInfo)
        break
    
    else:
        continue


        
file.close()
