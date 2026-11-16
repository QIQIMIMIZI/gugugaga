import os,glob,numpy as np,cv2
D=os.path.join(os.path.expanduser("~"),"Desktop")
I=[d for d in os.listdir(D) if d.startswith("cam_mix")][0]
F=sorted(glob.glob(os.path.join(D,I,"**","*.jpg"),recursive=True))
g0=cv2.cvtColor(cv2.imread(F[0]),cv2.COLOR_BGR2GRAY)
P=None
for p in [(10,7),(7,10)]:
    if cv2.findChessboardCorners(g0,p)[0]:
        P=p
        break
print("pattern",P)
o=np.zeros((P[0]*P[1],3),np.float32)
o[:,:2]=np.mgrid[0:P[0],0:P[1]].T.reshape(-1,2)
a=[];b=[];h,w=g0.shape
for f in F:
    g=cv2.cvtColor(cv2.imread(f),cv2.COLOR_BGR2GRAY)
    ok,c=cv2.findChessboardCorners(g,P)
    if not ok:
        continue
    c=cv2.cornerSubPix(g,c,(11,11),(-1,-1),(3,30,0.001))
    a.append(o);b.append(c)
print("used",len(a))
r,K,dc,x,y=cv2.calibrateCamera(a,b,(w,h),None,None)
print("err",r)
print(K)
print(dc.ravel())
s=cv2.imread(F[0]);u=cv2.undistort(s,K,dc)
cv2.imwrite(os.path.join(D,"before.png"),s)
cv2.imwrite(os.path.join(D,"after.png"),u)
cv2.imwrite(os.path.join(D,"compare.png"),np.hstack([s,u]))
print("done")
