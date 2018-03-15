def rss_parser(url, force_https=False):
    import re
    import feedparser
    def _parse_img(content, alt):
        matches = re.findall(r'\ssrc="([^"]+)"', content)
        matches = ' '.join(matches)
        res = None
        if len(matches):
            res = matches

        # try alternative
        if res is None:
            for link in alt:
                if "image" in link.get("type", ""):
                    res = link.get("href", None)
        return res

    def _clean_html(content):
        matches = re.findall('<.*?>', content)
        for m in matches:
            content = content.replace(m, "")
        return content.strip()


    feed = feedparser.parse(url)

    results = {
        "title": "",
        "articles": []
    }

    feed_title = feed.get('feed', {}).get('title', '')
    results["title"] = feed_title
    feed_entries = feed.entries

    for entry in feed_entries:
        url = getattr(entry, "link", "")
        if force_https:
            url = url.replace("http://", "https://")
        tmp = {
            "title": getattr(entry, "title", ""),
            "author": getattr(entry, "author", ""),
            "desc": _clean_html( getattr(entry, "summary", "") ),
            "pubDate": getattr(entry, "published", ""),
            "url": url,
            "urlImg": _parse_img( getattr(entry, "summary", ""), entry.get("links", None) )
        }
        results["articles"].append(tmp)

    return results
