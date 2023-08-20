# pastebin
> python wrapper for the pastebin api

## API Documentation:
* [Pastebin API](https://pastebin.com/doc_api)

## Example:
```python
#!/usr/bin/env python
import pastebin
api_key = 'CHANGEME'
api     = pastebin.PasteBin(api_key)
data    = open(__file__).read()
result  = api.paste(data, guest=True, name='Example Script', format='Python', private='1', expire='10M')
print('PasteBin URL: ' + result)
```

**Note**: A posix shell script example can be found [here](https://github.com/acidvegas/random/blob/master/pastebin)

___

###### Mirrors
[acid.vegas](https://git.acid.vegas/pastebin) • [GitHub](https://github.com/acidvegas/pastebin) • [GitLab](https://gitlab.com/acidvegas/pastebin) • [SuperNETs](https://git.supernets.org/acidvegas/pastebin)
