Changelog
=========


1.0.0 (2023-02-17)
------------------

- Improve code to avoid to many refresh of the map
  [mpeeters]


1.0b8 (2022-06-18)
------------------

- Ensure Plone 6 compatibility
  [boulch, laulaz]

- Fix image field fetching on objects (for display on map markers popups)
  [laulaz]

- Fix faceted map js on page load
  [boulch]


1.0b7 (2022-06-01)
------------------

- Add Github Action / fix buildout & tests
  [laulaz]

- Include missing collective.geolocationbehavior
  Otherwise, its profile is not available (as a dependency)
  [laulaz]


1.0b6 (2020-09-11)
------------------

- Avoid an error when there is no marker to display
  [mpeeters]


1.0b5 (2020-07-16)
------------------

- Handle content without geolocation for popups on hover
  [mpeeters]

- Add a css class to faceted map element that indicate if the element is geolocated
  [mpeeters]


1.0b4 (2020-05-04)
------------------

- Fix an issue when there is no geolocated results to display
  [mpeeters]


1.0b3 (2020-01-29)
------------------

- Do not use marker cluster
  [mpeeters]


1.0b2 (2020-01-29)
------------------

- Trigger the open of marker popups on hover
  [mpeeters]

- Add faceted-map-geojson-popup view to have possibility to override pointer popup value.
  [bsuttor]


1.0b1 (2020-01-28)
------------------

- Add map_configuration property on viewlet.
  [bsuttor]

- Add i18n:domain on viewlet.
  [bsuttor]


1.0a4 (2020-01-27)
------------------

- Move faceted map to a viewlet to avoid reload of map on every refresh
  [mpeeters]

- Add faceted map view.
  [bsuttor]


1.0a3 (2019-10-22)
------------------

- Add content lead image if it exists
  [mpeeters]

- Ensure that all markers are green
  [mpeeters]


1.0a2 (2019-10-18)
------------------

- Avoid to return an empty list of features that breaks Leaflet
  [mpeeters]


1.0a1 (2019-10-16)
------------------

- Initial release.
  [mpeeters]
