def mask(s, show=3):
   '''
   >>> mask('an arbitrarily long string')
   '***********************ing'
   >>> mask('another one', 5)
   '******r one'
   >>> mask('yet another', 450)
   'yet another'
   '''
   m = len(s) - show;
   masked = '*' * m if m > 0 else ''
   showed = s[-show:]
   return masked + showed
