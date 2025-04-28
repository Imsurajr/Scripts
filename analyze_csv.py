import csv
import boto3


def read_and_analyze_csv(file_path, grade_threshold):
    students_above_threshold = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            name, age, grade = row
            grade = float(grade)
            if grade > grade_threshold:
                students_above_threshold.append(name)
    return students_above_threshold


def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("List of S3 Buckets:")
    for bucket in response['Buckets']:
        print(bucket['Name'])


def main():
    grade_threshold = 80
    csv_file_path = '/home/ec2-user/students.csv'

    students = read_and_analyze_csv(csv_file_path, grade_threshold)
    print(f"Students with average grade above {grade_threshold}:")
    for student in students:
        print(student)

    list_s3_buckets()


if __name__ == "__main__":
    main()
