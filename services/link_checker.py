import re

def check_links(email:str):
    urls=re.findall(r'https?://\S+',email)

    suspicious_links=[]

    for url in urls:
        if "@" in url or "bit.ly" in url or "tinyurl" in url:
            suspicious_links.append(url)
    
    return{
        "total_links":len(urls),
        "suspicious_links": suspicious_links
    }
