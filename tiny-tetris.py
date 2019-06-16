from random import*;import time,sys;import curses as h;w=h.initscr();h.noecho() #
P,Q,m,s,e,p,a,q=20,10,5,300,{0:"· ",1:"██"},[[[1,1]]*2,[[0,1,0],[1]*3,[0]*3],[[1#
,0,0],[1]*3,[0]*3],[[0,0,1],[1]*3,[0]*3],[[1,1,0],[0,1,1],[0]*3],[[0,1,1],[1,1,0#
],[0]*3],[[0]*4,[1]*4,[0]*4,[0]*4]],range,len;M,b=p[randint(0,6)],[[0]*Q for r  #
in a(P)];h.cbreak();y,R,C,cr,l,d,n=lambda z,x,y:e[z[x][y]],0,4,0,1,s,p[randint(0#
,6)];w.nodelay(1);w.keypad(1);h.curs_set(0);A,B,sw=list,zip,{'U':'if not k(R,C'+#
',A(B(*M[::-1]))):M=A(B(*M[::-1]))','D':'V();R+=1','L':'if not k(R,C-1,M):C-=1',#
'R':'if not k(R,C+1,M):C+=1'};exec(('def k(R,C,se):\n for(r,c)in[(r,c)for c in '#
'a(q(M))for r in a(q(M))]:\n  if se[r][c]>0 and(not(0<=R+r<P and 0<=C+c<Q)or b['#
'R+r][C+c]>0):return 1\ndef V():\n global R,C,M,n,l,d\n if(k(R+1,C,M)and R<1 an'#
'd sys.exit())or k(R+1,C,M):\n  for(r,c)in[(r,c)for c in a(q(M))for r in a(q(M)'#
')]:\n   if R+r in a(P)and C+c in a(Q)and M[r][c]>0:b[R+r][C+c]=M[r][c]\n  M,n,'#
'R,C,d=n,p[randint(0,6)],-1,4,s+m-l*m\n  for i in[j for j in a(P)if sum(b[j])>9'#
']:b[1:i+1]=b[:i];b[0],l=[0]*Q,l+1\ntry:\n while 1:\n  o,z=a(q(n)),a(q(M));u=[('#
'r,c)for c in z for r in z];time.sleep(.001)\n  for(r,c)in[(r,c)for c in a(Q)fo'#
'r r in a(P)]:`(r,c*q(e),y(b,r,c))\n  for(r,c)in[(r,c)for(r,c)in u if M[r][c]>0'#
']:`(R+r,(C+c)*2,y(M,r,c))\n  for(r,c)in[(r,c)for c in o for r in o]:`(r,22+c*2'#
',y(n,r,c)+"· · ")\n  try:cr=(cr+1)%d;ch=w.getkey();exec(sw[ch[4:5]]);raise\n  '#
'except:exec("if cr<1:V();R+=1");`(P,0,"level "+str(l))\nexcept:h.echo();w.keyp'#
'ad(0);h.nocbreak();h.endwin();print("level "+str(l))').replace('`','w.addstr'))#