from gltt import *

def test_single_commit():
    assert(gltt("d491dd78 - Error handling for calculate page_number and pass tests (3 days ago) <sbimochan>") == "1) Error handling for calculate page_number and pass tests" )