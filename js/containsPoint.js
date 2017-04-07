if (arguments.length < 2) throw new Error('Required arguments: lat, lng')

const lat = arguments[0]
const lng = arguments[1]

const MAP_BOUNDS = app.getRegion("map").currentView.map.getBounds();
const POINT = new L.LatLng(lat, lng);
return MAP_BOUNDS.contains(POINT);
