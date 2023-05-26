import os
from scanner import scan
def test_nmap_installed_with_version():
    assert not os.system("nmap --version") is None

def test_nmap_scans_google():
    assert not scan("www.google.com") is  None 