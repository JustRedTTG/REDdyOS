data,lookup,pe=None,None,None
def verify():
  return "module"
def init(dataV,lookupV):
  global data,lookup,pe
  data = dataV
  lookup = lookupV
  pe = lookup.get("PGE")
  return "EZtext"

class align:
  def init(textV):
    textV.pos = (textV.original_pos[0] + pe.Layer[textV.layer][1][0], textV.original_pos[1] + pe.Layer[textV.layer][1][0])
    textV.fonto = pe.pygame.font.Font(textV.font, textV.fontsize)
    textV.texto = textV.fonto.render(textV.text, True, textV.color, textV.background)
    textV.textRect = textV.texto.get_rect()
    return textV
  def topleft(textV):
    textV = align.init(textV)
    textV.textRect.topleft = textV.pos
    return textV
  def center(textV):
    textV = align.init(textV)
    textV.textRect.center = textV.pos
    return textV

def fit(text,color,rect,g=25):
  return pe.text.make(text, 'freesansbold.ttf', int((rect[0]-rect[2])/g), pe.math.center(rect), (color, None))
def size(text,color,rect,g=25):
  return pe.text.make(text, 'freesansbold.ttf', g, pe.math.center(rect), (color, None))
def cram(text,color,rect):
  maxY = int(rect[3]*0.9)
  maxX = int(rect[2]/(rect[3]/2))
  cram=False
  if maxX < len(text):
    cram = True
    text = text[0:maxX-4]+"..."
  if cram:
    textV = pe.text.make(text, 'freesansbold.ttf', maxY, (rect[0],rect[1]), (color, None))
    return align.topleft(textV)
  else:
    return pe.text.make(text, 'freesansbold.ttf', maxY, pe.math.center(rect), (color, None))
backtick=[False,0]
def type(text, newEnable=True):
  for event in data.events:
    if event.type == pe.pygame.KEYDOWN:
      if event.key == pe.pygame.K_BACKSPACE:
        text = text[:-1]
        backtick[0]=True
        backtick[1] = 0
      elif event.key == pe.pygame.K_RETURN and newEnable:
        text += "\n"
      else:
        text += event.unicode
    elif event.type == pe.pygame.KEYUP:
      if event.key == pe.pygame.K_BACKSPACE:
        backtick[0]=False
    else:
      try:
        text += event.unicode
      except:
        pass
  if backtick[0]:
    backtick[1]+=1
  if backtick[1]>=5:
    backtick[1]=0
    text = text[:-1]
  return text
class textbox:
  def single(ctext,color,rect,background=(255,255,255),outline=(0,0,0),outlinewidth=2):
    if ctext == None:
      ctext = {'text':'','font':pe.pygame.font.Font(None,rect[3]),'rect':rect,'cursorTick':0}
    elif ctext['rect'] != rect:
      ctext['font'] = pe.pygame.font.Font(None,rect[2])

    surface = pe.pygame.Surface((rect[2],rect[3]))
    Srect = (0,0,rect[2],rect[3])
    last=pe.display_a
    pe.display.set(surface)
    pe.fill.full(background)
    #
    ctext['text'] = type(ctext['text'],False).replace("\n","")
    tS = ctext['font'].render(ctext['text'],True,color)
    cursorX = tS.get_width()+2
    if cursorX>rect[2]:
      cursorX = rect[2]-(rect[3]/2)
    surface.blit(tS,(2+cursorX-tS.get_width(),5))
    pe.draw.rect(outline, Srect, outlinewidth)
    if ctext["cursorTick"] <= 10:
      pe.draw.line(pe.colors.black,(cursorX+2,outlinewidth+2),(cursorX+2,rect[3]-outlinewidth-2),2)
    if ctext["cursorTick"] >= 20:
      ctext["cursorTick"] = 0
    else:
      ctext["cursorTick"]+=1
    #
    pe.display.set(last)
    pe.display.blit.rect(surface,rect)
    return ctext