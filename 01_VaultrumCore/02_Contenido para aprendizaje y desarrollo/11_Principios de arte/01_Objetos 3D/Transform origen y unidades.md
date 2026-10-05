## Definición

Todo objeto 3D tiene una **transform** —posición, rotación y escala— que lo ubica en la escena, un **origen** —el punto alrededor del cual rota y desde el cual se coloca— y está escrito en unas **unidades**.

```txt
transform   donde esta, como esta girado, cuanto esta escalado
origen      el pivote: desde donde se coloca, alrededor de que gira
unidades    que significa "1": un metro, un centimetro, nada
ejes        que eje es arriba y cual es adelante
```

---

## Idea central

**La malla puede estar perfecta y el objeto, roto.** Estos cuatro datos no se ven en la malla y deciden si el asset entra al motor sin caso especial.

```txt
escala sin aplicar   el objeto mide bien en pantalla y sus datos no: la fisica, el
                     skinning y los modificadores leen la escala del objeto y no la de
                     la malla. Una escala negativa, al aplicarse u hornearse, ademas
                     invierte el sentido de las caras
origen mal puesto    lo que apoya flota o se hunde al colocarlo; lo que rota gira
                     alrededor de otro punto. Un apoyo sin medir no se ve: Kit_Arbusto
                     estuvo 422 mm bajo el piso una sesion entera
unidades             un asset en centimetros entra cien veces mas grande, o cien veces
                     mas chico, y nadie lo ve hasta que esta al lado de otro
ejes                 cada motor tiene su convencion
```

---

## Los ejes de cada lado

```txt
Blender    Z arriba
Unity      Y arriba, Z adelante
Unreal     Z arriba, X adelante
glTF       Y arriba; el frente del asset mira a +Z
```

El exportador convierte, y **la conversión se verifica leyendo el archivo entregado**, no el fuente (ley 6 del Área de Arte, `RA-007`).

La convención interna del área —*mira a +Y*— no coincide con la de todos los formatos. El contrato del cliente le gana a la convención interna; cómo compensa la IA al exportar, sin tocar el asset, está en IA Operativa (`Blender por MCP`).

---

## El origen sigue a la función

```txt
lo que apoya      al piso, en el centro de su planta: z_min = 0 exacto
lo que vuela      en su centro de masa real
lo que gira       en su eje de giro (una puerta, en la bisagra)
lo que se encastra  en su punto de encastre
```

Es `RA-008`. El origen no es un detalle de prolijidad: es lo que hace que una regla de apilado —*todo apoya en z=0 y el nivel lo sube 0.30*— funcione sin un solo caso especial.

---

## Cómo se juzga

```txt
se mide     escala (1,1,1) y rotacion 0 aplicadas, z_min, bbox en metros, centro:
            arte.malla(), ley 3, sobre el asset ARMADO (despues de emparentar).
            Ejes y unidades del archivo entregado: arte.entrega(), ley 6
se juzga    donde va el origen de algo que no apoya, no vuela y no gira
```

---

## Errores comunes

```txt
Verificar antes de emparentar: la malla esta bien, la colocacion no se probo (RA-008.5).
Confiar en un matrix_world desactualizado (RA-005).
Escalar en modo objeto para "ajustar" y no aplicar.
Mover el origen a ojo en vez de ponerlo por funcion.
Dar por bueno el eje porque en el DCC mira bien: se verifica en el archivo entregado.
```

---

## Fuentes

- `71_Blender_Manual` — transform, aplicar escala, origen.
- `glTF 2.0`, especificación de Khronos — la convención de ejes del formato.
- Área de Arte: el contrato del asset, `RA-003`, `RA-005`, `RA-007` y `RA-008`.
