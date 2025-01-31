from numb3rs import validate


def test_validate():
    assert validate("275.3.6.28") == False
    assert validate("hello") == False
    assert validate("10.0.10") == False
    assert validate("192.168.1.1.1") == False
    assert validate("255.256.256.256") == False
    assert validate("192.168.1.1") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("199.911.288.882") == False
    assert validate("249.249.249.249") == True
