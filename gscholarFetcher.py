from scholarly import scholarly

def get_author(author,university=""):
  url_part = "https://scholar.google.co.in/citations?user="
  authorSearch = scholarly.search_author(author+(", "+university if university!='' else ''))
  try:
    authorResult = next(authorSearch)
  except:
    return "Not Found"
  authorRaw = scholarly.fill(authorResult,sections=['basics','indices','publications'])
  authorDetails = {'name':authorRaw['name'],'affiliation':authorRaw['affiliation'],'email_domain':authorRaw['email_domain'],'interests':authorRaw['interests']
                  ,'publications':len(authorRaw['publications']),'citedby':authorRaw['citedby'],'hindex':authorRaw['hindex'],'i10index':authorRaw['i10index']
                  ,'gscholar_url':url_part+authorRaw['scholar_id']}
  return authorDetails