import pandas as pd

def load_data():
    try:
        df = pd.read_csv('students.csv')
        df.columns = df.columns.str.strip()
        df['Average'] = df[['Python', 'Math', 'ML']].mean(axis=1)
        return df
    except FileNotFoundError:
        print("Khong tim thấy file. Vui long check lại : ")
        return None

def display_menu():
    print("================================")
    print(" student performance analysis")
    print("------------------------------------------------------")
    print("1. display all students")
    print("2. search for a student")
    print("3. calculate student average")
    print("4. analyze subject performance")
    print("5. analyze class performance")
    print("6. show top 3 students")
    print("7. exit")
    print("================================")

def main():
    df = load_data()
    if df is None:
        return

    while True:
        display_menu()
        choice = input("chọn lựa từ 1 đến 7 ").strip()

        if choice == '1':
            print(df.drop(columns=['Average']).to_string(index=False))

        elif choice == '2':
            student_id = input("Nhập ID của sinh vien: ").strip()
            student = df[df['student_id'] == student_id]
            if student.empty:
                print("Student not found")
            else:
                print(student.drop(columns=['Average']).to_string(index=False))

        elif choice == '3':
            student_id = input("nhập Id sinh vien: ").strip()
            student = df[df['student_id'] == student_id]
            if student.empty:
                print("khong tim thấy sinh viên: ")
            else:
                row = student.iloc[0]
                scores = [row['Python'], row['Math'], row['ML']]
                print("===== STUDENT RESULT =====")
                print(f"Name: {row['name']}")
                print(f"Python: {row['Python']}")
                print(f"Math: {row['Math']}")
                print(f"ML: {row['ML']}")
                print(f"Average: {row['Average']:.2f}")
                print(f"Highest: {max(scores)}")
                print(f"Lowest: {min(scores)}")

        elif choice == '4':
            print("===== SUBJECT PERFORMANCE =====")
            print(f"{'':<15}{'Average':<10}{'Total':<10}{'Highest':<10}{'Lowest':<10}")
            for subj in ['Python', 'Math', 'ML']:
                avg = df[subj].mean()
                total = int(df[subj].sum())
                highest = df[subj].max()
                lowest = df[subj].min()
                print(f"{subj:<15}{avg:<10.2f}{total:<10}{highest:<10}{lowest:<10}")

        elif choice == '5':
            print("===== CLASS PERFORMANCE =====")
            class_grp = df.groupby('class_name').agg(
                Students=('student_id', 'count'),
                Python=('Python', 'mean'),
                Math=('Math', 'mean'),
                ML=('ML', 'mean'),
                Overall_Average=('Average', 'mean')
            ).reset_index()
            
            print(f"{'Class':<10}{'Students':<10}{'Python':<10}{'Math':<10}{'ML':<10}{'Overall Average':<15}")
            for _, row in class_grp.iterrows():
                print(f"{row['class_name']:<10}{row['Students']:<10}{row['Python']:<10.2f}{row['Math']:<10.2f}{row['ML']:<10.2f}{row['Overall_Average']:<15.2f}")

        elif choice == '6':
            print("Top 3 sinh viên \n: ")
            top3 = df.sort_values(by='Average', ascending=False).head(3)
            print(f"{'Student ID':<15}{'Name':<20}{'Class':<10}{'Average':<10}")
            for _, row in top3.iterrows():
                print(f"{row['student_id']:<15}{row['name']:<20}{row['class_name']:<10}{row['Average']:<10.2f}")

        elif choice == '7':
            break
        else:
            print("thử lại: ")

if __name__ == "__main__":
    main()