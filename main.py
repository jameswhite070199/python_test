def in_autotest_we_trust(a, b):
    if a == b:
        print('Test passed')
    else:
        print('Test failed')

in_autotest_we_trust(10, '10')

in_autotest_we_trust(0, False)
