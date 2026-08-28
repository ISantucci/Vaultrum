import math
T=0.5; t_frame=0.10; BASE=(1-t_frame)**60   # lo que queda tras 1 s a 60 fps -> el objetivo
filas=[]
for fps in (30,60,144):
    n=int(fps*T); dt=1.0/fps
    ing=(1-t_frame)**n
    t_dt=1-BASE**dt
    cor=(1-t_dt)**n
    filas.append((fps,n,ing,cor))
# INVARIANTES
ref=filas[1][2]
assert abs(filas[1][2]-filas[1][3])<1e-9, "I3: a 60 fps las dos formas deben coincidir"
cors=[c for _,_,_,c in filas]
assert max(cors)-min(cors) < 1e-9, f"I2 rota: el correcto depende de fps {cors}"
ings=[i for _,_,i,_ in filas]
assert max(ings)/min(ings) > 100, f"I1: el caso elegido no exhibe la dependencia {ings}"
for _,_,i,c in filas:
    assert 0 < i <= 1 and 0 < c <= 1, "I4 rota"
print(f"suavizado 'lerp(a,b,0.10) por frame' — despues de {T}s")
print(f"{'fps':>5}{'frames':>8}{'INGENUO restante':>20}{'CORRECTO restante':>20}")
for fps,n,i,c in filas:
    print(f"{fps:>5}{n:>8}{i:>19.1%}{c:>19.1%}")
print(f"\nforma correcta:  t_dt = 1 - base^dt   con base = {BASE:.4f}  (lo que queda tras 1 s)")
print("INVARIANTES VERIFICADAS: I1 ingenuo=(1-t)^n depende de fps · I2 correcto=base^segundos NO depende")
print("                         I3 ambas coinciden en el fps de calibracion · I4 restante en (0,1]")
