import employee_info as empinfo

def test_get_employees_by_age_range():
    result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert(empinfo.get_employees_by_age_range(20,35) == result)


def test_calculate_average_salary():
    assert(round(empinfo.calculate_average_salary(), 2) == 60166.67)

def test_get_employee_by_dept():
    result = [
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert(empinfo.get_employees_by_dept('Engineering') == result)