if (arguments.length < 1) throw new Error('Required arguments: bbox as an array' +
                                          '[sw lat, sw lng], [ne lat, ne lng]')

const bbox = arguments[0];
//alert(bbox + ' ' +  bbox.length +' ' +bbox[0].length + ' ' + typeof bbox);
const MAP_BOUNDS = app.getRegion('map').currentView.map.getBounds();
const BBOX_BOUNDS = new L.LatLngBounds(bbox[0], bbox[1]);
alert(MAP_BOUNDS.toBBoxString() + ' ' + BBOX_BOUNDS.toBBoxString());
return MAP_BOUNDS.contains(BBOX_BOUNDS);
