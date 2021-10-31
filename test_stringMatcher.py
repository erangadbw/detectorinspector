import stringMatcher

def test_returnMeterStringPattern():
    assert stringMatcher.returnMeterStringPattern("2.0 m  (asd13q221#)") == '2.0  '
    assert stringMatcher.returnMeterStringPattern("2122.0 m  (asd13q221#)") == '2122.0  '
    assert stringMatcher.returnMeterStringPattern("A2122.0 m  (asd13q221#)") =='2122.0  '
    assert stringMatcher.returnMeterStringPattern("asdasd") is None
def test_returnStringPattern():
    assert stringMatcher.returnStringPattern("12:00:12","(^|[ ])\\d+[:.]\\d+([:.]\\d+)?") == '12:00:12'
    assert stringMatcher.returnStringPattern("12.00:12","(^|[ ])\\d+[:.]\\d+([:.]\\d+)?") == '12.00:12'
    assert stringMatcher.returnStringPattern("12asdasd","(^|[ ])\\d+[:.]\\d+([:.]\\d+)?") is None
def test_isFloat():
    assert stringMatcher.is_float("2.0") == True
    assert stringMatcher.is_float("2") == True
    assert stringMatcher.is_float("Aasdsad2123.0") == False