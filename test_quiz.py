from actions import driver_init, check_home, enter_info


def test_quiz():
    driver_init()
    check_home()
    enter_info('aa@gmail.com', 'Helooo')
