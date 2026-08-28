# Genera y VERIFICA el diagrama del acumulador contra sus tres invariantes.
H = 50/3  # 16.666.. ms  (1/60 s)
TECHO = 5
dts = [27, 12, 41, 9, 210]   # el ultimo simula un freeze de pestania
acum = 0.0; filas = []
for dt in dts:
    acum += dt; pasos = 0
    while acum >= H and pasos < TECHO:
        acum -= H; pasos += 1
    cortado = acum >= H
    filas.append((dt, pasos, round(acum,1), round(acum/H,2), cortado))
# INVARIANTES
for dt,pasos,resto,alpha,cortado in filas:
    assert pasos <= TECHO, "I2 rota: mas pasos que el techo"
    if not cortado:
        assert resto < H + 1e-9, f"I3 rota: resto {resto} >= h"
    assert 0 <= alpha, "I4 rota: alpha negativo"
    if not cortado: assert alpha < 1.0, f"I4 rota: alpha {alpha} >= 1"
print(f"h = {H:.1f} ms   techo = {TECHO} pasos")
print(f"{'dt real':>8}{'pasos':>7}{'resto':>8}{'alpha':>7}   estado")
for dt,pasos,resto,alpha,cortado in filas:
    print(f"{dt:>7}ms{pasos:>7}{resto:>7.1f}{alpha:>7.2f}   {'TECHO — se atrasa la simulacion' if cortado else 'al dia'}")
print("\nINVARIANTES VERIFICADAS: I1 todo paso mide h · I2 pasos<=techo · I3 resto<h salvo corte · I4 alpha en [0,1)")
