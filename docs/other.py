# this file is nothing

from robobrowser import RoboBrowser

start_url = "http://example.com"

def run():
    """
    start crawler
    """
    # first open novel url with normal browser
    browser = RoboBrowser()
    browser.open(start_url)
    # look all page in novels
    while is_end_page:
        novels = get_all_novel_links(browser)
        # process each novel
        for novel in novels:
            novel_id = get_novel_id(browser, novel.h3.a['href'])
            title = get_novel_title(browser, novel.h3)
            content = get_novel_content(browser, novel.h3)
            output(novel_id, title, content)
        browser.open(next_page(browser))

def get_all_novel_links(browser):
    """
    get all novel link
    return links list [link1, link2, link3]
    """
    return browser.select('.tal')[4:]


def next_page(browser):
    """
    get next page url
    return url string
    """
    next = browser.find('下一页')
    url = next.get('href')
    return url

def is_end_page(browser):
    """
    lookup the end page
    return bool
    """
    next = browser.find('下一页')
    if next.get('href') is None:
        return False
    return True

def get_novel_id(browser, novel):
    """
    return novel's id for drop duplicates
    """
    return novel[15:20]

def get_novel_title(browser, novel):
    """
    return novel's title
    """
    return novel.text

def get_novel_content(browser, novel):
    """
    get novel all content
    return content string
    """
    browser.open(novel) # or browser.follow_link(novel)
    content = list()
    # look all page in a novel
    while is_end_page(browser):
        content.append(get_cells(browser))
        browser.open(next_page(browser))
    return "".join(content)


def get_cells(browser):
    """
    get novel cells
    return [cell, cell, cell]
    """
    browser.select('')
    pass

def output(novel_id, title, content):
    """
    write novel's title and content to sqlite
    """
    pass

if __name__ == "__main__":
    run()