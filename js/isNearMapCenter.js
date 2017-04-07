if (arguments.length < 2) throw new Error('Required arguments: lat, lng')

const lat = arguments[0]
const lng = arguments[1]
const delta = arguments.length == 3 ? arguments[2] : 1e-4


const isNear = (x) => {
    return Math.abs(x) < delta
}
const MAP_CENTER = app.getRegion("map").currentView.map.getCenter();

latIsNear = isNear(MAP_CENTER.lat - lat)
lngIsNear = isNear(MAP_CENTER.lng - lng)
return  latIsNear && lngIsNear
