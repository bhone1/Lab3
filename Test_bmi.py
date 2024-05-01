import Lab2.bmi as bmi

def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(65,1.7) == 0)

def test_bmi_over_weight():
    assert(bmi.calculate_bmi(100,1.6) == 1)

def test_bmi_under_weight():
    assert(bmi.calculate_bmi(40,1.8) == -1)
