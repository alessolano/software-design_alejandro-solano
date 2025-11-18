# Tarea 4 - Alejandro Solano C27534 
## Patrones de Diseño usados: Decorator y Observer  
### Simulación de una cafetería

---

Esta tarea implementa una simulación de pedidos en una cafetería aplicando dos patrones de diseño según el enunciado de la tarea:

- **Decorator**  
- **Observer**

Además, se emplea una estructura modular que refuerza buenas prácticas de diseño, separación de responsabilidades, claridad arquitectónica y extensibilidad del sistema.

El programa permite:

- Crear productos (bebidas y alimentos).  
- Agregarles extras utilizando el patrón Decorator.  
- Registrar clientes como observadores mediante el patrón Observer.  
- Construir pedidos y vincularlos a cada cliente.  
- Preparar productos utilizando servicios dedicados (Barista y Pastelero).  
- Notificar clientes cuando sus pedidos están listos.  
- Generar exactamente la salida en consola solicitada en el enunciado.

---

## Estructura del Proyecto

La organización del proyecto es la siguiente:

```
src/
├─ main.py
├─ domain/
│  ├─ __init__.py
│  ├─ products.py
│  ├─ extras.py
│  ├─ order.py
│  └─ customer.py
├─ patterns/
│  ├─ __init__.py
│  └─ observer.py
└─ services/
   ├─ __init__.py
   ├─ kitchen.py
   └─ simulation.py
```

### Descripción de carpetas

#### `domain/`
Contiene todas las entidades centrales del sistema:

- Productos base (`Product`, `Beverage`, `Food`).  
- Decoradores concretos (`WithMilk`, `WithCinnamon`, etc.).  
- Pedidos (`Order`) como Subjects del patrón Observer.  
- Clientes (`Customer`) como Observers concretos.

#### `patterns/`
Implementación reutilizable del patrón **Observer**:

- `Observer` (interface).  
- `Subject` (interface base).

#### `services/`
Servicios y lógica de aplicación:

- `kitchen.py` → preparación de bebidas y alimentos.  
- `simulation.py` → flujo completo de la simulación.

#### `main.py`
Punto de entrada que invoca la función `run_simulation()`.

---

## Uso de patrones

### Patrón: Decorator

El patrón **Decorator** permite extender el comportamiento de un objeto de forma flexible sin modificar sus clases base.

### Aplicación en este proyecto

Partimos de productos simples:

- `Beverage`
- `Food`

A los cuales se les agregan extras tales como:

- Leche  
- Canela  
- Crema  
- Relleno de chocolate  

Cada extra se añade envolviendo el producto original con un decorador:

```python
coffee_with_extras = WithCinnamon(WithMilk(Beverage("cafe")))
```

Esto genera una descripción final como:

```
"cafe con leche y canela"
```

De esta forma el sistema permite construir combinaciones ilimitadas sin crear clases específicas para cada variante.

---

### Patrón: Observer

El patrón **Observer** modela relaciones donde uno o varios objetos observan a otro para ser notificados cuando cambia su estado.

### Aplicación en este proyecto

- `Order` actúa como **Subject**.  
- `Customer` actúa como **Observer**.

Cada cliente se suscribe a sus pedidos mediante:

```python
order.attach(customer)
```

Cuando el pedido cambia de estado a `READY`, se emite una notificación:

```python
order.change_status(OrderStatus.READY)
```

La implementación real del método `update` en el cliente no imprime en consola para cumplir con el formato exacto del enunciado, pero la lógica del patrón está completamente implementada.

---

## Simulación

La simulación incluye:

1. Creación de clientes.  
2. Creación de productos decorados.  
3. Construcción de pedidos y suscripción de observadores.  
4. Impresión del detalle de pedidos.  
5. Preparación de bebidas/alimentos con Barista y Pastelero.  
6. Cambio de estado de los pedidos.  
7. Notificación interna a clientes.  
8. Generación de la salida EXACTA requerida.

Esta lógica está centralizada en `services/simulation.py`.

---

## Salida del programa

La siguiente es la salida generada por el programa:

```
=== Simulacion de Cafeteria ===

Cliente: Ana

Ordena un cafe con leche y canela

Ordena un croissant con relleno de chocolate

Cliente: Carlos

Ordena un te verde

Ordena un cafe doble espresso con crema

[Barista]: Preparo bebida: Cafe con leche y canela

[Pastelero]: Preparo alimento: Croissant con relleno de chocolate

[Barista]: Preparo bebida: Te verde

[Barista]: Preparo bebida: Cafe doble espresso con crema

[Sistema]: Se notifican los clientes cuando sus pedidos estan listos.
```

---

## Buenas prácticas aplicadas

La tarea incorpora una serie de buenas prácticas de diseño y organización de código que permiten que la solución sea mantenible, extensible y coherente con los principios fundamentales del desarrollo orientado a objetos. Entre las más importantes se encuentran las siguientes:

### 1. Separación clara de responsabilidades
Cada módulo y clase cumple una función específica dentro del sistema.  
Las entidades centrales del dominio (productos, pedidos, clientes) se encuentran en el paquete `domain`, los patrones reutilizables en `patterns`, la lógica operativa en `services` y el punto de entrada en `main.py`.  
Esta separación evita concentrar demasiada lógica en un solo componente y facilita comprender el propósito de cada parte del código.

### 2. Uso adecuado de la herencia y del polimorfismo
Se definen clases base como `Product`, `Beverage` y `Food` que sirven como tipos genéricos de productos.  
Los decoradores extienden el comportamiento de estas clases sin alterar su implementación interna, y los observadores implementan interfaces bien definidas.  
El polimorfismo permite que los servicios de cocina reciban cualquier objeto que implemente la interfaz esperada sin depender de implementaciones concretas.

### 3. Aplicación correcta de los patrones de diseño
La estructura del proyecto hace un uso limpio del patrón Decorator para extender funcionalidad sin modificar clases base, y del patrón Observer para desacoplar la notificación de cambios del código que reacciona a ellos.  
La integración de ambos patrones demuestra cohesión en el diseño, ya que cada patrón resuelve un problema específico sin interferir con los demás componentes del sistema.

### 4. Código extensible y preparado para cambios futuros
El proyecto está diseñado para permitir modificaciones sin afectar el resto del sistema.  
Por ejemplo, agregar un nuevo tipo de extra para las bebidas o alimentos únicamente requiere definir un nuevo decorador.  
Igualmente, extender la lógica de la cocina mediante nuevos roles (como un chef especializado) puede hacerse creando nuevas clases en `services` sin necesidad de modificar clases existentes.

### 5. Nombres descriptivos y consistentes
Clases, métodos y variables utilizan nombres claros, específicos y en inglés, lo cual facilita comprender su propósito sin necesidad de comentarios adicionales.  
Los nombres siguen un estilo uniforme, evitando abreviaturas confusas o significados ambiguos, lo cual mejora la lectura del código.

### 6. Minimización del acoplamiento entre módulos
Los componentes dependen de abstracciones, no de implementaciones concretas.  
Por ejemplo, los clientes no necesitan conocer cómo se prepara un producto ni los detalles de la cocina; solo reaccionan a cambios de estado.  
Esta estrategia reduce dependencias innecesarias y facilita mover o modificar partes del sistema sin afectar otras.

### 7. Proyecto organizado por capas
El código está distribuido siguiendo una estructura por capas: dominio, patrones, servicios y entrada.  
Esto facilita localizar rápidamente cada elemento, evita confusiones y permite que el proyecto crezca manteniendo un orden coherente.

### 8. Simplicidad en el punto de entrada
La función `main()` delega toda la lógica a la simulación ubicada en `services/simulation.py`.  
Esto permite que el punto de entrada sea limpio, fácil de entender y compatible con diferentes escenarios de ejecución o pruebas unitarias.

### 9. Código apto para pruebas
La separación de lógica en clases pequeñas y autónomas permite que funciones clave puedan ser probadas individualmente.  
Los patrones Observer y Decorator refuerzan esta característica, ya que cada componente tiene responsabilidades bien delimitadas y un comportamiento predecible.

En conjunto, estas buenas prácticas producen un diseño que favorece la mantenibilidad, la escalabilidad, la claridad conceptual y la correcta aplicación de principios orientados a objetos. 

---

## Cómo ejecutar

Desde la carpeta `src`:

```bash
python main.py
```
