from TestCases.test_HomePageTitle import Test_001_Title
from TestCases.test_Login import Test_002_Login
from TestCases.test_Leave import Test_003_Leave
from TestCases.test_Logout import Test_004_Logout



if __name__ == '__main__':
    test01 = Test_001_Title()
    test02 = Test_002_Login()
    test03 = Test_003_Leave()
    test04 = Test_004_Logout()

    print("Running test: Verify Home Page Title")
    try:
        test01.test_LoginpageTitle()
    except AssertionError as e:
        print("Test 'Verify Home Page Title' failed.")

    print("Running test: Verify Dashboard page loaded")
    try:
        test02.test_login()
    except AssertionError as e:
        print("Test 'Verify Login functionality' failed.")

    print("Running test: Verify Leave page loaded")
    try:
        test03.test_leave()
    except AssertionError as e:
        print("Test 'Verify Leave functionality' failed.")

    print("Running test: Verify Logout Functionality")
    try:
        test04.test_logout()
    except AssertionError as e:
        print("Test 'Verify Logout functionality' failed.")


