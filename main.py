from sub import *
import csv
import asyncio
import os
import random
import requests
from bs4 import BeautifulSoup
import logging
import subprocess
import json

feed_filename = "links.txt"






async def fetch_all():
        links = []
        mislinks = await extract_missav("https://missav.com/dm561/en/uncensored-leak", end_page=2)
        print("Staring")
        for link in mislinks:
            src_result = await crawl_missav(link[-1])  # Await the coroutine
            src = src_result[-1]  # Access the last element of the returned result
            link.append(src)
            print(link)
            links.append(link)
        vids = extract_hanime()
        print(vids)
        links.extend(vids)
        vids = extract_htv()
        print(vids)
        links.extend(vids)
        return links



async def main():
       with open(feed_filename,"a+") as feed:
              links = await fetch_all()
              for link in links:
                   file.write(link+"\n")





asyncio.run(main())
