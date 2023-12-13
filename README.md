This project scrapes all the languages used in a GSoC year, and sorts them in descending order of frequency.

Before using, you need to install `selenium`. You can do that by the following command:
```commandline
pip3 install selenium
```

Now, clone this repository using

```commandline
git clone https://github.com/aryan12cc/GSoC-Lang-Scraper
```

Next, run the scraper using
```commandline
python3 scraper.py
```

It will take some time, as the code parses lots of information. After it has finished running, you should be able to see the list of languages sorted in descending order of their frequencies.