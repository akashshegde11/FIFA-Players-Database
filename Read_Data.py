import csv

n = 14
fields = []
rows = []
no_files = [[0 for i in range(n)] for j in range(len(rows))]

def input_file_name():
    file_name = raw_input("Enter file name: ")
    input_file_name.file_name_appended = "D:\\Projects\\Tracking Player Potentials\\" + file_name + ".csv"
    print("\nFile to be imported is {0}".format(input_file_name.file_name_appended))

def file_opener():
    try:
        with open(input_file_name.file_name_appended, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            fields = csv_reader.next()
            for row in csv_reader:
                rows.append(row)
            print("\nTotal number of rows: {0}".format(csv_reader.line_num))
        print("\nFields are: " + ", ".join(field for field in fields))
        print("\nRows are:\n")
        #print(rows)
        for row in rows[:5]:
            for col in row:
                print("%25s"%col),
            print('\n')
    except:
        print("\nFile not found!\n")  

#def 

def main():
    input_file_name()
    file_opener()
    no_files.append(rows)
    for num_1 in no_files:
        for num_2 in num_1:
            print("%25s"%num_2)

if __name__ == "__main__":
    main()