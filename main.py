# v37f: 50k nodes, R=3, ID16
import os,sys,json,urllib.request
d='nbrq'
X=print
W=range
V=len
J=int
G=abs
R=[0,100,320,330,500,900,0]
j="PPPPQRRLQONPPPPTQQRURRTVZZZZPPPP"
k="FHJJHLPQJQRSJPSTJQSTJPRSHLPPFHJJ"
Z=(14,18,31,33,-14,-18,-31,-33)
D=(1,15,16,17,-1,-15,-16,-17)
l=(),(),Z,D[1::2],D[0::2],D,D
a={0:13,4:12,7:14,112:7,116:3,119:11}
S=1E9
m=1E5
u={};v=[0]*64;Y={}
def T(x):
	O="KQkq";global A,B,I,E,H,N;A=[0]*128;N=[];C=x.split();P=C[0].split('/');Q="PNBRQK";H=[0]*2
	for(R,S)in enumerate(P):
		L=7-R;D=0
		for F in S:
			if F.isdigit():D+=J(F)
			else:
				K=(Q.index(F.upper())+1)*(2*(F<'a')-1);A[L*16+D]=K
				if G(K)==6:H[K<0]=L*16+D
				D+=1
	B=1 if C[1]=='w'else-1;I=sum(1<<O.index(A)for A in C[2]if A in O);E=-1
	if V(C)>3 and C[3]!='-':E=J(C[3][1])*16+ord(C[3][0])-113
def U(s,t):
	for C in(15,17):
		B=s-C if t>0 else s+C
		if not B&136 and A[B]==t:return 1
	for(F,H)in((Z,2),(D,6)):
		for C in F:
			B=s+C
			if not B&136 and A[B]==H*t:return 1
	for C in D:
		B=s+C
		while not B&136:
			E=A[B]
			if E:
				if E in(5*t,(3+(G(C)not in(15,17)))*t):return 1
				break
			B+=C
	return 0
def b(s,p):
	for A in((5,4,3,2)if p>>4==7*(B>0)else(0,)):F.append(s|p<<7|A<<14)
def c():
	global F;F=[]
	for C in W(128):
		if C&136:continue
		O=A[C]
		if not O or O*B<0:continue
		L=G(O)
		if L==1:
			J=16*B;P=C+J
			if not P&136 and not A[P]:
				b(C,P)
				if C>>4==1+5*(B<0)and not A[C+2*J]:F.append(C|C+2*J<<7)
			for M in(J-1,J+1):
				H=C+M
				if H&136:continue
				N=A[H]
				if N*B<0 or H==E:b(C,H)
		else:
			for M in l[L]:
				H=C+M
				while not H&136:
					N=A[H]
					if not N or N*B<0:F.append(C|H<<7)
					if N:break
					if L<3 or L>5:break
					H+=M
	for(t,d,k)in((1,4,6),(2,4,2),(4,116,118),(8,116,114)):
		if k>d:Q=d+3;R=d+1,k;S=d,d+1,k
		else:Q=d-4;R=d-1,d-2,d-3;S=d,d-1,k
		if I&t and A[Q]==4*B and A[d]==6*B and not any(A[B]for B in R)and not any(U(A,-B)for A in S):F.append(d|k<<7)
	return F
def e(n):
	global B,I,E;N.append((A[:],B,I,E,H[:]));C=n&127;D=n>>7&127;J=n>>14&7;F=A[C];L=A[D]
	if G(F)==1 and D==E and not L:A[D-16*B]=0
	A[C]=0;A[D]=F
	if J:A[D]=J*B
	if G(F)==6:
		H[B<0]=D
		if G(D-C)==2:K=C+(3 if D>C else-4);M=C+(1 if D>C else-1);O=A[K];A[K]=0;A[M]=O
	I=I&a.get(C,15)&a.get(D,15);E=-1
	if G(F)==1 and G(D-C)==32:E=(C+D)//2
	B=-B
def f():global B,I,E;A[:],B,I,E,H[:]=N.pop()
def n():
	D=0
	for C in W(128):
		if C&136 or not A[C]:continue
		E=A[C];F=G(E);H=j if F<2 else k;I=min(C&7,7-(C&7));s=E//F;r=(C>>4)if s>0 else 7-(C>>4)
		D+=s*(R[F]+(ord(H[r*4+I])-80)*5-(F>5)*r*10)
	return D if B>0 else-D
def g(a,z,d,y):
	D=y;global K,L;K+=1
	if K>50000:raise KeyError
	x=d>0 and(tuple(A),B);y=u.get(x,0)
	F=d<=0;M=U(H[B<0],-B)
	if d>2 and M<1 and(e(1032),-g(-z,1-z,d-3,D+1),f())[1]>=z:return z
	if F and not M:
		C=n()
		if C>=z:return z
		if C>a:a=C
		w=[B for B in c()if A[o:=B>>7&127]or B>>14&7 or o==E]
	else:w=c()
	w.sort(key=lambda m:-(m==y)*2000-R[G(A[m>>7&127])]-(m==v[D])*400-Y.get(m,0));J=-S;N=0
	for P in w:
		e(P)
		if U(H[B>0],B):f();continue
		N+=1
		if D<1 and N<2:L=P
		if N>3 and d>2 and not(A[P>>7&127]or P>>14&7)and not M:C=-g(-z,-a,d-2,D+1);C=-g(-z,-a,d-1,D+1)if C>a else C
		else:C=-g(-z,-a,d-1,D+1)
		f()
		if C>=z:
			if not A[P>>7&127]:v[D]=P;Y[P]=Y.get(P,0)//2+d*d
			if x and V(u)<m:u[x]=P
			return z
		if C>J:
			J=C
			if not D:L=P
		if C>a:a=C
	if not N:return-m+D if M else(a,0)[not F]
	return a if F else J
def o(d):
	global K,L;K=L=0
	for A in W(1,d+1):
		M=L
		try:g(-S,S,A,0)
		except KeyError:L=M or L;break
	return L
def p(m):A=m&127;B=m>>7&127;C=m>>14&7;return'%c%d%c%d%s'%(97+A%8,A//16+1,97+B%8,B//16+1,d[C-2]if C else'')
O=os.environ.get("MAKEFUN_ENV_URL")or sys.exit(1)
def P(a,b):
	c=urllib.request.Request(O+a,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
	try:
		with urllib.request.urlopen(c)as d:return json.load(d)
	except Exception:return 0
while 1:
	C=P("/game",{})
	if C["status"]=="done":break
	while C["status"]=="your_move":
		T(C["fen"]);o(16);M=p(L)
		Q=P("/move",{"game":C["game"],"move":M})
		if not Q:Q=P("/move",{"game":C["game"],"move":C["legal_moves"][0]})
		C=Q
