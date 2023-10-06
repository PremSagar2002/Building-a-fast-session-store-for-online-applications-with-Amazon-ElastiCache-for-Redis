@app.route('/') 
def index(): 
 if 'username' in session: 
 username = escape(session['username']) 
 visits = store.hincrby(username, 'visits', 1) 
 # BEGIN NEW CODE # 
 store.expire(username, 10) 
 # END NEW CODE # 
 return ''' 
 Logged in as {0}.<br> 
 Visits: {1} 
 '''.format(username, visits) 
 return 'You are not logged in' 
