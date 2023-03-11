def scan_resume(resume):
    from resume_parser import resumeparse
    data = resumeparse.read_file(resume)
    for i, j in data.items():
        print(f"{i}:>>{j}")

name = input('Enter your Name: ')
scan_resume(f"{name}.docx")