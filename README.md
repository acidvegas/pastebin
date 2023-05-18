# pastebin
> python wrapper for the pastebin api

## API Documentation:
* [Pastebin API](https://pastebin.com/doc_api)
* [Pastebin Scraping API](https://pastebin.com/doc_scraping_api)

## Example:
```python
#!/usr/bin/env python
import pastebin
api_dev_key = 'CHANGEME'
api    = pastebin.PasteBin(api_dev_key)
data   = open(__file__).read()
result = api.paste(data, guest=True, name='Example Script', format='Python', private='1', expire='10M')
print('PasteBin URL: ' + result)
```

**Note**: A posix shell script example can be found [here](https://github.com/acidvegas/random/blob/master/pastebin)

## Mirrors
- [acid.vegas](https://git.acid.vegas/pastebin)
- [SuperNETs](https://git.supernets.org/acidvegas/pastebin)
- [GitHub](https://github.com/acidvegas/pastebin)
- [GitLab](https://gitlab.com/acidvegas/pastebin)
