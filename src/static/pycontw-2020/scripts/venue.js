import L from 'leaflet'
import 'leaflet-easybutton'

const venue = L.layerGroup()
const coordinates = [22.997908, 120.215657] // 成大國際會議廳

// Marker style and layer definition.
L.marker(coordinates, {
	icon: L.icon({
		iconUrl: window.VENUE_ICON,
		iconSize: [100, 78],
		iconAnchor: [50, 55],
	}),
})
.addTo(venue)
.bindTooltip(window.VENUE_NAME, {
	offset: [-4, 20],
	direction: 'bottom',
})
.openTooltip()

// Tile attributions.
const mbAttr1 = 'Tiles by <a href="https://stamen.com">Stamen Design</a>. Data &copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors.'
const mbUrl1 = 'http://{s}.sm.mapstack.stamen.com/((toner-background,$fff[@20],$224298[hsl-color])[@90],(toner-lines,$fff[@80],$fff[hsl-saturation@20],$f4d45f[hsl-color]),(toner-labels,$fff[@30]))/{z}/{x}/{y}.png'
const mbAttr2 = 'Maps &copy; <a href="https://www.thunderforest.com" target="_blank" rel="noopener">Thunderforest</a>, Data &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap </a> contributors.'
const mbUrl2 = 'https://{s}.tile.thunderforest.com/transport/{z}/{x}/{y}.png?apikey=6170aad10dfd42a38d4d8c709a536f38'


const stamen = L.tileLayer(mbUrl1, {attribution: mbAttr1})
const transport = L.tileLayer(mbUrl2, {attribution: mbAttr2})

// Initialize map.
const pymap = L.map('venue-map', {
	center: coordinates,
	zoom: 12,
	layers: [stamen, venue],
	scrollWheelZoom: false,
	zoomControl: false,
})
L.control.zoom({position: 'topright'}).addTo(pymap)

// Adjust map to center the icon in the non-covered area.
function centerMap() {
	const mapw = document.getElementById('venue-map').clientWidth
	const ovlw = document.getElementById('venue-info-overlay').clientWidth

	let lng = coordinates[1]
	if (ovlw && mapw > ovlw) {
		const bs = pymap.getBounds()
		lng -= (bs.getEast() - bs.getWest()) * ovlw / mapw / 2
	}
	pymap.panTo([coordinates[0], lng])
}
centerMap()
window.map = pymap

// Icon for venue.
L.easyButton(
	`<img src="${window.VENUE_BUTTON}" alt="Map Home">`,
	centerMap,
	{position: 'topright'},
).addTo(pymap)

// Layers and functionalities.
const baseLayers = {
	'Stamen': stamen,
	'Transport': transport,
}
const overlays = {
	'Venue': venue
}

// Layers and functionalities.
L.control.layers(baseLayers, overlays, {position: 'bottomright'}).addTo(pymap)
