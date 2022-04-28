// no ofc this isnt the actual boogiefn backend but its a backend me (noteason) tried 
//to make so that your lazy skiddy asses can make your own hybrid and not skid storm like bozos
// note that this is very similar to the boogiefn backend, just not as complicated and good ofc but it should meet basic requirements of a fortnite hybrid server
const express = require('express');

const app = express()
const port = 69

app.get('/', (req, res) => {
  res.json({})
})

app.get('/content/api/pages/fortnite-game/media-events', (req, res) => {
  res.json([])
})

app.post('/fortnite/api/game/v2/enabled_features', (req, res) => {
  res.json([])
})

app.post('/fortnite/api/v2/versioncheck/:version', (req, res, version) => {
  res.json({"type":"NO_UPDATE"})
})


app.post('/fortnite/api/calendar/v1/timeline', (req, res) => {
  res.json([
			{
				"channels":{
				"client-events":{
						"states":[
							{
								"state":{
									"seasonNumber":3,
									"seasonTemplateId":"AthenaSeason:athenaseason3",
									"seasonBegin":"0001-06-23T04:00:00Z",
									"seasonEnd":"9999-07-23T04:00:00Z",
									"seasonDisplayedEnd":"9999-07-23T04:00:00Z"
								}
							}
						]
					}
				},
				"currentTime": "9998-06-23T04:00:00Z"
			}
		])
})

app.post('/socialban/api/public/v1/:accountId', (req, res, accountId) => {
  res.empty()
})

app.get('/fortnite/api/storefront/v2/keychain', (req, res) => {
  res.redirect('https://api.nitestats.com/v1/epic/keychain');
})

app.post('/content/api/pages/fortnite-game', (req, res) => {
  res.sendFile('fortnite-game.json', { root : __dirname});
})



app.listen(port, () => {
  console.log(`Basic Fortnite Hybrid Backend Made By noteason |  listening on port ${port}`)
})
