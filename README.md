# Web scraping demo project (books)

Hi! I'm **Mahmoud Moussa** and I have created this project to demonstrate the usage of **scrapy** framework using two spider templates (basic and crawl) while scraping a demo website ("books.toscrape.com").

# Requirements

 1. First you need python to be installed on your system. you can download it from the official website **"https://www.python.org/downloads/**.
 2. The only package required to run this project is **scrapy**. to install it type **"pip install scrapy"** in a terminal.

# Usage

 - You need to be inside the project folder to run a spider. 
 
 - Now all you need to do is typing on command in the terminal to start scraping.
 - To run the basic spider template:
> scrapy crawl books_basic -o books.csv
 - To run the crawl spider template:
> scrapy crawl books_crawl -o books.csv
 - After the spider finishes it's work you'll find a file called **books.csv**  inside the project folder contains all the books info that exists on the website.
