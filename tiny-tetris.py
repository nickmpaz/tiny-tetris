#=========#=========#=========#=========#=========#=========#=========#=========#
import curses,time,random,sys;w=curses.initscr();curses.noecho();curses.cbreak()#
rs,cs,m,s,e,sh=20,10,5,300,{0:"  ",1: "# "},[[[1,1],[1,1]],[[0,1,0],[1,1,1],[0, #
0,0]],[[1,0,0],[1,1,1],[0,0,0]],[[0,0,1],[1,1,1],[0,0,0]],[[1,1,0],[0,1,1],[0,0,#
0]],[[0,1,1],[1,1,0],[0,0,0]],[[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]]]        #
b,cu,f,t=[[0]*cs for r in range(rs)],sh[random.randrange(0,len(sh))],False,True #
n,ro,co,cr,l,d=sh[random.randrange(0,len(sh))],0,cs//2,0,1,s                    #
w.nodelay(t);w.keypad(t);curses.curs_set(f);ra=lambda r:range(r)                #
def c_c(ro, co, se):                                                            #
    for (r,c) in [(r,c) for c in range(len(cu)) for r in range(len(cu))]:       #
        if se[r][c]==1 and(ro+r<0 or ro+r>=rs or co+c<0 or co+c>=cs):return f   #
        if se[r][c]==1 and b[ro+r][co+c]+se[r][c]>1: return False               #
    return True    # TINY TETRIS                                                #
def m_d():         # A Tetris implementation in 38 lines x 80 characters        #
    global ro,co,cu,n,l,d;v,g=lambda cu=cu:cu[r][c]>0,lambda j,b=b:sum(b[j])==cs#
    if not c_c(ro + 1, co, cu):                                                 #
        if ro==0: sys.exit()                                                    #
        for (r,c) in [(r,c) for c in range(len(cu)) for r in range(len(cu))]:   #
            if ro+r in ra(rs)and co+c in ra(cs)and v():b[ro+r][co+c]=cu[r][c]   #
        cu,n,ro,co,d=n,sh[random.randrange(0,len(sh))],-1,cs//2,s+m-l*m         #
        for i in[j for j in range(rs)if g(j)]:b[1:i+1]=b[:i];b[0],l=[0]*cs,l+1  #
try:               # $ git clone https://github.com/nickmpaz/tiny-tetris        #
    while True:    # $ cd tiny-tetris && python3 tiny-tetris.py                 #
        w.move(0,0);kd,kl,kr,ku='KEY_DOWN','KEY_LEFT','KEY_RIGHT','KEY_UP'      #
        for (r,c) in [(r,c) for c in range(cs) for r in range(rs)]:             #
            w.addstr(r,c*len(e),e[b[r][c]]+" "*10)                              #
        w.addstr(rs,0,"-"*cs*len(e[0])+"\nlevel: "+str(l));time.sleep(0.001)    #
        for (r,c) in [(r,c) for c in range(len(cu)) for r in range(len(cu))]:   #
            if cu[r][c]==1: w.addstr(ro+r, (co+c)* len(e[0]), e[cu[r][c]])      #
        for (r,c) in [(r,c) for c in range(len(n)) for r in range(len(n))]:     #
            w.addstr(r,cs*len(e[0])+2+c*len(e[0]),e[n[r][c]])                   #
        try: cr = (cr+1)%d;ch = w.getkey()                # up - rotate         #
        except: ch = None                                 # left - move left    #
        if ch==kd: m_d();ro+=1                            # right - move right  #
        elif ch==kl and c_c(ro, co - 1, cu): co -= 1      # down - move down    #
        elif ch==kr and c_c(ro, co + 1, cu): co += 1      # ctrl-c - quit       #
        elif ch==ku and c_c(ro,co,list(zip(*cu[::-1]))):cu=list(zip(*cu[::-1])) #
        if cr==0: m_d();ro+=1                                                   #
except:curses.echo();w.keypad(f);curses.nocbreak();curses.endwin();print(str(l))#
#=========#=========#=========#=========#=========#=========#=========#=========#