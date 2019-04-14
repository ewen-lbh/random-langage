import random as r
from termcolor import cprint
CHARSLIST = list("#@&\"'§!°-_*$`%=+/:;.,?^|<>{}[]()")
ACTIONS   = {
  '=':'Assign a value',
  ':':'Specify a type',
  '<':'Start cast to a type',
  '>':'End cast to a type',
  '[':'Start a list',
  ']':'End a list',
  'ö':'Start a dict',
  'ë':'End a dict',
  '°':'End a dict',
  '$':'Concatenation',
  '`':'Interpolation start',
  'ô':'Interpolation end',
  '+':'Addition',
  '-':'Substraction',
  '*':'Multiplication',
  '^':'Power',
  '/':'Division',
  '%':'Modulo',
  '@':'Start index localisation',
  'ê':'End index localisation',
  '#':'Add a comment',
  '¨':'Open a multiline comment',
  '£':'Close a multiline comment',
  'ç':'Check equality',
  'à':'Check strong equality',
  '!':'Logical NOT',
  '&':'Logical AND',
  '|':'Logical OR',
  '.':'Access an object property',
  'é':'Access a class property',
  '?':'Start a tertiary condition',
  '{':'Start a scope',
  '}':'End a scope',
  '(':'Start a function call',
  ')':'End a function call',
  '"':'Indicate a string',
  ';':'End a line',
  ',':'Common separator'
}
SAMPLE = """
# DO NOT use that
unsecure_mode: bool = 0;
# Get userinput
plz = "please";
usrin = input("Your name `plzô")<str>;
if !empty(usrin) & xss_safe(usrin) | unsecure_mode {
  col1: hexColor = "0x" $ input();
  col2: hexColor = "0x" $ input();
  info = ö
    "IP":get_ip(),
    "date":now()<str>,
    "theme":[col1, col2]
  ë
  header_color.set(info@themeê@0ê);
  display(WebsiteéResourceséLogo(col2));

} else {
  ¨
  We should really handle that shit though
  this is not my job anymore
  Show a random calculation instead
  £
  display(8 + 9 / 4 * 5 ^ 9 % 8);
}
"""
MIN_LEN   = 1
MAX_LEN   = 3
MAX_RPT   = 3

def gen_operator(length=None, blacklist=False, unallowed=[]):
  charslist = [e for e in CHARSLIST if e not in (blacklist if blacklist else [])]
  result = str()
  length = r.randint(MIN_LEN, MAX_LEN) if length is None else int(length)
  for i in range(length):
    seled = r.choice(charslist)
    while seled in unallowed:
      cprint(f'Tried: {seled}, already taken','red')
      seled = r.choice(charslist)
    # todo add approx. 75% chance to choose a previous char (from current buffer), in order to reduce chaosness in result
    result += seled
  return result

maxlen = max([len(e) for e in ACTIONS.values()])
repl_map = dict()
mul_length_codes = list("¨£#&|$")
forced_codes = list('')
for acode, a in ACTIONS.items():
  if acode in forced_codes:
    repl_map[acode] = acode
    continue

  l = None if acode in mul_length_codes else 1
  op = gen_operator(l, blacklist=forced_codes, unallowed=list(repl_map.values()))
  sp = ' ' * (1 + maxlen - len(a))
  print(f"{a}{sp}{op}")
  repl_map[acode] = op

print("=" * 30 + "This is what a code sample would like:")
sample = str()
for c in SAMPLE:
  sample += repl_map.get(c, c)

print(sample)