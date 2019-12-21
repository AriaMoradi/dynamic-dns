import sys
import logging
from time import sleep

DYNAMIC_DNS_URL = "<cloudns dynamic URL>"
SLEEP_SECS = 60

while True:
  try:
    import urllib.request
    page = urllib.request.urlopen(DYNAMIC_DNS_URL);
    page.close();
    print("request done. sleeping for {} secs".format(SLEEP_SECS))
    sleep(SLEEP_SECS)
  except Exception as e:
    print("Hit exception {}".format())
      pass

