# Data Science Challenge - Mercado Libre

Este repositorio contiene todos los códigos empleados en la solución de la prueba. 
El caso de negocio escogido fue el siguiente:
"El equipo comercial quiere realizar estrategias focalizadas para los sellers, pero en este momento no existe una clasificación que permita identificar a aquellos que tienen un buen perfil y son relevantes para el negocio.¿Cómo podrías ayudar al equipo comercial a identificar estos sellers?"

Para resolverlo, primero se inicia por construir la base de datos a partir de las API de Mercado Libre. Este proceso puede ser consultado en el Notebook "Build_Dataset". La función que se construye en este Notenook permite construir bases de datos a partir de cualquier categoría de ítems para cualquiera de los países disponibles. No obstante, para la solución del caso de negocio en particular se escogió identificar los mejores vendedores de la categoría "Animales y Mascotas" para el marketplace de Colombia. Para reference, el id de la categoría es  "MCO1071".

Tras haber construido la base de datos, se empieza el análisis de la base de datos. Para esto, se consultan las variables con las que se cuenta y la definición de las mismas en el diccionario disponible en https://api.mercadolibre.com/items/MCO1071#options
Se escogen las variables (tanto numéricas como no numéricas) relevantes de cara a solucionar el caso de negocio y se inspeccionan sus valores, estadísticas descriptivas y solución. Se encuentran algunos insights relevantes acerca del entendimiento del negocio, como que todos los sellers aceptan Mercado Pago. También se identifican algunas limitaciones en la data, como que no se tiene información sobre descuentos o promociones, pero sí se tiene el precio original que solo es poblado si es mayor al precio de venta. También se analiza el identificador de los sellers, el cual se refiere el ID que se encuentra dentro de un campo que refleja la información dentro de un diccionario. De manera similar, se inspeccionan los tags de los ítems, los cuales pueden contener información valiosa para detectar a los sellers de mayor valor para el negocio.

Luego de inspeccionar las variables relevantes e identificar los pasos a seguir para procesar los datos, se realizan acciones a cada uno de los campos para poder emplearlos de manera exitosa en el modelamiento. Las variables numéricas son estandarizadas, y las variables no numéricas son codificadas dependiendo de la naturaleza de los campos. Adicionalmente, el ID y los tags son extraídos de los campos correspondientes. Finalmente, los ID's de los items son clusterizados para poder codificarlos y usar esta información en el modelamiento. Para más detalle acerca del análisis y procesamiento de los datos referirse al Notebook "Database_Analysis".

Posteriormente se realiza el proceso de modelamiento. Se escoge realizar dos tipos de modelos: de clusterización y de detección de anomalías, los cuales se complementan, como se verá más adelante. Respecto a los modelos de clusterización, se entrenan los siguientes modelos:
* K-Means
* Hierarchical Clustering
* DBSCAN Clustering

Respecto a la detección de anomalías, se entrena un modelo Isolation Forest.

De los modelos de clusterización, se escoge el que tiene mejor desempeño en la base de prueba empleando las métricas Silhouette Score y Calinski-Harabasz Score. El modelo K-Means da buenos resultados en términos de las métricas, por ende es el elegido para ser desplegado. 

Al implementar el K-Means se obtienen 5 grupos, siendo el grupo 3 el que tiene mejor desempeño que el resto en términos de las variables relevantes. Posteriormente, se despliega el Isolation Forest bajo un parámetro de contaminación del 10%. Utilizando este modelo, se detectan las anomalías, realizando un énfasis en el grupo 3 del clustering. Así, se detecta que las anomalías dentro de este grupo tienen aún mejor comportamiento en término de ventas.

De esta forma, se desarrolla un indicador del valor del seller. Así, el entregable del presente ejercicio es una categorización de los sellers en 3 niveles:
* Nivel 0: el seller no es relevante
* Nivel 1: el seller es altamente relevante para el negocio
* Nivel 2: el seller es muy relevante para el negocio dado su alto comportamiento en ventas y demás variables.

Para consultar más detalles respecto al modelamiento y la conclusión del challenge, referirse al Notebook "Modeling"

