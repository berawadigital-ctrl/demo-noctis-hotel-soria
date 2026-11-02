# Contenido de la demo Noctis Hotel (Soria) (es/en/fr/de). Hechos de noctishotel.es leidos el 02/11/2026 (ver berawa/sources.json). Sin valoraciones; sin precios.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Suites en la Roca y Suites nido','Burbujas Premium y La Villa'],'en':['Rock Suites and Nest Suites','Premium Bubbles and La Villa'],'fr':['Suites dans la roche et Suites nid','Bulles Premium et La Villa'],'de':['Felsensuiten und Nestsuiten','Premium-Bubbles und La Villa']}
RD={
'es':['Suites con jardín y piscina climatizada privados, o elevadas entre los árboles con terraza, bañera y lucernario para ver las estrellas desde la cama.','Burbujas con vistas al cielo, una con piscina infinity y otra en el bosque; y La Villa, una casa restaurada con cinco habitaciones.'],
'en':['Suites with private garden and heated pool, or raised among the trees with terrace, bathtub and skylight to see the stars from bed.','Bubbles with views of the sky, one with an infinity pool and one in the forest; and La Villa, a restored house with five bedrooms.'],
'fr':['Suites avec jardin et piscine chauffée privés, ou perchées dans les arbres avec terrasse, baignoire et puits de lumière pour voir les étoiles depuis le lit.','Bulles avec vue sur le ciel, l’une avec piscine à débordement, l’autre en forêt ; et La Villa, une maison restaurée de cinq chambres.'],
'de':['Suiten mit privatem Garten und beheiztem Pool, oder zwischen den Bäumen erhöht mit Terrasse, Badewanne und Oberlicht, um vom Bett aus die Sterne zu sehen.','Bubbles mit Blick in den Himmel, eine mit Infinity-Pool und eine im Wald; dazu La Villa, ein restauriertes Haus mit fünf Schlafzimmern.']}
ART={
'hero':('hills',4231,['#0c1420','#c9b27a','#efe1b8','#2e4a3a','#22382c','#121e18']),
'intro':('hills',4232,['#eef0ea','#f3ead4','#b9a06a','#7e8a6a','#5a6a4e','#3c4a34']),
'r1':('columns',4241,['#ece9e0','#b9a06a','#6e6040','#4a402a','#262014']),
'r2':('waves',4242,['#0c1420','#d2bc84','#f2e6c2','#365444','#28403a','#14221c']),
'g1':('hills',4251,['#0c1420','#c9b27a','#efe1b8','#2e4a3a','#22382c','#121e18']),
'g2':('arches',4252,['#eeebe2','#f8f5ee','#76664a','#4e4430','#262014']),
'g3':('waves',4253,['#e8ece8','#f2ecdc','#bba46e','#6e8a78','#4e6a5a','#2e4a3c']),
'g4':('skyline',4254,['#0c1420','#d2bc84','#f2e6c2','#365444','#28403a','#14221c'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Noctis Hotel · Suites y burbujas con vistas a las estrellas en Soria',see_rooms='Ver los alojamientos',nav_rooms='Alojamientos',hero_k='Soria · Paraje de San Marcos, 13',hero_t='Elegancia y tranquilidad en un entorno natural',hero_s='Suites, burbujas premium y una villa a 3 km del centro de Soria, en la Sierra de San Marcos.',
 intro_t='El privilegio de la pausa',intro_p1='Un lugar donde lo natural no está reñido con el lujo: alojamientos exclusivos de materiales sostenibles en la Sierra de San Marcos.',
 intro_p2='Su arquitectura se inspira en las casas cuboides de los pueblos tradicionales, que crecen juntas entre vegetación y rocas.',
 stats=['A 3 km de Soria','Sierra de San Marcos','Burbujas con vistas al cielo','Cocina de producto'],rooms_t='Suites, burbujas y villa',rooms_s='Alojamientos independientes para disfrutar de la naturaleza.',
 svcs=['Suites con piscina climatizada privada','Burbuja con piscina infinity','Bañeras en la terraza','Espacio Jaima al aire libre','La Cabaña para cenas tranquilas','Eventos'],
 around_s='El entorno de la Sierra de San Marcos y la ciudad de Soria, a escasos 3 km.',
 loc_p='Paraje de San Marcos nº 13 · 42005 Soria. Información de reservas de lunes a domingo de 9:00 a 00:00 horas.',
 chips=['¿Qué alojamientos tenéis?','¿Hay piscina?','¿A qué hora es el check-in?','¿Cómo reservo?']),
'en':dict(title='Noctis Hotel · Suites and bubbles under the stars in Soria',see_rooms='See the accommodation',nav_rooms='Accommodation',hero_k='Soria · Paraje de San Marcos, 13',hero_t='Elegance and calm in a natural setting',hero_s='Suites, premium bubbles and a villa 3 km from central Soria, in the Sierra de San Marcos.',
 intro_t='The privilege of pausing',intro_p1='A place where nature and luxury go together: exclusive lodgings made of sustainable materials in the Sierra de San Marcos.',
 intro_p2='Its architecture is inspired by the cuboid houses of traditional villages, growing together among plants and rocks.',
 stats=['3 km from Soria','Sierra de San Marcos','Bubbles with sky views','Produce-led cuisine'],rooms_t='Suites, bubbles and villa',rooms_s='Independent lodgings to enjoy nature.',
 svcs=['Suites with private heated pool','Bubble with infinity pool','Bathtubs on the terrace','Open-air Jaima space','La Cabaña for quiet dinners','Events'],
 around_s='The Sierra de San Marcos and the city of Soria, just 3 km away.',
 loc_p='Paraje de San Marcos nº 13 · 42005 Soria. Booking information Monday to Sunday from 9:00 to 00:00.',
 chips=['What accommodation do you have?','Is there a pool?','What time is check-in?','How do I book?']),
'fr':dict(title='Noctis Hotel · Suites et bulles sous les étoiles à Soria',see_rooms='Voir les hébergements',nav_rooms='Hébergements',hero_k='Soria · Paraje de San Marcos, 13',hero_t='Élégance et calme dans un cadre naturel',hero_s='Suites, bulles premium et une villa à 3 km du centre de Soria, dans la Sierra de San Marcos.',
 intro_t='Le privilège de la pause',intro_p1='Un lieu où nature et luxe vont de pair : des hébergements exclusifs en matériaux durables dans la Sierra de San Marcos.',
 intro_p2='Son architecture s’inspire des maisons cubiques des villages traditionnels, qui poussent ensemble entre végétation et rochers.',
 stats=['À 3 km de Soria','Sierra de San Marcos','Bulles avec vue sur le ciel','Cuisine du terroir'],rooms_t='Suites, bulles et villa',rooms_s='Des hébergements indépendants pour profiter de la nature.',
 svcs=['Suites avec piscine chauffée privée','Bulle avec piscine à débordement','Baignoires en terrasse','Espace Jaima en plein air','La Cabaña pour dîner au calme','Événements'],
 around_s='La Sierra de San Marcos et la ville de Soria, à seulement 3 km.',
 loc_p='Paraje de San Marcos nº 13 · 42005 Soria. Informations de réservation du lundi au dimanche de 9h00 à 00h00.',
 chips=['Quels hébergements avez-vous ?','Y a-t-il une piscine ?','À quelle heure est l’arrivée ?','Comment réserver ?']),
'de':dict(title='Noctis Hotel · Suiten und Bubbles unter den Sternen in Soria',see_rooms='Unterkünfte ansehen',nav_rooms='Unterkünfte',hero_k='Soria · Paraje de San Marcos, 13',hero_t='Eleganz und Ruhe in natürlicher Umgebung',hero_s='Suiten, Premium-Bubbles und eine Villa 3 km vom Zentrum Sorias, in der Sierra de San Marcos.',
 intro_t='Das Privileg der Pause',intro_p1='Ein Ort, an dem Natur und Luxus zusammengehen: exklusive Unterkünfte aus nachhaltigen Materialien in der Sierra de San Marcos.',
 intro_p2='Die Architektur ist von den würfelförmigen Häusern traditioneller Dörfer inspiriert, die zwischen Pflanzen und Felsen zusammenwachsen.',
 stats=['3 km von Soria','Sierra de San Marcos','Bubbles mit Himmelsblick','Regionale Küche'],rooms_t='Suiten, Bubbles und Villa',rooms_s='Unabhängige Unterkünfte, um die Natur zu genießen.',
 svcs=['Suiten mit privatem beheiztem Pool','Bubble mit Infinity-Pool','Badewannen auf der Terrasse','Jaima-Bereich im Freien','La Cabaña für ruhige Abendessen','Veranstaltungen'],
 around_s='Die Sierra de San Marcos und die Stadt Soria, nur 3 km entfernt.',
 loc_p='Paraje de San Marcos nº 13 · 42005 Soria. Buchungsinformation Montag bis Sonntag von 9:00 bis 00:00 Uhr.',
 chips=['Welche Unterkünfte gibt es?','Gibt es einen Pool?','Ab wann ist der Check-in?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://hotels.cloudbeds.com/{}/reservation/2129rK'
BOOK=dict(mode='engine',url=dict(es=R.format('es'),en=R.format('en'),fr=R.format('fr'),de=R.format('de')))
D=dict(name='Noctis Hotel',ac='#121c28',ac2='#6e6040',ac2_a11y='#5a4e32',book=BOOK,around=['Sierra de San Marcos','Soria'],foot=FOOT,
 address='Paraje de San Marcos nº 13 · 42005 Soria',phones=['+34 618 79 45 04'],emails=['info@noctishotel.es'],maps='Noctis Hotel, Paraje de San Marcos 13, 42005 Soria',t=T)
META=dict(repo='demo-noctis-hotel-soria',name='Noctis Hotel',legal_name='FINCA SAN MARCOS EVENTOS S.L. (aviso legal de su web)',registry_ids=['B88415484'],
 url='https://noctishotel.es/',domain='noctishotel.es',municipality='Soria',province='Soria',sector='hotel boutique de suites y burbujas en la Sierra de San Marcos (Soria)',
 read_at='2026-11-02T07:16:00+01:00',created_at='2026-11-02T07:15:00+01:00',built_at='2026-11-02T07:25:00+01:00',audit_date='2026-11-02T06:46:26+01:00',
 rating=dict(value=4.8,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Noctis+Hotel/@41.7341822,-2.4966889,17z'),
 book=dict(mode='engine',url=R.format('es'),note='motor de reservas real enlazado desde su web (Cloudbeds 2129rK), HTTP 200 comprobado el 02/11/2026 con /es, /en, /fr y /de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué alojamientos tenéis?','K01'),('¿Cómo son las burbujas?','K02'),('¿Tenéis suites?','K03'),('¿Hay piscina?','K04'),('¿A qué hora es el check-in?','K05'),('¿Qué es La Villa?','K06'),('¿Hay restaurante?','K07'),('¿Hacéis eventos?','K08'),('¿Dónde estáis?','K09'),('¿Cómo reservo?','K10'),('¿Podéis confirmarme disponibilidad para mañana?','K10'),('¿Cuánto cuesta la noche?',None),('¿Tenéis campo de golf?',None)],
'en':[('What accommodation do you have?','K01'),('What are the bubbles like?','K02'),('Do you have suites?','K03'),('Is there a pool?','K04'),('What time is check-in?','K05'),('What is La Villa?','K06'),('Is there a restaurant?','K07'),('Do you host events?','K08'),('Where are you?','K09'),('How do I book?','K10'),('Can you confirm availability for tomorrow?','K10'),('How much is a night?',None),('Do you have a golf course?',None)],
'fr':[('Quels hébergements avez-vous ?','K01'),('Comment sont les bulles ?','K02'),('Avez-vous des suites ?','K03'),('Y a-t-il une piscine ?','K04'),('À quelle heure est l’arrivée ?','K05'),('Qu’est-ce que La Villa ?','K06'),('Y a-t-il un restaurant ?','K07'),('Organisez-vous des événements ?','K08'),('Où êtes-vous ?','K09'),('Comment réserver ?','K10'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K10'),('Combien coûte la nuit ?',None),('Avez-vous un terrain de golf ?',None)],
'de':[('Welche Unterkünfte gibt es?','K01'),('Wie sind die Bubbles?','K02'),('Haben Sie Suiten?','K03'),('Gibt es einen Pool?','K04'),('Ab wann ist der Check-in?','K05'),('Was ist La Villa?','K06'),('Gibt es ein Restaurant?','K07'),('Veranstalten Sie Events?','K08'),('Wo liegt die Unterkunft?','K09'),('Wie kann ich buchen?','K10'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K10'),('Was kostet eine Nacht?',None),('Haben Sie einen Golfplatz?',None)]}
