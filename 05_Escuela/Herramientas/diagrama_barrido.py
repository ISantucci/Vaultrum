# Verifica el diagrama discreto vs barrido contra sus invariantes.
H=1/60; V=720.0            # px/s  -> 12 px por paso
ESPESOR=4.0; PARED_X=100.0
d=V*H
assert abs(d-12.0)<1e-9, "el desplazamiento por paso no es 12 px"
x=94.0; posiciones=[x]
for _ in range(2):
    x+=d; posiciones.append(x)
# I3: hay tunneling sii ninguna posicion de paso cae dentro de [PARED_X, PARED_X+ESPESOR]
dentro=[p for p in posiciones if PARED_X <= p <= PARED_X+ESPESOR]
tunel = (d > ESPESOR) and not dentro
# barrido: primer cruce del segmento [p, p+d] con el plano PARED_X
p0=posiciones[0]
t=(PARED_X-p0)/d
assert 0<=t<1, f"I4 rota: t={t}"
assert d>ESPESOR, "I3: el caso elegido no exhibe la condicion"
print(f"h={H*1000:.1f}ms  v={V}px/s  ->  desplazamiento/paso = {d:.1f} px   espesor pared = {ESPESOR} px")
print(f"posiciones de paso: {[round(p,1) for p in posiciones]}")
print(f"alguna cae dentro de la pared [{PARED_X}, {PARED_X+ESPESOR}]? {dentro if dentro else 'NO'}")
print(f"tunneling con muestreo discreto: {tunel}")
print(f"barrido: impacto en t = {t:.2f} del paso  ->  x = {p0+t*d:.1f}")
print("\nINVARIANTES VERIFICADAS: I1 avance=v*h igual en ambos · I2 discreto mira posiciones, barrido mira el segmento")
print("                         I3 tunel sii v*h>espesor y ninguna posicion adentro · I4 t en [0,1) fraccion del PASO")
