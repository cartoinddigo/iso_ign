import requests
from concurrent.futures import ThreadPoolExecutor    
#liste d'url que le programme va tester 
urlList =  {  
    'isochroneVoitureV2PGRTemps' :{
        "nom": "Isochrone Voiture V2 PGR Temps",
        "lien": "https://itineraire.ign.fr/simple/1.0.0/isochrone?resource=bdtopo-pgr&profile=car&costType=time&costValue=100&direction=departure&point=5.161412,48.776848&constraints=&geometryFormat=geojson"},
        
    'isochronePietonV2PGRTemps' :{
        "nom": "Isochrone Pieton V2 PGR Temps", 
        "lien": "https://itineraire.ign.fr/simple/1.0.0/isochrone?resource=bdtopo-pgr&profile=pedestrian&costType=time&costValue=100&direction=departure&point=5.161412,48.776848&constraints=&geometryFormat=geojson"},

    'isochronevoitureV2PGRDistance' :{
        "nom": "Isochrone Voiture V2 PGR Distance",
        "lien": "https://itineraire.ign.fr/simple/1.0.0/isochrone?resource=bdtopo-pgr&profile=car&costType=distance&costValue=100&direction=departure&point=5.161412,48.776848&constraints=&geometryFormat=geojson"},

    'isochronePietonV2PGRDistance' :{
        "nom": "Isochrone Pieton V2 PGR Distance", 
        "lien": "https://itineraire.ign.fr/simple/1.0.0/isochrone?resource=bdtopo-pgr&profile=pedestrian&costType=distance&costValue=100&direction=departure&point=5.161412,48.776848&constraints=&geometryFormat=geojson"},

    'itineraireVoitureV2Bdtopo' :{
        "nom": "Itinéraire Voiture V2 Bdtopo", 
        "lien": "https://wxs.ign.fr/calcul/geoportail/itineraire/rest/1.0.0/route?resource=bdtopo-osrm&profile=car&optimization=fastest&start=5.161412,48.776848&end=5.2,48.8&intermediates=&constraints=&geometryFormat=polyline&getSteps=true&getBbox=true"},

    'itinerairePietonV2Bdtopo' :{
        "nom": "Itinéraire Pieton V2 Bdtopo", 
        "lien": "https://wxs.ign.fr/calcul/geoportail/itineraire/rest/1.0.0/route?resource=bdtopo-osrm&profile=pedestrian&optimization=fastest&start=5.161412,48.776848&end=5.2,48.8&intermediates=&constraints=&geometryFormat=polyline&getSteps=true&getBbox=true"}
    }   
#Creation de la classe ressource IGN
class ressourceIgn ():
    #liste de résultats avec un code 200
    res =[]
    #liste de résultats avec un code erreur
    err =[]
    def __init__(self):
        self      
    def testIgnServices(self, url,nom):

        html = requests.get(url, nom,stream=True)
        if html.status_code == 200 :
            self.res.append(nom)
        else :
            if nom not in self.err :
                self.err.append(nom+ " - Code d'erreur :"+str(html.status_code))
        if len(self.processes) == 6 :
            self.err.clear()
    def resultats(self):
        self.processes = []
        with ThreadPoolExecutor(max_workers=6) as executor:
            for url in urlList.values():
                self.processes.append(executor.submit(self.testIgnServices(self,url['lien'],url['nom'])))
            if len(self.res) == 6:
                self.res.clear()
                return "Tous les services de l'IGN fonctionnent"
            else :
                print(self.err)
                if len(self.err) ==1:
                    return "Ce service ne fonctionne pas : "+str(self.err)
                if len(self.err) <=2:
                    return "Ces services ne fonctionnent pas : "+str(self.err)
                if len(self.err) ==6:
                    return "Tous les services de l'IGN sont à l'arrêt"

#Code à garder, sait-on jamais
'''
def testUrlsV2 ():
    respV2 = []
    ErrV2 = []
    for d in urlsV2.values():
        rq = requests.get(str(d['lien']), verify=False)
        if rq.status_code == 200:
            str((d['nom'] +' est ok'))
            respV2.append(str((d['nom'] +' est ok')))
        else:
            ErrV2.append(str((d['nom'] +" Code d'erreur : "+ str(rq.status_code))))
    if len(respV2) == 8:
        return str("Tous les service de l'IGN V2 sont fonctionnels")
    if len(ErrV2) >= 1:
        return str('Service V2 indisponible : \n'+', '.join(ErrV2))
def testUrlsV1 ():
    respV1 = []
    ErrV1 = []
    for d in urlsV1.values():
        rq = requests.get(str(d['lien']), verify=False)
        if rq.status_code == 200:
            str((d['nom'] +' est ok'))
            respV1.append(str((d['nom'] +' est ok')))
        else:
            ErrV1.append(str((d['nom'] +" Code d'erreur : "+ str(rq.status_code))))
    if len(respV1) == 6:
        return str("Tous les service de l'IGN V1 sont fonctionnels")
    if len(ErrV1) >= 1:
        return str('Service V1 indisponible \n'+ ', '.join(ErrV1))
'''
ressource_complementaires ={
     'itineraireVoitureV2PGR' :{
        "nom": "Itinéraire Voiture V2 PGR", 
        "lien": "https://wxs.ign.fr/calcul/geoportail/itineraire/rest/1.0.0/route?resource=bdtopo-pgr&profile=car&optimization=fastest&start=5.161412,48.776848&end=5.2,48.8&intermediates=&constraints=&geometryFormat=polyline&getSteps=true&getBbox=true"},

    'itinerairePietonV2PGR' :{
        "nom": "Itinéraire Pieton V2 PGR", 
        "lien": "https://wxs.ign.fr/calcul/geoportail/itineraire/rest/1.0.0/route?resource=bdtopo-pgr&profile=pedestrian&optimization=fastest&start=5.161412,48.776848&end=5.2,48.8&intermediates=&constraints=&geometryFormat=polyline&getSteps=true&getBbox=true"},

    'itineraireVoitureV1' : {
        "nom": "Itinéraire Voiture V1",
        "lien":"https://wxs.ign.fr/oz4nfwppbqu1iaqygbkypf6b/itineraire/rest/route.json?origin=2.424573,48.845726&destination=2.352677,48.858157&method&#061;TIME&waypoints&#061;&graphName&#061;Voiture&exclusions&#061;&srs&#061;EPSG:4326"},

    'itinerairePietonV1' : {
        "nom": "Itinéraire Piéton V1",
        "lien": "https://wxs.ign.fr/oz4nfwppbqu1iaqygbkypf6b/itineraire/rest/route.json?origin=2.424573,48.845726&destination=2.352677,48.858157&method&#061;TIME&waypoints&#061;&graphName&#061;Pieton&exclusions&#061;&srs&#061;EPSG:4326"},
    
    'isochroneVoitureV1Temps' : {
        "nom": "Isochrone Voiture V1 Temps", 
        "lien": "https://wxs.ign.fr/oz4nfwppbqu1iaqygbkypf6b/isochrone/isochrone.json?smoothing=true&holes=false&reverse=false&method=time&time=60&graphName=Voiture&location=5.2,48.8"},
    
    'isochronePietonV1Temps' : {
        "nom": "Isochrone Pieton V1 Temps", 
        "lien": "https://wxs.ign.fr/oz4nfwppbqu1iaqygbkypf6b/isochrone/isochrone.json?smoothing=true&holes=false&reverse=false&method=time&time=60&graphName=Pieton&location=5.161412,48.776848"},

    'isochroneVoitureV1Distance' : {
        "nom": "Isochrone Voiture V1 Distance", 
        "lien": "https://wxs.ign.fr/oz4nfwppbqu1iaqygbkypf6b/isochrone/isochrone.json?smoothing=true&holes=false&reverse=false&method=distance&distance=60&graphName=Voiture&location=5.161412,48.776848"},
    
    'isochronePietonV1Distance' : {
        "nom": "Isochrone Pieton V1 Distance", 
        "lien": "https://wxs.ign.fr/oz4nfwppbqu1iaqygbkypf6b/isochrone/isochronee.json?smoothing=true&holes=false&reverse=false&method=distance&distance=60&graphName=Pieton&location=5.161412,48.776848"}}