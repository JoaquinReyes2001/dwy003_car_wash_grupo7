# dwy003_car_wash_grupo7
Integrantes:
Joaquín Antonio Reyes Montero.
Maximiliano Antonio Mora Chandía.
José Miguel López Molina.

Sección:003

Casos de prueba.
Se definieron casos de prueba para las siguientes tablas:
Insumo, MisionyVision, User.

-----TABLA DE INSUMO-----
A)Test de grabar insumo.
id:1.
Descripción:
Ingresamos datos de manera correcta con los atributos de nombre,descripcion,precio y stock, para que nos retorne un valor cuando se agrege o no.
Datos:
"Cera para vehículo","Nueva cera ultra brillante",1000,10.
Resultado Esperado:
Al momento de almacenarlo en la base de datos nos retornará un valor entero igual a 1 y en caso contrario un 0.
Resultado obtenido:
El metodo nos retorna un 1.

B)Test de eliminar insumo.
id:2.
Descripción:
Ingresamos un texto como id, para que lo busque y haga la eliminación en caso de que si exista y retornar un valor, al igual que en caso contrario.
Datos:
"Shampoo".
Resultado Esperado:
Al momento de hacer la eliminación y este insumo si existe, me retornará un entero igual a 1 y en caso contrario un 0.
Resultado obtenido:
El método nos retorna un 1.

C)Test de modificar insumo.
id:3.
Descripción:
Ingresamos un texto como nombre, para que encuentre el insumo con el mismo parámetro que se esta pasado y se registre la nueva información.En caso de ser encontrado
y modificado me retorna un valor, al igual que en el caso contrario.
Datos:
"Silicona",500,"Silicona en spray que entrega mayor brillo al automóvil",10.
Resultado Esperado:
Al momento de hacer la modificación y este insumo si existe, me retornará un entero igual a 1 y en caso contrario un 0.
Resultado obtenido:
El método nos retorna un 1.

-----TABLA DE MISIONYVISION-----
D)Test de grabar misión y visión.
id:4.
Descripción:
Se ingresan datos de manera correcta para que al momento de ser almacenado en la base de datos me retorne un valor, al igual que en el caso contrario.
Datos:
"Silicona",500,"Silicona en spray que entrega mayor brillo al automóvil",10.
Resultado Esperado:
Al momento de grabar correctamente la mision y la visión nos retornará el valor 1 y si no es posible almacenar la información un 0.
Resultado obtenido:
El método nos retorna un 1.

-----TABLA DE USER-----
E)Test de grabar usuario.
id:5.
Descripción:
Se registran datos de manera correcta para que los grabe y nos retorne un valor, al igual que en el caso contrario.
Datos:
"Joaquín","Reyes","joacoantonio@hotmail.com","joaquinreyes2001","micontraseñacar123".
Resultado Esperado:
Tras realizar el grabado del usuario y que este tenga almacenamiento en la base de datos, nos debera retornar un valor entero igual a  1 y un 0 en caso contrario.
Resultado obtenido:
El método nos retorna un 1.

