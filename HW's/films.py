film = {'name':'Shawshank Redemption','rating':87,'year':1994,'director':'Frank Darabont'}



film['starring'] = ['Tim Robbins','Morgan Freeman']
film['budget'] = 200
herec = "Arnold"
film['starring'].append(herec)
del film['budget']
#film.clear()


films={}
films['DRAMA'] = film
films['TECHNO'] = film

print('we can currently offer:\n', list(films))
genre = input('What one are you interested in? ')
print('here it is:\n',films[genre])
