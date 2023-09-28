"""Hamburger"""
def hamburger(lbun, rbun):
    """make him a humburger"""
    ham = (lbun + rbun) * 2
    print("|" * lbun + "*" * ham + "|" * rbun)
hamburger(lbun=int(input()), rbun=int(input()))
