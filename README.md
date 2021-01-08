# Medidor CO2

## Tabla de contenidos
1. [Empezando por el principio: ¿porqué un medidor de CO₂?](#empezando)
2. [Consideraciones previas](#consideraciones)
3. [Manos a la obra: ¿qué necesitamos?](#componentes)
4. [Hardware: Montando el sensor de CO₂](#sensor)
5. [Hardware: Montando la pantalla](#pantalla)
6. [Software: Dándole vida](#software)
7. [Cómo funciona](#funcionamiento)
8. [Posibilidades y ampliaciones](#posibilidades)
9. [Notas para técnicos y profesionales](#notas-para-tecnicos)
10. [Preguntas frecuentes acerca de funcionamiento, uso y calibración](#faq)
11. [Referencias y créditos](#creditos)

### 1. Empezando por el principio: ¿porqué un medidor de CO₂? <a name="empezando"></a>
La pandemia de COVID-19 ha movido a muchos profesionales y expertos a divulgar conocimiento, cada uno en su campo: Acerca del propio virus SARS-CoV-2 o de las herramientas de las que disponemos para combatirlo. Entre éstas últimas está la tecnología de la que disponemos en el siglo XXI.

Gracias al trabajo de científicos como [Jose-Luis Jimenez](https://twitter.com/jljcolorado), y a la labor informativa de personas como [Pablo Fuente](https://twitter.com/PabloFuente), hoy tenemos acceso a muchísima información de corte científico.

Nosotros, los trabajadores del sector tecnológico, tenemos el deber de nutrirnos de dichos conocimientos para crear una gama de herramientas útiles y sencillas de usar para, finalmente, ponerlas a disposición de toda la población.

Pero yendo un paso mas allá, quizá sea el momento de que todos hagamos un pequeño esfuerzo por mejorar nuestras competencias tecnológicas, para así alcanzar un nivel de sincronía adecuado con el año en el que vivimos y la tecnología que nos rodea. 
Solo comprendiendo las herramientas de las que disponemos, conseguiremos usarlas correctamente en nuestro beneficio.

#### 1.1 Pero ¿porqué medir la concentración de CO₂?
En un espacio interior como pueda ser una tienda, un restaurante, o la casa de un amigo, la concentración de CO₂ se eleva en función del número de personas que hay respirando.
Al exhalar CO₂ con la respiración, poco a poco la habitación se va "llenando" de este gas. Si no se ventila, dicha concentración de CO₂ se va acumulando con el paso de los minutos y las horas. 
El trabajo de científicos reputados como [Jose-Luis Jimenez](https://twitter.com/jljcolorado), nos indica que la ventilación y la renovación de aire es vital para evitar la propagación de enfermedades que se transmiten por el aire, como el COVID-19.

Por lo tanto si somos capaces de medir cuánta concentración de CO₂ tenemos en una habitación, dispondremos un indicador certero para saber si debemos ventilar la estancia en función del número de personas que hay dentro de ella, reduciendo así el riesgo de contagio de manera dramática.

Parece complicado, pero en realidad no lo es tanto. Veamos cómo hacer nuestro propio medidor de CO₂

### 2. Consideraciones previas <a name="consideraciones"></a>
Antes de ponernos a trabajar tenemos que tener muy claras ciertas pautas:
 - Esto es un proyecto "maker". Esto significa que no fabricarás una herramienta comercial y por lo tanto no dispone de garantía de fabricante, mas allá de la individual de sus componentens. Los proyectos "maker" se comparten con la intención de poner a disposición de todo el mundo un conocimiento o una experiencia adquirida.
 - Lo que vas a encontrar es el primer empujón para crear tu propio dispositivo.
 - Si no has hecho nunca nada así, tu éxito depende enteramente de que sigas las instrucciones que se proveen. No se requiere ninguna habilidad técnica.
 - Cuando termines tu medidor de CO₂, te animo personalmente a que sigas trabajando en él: búscale un lugar adecuado, dótalo de una carcasa o soporte físico mejor, procúrale una mejor fuente de alimentación, etc.
 - Dado que no somos fabricantes, no vas a obtener un aparato "bonito", pero si funcional. Diponer de equipos caros como una impresora 3D o una inyectora de plástico haría que tu medidor de CO₂ luciera mejor. Pero se trata de reducir el coste al máximo, manteniendo la facilidad de montaje y la premisa de no requerir conocimientos técnicos previos.
 
Si no estás de acuerdo con estos puntos, es mejor que no continúes. Pero si te parece bien ¡adelante!

### 3. Manos a la obra: ¿qué necesitamos? <a name="componentes"></a>
Sin pensar mucho podemos llegar a la conclusión de que vamos a necesitar: un sensor de CO₂ y algo que nos permita ver la medición. Has acertado el casi la totalidad de los componentes.
Vamos a usar principalmente:
- **Un sensor de CO₂**: Va a ser la pieza encargada de realizar la medición. Concretamente el MH-Z19B.
- **Una pantalla muy pequeña**: No necesitamos mucho para mostrar un valor, así que usaremos una pantalla de apenas una pulgada.
- **Raspberry Pi Zero**: Necesitamos un "cerebro" que coordine todo esto. Raspberry es una plaquita que contiene un mini-ordenador. Es de muy bajo coste, fácil de usar y es perfecta para este proyecto.
- **Una fuente de alimentación portátil**: dado que nuestro "cerebro" se alimenta por USB, podemos usar una batería portátil cualquiera, o una que se pueda integrar con toda la lista anterior.

Ésta es la lista de la compra:

#### 3.1 Raspberry Pi Zero
Esta plaquita nos va a dar el soporte necesario para poder fabricar nuestro medidor de CO₂. Se trata básicamente de un microordenador y está orientada a aficionados de la computación educativa y emprendedores informáticos que desean tener equipos económicos para crear desarrollos y proyectos ambiciosos dentro del campo de la robótica y la automatización.
Para comprarla, tenemos que tener en cuenta lo siguiente:
  * El nombre completo del modelo que necesitamos es Raspberry Pi Zero WH.
  * Tiene que venir con un montón de patillas ya soldadas, como se ve en la foto.
  * No necesitamos un kit con carcasa y todo lo demás. Sólo la placa con las patillas soldadas.
  
Existen muchísimas tiendas donde comprar este pequeño ordenador. Os dejo una lista con algunas de las tiendas en las que suelo comprar:
  * [Tienda KUBII](https://www.kubii.es/raspberry-pi-3-2-b/2076-raspberry-pi-zero-wh-kubii-3272496009394.html)
  * [Tienda Ultra-Lab](http://ultra-lab.net/producto/raspberry-pi-zero-wh/)
  * [Tienda Tienda-Tec](https://www.tiendatec.es/raspberry-pi/gama-raspberry-pi/768-raspberry-pi-zero-wh-0327249600939.html)

Si andáis justos de presupuesto, buscad el mas barato. La placa es la misma independientemente del precio.

**Coste medio: 15€**

![Raspberry-Pi-Zero_WH](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/RaspberryPiZeroWH-small.png?raw=true)

---

#### 3.2 Tarjeta Micro SD
Una tarjeta SD mínimo de 8Gb en la que instalaremos el software que manejará todo el sistema. La introduciremos en nuestra Raspberry Pi Zero.

Como siempre tenéis muchísimas opciones. Os dejo un par de enlaces en Amazon:
 * [Tarjeta SD 8Gb](https://www.amazon.es/Transcend-TS8GUSD300S-Tarjeta-microSD/dp/B07JHGQTCY/ref=sr_1_5?__mk_es_ES=ÅMÅŽÕÑ&dchild=1&keywords=tarjeta+8gb&qid=1610098200&refinements=p_85%3A831314031&rnid=831276031&rps=1&sr=8-5)
 * [Tarjeta SD 16Gb](https://www.amazon.es/Kingston-Tarjeta-SDCS2-16GB-Adaptador/dp/B07YGZHSJS/ref=sr_1_4?__mk_es_ES=ÅMÅŽÕÑ&dchild=1&keywords=tarjeta+8gb&qid=1610098200&refinements=p_85%3A831314031&rnid=831276031&rps=1&sr=8-4)

**Coste medio: 5€**

---

#### 3.3 Sensor de CO₂ MH-Z19B
Hay varios modelos comeriales de este sensor y tenemos que tener en cuenta varias cosas antes de comprar el adecuado:
  * Que venga con las patillas soldadas
  * Que venga con las patillas al aire, sin ningún tipo de conector ni cable
  
Particularmente lo he comprado [en esta tienda de electrónica](https://electronperdido.com/shop/sensores/calidad-aire/mh-z19-sensor-co2-ndir-5000ppm/) pero podéis buscarlo o pedirlo en tiendas de vuestra confianza.

Ésta es la pieza mas cara de nuestro medidor de CO₂. No conviene escatimar en este componente.

**Coste medio: 35€**

![Sensor-co2-correcto](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/SensorCO2-correcto.png?raw=true)

---

#### 3.4 Mini pantalla
Aquí las opciones son muchas y muy variadas. Para este proyecto hemos seleccionado una pantalla de 1.8 pulgadas que nos ofrece unas pocas líneas de texto. Concretamente ésta.

![pantalla](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/Pantalla18-micro.png?raw=true)

Yo la he conseguido desde [Amazon](https://www.amazon.es/gp/product/B078J5TS2G/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) pero podéis buscarla en cualquier otro comercio.

**Coste medio: 8€**

---

#### 3.5 Batería
Cualquer batería o powerbank que tengamos por casa nos vale para este proyecto. Por eso no voy a incluir el precio en este documento.

**IMPORTANTE**: Necesitaremos un cable USB

---

#### 3.6 Cableado
Necesitamos un tipo de cableado especial que se llama "puente Dupont", para conectar la pantalla y el sensor a la placa. Ésto nos va a evitar la soldadura. 

Son realmente baratos, y los venden en packs en muchas ocasiones, con diferentes longitudes. Tenemos que tener en cuenta lo siguiente:
 * Los cables y sus conectores han de ser individuales
 * Vamos a necesitar 12 cables de este tipo
 * Todos los cables han de tener conectores hembra por ambos lados
 * Es recomendable que no superen los 20cm

Os invito a buscar los mas adecuados para vuestro uso. Os dejo algún ejemplo
 * [Tienda PC-Componentes](https://www.pccomponentes.com/kit-40-jumpers-de-20cm-hembra-hembra?gclid=CjwKCAiAouD_BRBIEiwALhJH6LzFre7n5-CoJpS7f5hDsUbYnUqA9tx4Qyu0J-1MPEz_wFEC3rV2ahoCu9sQAvD_BwE&)
 * [Tienda Shoptrónica](https://www.shoptronica.com/conectores-dupont/3932-conector-dupont-hembra-hembra-cable-140mm-1pin-0689593949783.html)
 * [Tienda Iberobotics](https://www.iberobotics.com/producto/40x-cables-dupont-hembra-hembra/)

**Coste medio: 3€**

![Cables-dupont](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/CablesDupont.png?raw=true)

---

Con todo esto estamos listos para montar nuestro propio sensor de CO₂ por un **coste total aproximado de 70€**

### 4. Hardware: Montando el sensor de CO₂ <a name="sensor"></a>
Para poder activar y leer el sensor de CO₂ que hemos comprado, lo primero que tenemos que hacer es conectarlo a la placa Raspberry Pi Zero. Como ya habrás supuesto, para eso están esas "patillas" que tienen tanto el sensor como la placa.

Si nos fijamos en la placa, tenemos dos hileras largas de patillas. Cada una de ellas tiene una función específica, pero no entraremos en detalles mas allá de lo que necesitamos saber.

Coloca la placa de tal modo que las "patillas" queden boca arriba y lo mas lejos de ti posible.

Ahora fíjate en el siguiente esquema y conecta el sensor exactamente como se indica. Te recomiendo que respetes los colores rojo (corriente) y negro (tierra) de los cables Dupont para tenerlos idenficados (puedes ver una imagen mas grande en [este enlace](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/conexiones-sensor.png?raw=true))

![esquema-sensor](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/conexiones-sensor-small.png?raw=true)

Especial atención a las "patillas" del sensor. Hay que fijarse muy bien en las inscripciones que lleva impresas:
 * **"GND"**: Toma de tierra
 * **"Vin"**: Toma de corriente (+5V)
 * **"Tx"**: (en ocasiones viene como TXD)
 * **"Rx"**: (en ocasiones viene como RXD)
 
No podemos cometer errores con esto o no funcionará. En el peor de los casos si confundimos el cable rojo o el negro podremos dañar el sensor. Es preferible repasar varias veces las conexiones antes de continuar.

¡Nada mas por el momento! Es así de sencillo. Podemos dejarlo "colgando" para probar mas adelante que efectivamente funciona. No hay problema.

### 5. Hardware: Montando la pantalla <a name="pantalla"></a>
Sin mover nuestra Raspberry Pi Zero de la posición en la que está, tomamos la pantalla y comenzamos a conectarla usando los cables Dupont, siguiendo el siguiente esquema. De nuevo te recomiendo respetar los colores rojo (corriente) y negro (tierra) de los cables Dupont para tenerlos idenficados. (puedes ver una imagen mas grande en [este enlace](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/conexiones-pantalla.png?raw=true))

![esquema-pantalla](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/conexiones-pantalla-small.png?raw=true)

Especial atención a las "patillas" de la pantalla. Hay que fijarse muy bien en las inscripciones que lleva impresas:
 * **"VCC"**: Toma de corriente (+5V)
 * **"GND"**: Toma de tierra
 * **"CS"**
 * **"RESET"**
 * **"AO"**
 * **"SDA"**
 * **"SCK"**
 * **"LED"**

Ahora mismo tendrás una maraña de cables y la pantalla y el sensor por ahi "colgando". No te preocupes, esto es normal y es la manera en la que vamos a probar que todo funciona.

Una vez mas, es el momento de repasar bien todas las conexiones. Te dejo un esquema que representa cómo deberías tenerlo ahora mismo (puedes ver una imagen mas grande en [este enlace](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/conexiones-final.png?raw=true))

![esquema-final](https://github.com/jorgej-ramos/medidor-co2/blob/main/images/conexiones-final-small.png?raw=true)

Si todo está correcto, ya te puedes olvidar de las "patillas", los cables y conectar cosas: hemos terminado con el hardware.

### 6. Software: Dándole vida <a name="software"></a>

### 7. Cómo funciona <a name="funcionamiento"></a>

### 8. Posibilidades y ampliaciones <a name="posibilidades"></a>

### 9. Notas para técnicos y profesionales <a name="notas-para-tecnicos"></a>

### 10. Preguntas frecuentes acerca de funcionamiento, uso y calibración <a name="faq"></a>

### 11. Referencias y créditos <a name="creditos"></a>
